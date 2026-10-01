"""Renders every template to plain HTML in static-preview/ so you can double-click them.
Run once:  python build_static_preview.py   (needs: pip install flask)
"""
import os, re, glob
from preview import app, ALIAS

OUT = "static-preview"
os.makedirs(OUT, exist_ok=True)
pages = {"/": "index.html", "/login": "auth-login.html", "/register": "auth-register.html"}
for f in glob.glob("templates/*/*.html"):
    role, name = f.split("/")[1], os.path.basename(f)[:-5]
    if role in ("citizen", "worker", "admin"):
        pages[f"/{role}/{name}"] = f"{role}-{name}.html"
        for a, real in ALIAS.items():
            if real == name: pages[f"/{role}/{a}"] = f"{role}-{name}.html"
c = app.test_client()
for url, fn in pages.items():
    if url.startswith(("/citizen/pickup-request",)): continue
    html = c.get(url).get_data(as_text=True)
    html = html.replace('href="/static/', 'href="../static/').replace('src="/static/', 'src="../static/')
    html = re.sub(r'href="(/[^"#]*)"', lambda m: f'href="{pages.get(m.group(1), m.group(1))}"', html)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
print("Done ->", OUT, "| open static-preview/index.html")
