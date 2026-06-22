# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import os

DL   = r"C:\Users\e4user\Downloads"
ROOT = r"C:\Users\e4user\Documents\ParticleworksProjects\pw-website\experience"
OUT  = os.path.join(ROOT, "cards")
os.makedirs(OUT, exist_ok=True)

FONT = os.path.join(DL, "OfficinaSans-Bold.otf")
BG   = os.path.join(DL, "backgroun_new.png")
LOGO = os.path.join(DL, "experience_logo.png")
SPK  = os.path.join(ROOT, "speakers")

S = 1200
WHITE=(255,255,255); GREEN=(46,207,120); SUB=(255,224,216); SUBLOC=(255,217,207)
GRAD_A=(0,136,204); GRAD_B=(37,163,97)  # avatar gradient

def f(sz): return ImageFont.truetype(FONT, sz)

def base_bg():
    im = Image.open(BG).convert("RGB")
    # cover-crop to square
    w,h = im.size
    scale = S / w
    im = im.resize((S, int(h*scale)), Image.LANCZOS)
    top = int((im.size[1]-S)*0.36)
    im = im.crop((0, top, S, top+S))
    # legibility scrim: darken, a touch stronger on the left where the text lives
    scrim = Image.new("L",(S,S),0)
    sd = ImageDraw.Draw(scrim)
    for x in range(S):
        a = int(120 - 55*(x/S))        # 120 -> 65 left to right
        sd.line([(x,0),(x,S)], fill=max(40,a))
    black = Image.new("RGB",(S,S),(60,8,10))
    im = Image.composite(black, im, scrim)
    # gentle bottom darken for the logo / venue row
    sc2 = Image.new("L",(S,S),0); d2=ImageDraw.Draw(sc2)
    for y in range(S):
        d2.line([(0,y),(S,y)], fill=int(max(0,(y-820)/ (S-820))*110) if y>820 else 0)
    im = Image.composite(Image.new("RGB",(S,S),(40,6,8)), im, sc2)
    return im

def draw_frame(d):
    d.rectangle([30,30,S-31,S-31], outline=WHITE, width=3)
    d.rectangle([48,48,S-49,S-49], outline=GREEN, width=5)

def calendar_icon(im, x, y, s=54, col=WHITE):
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([x, y+8, x+s, y+s], radius=7, outline=col, width=4)
    d.rectangle([x, y+8, x+s, y+22], fill=col)
    d.line([x+13,y+2,x+13,y+14], fill=col, width=4)
    d.line([x+s-13,y+2,x+s-13,y+14], fill=col, width=4)
    for r in range(3):
        for c in range(3):
            d.ellipse([x+11+c*15, y+30+r*9, x+16+c*15, y+35+r*9], fill=col)

def fit(text, max_w, start, lo=22):
    sz=start
    while sz>lo:
        ft=f(sz)
        if ft.getlength(text)<=max_w: return ft
        sz-=2
    return f(lo)

