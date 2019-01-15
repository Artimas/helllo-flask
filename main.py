from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="first_name">First Name:</label>
            <input type="text" id="first_name" name="first_name" />
            <input type="submit"/>

        </form>
</html>
"""

@app.route("/")
def index():

    return form

@app.route("/hello", methods=["post"])
def hello():
    first_name = request.form["first_name"]
    return "<h1>Hello " + first_name + "</h1"

app.run()