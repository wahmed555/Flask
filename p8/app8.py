# URL 4 is used invaigation bar for redirection , path navigation and path route
from flask import Flask, render_template, \
url_for

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