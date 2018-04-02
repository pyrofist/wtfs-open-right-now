from flask import Flask, render_template, request

application = Flask(__name__)

@application.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@application.route("/location", methods=["POST"])
def lookup():
    address = request.form["address"]
    return render_template("location.html", location=address)

if __name__ == "__main__":
    application.run()
