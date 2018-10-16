<<<<<<< HEAD
# P1  Hello World #
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'HELLO WORLD!'

=======
# P1  Hello World #
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'HELLO WORLD!'

>>>>>>> 6cd3eb2934989fdf7c04f35cce60577cf06dc7de
app.run(debug=True)