from flask import render_template

@app.route('/')
def homepage():
    return render_template('Index.html')