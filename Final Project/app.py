from flask import Flask, render_template, request
from flight import get_lat_lng, get_flights_from_boston, MAPBOX_TOKEN

app = Flask(__name__)


@app.get("/flight")
def flight_page():
    return render_template("flight.html")


@app.post("/flight")
def flight_submit():
    place = request.form.get("place")

    if not place:
        return render_template("flight.html", error="Enter a location")

    try:
        start_lat, start_lng = get_lat_lng(place)

        # Boston Logan Airport
        end_lat = 42.3656
        end_lng = -71.0096

        flights = get_flights_from_boston()

        return render_template(
            "flight.html",
            mapbox_token=MAPBOX_TOKEN,
            start_lat=start_lat,
            start_lng=start_lng,
            end_lat=end_lat,
            end_lng=end_lng,
            flights=flights,
            place=place
        )

    except ValueError as e:
        return render_template("flight.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)