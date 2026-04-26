## April 22, 2026
# What you asked
We asked AI to find websites that use flight tracking APIs and to get the coordinates of the terminals in the Boston Logan Airport.

# What AI generated
AI told us to use Aviationstack or FlightAware to find the API. It also told us the coordinates of the terminals: LOGAN_TERMINALS = {
    "A": (42.3656, -71.0202),
    "B": (42.3662, -71.0170),
    "C": (42.3643, -71.0175),
    "E": (42.3650, -71.0096)
}
# What you did with it 
From there we looked at the Aviationstack website to create an account and get the API key. For the coordinates of the terminals, we verified these by right clicking on the terminal locations on Google maps and then added them to the code so the location to each terminal could be better measured.

# What you learned 
We understood the different API websites for tracking flights better and we now know the precise locations of each terminal in the Boston Logan Airport.

## April 25, 2026
# What you asked
We asked AI to ajust our html to fit our app better and we asked AI to alter our code from asking users to input their flight numbers and starting location to outputing flights from Boston with the users inputed starting location accompanied by a map with the route.

# What AI generated
AI generated latitude and longitude coordinates for the Boston Logan Airport as well as the get_flights_from_boston function. It also expanded the code in html to make the web application more appealing and advanced.

# What you did with it 
We used the Boston Logan Airport coordinates in the app.py to create the route from the user's starting to the airport. We also used the html code to create the map with highlighted route and starting/ending points.

# What you learned 
From this, we learned that multiple functions from the flight.py have to be called in the app.py. Before using AI, we didn't understand why the app.py wasn't running correctly even though the flight.py was set up correctly. We then learned that we needed to call multiple functions because they produced different outputs.