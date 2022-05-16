#Chapter 18 Flask

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index() :
    return "<font color=\"red\">Hello WORLD !</font>"

app.run(port=8000)
