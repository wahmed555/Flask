<<<<<<< HEAD
# Multiple Line Return using  \ or """ """

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     return '<h1> hello world </h1> \
       Ali is Nice person '

@app.route("/aboutus")
def index2():
    return """ Our Farm and Agriculture Firms are  here since 1980 
                  Mitcheles is knows for its Fruit Farms and Jellys"""

=======
# Multiple Line Return using  \ or """ """

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     return '<h1> hello world </h1> \
       Ali is Nice person '

@app.route("/aboutus")
def index2():
    return """ Our Farm and Agriculture Firms are  here since 1980 
                  Mitcheles is knows for its Fruit Farms and Jellys"""

>>>>>>> 6cd3eb2934989fdf7c04f35cce60577cf06dc7de
app.run(debug=True)