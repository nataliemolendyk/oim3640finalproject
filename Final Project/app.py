from flask import Flask, render_template, request
from flight import (
    get_lat_lng,
    get_drive_time,
    get_flights_grouped,
    get_next_flight,
    MAPBOX_TOKEN
)

app = Flask(__name__)

BOSTON_LAT = 42.3656
BOSTON_LNG = -71.0096


@app.get("/flight")
def home():
    return render_template("flight.html", flights={})


@app.post("/flight")
def search():

    origin = request.form.get("origin")
    destination = request.form.get("destination")

    if not origin or not destination:
        return render_template("flight.html", flights={}, error="Missing input")

    o_lat, o_lng = get_lat_lng(origin)

    flights = get_flights_grouped(destination)
    next_flight = get_next_flight(flights)

    drive_time = get_drive_time(o_lat, o_lng, BOSTON_LAT, BOSTON_LNG)

    return render_template(
        "flight.html",
        mapbox_token=MAPBOX_TOKEN,
        origin_lat=o_lat,
        origin_lng=o_lng,
        flights=flights,
        next_flight=next_flight,
        drive_time=drive_time,
        origin=origin,
        destination=destination
    )


if __name__ == "__main__":
    app.run(debug=True)