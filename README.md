Karnataka Metro Fare and Ticketing System
Overview
This Python program simulates a fare and ticketing system for the Karnataka Metro Green Line (Nagasandra to Yelachenahalli). It allows users to select their start and end stations, calculate the fare, and purchase tickets. The fare is calculated based on the distance between the stations and the number of stations passed.

Features
Fare Calculation: The system calculates the fare based on the stations selected. The fare increases with the distance between the stations.

Station Listing: Displays a list of available metro stations with their respective numbers, allowing users to choose stations by their number.

Ticket Purchase: Allows users to buy tickets by providing a start station, an end station, and the number of tickets required.

Error Handling: The system checks for invalid stations, invalid station order (i.e., ensuring the start station comes before the end station), and invalid inputs for the number of tickets.

Requirements
Python 3.x (any version above 3.6)
No external libraries are required
How to Use
Run the Program:

Ensure that the script is saved as a .py file (e.g., karnataka_metro.py).
Run the script using any Python interpreter (e.g., python karnataka_metro.py).
Select Stations:

The program will display a list of stations along the Green Line with numbers.
Choose a start station and an end station by entering the corresponding station numbers.
Enter the Number of Tickets:

After selecting the stations, the program will ask for the number of tickets required. Enter the number of tickets you want to purchase.
Ticket Details:

The program will display the fare per ticket, the total fare for the specified number of tickets, and confirmation of successful ticket purchase.
Error Handling:

If invalid station numbers are selected, or if the stations are in the wrong order (e.g., selecting a station after the end station), the program will prompt an error message and allow the user to correct it.
Code Explanation
Class KarnatakaMetro
__init__(): Initializes the metro system with the station names and fare structure.
calculate_fare(start_station, end_station): Calculates the fare between two selected stations. It ensures the stations are valid and checks if the start station comes before the end station.
display_stations(): Displays the list of available stations and their corresponding numbers.
buy_ticket(start_station, end_station, num_tickets): Calculates the fare for a specific route and handles ticket purchase by displaying the total fare and ticket details.
Error Handling
Invalid station numbers or station names result in error messages.
The route is validated to ensure that the start station comes before the end station.
Invalid input for the number of tickets (e.g., a non-numeric value or zero/negative number) is handled by the program.
