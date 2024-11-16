from init import app
from flask import url_for, redirect, render_template


@app.route('/home')
def Home():
    return render_template("home.html", title="Home")