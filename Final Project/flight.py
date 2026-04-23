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


def haversine(lat1, lng1, lat2, lng2):
    R = 3958.8

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def get_flight_info(flight_number):
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": AVIATION_TOKEN,
        "flight_iata": flight_number
    }

    r = requests.get(url, params=params)
    data = r.json()

    flights = data.get("data", [])
    if not flights:
        raise ValueError("Flight not found")

    flight = flights[0]

    return {
        "airport": flight["arrival"]["airport"],
        "terminal": flight["arrival"].get("terminal"),
        "gate": flight["arrival"].get("gate")
    }

def get_drive_time(start_lat, start_lng, end_lat, end_lng):
    url = f"https://api.mapbox.com/directions/v5/mapbox/driving/{start_lng},{start_lat};{end_lng},{end_lat}"

    params = {
        "access_token": MAPBOX_TOKEN,
        "overview": "false"
    }

    r = requests.get(url, params=params)
    data = r.json()

    routes = data.get("routes", [])
    if not routes:
        raise ValueError("No route found")

    duration_sec = routes[0]["duration"]
    return duration_sec / 60  # minutes

LOGAN_TERMINALS = {
    "A": (42.3656, -71.0202),
    "B": (42.3662, -71.0170),
    "C": (42.3643, -71.0175),
    "E": (42.3650, -71.0096)
}

def get_trip_info(start_location, flight_number):
    start_lat, start_lng = get_lat_lng(start_location)
    
    flight = get_flight_info(flight_number)

    terminal = flight["terminal"]
    gate = flight["gate"]

    if terminal not in LOGAN_TERMINALS:
        raise ValueError("Unknown terminal")

    end_lat, end_lng = LOGAN_TERMINALS[terminal]

    drive_time = get_drive_time(start_lat, start_lng, end_lat, end_lng)

    return {
        "terminal": terminal,
        "gate": gate,
        "drive_time_minutes": round(drive_time, 1)
    }