"""All 11 talks of Particleworks Experience 2026 in programme order, for the open list on the proceedings page.
status: 'form' = slides + recording after the form; 'slides' = slides only after the form; 'none' = speaker did not release slides; 'later' = released on a later date."""
PROGRAMME = [
    ('01', 'speakers/iori-saigo.jpg', 'Particleworks 9.0 &amp; Granuleworks 4.0', 'Issei Masaie &amp; Iori Saigo', 'Prometech Software (JP)', 'slides', ''),
    ('03', 'speakers/alpcan-guray.jpg', 'Simulation of Shot Peening: A CFD-DEM Coupled Case Study', 'Alpcan Güray', 'MTU Aero Engines AG (DE)', 'none', ''),
    ('02', 'speakers/michelangelo-raimondo.jpg', 'An Integrated Simulation Approach for Stator Oil Jacket and Jet Cooling Systems', 'Michelangelo Raimondo', 'University of Modena and Reggio Emilia (IT)', 'later', 'January 2027'),
    ('04', None, None, None, None, 'form', ''),
    ('05', None, None, None, None, 'form', ''),
    ('06', None, None, None, None, 'form', ''),
    ('07', None, None, None, None, 'form', ''),
    ('08', 'speakers/rene-kockisch.jpg', 'From Formation to Dissolution: Air Bubble Dynamics in Gear Oil of an Electric 3-Speed Commercial Vehicle Drivetrain', 'René Kockisch', 'IAV GmbH (DE)', 'slides', ''),
    ('09', 'speakers/naohiro-fujita.jpg', 'Application of Particleworks to Gear Lubrication Analysis and Its Expansion to R&amp;D on Airflow Effects', 'Naohiro Fujita', 'Univance Corporation (JP)', 'slides', ''),
    ('10', None, None, None, None, 'form', ''),
    ('11', None, None, None, None, 'form', ''),
]
STATUS = {
    'form': 'Slides and recording after the form',
    'slides': 'Slides after the form, no recording',
    'none': 'Slides not available',
    'later': 'Slides and recording: ',
}
