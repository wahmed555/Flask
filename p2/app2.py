<<<<<<< HEAD
# Multi Route 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
     return '<h1> hello world </h1>'


@app.route("/about")
def index2():
    return '<h1>About Us Page </h1>'


=======
# Multi Route 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
     return '<h1> hello world </h1>'


@app.route("/about")
def index2():
    return '<h1>About Us Page </h1>'


>>>>>>> 6cd3eb2934989fdf7c04f35cce60577cf06dc7de
app.run(debug=True)