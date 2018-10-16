# RENDER tEMPLATE along with Jinja {% include %}

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     return render_template('index.html')

@app.route("/aboutus")
def index2():
    return render_template('aboutus.html')

# @app.route("/aboutus/<name>")
# def index3(name):
#     return render_template('index.html',name=name)

app.run(debug=True)