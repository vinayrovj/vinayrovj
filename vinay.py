class KarnatakaMetro:
    def __init__(self):
        # Example fare structure for different stations along the Green Line (Nagasandra to Yelachenahalli)
        self.station_fare = {
            'Nagasandra Metro Station': 10,
            'Jalahalli Metro Station': 15,
            'Peenya Industry Metro Station': 20,
            'Peenya Metro Station': 25,
            'Yeshwanthpur Metro Station': 30,
            'Malleswaram Metro Station': 35,
            'Srirampura Metro Station': 40,
            'Rajajinagar Metro Station': 45,
            'Mahalakshmi Metro Station': 50,
            'Fifth Stage Metro Station': 55,
            'VV Puram Metro Station': 60,
            'Shanthinagar Metro Station': 65,
            'Lalbagh Metro Station': 70,
            'South End Circle Metro Station': 75,
            'Jayanagar Metro Station': 80,
            'Banshankari Metro Station': 85,
            'Yelachenahalli Metro Station': 90
        }
        
        # List of stations
        self.stations = [
            'Nagasandra Metro Station', 'Jalahalli Metro Station', 'Peenya Industry Metro Station', 'Peenya Metro Station',
            'Yeshwanthpur Metro Station', 'Malleswaram Metro Station', 'Srirampura Metro Station', 'Rajajinagar Metro Station',
            'Mahalakshmi Metro Station', 'Fifth Stage Metro Station', 'VV Puram Metro Station', 'Shanthinagar Metro Station',
            'Lalbagh Metro Station', 'South End Circle Metro Station', 'Jayanagar Metro Station', 'Banshankari Metro Station',
            'Yelachenahalli Metro Station'
        ]

    def calculate_fare(self, start_station, end_station):
        # Check if stations are valid
        if start_station not in self.station_fare or end_station not in self.station_fare:
            print("Invalid stations!")
            return None
        
        # Check if stations are in the correct order
        if self.stations.index(start_station) > self.stations.index(end_station):
            print("Invalid route! Please make sure the start station comes before the end station.")
            return None
        
        # Calculate the total fare based on distance
        start_index = self.stations.index(start_station)
        end_index = self.stations.index(end_station)
        total_fare = sum([self.station_fare[self.stations[i]] for i in range(start_index, end_index)])
        return total_fare
    
    def display_stations(self):
        print("\nAvailable Stations:")
        for idx, station in enumerate(self.stations, 1):
            print(f"{idx}. {station}")

    def buy_ticket(self, start_station, end_station, num_tickets):
        fare = self.calculate_fare(start_station, end_station)
        if fare:
            total_cost = fare * num_tickets
            print(f"\nTicket purchased successfully!")
            print(f"Route: {start_station} to {end_station}")
            print(f"Fare per Ticket: ₹{fare}")
            print(f"Number of Tickets: {num_tickets}")
            print(f"Total Fare: ₹{total_cost}")
        else:
            print("Ticket purchase failed. Please check the stations.")

# Main Program
if __name__ == "__main__":
    metro = KarnatakaMetro()

    # Display stations with their numbers
    metro.display_stations()

    try:
        # Get user input for start and end stations by selecting station numbers
        start_station_number = int(input("\nEnter the number of your start station: "))
        end_station_number = int(input("Enter the number of your end station: "))

        # Check if the numbers are valid
        if start_station_number < 1 or end_station_number < 1 or start_station_number > len(metro.stations) or end_station_number > len(metro.stations):
            print("Invalid station numbers. Please select valid numbers from the list.")
        else:
            # Get the station names based on the numbers selected
            start_station = metro.stations[start_station_number - 1]
            end_station = metro.stations[end_station_number - 1]

            # Ask for the number of tickets
            num_tickets = int(input("Enter the number of tickets needed: "))
            if num_tickets <= 0:
                print("Number of tickets must be greater than 0.")
            else:
                # Buy the ticket
                metro.buy_ticket(start_station, end_station, num_tickets)

    except ValueError:
        print("Please enter valid numbers for station and ticket quantity.")
