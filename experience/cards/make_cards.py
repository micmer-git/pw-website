# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import numpy as np, os

DL   = r"C:\Users\e4user\Downloads"
ROOT = r"C:\Users\e4user\Documents\ParticleworksProjects\pw-website\experience"
OUT  = os.path.join(ROOT, "cards")
PROC = os.path.join(DL, "_proc")          # white-bg cutout photos + sim images
os.makedirs(OUT, exist_ok=True)

FONT = os.path.join(DL, "OfficinaSans-Bold.otf")
BG   = os.path.join(DL, "backgroun_new.png")
LOGO = os.path.join(DL, "experience_logo.png")

S=1200
WHITE=(255,255,255); GREEN=(52,210,124); SUB=(255,224,216); SUBLOC=(255,217,207)
INI=(10,106,161)                          # initials colour on white circle

def f(sz): return ImageFont.truetype(FONT, sz)

def base_bg():
    im=Image.open(BG).convert("RGB"); w,h=im.size
    sc=S/w; im=im.resize((S,int(h*sc)),Image.LANCZOS)
    top=int((im.size[1]-S)*0.36); im=im.crop((0,top,S,top+S))
    scrim=Image.new("L",(S,S),0); sd=ImageDraw.Draw(scrim)
    for x in range(S): sd.line([(x,0),(x,S)],fill=max(45,int(120-55*(x/S))))
    im=Image.composite(Image.new("RGB",(S,S),(60,8,10)),im,scrim)
    sc2=Image.new("L",(S,S),0); d2=ImageDraw.Draw(sc2)
    for y in range(S): d2.line([(0,y),(S,y)],fill=int(max(0,(y-820)/(S-820))*110) if y>820 else 0)
    im=Image.composite(Image.new("RGB",(S,S),(40,6,8)),im,sc2)
    return im

def draw_frame(d):
    d.rectangle([30,30,S-31,S-31],outline=WHITE,width=3)
    d.rectangle([48,48,S-49,S-49],outline=GREEN,width=5)

def calendar_icon(im,x,y,s=56,col=WHITE):
    d=ImageDraw.Draw(im)
    d.rounded_rectangle([x,y+8,x+s,y+s],radius=7,outline=col,width=4)
    d.rectangle([x,y+8,x+s,y+23],fill=col)
    d.line([x+14,y+2,x+14,y+15],fill=col,width=4); d.line([x+s-14,y+2,x+s-14,y+15],fill=col,width=4)
    for r in range(3):
        for c in range(3): d.ellipse([x+12+c*15,y+31+r*9,x+17+c*15,y+36+r*9],fill=col)

def white_logo():
    logo=Image.open(LOGO).convert("RGBA"); a=np.array(logo)
    r,g,b,al=a[...,0].astype(int),a[...,1].astype(int),a[...,2].astype(int),a[...,3]
    X=np.broadcast_to(np.arange(a.shape[1]),a.shape[:2])
    lum=0.299*r+0.587*g+0.114*b
    dark=(lum<120)&(al>40)&(X>190)          # the black "Particleworks" wordmark -> white
    a[...,0][dark]=255;a[...,1][dark]=255;a[...,2][dark]=255
    return Image.fromarray(a)

def fit(text,max_w,start,lo=24):
    sz=start
    while sz>lo:
        if f(sz).getlength(text)<=max_w: return f(sz)
        sz-=2
    return f(lo)

def wrap(text,ft,max_w):
    out=[]; cur=""
    for w in text.split():
        t=(cur+" "+w).strip()
        if ft.getlength(t)<=max_w: cur=t
        else:
            if cur: out.append(cur)
            cur=w
    if cur: out.append(cur)
    return out

