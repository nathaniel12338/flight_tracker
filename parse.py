import json
import datetime, pytz
from pytz import timezone



def parse_timedetails(time_details):
     
     
    
    content = json.loads(time_details)

    lagos = timezone("Africa/Abidjan")
    # content = tz.gettz('UTC')
    # content = tz.gettz('Asia/Kolkata')
    # content = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')
    # utc = utc.replace(tzinfo=)
    # central = utc.astimezone(content)
    
    #lagos = timezone("US/Eastern")
    
    

    for each in content.keys():
        if each == "historical": pass
        else:
            for key_ in  content[each].keys():          
            
                value = content[each][key_]
                if value == None: pass
                else:
                    formatted = lagos.localize(datetime.datetime.utcfromtimestamp(int(value)))
                    content[each][key_] = str(formatted)
    
    
                    
    return content

def get_airline_name(airlineICAO):
    with open("nigerian_airlines.json" , "r") as airlines:
        content = json.load(airlines)
    
    if airlineICAO in content.keys():
        return content[airlineICAO]["name"]
    else:
        print(f"No Nigerian airline found with this ICAO code {airlineICAO}. Airline may be defunct")
        return None


if __name__ == '__main__':
    pass



