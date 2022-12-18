from FlightRadar24.api import FlightRadar24API
import json
from parse import parse_timedetails, get_airline_name

#Initialize Flightradar Object
radar = FlightRadar24API()


def get_airline_flights(airlineICAO):

    #Gets airline name using ICAO
    airline_name = get_airline_name(airlineICAO)

    if airline_name != None:

        #Get all the current flight of the airline
        airline_flights = radar.get_flights(airline = airlineICAO)

        #Get the details of each flight for the airline
        for flight in airline_flights:    
        
            #Initialization. Do not edit this section
            #--------------------------------------------.
            
            details = radar.get_flight_details(flight.id)    
            flight.set_flight_details(details)
            #--------------------------------------------

            #Flight details
            FlightID = flight.id
            FlightNumber = flight.number
            origin = flight.origin_airport_name
            origin_ICAO =  flight.origin_airport_icao
            destination = flight.destination_airport_name
            destination_ICAO = flight.destination_airport_icao
            status = flight.status_text
            aircraft_code = details['aircraft']['model']['code']
            aircraft_name = details['aircraft']['model']['text']
            
            time_details = parse_timedetails(json.dumps(flight.time_details))
            # print(json.dumps(flight.time_details))
                        
            initial_departure = time_details['scheduled']['departure']
            initial_arrival = time_details['scheduled']['arrival']
            new_departure = time_details['estimated']['departure']
            new_arrival = time_details['estimated']['arrival']

           

            if "Delayed" in status:                 
                print(f"Flight {FlightNumber} of {airline_name} has been delayed\nStatus: {status}\nOrigin: {origin}\nDestination: {destination}\nInitial Departure Time : {initial_departure}\nInitial arrival time: {initial_arrival}\nNew departure time : {new_departure}\nNew arrival time: {new_arrival}\n\n")  
            elif not "Delayed" in status:
                print(f"Flight {FlightNumber} of {airline_name}\nStatus: {status}\nOrigin: {origin}\nDestination: {destination}\nInitial Departure Time : {initial_departure}\nInitial arrival time: {initial_arrival}\nNew departure time : {new_departure}\nNew arrival time: {new_arrival}\n\n") 


def main():
    #Get all nigerian airlines ICAO
    with open("nigerian_airlines.json", "r") as ngn:
        ngn_airlines = json.load(ngn)

    #Get all Nigerian airline ICAO
    nigerian_airlines_ICAO = [each for each in ngn_airlines]

    for ICAO in nigerian_airlines_ICAO:
        get_airline_flights(ICAO)


if __name__ == '__main__':
    main()
    
    




    