def circle_photo(im,path,cx,cy,dia):
    ring=8
    sh=Image.new("RGBA",(S,S),(0,0,0,0)); ImageDraw.Draw(sh).ellipse(
        [cx-dia//2-ring,cy-dia//2-ring+6,cx+dia//2+ring,cy+dia//2+ring+6],fill=(0,0,0,90))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(9)))
    d=ImageDraw.Draw(im); d.ellipse([cx-dia//2-ring,cy-dia//2-ring,cx+dia//2+ring,cy+dia//2+ring],fill=WHITE)
    ph=ImageOps.fit(Image.open(path).convert("RGB"),(dia,dia),Image.LANCZOS,centering=(0.5,0.42))
    mask=Image.new("L",(dia,dia),0); ImageDraw.Draw(mask).ellipse([0,0,dia,dia],fill=255)
    im.paste(ph,(cx-dia//2,cy-dia//2),mask)

def circle_initials(im,initials,cx,cy,dia):
    ring=8
    sh=Image.new("RGBA",(S,S),(0,0,0,0)); ImageDraw.Draw(sh).ellipse(
        [cx-dia//2-ring,cy-dia//2-ring+6,cx+dia//2+ring,cy+dia//2+ring+6],fill=(0,0,0,90))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(9)))
    d=ImageDraw.Draw(im)
    d.ellipse([cx-dia//2-ring,cy-dia//2-ring,cx+dia//2+ring,cy+dia//2+ring],fill=WHITE)  # white circle
    ft=f(int(dia*0.4)); tw=ft.getlength(initials); bb=ft.getbbox(initials)
    d.text((cx-tw/2,cy-(bb[3]-bb[1])/2-bb[1]),initials,font=ft,fill=INI)

def sim_panel(im,path,box):
    x0,y0,x1,y1=box; w,h=x1-x0,y1-y0
    sh=Image.new("RGBA",(S,S),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle(
        [x0,y0+8,x1,y1+8],radius=24,fill=(0,0,0,95))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    img=ImageOps.fit(Image.open(path).convert("RGB"),(w,h),Image.LANCZOS)
    mask=Image.new("L",(w,h),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,w,h],radius=24,fill=255)
    card=Image.new("RGBA",(w,h),(0,0,0,0)); card.paste(img,(0,0)); card.putalpha(mask)
    im.alpha_composite(card,(x0,y0))
    ImageDraw.Draw(im).rounded_rectangle([x0,y0,x1,y1],radius=24,outline=WHITE,width=4)

def make_card(c):
    im=base_bg().convert("RGBA"); d=ImageDraw.Draw(im); draw_frame(d)
    M=95; sim=c.get("sim")
    # date
    calendar_icon(im,M,92); d=ImageDraw.Draw(im)
    d.text((M+74,90),c["date"],font=f(42),fill=WHITE)
    d.text((M+74,142),c["cat"],font=f(26),fill=SUB)
    # avatar top-right
    if sim: cx,cy,dia=S-95-85,178,170
    else:   cx,cy,dia=S-95-100,200,200
    p=c["photos"][0]
    (circle_photo if p[0] else circle_initials)(im,p[1],cx,cy,dia)
    # sim panel
    if sim: sim_panel(im,sim,(705,322,1105,760))
    # text block (title -> company -> presenter), vertically centred
    tw = 580 if sim else (S-2*M)
    tf=f(56); lines=wrap(c["title"],tf,tw)
    if len(lines)>3: tf=f(48); lines=wrap(c["title"],tf,tw)
    if len(lines)>4: tf=f(42); lines=wrap(c["title"],tf,tw)
    cf=fit(c["company"],tw,48); pf=fit(c["speakers"],tw,46)
    tlh=tf.size+12; g1=26; g2=8
    H=len(lines)*tlh+g1+cf.size+g2+pf.size
    top,bot=326,824; y=top+max(0,(bot-top-H)//2)
    d=ImageDraw.Draw(im)
    for ln in lines: d.text((M,y),ln,font=tf,fill=WHITE); y+=tlh
    y+=g1; d.text((M,y),c["company"],font=cf,fill=WHITE); y+=cf.size+g2
    d.text((M,y),c["speakers"],font=pf,fill=GREEN)
    # white logo (no badge), bottom-left
    lg=white_logo(); lw=348; lg=lg.resize((lw,int(lg.size[1]*lw/lg.size[0])),Image.LANCZOS)
    im.alpha_composite(lg,(M,S-96-lg.size[1]))
    # venue bottom-right
    t1,t2=c["loc1"],c["loc2"]
    d.text((S-95-f(40).getlength(t1),S-152),t1,font=f(40),fill=WHITE)
    d.text((S-95-f(27).getlength(t2),S-104),t2,font=f(27),fill=SUBLOC)
    im.convert("RGB").save(os.path.join(OUT,c["file"]),"PNG")
    print("wrote",c["file"],"|",len(lines),"title lines",("+sim" if sim else ""))

def ph(name): return (True, os.path.join(PROC,name))
def ini(s):   return (False, s)
def simp(n):  return os.path.join(PROC,n)
DATE="October 7, 2026"; L1="Modena, Italy"; L2="BPER FORUM Monzani"

cards=[
 dict(file="card-01-prometech.png",date=DATE,cat="Developer keynote",company="PROMETECH SOFTWARE",
      speakers="Iori Saigo",title="What's New in Particleworks 9.0 and Granuleworks 4.0",
      photos=[ph("iori-saigo.png")],loc1=L1,loc2=L2),
 dict(file="card-02-mtu.png",date=DATE,cat="Industrial speaker",company="MTU AERO ENGINES",
      speakers="Alpcan Güray",title="Simulation of Shot Peening: A CFD-DEM Coupled Case Study",
      photos=[ph("alpcan-guray.png")],loc1=L1,loc2=L2),
 dict(file="card-03-unimore-stator.png",date=DATE,cat="Academic speaker",company="UNIVERSITY OF MODENA AND REGGIO EMILIA",
      speakers="Michelangelo Raimondo",title="An Integrated Simulation Approach for Stator Oil Jacket and Jet Cooling Systems",
      photos=[ph("michelangelo-raimondo.png")],loc1=L1,loc2=L2),
 dict(file="card-04-rdcfd-pump.png",date=DATE,cat="Industrial speaker",company="R&D CFD",
      speakers="Leonardo Lanciotti",title="CHT Analysis of a Reciprocating Pump",
      photos=[ph("leonardo-lanciotti.png")],loc1=L1,loc2=L2),
 dict(file="card-05-hesso-pelton.png",date=DATE,cat="Academic speaker",company="HES-SO VALAIS//WALLIS",
      speakers="Jean Decaix",title="Moving Particle Simulation of Eroded Pelton Runners",
      photos=[ph("jean-decaix.png")],loc1=L1,loc2=L2),
 dict(file="card-06-skf.png",date=DATE,cat="Industrial speaker",company="SKF",
      speakers="Lijun Cao",title="Verification of Heat Transfer Coefficient in Particleworks for Bearings",
      photos=[ini("LC")],sim=simp("skf.png"),loc1=L1,loc2=L2),
 dict(file="card-07-deepfluid.png",date=DATE,cat="Industrial speaker",company="DEEPFLUID",
      speakers="Dr. Lukas Hafner",title="Direct Optical Air-in-Oil Measurement for Gearings and Hydraulic Systems",
      photos=[ph("lukas-hafner.png")],sim=simp("deepfluid.png"),loc1=L1,loc2=L2),
 dict(file="card-08-trackone.png",date=DATE,cat="Industrial speaker",company="TRACK ONE",
      speakers="Leonardo Tiberi",title="Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method",
      photos=[ini("LT")],loc1=L1,loc2=L2),
 dict(file="card-09-univance.png",date=DATE,cat="Industrial speaker",company="UNIVANCE CORPORATION",
      speakers="Naohiro Fujita",title="Application of Particleworks to Gear Lubrication Analysis and Its Expansion to R&D on Airflow Effects",
      photos=[ph("naohiro-fujita.png")],sim=simp("univance.png"),loc1=L1,loc2=L2),
 dict(file="card-10-iav.png",date=DATE,cat="Industrial speaker",company="IAV",
      speakers="René Kockisch",title="From Formation to Dissolution: Air Bubble Dynamics in Gear Oil of an Electric 3-Speed Drivetrain",
      photos=[ini("RK")],loc1=L1,loc2=L2),
]
for c in cards: make_card(c)
print("DONE ->",OUT)
