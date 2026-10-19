"""Shared post-event chrome for the Experience microsite: nav and footer without Program / Registration."""
import re


def fix_nav(s):
    s = re.sub(r'\s*<li class="nav-item"><a class="nav-link" href="program\.php">Oct 7 · Program</a></li>', '', s)
    s = re.sub(r'<li class="nav-item ms-lg-2"><a class="nav-link nav-register" href="registration\.php">Register</a></li>',
               '<li class="nav-item ms-lg-2"><a class="nav-link nav-register" href="proceedings2026.php">Proceedings 2026</a></li>', s)
    s = s.replace('<li><a class="dropdown-item" href="proceedings2026.php"><i class="bi bi-unlock"></i> Proceedings 2026</a></li>\n              ', '')
    s = re.sub(r'\s*<li class="nav-item"><a class="nav-link[^"]*" href="proceedings2026\.php">Proceedings 2026</a></li>(?=\s*<li class="nav-item dropdown">)', '', s)
    return s


def fix_footer(s):
    s = s.replace('<li class="mb-2"><a href="program.php">Program (Oct 7)</a></li>', '<li class="mb-2"><a href="proceedings2026.php">Proceedings 2026</a></li>')
    s = re.sub(r'\s*<li class="mb-2"><a href="registration\.php">Registration</a></li>', '', s)
    s = re.sub(r'\s*<li class="mb-2"><a href="https://particleworks-europe\.com/experience/call-for-abstract">Call for papers</a></li>', '', s)
    s = re.sub(r'\s*<li class="mb-2"><a href="proceedings2026\.php">Proceedings 2026</a></li>(\s*<li class="mb-2"><a href="proceedings2026\.php">Proceedings 2026</a></li>)', r'\1', s)
    return s
