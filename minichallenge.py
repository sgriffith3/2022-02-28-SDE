#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests
from flask import Flask


app = Flask(__name__)

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def get_astros():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    helmetson = groundctrl.json()

    print("\n\nConverted Python data")
    return helmetson

@app.route("/")
@app.route("/<craft>")
def craft_crew(craft="ISS"):
    people = get_astros()["people"]
    crew = []
    for astro in people:
        if craft == astro["craft"]:
            crew.append(astro["name"])
    print(crew)
    return "\n".join(crew)


if __name__ == "__main__":
    app.run(port=2224, host="0.0.0.0")

