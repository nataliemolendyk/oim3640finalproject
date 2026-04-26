import os
import requests
import dotenv
import math

dotenv.load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")
AVIATION_TOKEN = os.getenv("API_AVIATION_KEY")


def get_lat_lng(place_name):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"

    params = {
        "access_token": MAPBOX_TOKEN,
        "limit": 1
    }

    r = requests.get(url, params=params)
    data = r.json()

    if not data.get("features"):
        raise ValueError("No location found")

    lng, lat = data["features"][0]["geometry"]["coordinates"]
    return float(lat), float(lng)


def get_flights_from_boston():
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": AVIATION_TOKEN,
        "dep_iata": "BOS"
    }

    r = requests.get(url, params=params)
    data = r.json()

    flights = data.get("data", [])
    if not flights:
        raise ValueError("No flights found")

    results = []
    for f in flights[:8]:
        results.append({
            "flight": f["flight"]["iata"],
            "destination": f["arrival"]["airport"],
            "status": f.get("flight_status")
        })

    return results