"""Single source of truth for the PW Experience 2026 talks that may be published.
Written from the speakers' released PDFs AND the reviewed transcripts (quotes are verbatim, lightly tidied: fillers dropped).
Used by _gen_blog_pwexp2026.py (blog), and by the work-dir builders for the proceedings config, YouTube sheet, thumbnails and motion video.
`**x**` marks a highlight: <mark> in the blog, plain text elsewhere.
Times (`t`) are seconds from the start of that talk's video, so ?talk=04&t=1279 opens the right moment."""

# ---- verified numbers (slides) -------------------------------------------------------------
SKF_SPHERE = [  # W/m2K, 10 mm sphere in 1 m/s bearing oil, surface-average HTC
    ('Whitaker correlation (reference)', 184, 'ref'),
    ('PW local correlation: read at the wall', 66, 'bad'),
    ('… read 0.75 mm from the wall', 99, 'mid'),
    ('… read 1.5 mm from the wall', 169, 'good'),
    ('1 mm particles, default settings', 85, 'bad'),
    ('1 mm particles, Nusselt coefficient 0.745', 192, 'good'),
    ('Heat-flux method, 0.5 mm particles', 75, 'bad'),
    ('Heat-flux method, 0.25 mm particles', 127, 'mid'),
    ('Ansys Fluent', 180, 'good'),
]
TRK_ERR = {  # % error simulation vs bench, slide 18 / 19
    'cases': ['Case 1', 'Case 2'],
    'items': [('Collar', -1.9, -4.67), ('Cover', 1.6, -0.9), ('Roller shell', 10.53, 3.58), ('Shaft', 3.33, 3.12), ('Oil', 12.4, 6.0)],
}
DFL_AIR = {'air': [('Before calibration', 0.12), ('After calibration', 0.45), ('Measured', 0.43)],
           'bub': [('Before calibration', 800), ('After calibration', 186), ('Measured', 180)]}
BRG_SEP = [('Low flow rate', 10), ('High flow rate (×2)', 25)]

TAKEAWAYS = [  # proceedings page + blog close
    ('Thermal models closed with a steady CHT', 'Two talks solved oil and metal on separate clocks, in minutes to a day per case, and stated the gap to the bench: about 5–6 °C worst on the pump, up to about 12 % on the roller oil.'),
    ('The reading point changes the number', 'On one sphere the same code returned an HTC of 66 or 169 W/m²K depending on where it was sampled. One air content, 0.65 %, hid bubbles of 132 µm or 68 µm.'),
    ('Calibrate on measured bubbles', 'Optical bubble data took a gearbox aeration model from 0.12 % to 0.45 % air against 0.43 % measured, and from 800 to 186 µm bubbles against 180 µm.'),
    ('Simulation also says what not to do', 'Pelton torque loss and the wear zones of a separator housing were predicted. Doubling the separator flow rate, the obvious fix, raised the sand lost from 10 % to 25 %.'),
]

