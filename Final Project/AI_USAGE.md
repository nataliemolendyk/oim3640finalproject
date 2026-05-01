# April 22, 2026
## What you asked
We asked AI to find websites that use flight tracking APIs and to get the coordinates of the terminals in the Boston Logan Airport.

## What AI generated
AI told us to use Aviationstack or FlightAware to find the API. It also told us the coordinates of the terminals: LOGAN_TERMINALS = {
    "A": (42.3656, -71.0202),
    "B": (42.3662, -71.0170),
    "C": (42.3643, -71.0175),
    "E": (42.3650, -71.0096)
}
## What you did with it 
From there we looked at the Aviationstack website to create an account and get the API key. For the coordinates of the terminals, we verified these by right clicking on the terminal locations on Google maps and then added them to the code so the location to each terminal could be better measured.

## What you learned 
We understood the different API websites for tracking flights better and we now know the precise locations of each terminal in the Boston Logan Airport.

# April 25, 2026
## What you asked
We asked AI to ajust our html to fit our app better and we asked AI to alter our code from asking users to input their flight numbers and starting location to outputing flights from Boston with the users inputed starting location accompanied by a map with the route. We also asked AI to help change the display of flights to show the terminal, gate, flight_number, and airport name.

## What AI generated
AI generated latitude and longitude coordinates for the Boston Logan Airport as well as the get_flights_from_boston function. It also expanded the code in html to make the web application more appealing and advanced. This included the drive time being displayed with the terminals, gates, and status.

## What you did with it 
We used the Boston Logan Airport coordinates in the app.py to create the route from the user's starting to the airport. We also used the html code to create the map with highlighted route and starting/ending points. We then had the information to be sorted under headings, so the flight information would go under "Flights from Boston Logan" and the drive time would be near the map.

## What you learned 
From this, we learned that multiple functions from the flight.py have to be called in the app.py. Before using AI, we didn't understand why the app.py wasn't running correctly even though the flight.py was set up correctly. We then learned that we needed to call multiple functions because they produced different outputs. We learned that you have to be specific with what you want AI to do because we asked AI to create the route and it create the flight route, not the driving route, so we learned to be more clear and direct with what we ask.

# April 30, 2026
## What you asked
We asked AI to make the design/appearance of our website look more polished and cleaner. We also asked AI to find specific flights that user inputs. Since the Aviation API couldn't get the data for the specific flights, we had it search by destination. We then asked AI to take the inputed destination and provide the flights going to that location.

## What AI generated
AI generated code so popular cities were connected to acronyms of the different airports in that state. It also generated a fallback so the user would always see something on the dashboard. AI also changed the format of the webpage, added airline logos, and changed some of the terms to be more professional. AI gave us a new API called Air Labs and this allowed us to retrieve the flights leaving Boston.

## What you did with it
We used the generated code to provide better and more accurate results for the users because the airport acronyms are connected to certain cities by hard code. We used the airline logos and terms changed to make the display of flights more appealing to look at and real life. We used the new airport symbols that AI gave us to accurately fetch the flights going to the specific destination we chose.

## What you learned
We learned that it isn't that simple to just ask AI to change the code to lookup flights and you have to hard code flight symbols to match cities in order for results to show up. We also learned that it is more difficult to look up specific flights/flight numbers because the Aviation API doesn't expand that far. Something else we learned is that we have to be more specific when we ask AI to make our web app more polished. At first it was giving us minor changes, but then we had to specifically state what we want to see on our web app and it was giving us closer results to what we want, but sometimes we didn't know what we wanted to see on the display so it was a little challenging. We learned that multiple APIs can be used and different jobs can be split between them, although you have to be specific with if you want one API to be the main API and the other to be back up or for them to split up tasks.