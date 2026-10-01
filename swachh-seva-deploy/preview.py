"""UI preview server (does not touch the real backend).
Run:  python preview.py   ->  open http://127.0.0.1:5000
"""
import os
from flask import Flask, render_template, abort

app = Flask(__name__, template_folder="templates", static_folder="static")
ALIAS = {"request-pickup": "pickup-request"}   # nav URL -> template name


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("auth/login.html")


@app.route("/register")
def register():
    return render_template("auth/register.html")


@app.route("/<role>/<page>")
def page(role, page):
    if role not in ("citizen", "worker", "admin"):
        abort(404)
    page = ALIAS.get(page, page)
    path = os.path.join(app.template_folder, role, page + ".html")
    if not os.path.isfile(path):
        abort(404)
    return render_template(f"{role}/{page}.html")


@app.errorhandler(404)
def e404(_):
    return render_template("errors/404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
