from flask import Flask, render_template
@app.route("/")
def homepage():
    return render_template("index.html")  # Looks for index.html inside the templates folder