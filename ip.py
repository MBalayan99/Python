import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def give_ip():
    print("Inpute yor target ip:")
    ip = input()
    return ip



def get_location():
    ip_address = give_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "org":  response.get("org"),
        "calling_code": response.get("country_calling_code"),
        "network": response.get("network")
    }
    #print dict element 
    print(location_data["network"])
    def print_loop():
        for data in location_data.values():
            print(data)
    #return location_data
    print_loop()
 


print(get_location())
