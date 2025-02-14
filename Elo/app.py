from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/product-design')
def product_design():
    return render_template('product-design.html')

if __name__ == '__main__':
    app.run(debug=True)