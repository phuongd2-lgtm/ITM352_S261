# Application that allows user to login. If login credentials are correct,
# The user is welcomed. If not, an error message is displayed.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def home():
    return render_template("index.html")

app.route("login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        #Replace this with your actual authentication logic
        if USERS.get(username) == password:
            return redirect(url_for("success"), username=username)
        else:
            return render_template("Sorry bud.Try again")
    else:
        return render_template("login.html")
@app.route("/success/<username>")
def success(username):
    return render_template("success.html", username=username)
       

USERS = {"port": "port123",
        	  "kazman": "kazman123"}


if __name__ == "__main__":
    app.run(debug=True)


