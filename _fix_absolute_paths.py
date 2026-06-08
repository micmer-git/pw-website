"""Normalize absolute href/src/url paths in pages I've touched.

GitHub Pages serves this site at /pw-website/, so leading-slash paths
like href="/index.html" resolve to micmer-git.github.io/index.html
(404). Making them relative works both on github.io and on the
custom root domain (particleworks-europe.com).

Safe transformations only:
  href="/foo..."  ->  href="foo..."     (root pages)
  src="/foo..."   ->  src="foo..."      (root pages)
  url('/foo...')  ->  url('foo...')     (root pages)
  href="/foo..."  ->  href="../foo..."  (applications/ pages)

Skips:
  "//external.com" (protocol-relative)
  "/" (site root only) — though there aren't any
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent

ROOT_PAGES = [
    'civil-engineering-and-fire-prevention.html',
    'clutches-and-brakes.html',
    'cutting-tools.html',
    'e-motors.html',
    'engines-and-pistons.html',
    'gearboxes-and-bearings.html',
    'mixing-and-separation.html',
    'sterilization-food-and-consumer-goods.html',
    'vehicle-management.html',
    'SPH-MPS.html',
    'index.html',
]

APP_PAGES = [
    'applications/civil-engineering.html',
    'applications/clutches-and-brakes.html',
    'applications/cutting-tools.html',
    'applications/e-motors.html',
    'applications/engines-and-pistons.html',
    'applications/gearboxes-and-bearings.html',
    'applications/mixing-and-separation.html',
    'applications/sterilization-food-consumer.html',
    'applications/vehicle-management.html',
]

# Pattern: leading slash followed by [a-zA-Z] (so it doesn't match "//" or "/")
HREF = re.compile(r'(href|src)="/([a-zA-Z])')
URL_SQ = re.compile(r"url\('/([a-zA-Z])")
URL_DQ = re.compile(r'url\("/([a-zA-Z])')

def strip_leading_slash(html: str) -> str:
    html = HREF.sub(r'\1="\2', html)
    html = URL_SQ.sub(r"url('\1", html)
    html = URL_DQ.sub(r'url("\1', html)
    return html

def to_parent_path(html: str) -> str:
    html = HREF.sub(r'\1="../\2', html)
    html = URL_SQ.sub(r"url('../\1", html)
    html = URL_DQ.sub(r'url("../\1', html)
    return html

def main():
    changed = 0
    for f in ROOT_PAGES:
        p = ROOT / f
        if not p.exists():
            print(f'missing {f}')
            continue
        html = p.read_text(encoding='utf-8')
        new = strip_leading_slash(html)
        if new != html:
            p.write_text(new, encoding='utf-8')
            changed += 1
            print(f'fixed (root) {f}')
    for f in APP_PAGES:
        p = ROOT / f
        if not p.exists():
            print(f'missing {f}')
            continue
        html = p.read_text(encoding='utf-8')
        new = to_parent_path(html)
        if new != html:
            p.write_text(new, encoding='utf-8')
            changed += 1
            print(f'fixed (app) {f}')
    print(f'total changed: {changed}')

if __name__ == '__main__':
    main()
