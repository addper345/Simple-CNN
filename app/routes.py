from app import app
from flask import render_template

@app.route("/")
def grid():
    return render_template('index.html')