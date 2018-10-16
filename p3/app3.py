<<<<<<< HEAD
#  Dynamic <argument> 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
     return '<h1> hello world </h1> \
       Ali is Nice person '

@app.route("/<name>")
def index2(name):
    return '<h1> hello,{} </h1>'.format(name)


=======
#  Dynamic <argument> 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
     return '<h1> hello world </h1> \
       Ali is Nice person '

@app.route("/<name>")
def index2(name):
    return '<h1> hello,{} </h1>'.format(name)


>>>>>>> 6cd3eb2934989fdf7c04f35cce60577cf06dc7de
app.run(debug=True)