def wrap(text, ft, max_w):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if ft.getlength(t)<=max_w: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def circle_photo(im, path, cx, cy, dia):
    ring=8
    # white ring + soft shadow
    sh=Image.new("RGBA",(S,S),(0,0,0,0)); sd=ImageDraw.Draw(sh)
    sd.ellipse([cx-dia//2-ring, cy-dia//2-ring+6, cx+dia//2+ring, cy+dia//2+ring+6], fill=(0,0,0,90))
    sh=sh.filter(ImageFilter.GaussianBlur(9)); im.alpha_composite(sh)
    d=ImageDraw.Draw(im)
    d.ellipse([cx-dia//2-ring, cy-dia//2-ring, cx+dia//2+ring, cy+dia//2+ring], fill=WHITE)
    ph=Image.open(path).convert("RGB")
    ph=ImageOps.fit(ph,(dia,dia),Image.LANCZOS,centering=(0.5,0.42))
    mask=Image.new("L",(dia,dia),0); ImageDraw.Draw(mask).ellipse([0,0,dia,dia],fill=255)
    im.paste(ph,(cx-dia//2,cy-dia//2),mask)

def circle_initials(im, initials, cx, cy, dia):
    ring=8; d=ImageDraw.Draw(im)
    d.ellipse([cx-dia//2-ring, cy-dia//2-ring, cx+dia//2+ring, cy+dia//2+ring], fill=WHITE)
    grad=Image.new("RGB",(dia,dia))
    for yy in range(dia):
        for xx in range(0,dia,1):
            t=(xx+yy)/(2*dia)
            grad.putpixel((xx,yy),tuple(int(GRAD_A[i]+(GRAD_B[i]-GRAD_A[i])*t) for i in range(3)))
    mask=Image.new("L",(dia,dia),0); ImageDraw.Draw(mask).ellipse([0,0,dia,dia],fill=255)
    im.paste(grad,(cx-dia//2,cy-dia//2),mask)
    ft=f(int(dia*0.42)); tw=ft.getlength(initials)
    bb=ft.getbbox(initials); th=bb[3]-bb[1]
    d.text((cx-tw/2, cy-th/2-bb[1]), initials, font=ft, fill=WHITE)

def make_card(c):
    im = base_bg().convert("RGBA")
    d = ImageDraw.Draw(im)
    draw_frame(d)
    M=95
    # date block
    calendar_icon(im, M, 92)
    d=ImageDraw.Draw(im)
    d.text((M+72, 90), c["date"], font=f(40), fill=WHITE)
    d.text((M+72, 138), c["cat"], font=f(26), fill=SUB)
    # photos top-right
    photos=c["photos"]; dia=200; cy=200; rx=S-95-dia//2
    if len(photos)==1:
        p=photos[0]
        (circle_photo if p[0] else circle_initials)(im, p[1], rx, cy, dia)
    elif len(photos)>=2:
        d2=176; gap=28
        x2=S-95-d2//2
        x1=x2-d2-gap
        for (px,(isph,val)) in zip([x1,x2], photos[:2]):
            (circle_photo if isph else circle_initials)(im, val, px, cy, d2)
    # company + speakers
    d=ImageDraw.Draw(im)
    cf=fit(c["company"], S-2*M, 58); d.text((M, 452), c["company"], font=cf, fill=WHITE)
    sf=fit(c["speakers"], S-2*M, 48); d.text((M, 524), c["speakers"], font=sf, fill=GREEN)
    # title
    tf=f(46); maxw=S-2*M
    lines=wrap(c["title"], tf, maxw)
    if len(lines)>4:
        tf=f(40); lines=wrap(c["title"], tf, maxw)
    y=624; lh=tf.size+14
    for ln in lines:
        d.text((M,y), ln, font=tf, fill=WHITE); y+=lh
    # logo bottom-left on a clean white badge for legibility
    logo=Image.open(LOGO).convert("RGBA"); lw=330
    logo=logo.resize((lw,int(logo.size[1]*lw/logo.size[0])),Image.LANCZOS)
    lx, ly = M, S-96-logo.size[1]
    pad=20
    pill=Image.new("RGBA",(S,S),(0,0,0,0))
    ImageDraw.Draw(pill).rounded_rectangle(
        [lx-pad, ly-pad, lx+logo.size[0]+pad, ly+logo.size[1]+pad], radius=20, fill=(255,255,255,240))
    im.alpha_composite(pill)
    im.alpha_composite(logo,(lx,ly))
    # venue bottom-right
    vf=f(38); vsub=f(26)
    t1=c["loc1"]; t2=c["loc2"]
    d.text((S-95-vf.getlength(t1), S-150), t1, font=vf, fill=WHITE)
    d.text((S-95-vsub.getlength(t2), S-104), t2, font=vsub, fill=SUBLOC)
    im.convert("RGB").save(os.path.join(OUT, c["file"]), "PNG")
    print("wrote", c["file"], "| title lines:", len(lines))

def ph(name):  return (True, os.path.join(SPK, name))
def ini(s):    return (False, s)

DATE="October 7, 2026"; L1="Modena, Italy"; L2="BPER FORUM Monzani"
cards=[
 dict(file="card-01-prometech.png", date=DATE, cat="Developer keynote", company="PROMETECH SOFTWARE",
      speakers="Iori Saigo", title="What's New in Particleworks 9.0 and Granuleworks 4.0",
      photos=[ph("iori-saigo.jpg")], loc1=L1, loc2=L2),
 dict(file="card-02-mtu.png", date=DATE, cat="Industrial speaker", company="MTU AERO ENGINES",
      speakers="Alpcan Güray", title="Simulation of Shot Peening: A CFD-DEM Coupled Case Study",
      photos=[ph("alpcan-guray.jpg")], loc1=L1, loc2=L2),
 dict(file="card-03-unimore-stator.png", date=DATE, cat="Academic speaker", company="UNIVERSITY OF MODENA AND REGGIO EMILIA",
      speakers="Michelangelo Raimondo", title="An Integrated Simulation Approach for Stator Oil Jacket and Jet Cooling Systems",
      photos=[ph("michelangelo-raimondo.jpg")], loc1=L1, loc2=L2),
 dict(file="card-04-rdcfd-pump.png", date=DATE, cat="Industrial speaker", company="R&D CFD",
      speakers="Leonardo Lanciotti", title="CHT Analysis of a Reciprocating Pump",
      photos=[ph("leonardo-lanciotti.jpg")], loc1=L1, loc2=L2),
 dict(file="card-05-hesso-pelton.png", date=DATE, cat="Academic speaker", company="HES-SO VALAIS//WALLIS",
      speakers="Jean Decaix", title="Moving Particle Simulation of Eroded Pelton Runners",
      photos=[ph("jean-decaix.jpg")], loc1=L1, loc2=L2),
 dict(file="card-06-skf.png", date=DATE, cat="Industrial speaker", company="SKF",
      speakers="Lijun Cao", title="Verification of Heat Transfer Coefficient in Particleworks for Bearings",
      photos=[ini("LC")], loc1=L1, loc2=L2),
 dict(file="card-07-deepfluid.png", date=DATE, cat="Industrial speaker", company="DEEPFLUID",
      speakers="Dr. Lukas Hafner", title="Direct Optical Air-in-Oil Measurement for Gearings and Hydraulic Systems",
      photos=[ph("lukas-hafner.jpg")], loc1=L1, loc2=L2),
 dict(file="card-08-trackone.png", date=DATE, cat="Industrial speaker", company="TRACK ONE",
      speakers="Leonardo Tiberi", title="Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method",
      photos=[ini("LT")], loc1=L1, loc2=L2),
 dict(file="card-09-univance.png", date=DATE, cat="Industrial speaker", company="UNIVANCE CORPORATION",
      speakers="Naohiro Fujita", title="Application of Particleworks to Gear Lubrication Analysis and Its Expansion to R&D on Airflow Effects",
      photos=[ph("naohiro-fujita.jpg")], loc1=L1, loc2=L2),
 dict(file="card-10-iav.png", date=DATE, cat="Industrial speaker", company="IAV",
      speakers="René Kockisch", title="From Formation to Dissolution: Air Bubble Dynamics in Gear Oil of an Electric 3-Speed Drivetrain",
      photos=[ini("RK")], loc1=L1, loc2=L2),
]
for c in cards: make_card(c)
print("DONE ->", OUT)
