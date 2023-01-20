from FlightRadar24.api import FlightRadar24API
import json
from parse import parse_timedetails, get_airline_name
# from plyer import notification
# import tkinter as tk


#Initialize Flightradar Object
radar = FlightRadar24API()

# flights = radar.get_flights()

def get_airline_flights(airlineICAO):

    #Gets airline name using ICAO
    airline_name = get_airline_name(airlineICAO)
    
    flights_list = list()

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
            #print(json.dumps(flight.time_details), "Let's get it")
                        
            initial_departure = time_details['scheduled']['departure']
            initial_arrival = time_details['scheduled']['arrival']
            new_departure = time_details['estimated']['departure']
            new_arrival = time_details['estimated']['arrival']

            data = {"Flight Number": FlightNumber, "Airline": airline_name, "Status": status, "Origin": origin, "Destination": destination}

            flights_list.append(data)

           

            # if "Delayed" in status:                
            #     print(f"Flight {FlightNumber} of {airline_name} has been delayed\nStatus: {status}\nOrigin: {origin}\nDestination: {destination}\nInitial Departure Time : {initial_departure}\nInitial arrival time: {initial_arrival}\nNew departure time : {new_departure}\nNew arrival time: {new_arrival}\n\n") 
            
            
                
                
            # elif not "Delayed" in status:
            #     print(f"Flight {FlightNumber} of {airline_name}\nStatus: {status}\nOrigin: {origin}\nDestination: {destination}\nInitial Departure Time : {initial_departure}\nInitial arrival time: {initial_arrival}\nNew departure time : {new_departure}\nNew arrival time: {new_arrival}\n\n") 
    
    return flights_list
    # print(json.loads(json.dumps(flights_list), indent=3))

def get_flights_by_bounds():
    zones = radar.get_zones()
    bounds = radar.get_bounds(zones["africa"])
    bound_flights = radar.get_flights(bounds = bounds)
    flights = list()
    #Get the details of each flight for the airline
    for flight in bound_flights:    
        
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
            #print(json.dumps(flight.time_details), "Let's get it")
                        
            initial_departure = time_details['scheduled']['departure']
            initial_arrival = time_details['scheduled']['arrival']
            new_departure = time_details['estimated']['departure']
            new_arrival = time_details['estimated']['arrival']

            if FlightNumber != 'N/A':
                data = {"Flight Number": FlightNumber, "Status": status, "Origin": origin, "Destination": destination}
                flights.append(data)


    return flights()



def main(output):
    #Get all nigerian airlines ICAO
    def flights_by_airlines():
        with open("nigerian_airlines.json", "r") as ngn:
            ngn_airlines = json.load(ngn)

        #Get all Nigerian airline ICAO
        nigerian_airlines_ICAO = [each for each in ngn_airlines]
        flights = list()

        for ICAO in nigerian_airlines_ICAO:
            print(f'Accessing flight for {ICAO}')
            airline_flights = get_airline_flights(ICAO)
            flights += airline_flights

        with open(f"{output}.json", "w") as file_:
            json.dump(flights, file_, indent=2)

        print(json.dumps(flights, indent=3))
    
    def flights_by_bounds():
        flights = get_flights_by_bounds()

        with open(f"{output}.json", "w") as file_:
            json.dump(flights, file_, indent=2)

        print(json.dumps(flights, indent=3))

    decision = input("How do you want to get flight details\n1. Get flights by airlines\n2. Get flight by bounds\nChoice: ")
    if int(decision) == 1:
        print('\n Getting flight by AIRLINES')
        flights_by_airlines()
    elif int(decision) == 2:
        print('\n Getting flight by BOUNDS')
        flights_by_bounds()
    


if __name__ == '__main__':
    main()
    
    




    


