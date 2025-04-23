from flask import Flask, render_template

app = Flask(__name__, static_folder="templates/product", template_folder="templates")

@app.route("/")
def home():
    return render_template("pages/product.html")

if __name__ == "__main__":
    app.run(debug=True)
