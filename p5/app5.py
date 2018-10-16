# SIMPLE RENDER TEMPLATE

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     return '<h1> hello world </h1> \
       Ali is Nice person '

@app.route("/aboutus")
def index2():
    return render_template('index.html')



app.run(debug=True)