TALKS = {
'04': dict(
    time='11:45–12:15', tag='Heat', short_org='R&D CFD', topic='pump',
    title='CHT Analysis of a Reciprocating Pump',
    who='Leonardo Lanciotti — R&amp;D CFD S.R.L. – Comet S.p.A. (IT)', speaker='Leonardo Lanciotti', org='R&D CFD S.R.L. – Comet S.p.A. (IT)',
    photo=('leonardo-lanciotti.jpg', 'Leonardo Lanciotti'), pdf='04.R&D-CFD-Leonardo-Lanciotti.pdf',
    lead='An industrial pump bathed in oil, no thermal data on its contacts, and a model that counts as finished only when **the oil neither gains nor loses heat**.',
    context=[
        'Volumetric pumps for food, chemical and waste-water plants run all day at a fixed operating point. What goes wrong first is thermal: seals degrade, components overheat. Inside the pump the oil is the only link between hot and cold parts, and every watt finally leaves through natural convection. R&amp;D CFD, with its customer Comet, wanted a thermal model of the real operating point and a method it can reuse on the next pump.',
        'A fully coupled unsteady run was ruled out: it needs double precision, and sloshing lives in seconds while heat lives in hours, so the run would be far too long. The problem was cut in two. A few seconds of Particleworks sloshing give the heat-transfer map; a steady conjugate-heat-transfer (CHT) solution then converges in minutes.'],
    slideA=('s04-10', 'Why two steps: a short 3D sloshing run feeds a steady CHT, instead of days of unsteady coupling (R&amp;D CFD).'),
    findings=[
        ('Do not guess where the heat is born',
         'Loads on the contacts were not available. Trial and error was rejected as stochastic and unvalidated; a dynamic analysis of the pump with friction coefficients from the literature gave a power split instead, with far fewer free variables. The largest share sits on the piston–block pair, the contact that is also critical in the test.'),
        ('Two independent checks, not one',
         'First the thermocouples, compared one to one at the test positions. Then the oil: it is a heat carrier, not a heat sink, so the heat taken from the shaft must equal the heat given to the housing. If either fails, the power, the oil temperature or the ambient HTC is scaled and the loop restarts.'),
        ('The model shows where the seals suffer',
         'All thermocouples align; the worst, the open-side bearing, is off by about 5–6 °C and points to a local particle refinement as the next step. The shaft sits at 70–80 °C as in the test, and a **hot spot at the piston–seal contact** shows up where seals degrade abnormally in service.'),
        ('Cheap enough to do by hand',
         'Three to five iterations were enough, and a steady CHT takes minutes on a GPU. Once the model exists, a case takes about an hour and a half.')],
    quotes=[
        ('The oil is not a heat sink. All the heat carried by the oil should be exchanged with the other components of the pump, so the balance of the oil should be equal to zero.', 'Leonardo Lanciotti', 1279),
        ('Sometimes the setup is longer than the simulation itself. But, of course, we are talking about one hour and a half once the model is defined.', 'Leonardo Lanciotti', 1220)],
    quote_pos=(1, 3),  # after finding index 1 and 3 (0-based, quote goes after that finding)
    slidesB=[('s04-28', 'Simulated against measured thermocouples at the same positions: the gap is in °C for each one (R&amp;D CFD).')],
    note=dict(text='The oil balance is checked on a uniform surface mesh built from the HTC map. Heat enters the oil from the shaft and leaves it into the housing; the two flows must be equal, so the balance closes to 0 W.',
              eqs=[('Shaft to oil', '<var>Q&#775;</var><sub>shaft&rarr;oil</sub> = <span class="sum">&Sigma;</span><sub><var>i</var></sub> <var>HTC</var><sub><var>i</var></sub> (<var>T</var><sub><var>i</var></sub> &minus; <var>T</var><sub>oil</sub>) <var>A</var><sub><var>i</var></sub>'),
                   ('Oil to housing', '<var>Q&#775;</var><sub>oil&rarr;housing</sub> = <span class="sum">&Sigma;</span><sub><var>j</var></sub> <var>HTC</var><sub><var>j</var></sub> (<var>T</var><sub>oil</sub> &minus; <var>T</var><sub><var>j</var></sub>) <var>A</var><sub><var>j</var></sub>'),
                   ('Closure', '<var>Q&#775;</var><sub>shaft&rarr;oil</sub> &minus; <var>Q&#775;</var><sub>oil&rarr;housing</sub> = 0 <span class="n">W</span>')]),
    keys=['Sloshing and heat are decoupled: seconds of oil, minutes of steady CHT.', 'The oil balance at zero is the check that does not depend on the thermocouples.', 'About 1.5 h per case once the model exists; automation with Python is the natural next step.'],
    findings_pw=['A short Particleworks sloshing run gives the HTC map, a steady CHT converges in minutes: no days-long unsteady coupling.',
                 'The model is closed by two independent checks: thermocouples at the test positions, and an oil heat balance that must be zero.',
                 'Thermal field matches the test: shaft at 70–80 °C, hot spot on the piston seals that degrade in service; the worst thermocouple, the open-side bearing, is off by about 5–6 °C. Three to five manual iterations, about 1.5 h per case.'],
    moments=[(370, 'Why decouple sloshing and CHT'), (432, 'Power split'), (863, 'Results vs thermocouples'), (1011, 'Where it needs refinement'), (1208, 'Q&A: how many iterations?')],
    yt_hook='The oil is not a heat sink: closing a pump thermal model with a steady CHT in an hour and a half per case.'),

'06': dict(
    time='12:45–13:15', tag='Heat', short_org='SKF', topic='bearings',
    title='Integrating Particleworks into SKF Engineering Tools: Part I',
    who='Lijun Cao &amp; Fabrizio Mandrile — SKF (NL)', speaker='Lijun Cao & Fabrizio Mandrile', org='SKF (NL)',
    photo=('lijun-cao.jpg', 'Lijun Cao'), pdf='06.SKF-LIJUN-CAO-HTC.pdf',
    lead='Before trusting a heat-transfer coefficient inside a bearing tool, SKF tested it on the simplest cases that exist, and found that **the answer depends on where you read it**.',
    context=[
        'SKF frames the problem with one number: about 20 % of the world’s energy is lost to friction. Bearings fight friction, but even a good bearing is a source of heat, and temperature then shapes everything: the lubricant film, thermal expansion and the extra load it brings, and life, because every degree more shortens the life of the lubricant and of the bearing.',
        'Thermal analysis is a ladder, from lumped networks that answer in real time, through finite elements with HTCs from analytical formulas, to CFD coupled one way and finally two ways, where answers take days or weeks. SKF’s next rung is one-way: its in-house bearing tool BEAST provides dynamics and heat sources, Particleworks provides the HTC maps. Part I of the study is the verification of those HTCs. Rolling bearings cannot be measured easily, so the references are classic cases: a sphere in a cross-flow, and two concentric cylinders.'],
    slideA=('s06-11', 'The thermal-analysis ladder: from lumped networks to fully coupled CFD, trading speed for accuracy (SKF).'),
    findings=[
        ('One sphere, many answers',
         'The reference is the Whitaker correlation: 184 W/m²K. Particleworks’ local-correlation method reads the velocity of particles next to the wall, which tends to zero there, **so it reports a low HTC**: 66 at the wall, 169 when sampled 1.5 mm away. With coarser particles the default is 85, and raising the Nusselt coefficient lifts it to 192.'),
        ('The heat-flux method converges, at a price',
         'Solving the temperature field and reading the heat flux does not care about mapping distance, and improves with refinement (75 → 127 W/m²K from 0.5 to 0.25 mm, against 180 for Ansys Fluent). But a thermal particle is heavier than a flow-only one, so further refinement was too expensive. Local refinement was disappointing, and is improved in the new release.'),
        ('Concentric cylinders: defaults were enough',
         'Heat transfer here is governed by the vortex pattern, and published correlations each hold only in a parameter range. The vortices appeared **with mostly default settings** (watch the Courant limiter). Across four radius-ratio and speed cases Particleworks sits between −7 % and +28 % of the correlation, a spread comparable with Fluent (−8 % to +17 %).'),
        ('A lucky trial in the field',
         'On a confidential customer case, a large oil system with spherical thrust bearings, SKF simply imported the power loss from its bearing software as a heat source and let Particleworks run. The temperature map was something the customer could relate to.')],
    quotes=[
        ('Imagine if you apply a non-slip condition very close to the wall: the velocity is approaching zero, so you get a very low Reynolds number and therefore a very low HTC. There’s nothing wrong with it. This is just the nature of the method.', 'Lijun Cao', 1488),
        ('We never tried; we just pushed the button and saw what happens with default settings. [...] It worked. [...] Maybe we’re just being lucky in that occasion.', 'Fabrizio Mandrile', 2700)],
    quote_pos=(0, 3),
    chart='sphere', chart_after=1,
    slidesB=[('s06-20', 'Single-sphere results: HTC fields for 0.25 mm and 1 mm particles and the numbers behind the chart (SKF).')],
    note=None,
    keys=['Be conscious of what drives a discrepancy: mapping distance, Nusselt coefficient and refinement each moved the sphere HTC by a factor of two or more.', 'Next: a segmented bearing, ideally with a cyclic boundary condition (requested), then a full bearing with multi-layer refinement.', 'The correlation is a reference, not the truth.'],
    findings_pw=['On a single sphere the HTC (reference 184 W/m²K) depends on how it is read: 66 at the wall, 169 sampled 1.5 mm away; the heat-flux method improves with refinement (127 at 0.25 mm) but is expensive.',
                 'Concentric rotating cylinders: the vortex pattern is reproduced with mostly default settings (watch the Courant limiter); HTC lies between −7 % and +28 % of the literature correlation, against −8 % to +17 % for Ansys Fluent.',
                 'Plan: BEAST supplies dynamics and heat sources, Particleworks the HTC maps; a segmented bearing next, ideally with a cyclic boundary condition, then local refinement for the full bearing.'],
    moments=[(904, 'BEAST + Particleworks'), (1177, 'The two verification models'), (1768, 'HTC read at a distance'), (1861, 'Defaults: 85 vs 184'), (2343, 'Results and the limiter'), (2602, 'Wish: cyclic boundary condition'), (2700, 'The field case')],
    yt_hook='One sphere, five HTC answers: how SKF verified Particleworks heat transfer before plugging it into BEAST.'),

'10': dict(
    time='16:30–17:00', tag='Heat', short_org='TrackOne', topic='roller',
    title='Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method',
    who='Leonardo Tiberi — TrackOne SRL – Unimore (IT)', speaker='Leonardo Tiberi', org='TrackOne SRL – Unimore (IT)',
    photo=('leonardo-tiberi.jpg', 'Leonardo Tiberi'), pdf='10.TRACKONE-LEONARDO-TIBERI.pdf',
    lead='A sealed, partly filled oil bath heats itself as it turns. TrackOne maps its temperatures in about a day per case, and a bench test shows **where the model can be trusted**.',
    context=[
        'The carrier roller holds up the track chain of an excavator. The chain forces the shell to rotate around a fixed shaft; seals, bushings and a partial oil fill keep metal from touching metal. Under load, the friction creates internal thermal peaks, and “if not controlled, the spikes lead to component failure”. The goal was a steady-state temperature map for a given operating case.',
        'Because the oil only partly fills the roller, it is thrown and fragmented against the walls as the shell turns. That, and the narrow passages in cover, bushing and shaft, is why TrackOne, with the Enzo Ferrari engineering department of Unimore, chose a meshless method.'],
    slideA=('s10-05', 'The roller: shell and collars rotate with the chain, the shaft stays fixed to the chassis (TrackOne).'),
    findings=[
        ('Fluid and solid do not share a clock',
         'The oil reaches its pattern in milliseconds, the metal in hours, so a straight unsteady CHT is prohibitive. The answer is an iterative steady CHT with two phases: the oil alone produces average HTC and near-wall temperature maps (a few hours), then the solids alone are solved with those maps (a few minutes). The loop stops when the solid field no longer changes, after three to four iterations.'),
        ('A moving contact, rewritten for a steady model',
         'The chain touches only the top of the roller shell. A steady run with that contact alone would give “an unrealistic and unbalanced temperature map”. TrackOne spreads the cooling over the whole circumference and corrects it with a scale factor τ (footprint area over contact area) and an equivalent thermal contact resistance.'),
        ('Case 1 within about 12 %, case 2 below 7 %',
         'On the bench, with sensors outside and a probe in the oil, case 1 shows good convergence with a slight underestimation of the roller shell and the oil (errors up to about 12 %). Case 2, at higher speed and lower load, is excellent: all errors below 7 %. About one day per case.'),
        ('What is not resolved',
         'In the Q&A the numerics were questioned: the smallest gap, between shaft and bushing, is not resolved with particles. Next steps: oil rheology evolution, coupling with a FEM solver for deformation, and critical operating conditions.')],
    quotes=[
        ('The temporal scale of the fluid was very different from the temporal scale of the solid. So we decided to use an iterative steady-state CHT.', 'Leonardo Tiberi', 593),
        ('There is a good convergence between simulated and bench test temperature, with a slight underestimation of the roller shell and the internal oil temperature.', 'Leonardo Tiberi', 850)],
    quote_pos=(0, 2),
    chart='trk', chart_after=2,
    slidesB=[('s10-18', 'Case 1: simulated against bench temperatures, with the percentage error per component (TrackOne).'), ('s10-19', 'Case 2, higher speed and lower load: errors below 7 % (TrackOne).')],
    note=dict(text='Two closures keep the steady model realistic. The chain loads only the top of the shell, so the cooling is spread over the whole circumference and corrected with a scale factor. Air convection on exposed components follows an analytical law in the component velocity <var>v</var>, and oil viscosity follows an Arrhenius–Vogel law in temperature.',
              eqs=[('Contact scale factor', '&tau; = <var>A</var><sub>footprint</sub> / <var>A</var><sub>contact</sub>'),
                   ('Air convection', '<var>HTC</var><sub>air</sub> = 5.7 + 3.8 &middot; <var>v</var>')]),
    keys=['Phase 1 (oil, hours) and phase 2 (solids, minutes) alternate until the solid field is stable.', 'Errors are reported component by component: up to about 12 % in case 1, below 7 % in case 2.', 'Next: rheology evolution, FEM coupling, critical conditions.'],
    findings_pw=['Oil and metal live on different time scales, so an iterative steady CHT replaces the unsteady one: oil only for the HTC and near-wall temperature maps, then solids only, repeated 3–4 times.',
                 'The chain contacts only the top of the roller shell, so a scale factor and an equivalent contact resistance re-create the real heat path in a steady model.',
                 'Bench test: good convergence in case 1 (errors up to about 12 % on shell and oil), excellent in case 2 (all below 7 %). About one day per case; next rheology evolution and FEM coupling.'],
    moments=[(304, 'Why thermal peaks matter'), (466, 'Viscosity follows temperature'), (593, 'Why steady and iterative'), (638, 'The contact trick'), (726, 'Phase 1 / phase 2'), (850, 'Results vs bench'), (919, 'One day per case')],
    yt_hook='A day per case: an iterative steady CHT predicts the temperature of an excavator carrier roller.'),

'07': dict(
    time='14:30–15:00', tag='Air', short_org='deepfluid', topic='gear oil',
    title='Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems',
    who='Dr. Lukas Hafner — deepfluid (DE), with Gianluca Parma — EnginSoft', speaker='Dr. Lukas Hafner & Gianluca Parma', org='deepfluid (DE) – EnginSoft SpA (IT)',
    photo=('lukas-hafner.jpg', 'Lukas Hafner'), pdf='07.DEEPFLUID-LUKAS-HAFNER-Air-in-Oil_Measurement.pdf',
    lead='Two oils with the same air content can behave very differently. **Calibrate the aeration model on bubbles, not on a percentage.**',
    context=[
        'Air in oil is a multi-scale problem: root causes and effects sit in different places and develop over time. A gas phase changes the density and viscosity of the oil, so efficiency drops; it brings cavitation and NVH problems; it exposes the oil to thermal and chemical stress, with oxidation in the long run; and it makes the lubricant film unreliable where the gear needs it. Particleworks has an aeration module that predicts generation, transport, coalescence and disappearance of bubbles.',
        'What was available until now was a single number, the air content. deepfluid’s optical sensors, in the laboratory, on the test bench and in the field, take snapshots of every bubble and give the bubble count, the size distribution, the mean diameter and the **oil–air contact surface**, with the snapshot as evidence.'],
    slideA=('s07-06', 'Same air content, 0.65 %, two very different bubble populations (deepfluid).'),
    findings=[
        ('One air content, two bubble populations',
         'In scenario A, 361 bubbles of 132 µm offer 18 m² of oil–air surface. In scenario B, 1,289 bubbles of 68 µm offer 32 m² for the same volume of air. The surface is where oxidation happens, so oil aging, cavitation and compressibility differ although the percentage is identical.'),
        ('Measure, calibrate, then simulate',
         'The aeration model has many coefficients, and two things are calibrated: the total amount of air generated and the bubble-size distribution. Simulation then gives the global picture (flow paths, recirculation, aeration hot spots) while the sensor measures what is happening at one point: “measured data does not replace the simulation”.'),
        ('A differential gear, before and after',
         'In a differential gear in a pool of oil, the default coefficients gave 0.12 % air with 800 µm bubbles. After calibration on the measurement: 0.45 % against 0.43 % measured, and 186 µm bubbles against 180 µm. The bubble motion and the recirculation under the gear are visibly better captured.'),
        ('How far does a calibration travel?',
         'Geometry: no problem. Speed: coefficients scale with the velocity ratio from a calibrated reference. Additive package: no, because Particleworks does not solve chemistry; a new additive or anti-foam means a new calibration. Temperature: an open point, and the trend can even change sign from oil to oil.')],
    quotes=[
        ('Those 0.65 percent of air content can look very different: pretty big bubbles with a wide deviation in sizes, or very, very small bubbles all the time. And this changes your system behavior pretty much.', 'Dr. Lukas Hafner', 325),
        ('For one and the same base oil with different additive packages, you can have an increase in air content with an increase in temperature. But with the other one, you get a decrease in air content with an increase in temperature.', 'Dr. Lukas Hafner', 1462)],
    quote_pos=(0, 3),
    chart='dfl', chart_after=2,
    slidesB=[('s07-19', 'Quantitative comparison: air content and bubble-size distribution against the measurement, before and after calibration (deepfluid).')],
    note=None,
    keys=['Calibrate two things: total air generated and bubble-size distribution.', 'Scale with speed from a reference; recalibrate for a new additive package; temperature scaling is open.', 'The sensor complements the simulation: a local measurement against a global view.'],
    findings_pw=['The same air content (0.65 %) can hide 132 µm or 68 µm bubbles, and with them 18 or 32 m² of oil–air contact surface: oxidation, cavitation and compressibility follow the surface.',
                 'The Particleworks aeration model is calibrated on total air and bubble-size distribution: in a differential gear 0.12 % / 800 µm became 0.45 % / 186 µm against 0.43 % / 180 µm measured.',
                 'Coefficients scale with speed and not with geometry; a new additive package needs a new calibration, and the temperature dependence (even its sign) is an open point.'],
    moments=[(325, 'Same air, different bubbles'), (732, 'Calibrating the model'), (858, 'The differential gear'), (1138, 'Before vs after calibration'), (1316, 'Q&A: new additive, new calibration'), (1462, 'Additives and temperature')],
    yt_hook='Same 0.65 % air, 132 µm or 68 µm bubbles: why aeration simulation needs measured bubble data.'),

'05': dict(
    time='12:15–12:45', tag='Wear', short_org='HES-SO', topic='Pelton',
    title='Moving Particle Simulation of Eroded Pelton Runners',
    who='Jean Decaix — HES-SO Valais/Wallis (CH)', speaker='Jean Decaix', org='HES-SO Valais/Wallis (CH)',
    photo=('jean-decaix.jpg', 'Jean Decaix'), pdf='05.HES-JEAN-DECAIX-PELTON-TURBINES-EROSION.pdf',
    lead='Europe’s hydropower is ageing and silting up. HES-SO uses Particleworks to put a number on what sediment erosion costs a Pelton runner in torque.',
    context=[
        'ReHydro is a Horizon Europe project of 18 partners, coordinated by SINTEF, to refurbish and modernise European hydropower. The fleet is about 50 to 55 years old and now has to balance solar and wind, and as glaciers retreat more sediment reaches the turbines. In the worst plants, after a year of operation a Pelton runner can “lose maybe half a bucket”.',
        'A Pelton turbine is an impulse turbine: a water jet hits the buckets and the torque on the shaft is the power. The physics is simple and the machines are huge, so they cannot be tested in a laboratory. Measuring the efficiency of a real runner means stopping production for two or three days, which is why a prediction of the efficiency lost to erosion is worth having.'],
    slideA=('s05-04', 'Sediment and cavitation erosion in hydraulic turbines: from Francis runners to Pelton buckets (HES-SO).'),
    findings=[
        ('Whole revolutions, not fragments',
         'With Particleworks HES-SO can simulate more than one revolution of the runner on a single GPU, where a finite-volume code takes “more than one week”. After four years of use that changed what is feasible: several simulations, not one.'),
        ('Torque converges, and can be extrapolated',
         'For a healthy runner the dimensionless torque rises toward the target as the particles shrink, and a linear extrapolation to zero particle size lands close to it. That means a fast, coarse run can be used to estimate what a very fine one would give.'),
        ('Artificial erosion follows the known trends',
         'Flat, rounded and cut-out erosion reproduce the analytical and published efficiency drops, more closely with finer particles. A rounded erosion collapses onto a laboratory experiment on **another turbine at another scale**, which hints that the effect may not depend on runner size. The worn splitter tip is the exception: the particles are as large as the eroded layer.'),
        ('Real erosion: the loss comes early',
         'Three real runners were computed: new, after three years, after five (when the owner refurbished). The torque decrease is predicted accurately, and **mid-life is already close to end-of-life**: torque drops of 6 % and 6.6 % for the mid-life and end-of-life runners, “we have already lost the main part of efficiency even at stage T2”.')],
    quotes=[
        ('One of the power plants on which we are working in this project, you have the equivalent of a cargo train every year full of sediment that goes through the turbines.', 'Jean Decaix', 278),
        ('It could be one flood event that can make this high level of erosion. So after one flood event, we lost 2%. It’s not a progressive phenomenon.', 'Jean Decaix', 1339)],
    quote_pos=(0, 3),
    slidesB=[('s05-15', 'Dimensionless torque of the three physically eroded runners, T-3 new to T-1 after five years, with the extrapolation to zero particle size (HES-SO).')],
    note=None,
    keys=['Torque loss is predicted, which lets an owner decide whether to refurbish in February or November.', 'Next: partial load, where the drop should be larger, then a runner whose speed responds to load rejection.', 'A brick of a digital twin: what does 2 % of efficiency lost to one flood cost over a year?'],
    findings_pw=['Part of the Horizon Europe ReHydro project (18 partners): predicting the efficiency lost to sediment erosion, without stopping a plant for two or three days.',
                 'Particleworks computes whole runner revolutions in minutes to days on one GPU, where a finite-volume code needs more than a week; the torque extrapolates to zero particle size.',
                 'Torque loss of artificially and physically eroded runners (new, three, five years) is predicted accurately; mid-life already shows most of the loss. Next: partial load and load rejection.'],
    moments=[(70, 'ReHydro: why erosion matters'), (252, 'Half a bucket in a year'), (278, 'A cargo train of sediment'), (417, 'Revolutions in days, not weeks'), (549, 'Extrapolating to zero size'), (689, 'New, 3 years, 5 years'), (1012, 'Mid-life is already end-of-life'), (1196, 'Q&A: load rejection, digital twin')],
    yt_hook='A cargo train of sediment a year: predicting how erosion cuts Pelton runner torque with Particleworks.'),

'11': dict(
    time='17:00–17:30', tag='Wear', short_org='Börger', topic='separator',
    title='Simulation of Sand Separation and Wear in the Börger FlowSep',
    who='Bernd Valtwies — Börger GmbH (DE) &amp; Riccardo Sala — EnginSoft (IT)', speaker='Bernd Valtwies & Riccardo Sala', org='Börger GmbH (DE) – EnginSoft SpA (IT)',
    photo=('bernd-valtwies.jpg', 'Bernd Valtwies'), pdf='11.BORGER-BERND-VALTWIES.pdf',
    lead='A sand separator for biogas plants, simulated before its second prototype: the model showed where the sand escapes, why **more flow is worse**, and where the housing wears.',
    context=[
        'Biogas plants used to be fed with energy crops, a clean medium. Today they run on manure, and with it come sand, stones and soil. In the example shown, 1.9 m of sand settled in 36 months in a 16 m tank: about 1,000 tons. It blocks pipes, defeats the mixers, shrinks the usable volume, blocks the slurry tankers, and is expensive special waste to dig out.',
        'Börger’s BioSelect separator already removes fibres larger than 0.5 mm. The new FlowSep adds centrifugal forces to remove the sand below that size before the final tank. The first mock-up worked immediately; the open questions for the prototype were the geometry, the throughput that still gives an acceptable result, and where the machine wears. EnginSoft built a Particleworks and Granuleworks model, with Börger measuring flows, densities, ash content (burnt at 800 °C) and particle fractions.'],
    slideA=('s11-05', 'The problem: sand in the final storage tank of a biogas plant, 1.9 m after 36 months (Börger).'),
    findings=[
        ('Where the sand escapes',
         'About 10 % of the sand leaves through the clean outlet, close to what the tests showed, and **only the small particles**: large ones are centrifuged outward, as intended. The model shows the path: particles pushed onto the back plate recirculate, and where two opposed fluxes meet a particle that drifts slightly is sucked out with the water. That points straight at a geometry change.'),
        ('More flow, less separation',
         'Börger’s first idea was to raise the flow rate. At twice the flow the sand not separated grows from about 10 % to about 25 %, with more of the coarse fraction reaching the clean phase. “It’s better to go slower and separate better”, or change the geometry: radius, length, motor size.'),
        ('Where the housing wears',
         'Wall interaction was read from the particle number density within 1 mm of the wall together with velocity. It flags the area near the blades and the back plate, and the prototype, after about half a year of round-the-clock operation, showed strong erosion exactly there. With version 9 the force on the wall is the more direct indicator.'),
        ('Fewer prototypes',
         'Each prototype costs a lot, and the simulation says early which change makes sense, widening the radius or lengthening the unit, before steel is cut.')],
    quotes=[
        ('In a timeline of 36 months, they have had an average of 1.9 meters height of sand. [...] In a container with a diameter of 16 meters, we are talking about 1,000 tons of sand.', 'Bernd Valtwies', 353),
        ('At the beginning, the idea of Börger was: let’s just increase the flow rate, we will be faster, everything will be good. But then, with this simulation, we realized that it’s not possible. It’s better to go slower and separate better.', 'Riccardo Sala', 1544)],
    quote_pos=(0, 1),
    chart='brg', chart_after=1,
    slidesB=[('s11-27', 'Simulation: high sand interaction at the housing near the blades and at the back plate (Börger, EnginSoft).'), ('s11-30', 'The prototype housing: “the wear pattern corresponds to simulation” (Börger).')],
    pair=True,
    note=None,
    keys=['Of the sand that escapes, the small particles are the problem; the geometry can be changed to catch them.', 'Higher flow rate: bad separation 10 % → 25 %.', 'Simulated wear zones match the prototype: blades and back plate.'],
    findings_pw=['Sand in biogas storage tanks (1.9 m in 36 months, about 1,000 tons) blocks pipes and shrinks volume; the FlowSep removes sand below 0.5 mm with centrifugal force before the final tank.',
                 'About 10 % of the sand leaves the clean outlet, only the small particles, close to the tests; at twice the flow rate the sand badly separated rises to about 25 %.',
                 'Simulated wear zones at the back plate and near the blades match the prototype after about half a year of round-the-clock use; with version 9, use the force on the walls.'],
    moments=[(330, 'The sand problem'), (353, '1.9 m of sand'), (619, 'How the FlowSep works'), (1364, 'Who leaks'), (1495, 'Higher flow rate'), (1544, 'Faster is not better'), (1601, 'The wear map'), (1661, 'Prototype wear'), (1811, 'With 9.0: wall force')],
    yt_hook='Faster is not better: simulating sand separation and wear in a biogas separator before the second prototype.'),
}

