from flask import Flask, render_template, request
import lookup

application = Flask(__name__)

@application.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@application.route("/location", methods=["POST"])
def get_location():
    address = request.form["address"]
    if len(address) == 0:
        data = lookup.process_coords(request.form["lat"], request.form["lng"])
    else:
        data = lookup.process_address(address)
    return render_template("location.html", data=data)

if __name__ == "__main__":
    application.run()
