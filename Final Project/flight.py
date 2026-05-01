import os
import requests
import dotenv
from collections import defaultdict

dotenv.load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")
AVIATION_TOKEN = os.getenv("AVIATION_API_KEY")
AIRLABS_KEY = os.getenv("AIRLABS_API_KEY")


# ----------------------------
# GEO
# ----------------------------
def get_lat_lng(place):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json"

    r = requests.get(url, params={
        "access_token": MAPBOX_TOKEN,
        "limit": 1
    })

    data = r.json()
    lng, lat = data["features"][0]["geometry"]["coordinates"]
    return float(lat), float(lng)


# ----------------------------
# DRIVE TIME
# ----------------------------
def get_drive_time(a, b, c, d):
    url = f"https://api.mapbox.com/directions/v5/mapbox/driving/{b},{a};{d},{c}"

    r = requests.get(url, params={"access_token": MAPBOX_TOKEN})
    data = r.json()

    routes = data.get("routes", [])
    if not routes:
        return None

    return round(routes[0]["duration"] / 60, 1)


# ----------------------------
# AIRPORT MAP
# ----------------------------
AIRPORT_CITY = {
    "BOS": "Boston",
    "JFK": "New York",
    "LGA": "New York",
    "EWR": "New York",
    "LAX": "Los Angeles",
    "SFO": "San Francisco",
    "ORD": "Chicago",
    "LHR": "London",
    "CDG": "Paris",
    "AMS": "Amsterdam",
    "HND": "Tokyo",
    "NRT": "Tokyo",
    "DXB": "Dubai"
}


# ----------------------------
# SAFE PICK
# ----------------------------
def pick(*values):
    for v in values:
        if v not in [None, "", "—"]:
            return v
    return None


# ----------------------------
# API CALLS
# ----------------------------
def get_aviation():
    try:
        r = requests.get(
            "http://api.aviationstack.com/v1/flights",
            params={
                "access_key": AVIATION_TOKEN,
                "dep_iata": "BOS",
                "limit": 30
            },
            timeout=5
        )
        return r.json().get("data", [])
    except:
        return []


def get_airlabs():
    try:
        r = requests.get(
            "https://airlabs.co/api/v9/flights",
            params={
                "api_key": AIRLABS_KEY,
                "dep_iata": "BOS"
            },
            timeout=5
        )
        return r.json().get("response", [])
    except:
        return []


# ----------------------------
# PARSERS
# ----------------------------
def parse_aviation(f):
    flight = f.get("flight", {})
    arr = f.get("arrival", {})

    return {
        "flight": flight.get("iata"),
        "destination": arr.get("iata"),
        "status": f.get("flight_status")
    }


def parse_airlabs(f):
    return {
        "flight": f.get("flight_iata"),
        "destination": f.get("arr_iata"),
        "status": f.get("status")
    }


# ----------------------------
# STRICT FILTER + GROUPING
# ----------------------------
def get_flights_grouped(destination_city):

    destination_city = (destination_city or "").lower().strip()

    aviation = [parse_aviation(f) for f in get_aviation()]
    airlabs = [parse_airlabs(f) for f in get_airlabs()]

    merged = {}
    grouped = defaultdict(list)

    
    for f in aviation:
        if f.get("flight"):
            merged[f["flight"]] = f

    for f in airlabs:
        if f.get("flight"):
            merged[f["flight"]] = pick(merged.get(f["flight"]), f)


    for f in merged.values():

        dest_code = (f.get("destination") or "").upper()
        city = AIRPORT_CITY.get(dest_code)

        if not city:
            continue

        # ONLY matching destination allowed
        if destination_city and destination_city not in city.lower():
            continue

        grouped[city].append({
            "flight": f.get("flight"),
            "status": f.get("status")
        })

    return dict(grouped)


# ----------------------------
# NEXT FLIGHT
# ----------------------------
def get_next_flight(grouped):
    for flights in grouped.values():
        if flights:
            return flights[0]
    return None