import random
import string
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return "Howdy neighbor!"


@app.route("/rando")
def rando_str():
    s = ""
    for i in range(10):
         s += random.choice(string.ascii_letters)
    return s

if __name__ == "__main__":
    app.run(port=2224, host="0.0.0.0")