ORDER = ['04', '06', '10', '07', '05', '11']   # blog + proceedings order


# ---- slides-only talks (no recording): written from the speakers' released slides only; numbers checked against the slide tables ----
# Used by _gen_blog_pwexp2026.py. `rec=False`: no video moments, no quotes.
SLIDES_ONLY = {
'08': dict(
    tag='Air', short_org='IAV', topic='e-drivetrain', rec=False,
    title='Air Bubble Dynamics in the Gear Oil of an Electric 3-Speed Drivetrain',
    who='René Kockisch — IAV GmbH (DE)', speaker='René Kockisch', org='IAV GmbH (DE)',
    photo=('rene-kockisch.jpg', 'René Kockisch'), pdf='08.IAV-RENE-KOCKISCH_Air_Bubble_Dynamics.pdf',
    lead='In the gear oil of a real e-drivetrain, **more than half of the air in the target box started at one wall**, behind one shaft. An oil guide there cut the air in the box by 62&nbsp;%.',
    context=[
        'Air in the gear oil of an electric drivetrain changes lubrication, efficiency and durability. IAV, an engineering partner for powertrain systems, uses Particleworks for the oil level, the oil paths and flow rates, oil velocities, bearing lubrication, indications for heat-transfer coefficients, churning losses and air inclusion.',
        'The case was IAV\'s 3-speed electric commercial-vehicle powertrain, with a maximum input torque of 1,500 Nm. The model has 33 relevant model groups that mirror the transmission assembly, and it aims at the oil behavior and the air content in the suction area of the pump. A 1D thermal model and a 1D hydraulic model supply the inflows, six at the oil gallery for gear lubrication and one at the second intermediate shaft, and the pump is the outflow.',
        'In the coupled MPS/DEM run with Particleworks and Granuleworks, air is a set of DEM particles. Reading thousands of short-lived particles is the hard part, so IAV built a tool for it, the IAV Particle Explorer.'],
    slideA=('s08-17', 'The IAV Particle Explorer: input data, particle graphics, diagrams, and initial against final particle counts with and without one-time particles (IAV).'),
    findings=[
        ('Filter the noise first',
         'Some air particles exist for only a very short time. Counting them would mislead, so the Particle Explorer detects these one-time particles and shows the initial and final counts with and without them.'),
        ('Give every air particle a source',
         'The tool traces particles back to the area where they started and counts them per area; DEM and MPS particles can both be assigned to a source. A target box and a set of source boxes turn a cloud of particles into numbers, here for the first 25 s of simulated time.'),
        ('One wall behind one shaft',
         'With three source boxes, the target box held 83,187 air particles. 46,704 of them started at the backside wall behind the intermediate shaft (blue box), 2,370 at the backside wall behind the input shaft (brown) and 2,152 inside the covered final drive (green). **More than half of the air came from one source**; the rest started elsewhere.'),
        ('A small measure, and its count',
         'An oil guide for the lower intermediate shaft, meant to reduce oil splash and with it the air taken into the oil, brought the target box down to 31,781 air particles, **62&nbsp;% fewer**. The blue source fell to 0, the green to 275 and the brown to 214.')],
    chart='iav', chart_after=2,
    slidesB=[('s08-19', 'Before the measure: 83,187 air particles in the target box; green source 2,152, blue 46,704, brown 2,370 (IAV).'),
             ('s08-20', 'With the oil guide for the lower intermediate shaft: 31,781 in the target box; green 275, blue 0, brown 214 (IAV).')], pair=True,
    keys=['The coupled MPS/DEM process follows the air bubbles from formation to dissolution in detail.',
          'The IAV Particle Explorer turns transient particle behavior into countable analytics for each source.',
          'In this e-transmission **one source gave more than half of the air** in the target box, and an oil guide cut the total by 62&nbsp;%.'],
),
'09': dict(
    tag='Air', short_org='Univance', topic='chain and gear oil', rec=False,
    title='Gear Lubrication Analysis, and Its Expansion to R&amp;D on Airflow Effects',
    who='Naohiro Fujita — Univance Corporation (JP)', speaker='Naohiro Fujita', org='Univance Corporation (JP)',
    photo=('naohiro-fujita.jpg', 'Naohiro Fujita'), pdf='09.UNIVANCE-NAHOIRO-FUJITA-gearbox.pdf',
    lead='Univance checks its oil splash **in the design phase**, and now at a scale of **110 million particles**: a chain case 262 times the size of an earlier one, and a gear studied with oil and air as particles.',
    context=[
        'Univance is a Japanese drivetrain supplier, founded in 1937, with about 2,000 employees and products from transmissions and 4WD units to electric powertrain parts. CAE starts early in its V-model development, and Particleworks is mainly used in the design phase. The reasons given: lubrication reduces friction and wear and removes heat, physical tests show little of the oil flow inside a gearbox, and a late issue can mean a costly redesign.',
        'Two earlier cases show the routine use. A gear oil splash (200 rpm, 15 s, 800,000 particles of 3 mm, 12 hours on four K40 GPUs) was evaluated more than ten times in design before release, and its oil flow agreed with the experiment. A transfer-case chain (75 rpm, 3.0 s, 420,000 particles of 0.8 mm, 30 hours) also agreed with the experiment. Both cases shortened development and saved prototypes and tests.'],
    slideA=('s09-10', 'Chain oil splash at 325 rpm: 110 million particles of 0.4 mm, 6.0 s in 45 hours on four GPUs (Univance).'),
    findings=[
        ('A chain case 262 times bigger',
         'The earlier chain case had 420,000 particles of 0.8 mm and ran 3.0 s in 30 hours on four K40 GPUs. The 2026 case has 110 million particles of 0.4 mm and runs 6.0 s in 45 hours on four Blackwell GPUs. Oil penetrates between the links, a film forms on the inner wall of the case and flows down, and the air trapped during the tossing stays stagnant.'),
        ('At 6,500 rpm, air matters',
         'The same kind of chain at 6,500 rpm, 0.3 s in 46 hours, with oil and air as separate phases, makes the effect of the airflow on oil distribution and lubrication visible.'),
        ('Airflow explained what the camera saw',
         'On a test gear pair, Univance dropped oil on the gear and filmed it with a high-speed camera while PIV (particle image velocimetry) measured the air. Oil avoided the rotating gear, slid over the tooth tip, partly stuck to the teeth or was drawn into the mesh. An MPS–FVM coupled simulation reproduced the curved oil trajectory and the upward airflow, and the air velocities in the air curtain agree with the PIV measurements.'),
        ('Then oil and air as particles',
         'MPS–FVM coupling struggled with thin oil films, full-system models and stability. Univance moved to a gas-liquid two-phase analysis with oil and air as particles: 10,000 rpm, 5.0 s, 0.3 mm for both phases, 84 hours on four Blackwell GPUs in single precision (the coupled run before it: 6,000 rpm, 5.0 s, 0.5 mm, 48 hours on two A100). The splash patterns at 3,000 and 10,000 rpm and the airflow structures were reproduced.')],
    chart='univ', chart_after=0,
    slidesB=[('s09-11', 'The chain at 6,500 rpm: oil and air phases combined, then each phase on its own (Univance).'),
             ('s09-25', 'Oil splash patterns at 3,000 and 10,000 rpm: experiment against the two-phase simulation (Univance).')], pair=True,
    keys=['Particleworks supports design-phase lubrication checks: more than ten evaluations of one gear case before release.',
          'A chain case grew from 420,000 to **110 million particles** on four GPUs: twice the simulated time in 1.5 times the run time.',
          'Airflow explains the oil behavior seen with a high-speed camera and PIV: curved trajectories and an upward air stream in the mesh.'],
),
}
