from flask import Flask, render_template


app = Flask(__name__)


myvar = "Welcome to My Webpage"
nav_ee = [{"href": "http://example.com", "caption": "just an example site"}, {"href": "http://anotherexample.com", "caption": "another example"}]

@app.route("/")
def fill_it_out():
    return render_template("templ.example.html", a_variable=myvar, navigation=nav_ee)


if __name__ == "__main__":
    app.run(port=2224)

