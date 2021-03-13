import requests
import json

#find distance between 2 points


def distance(start, fin):
    api_key = 'AIzaSyBbwM-62klXAknNAhMWEZ-MVlpfUFYFYko'
    url_distance = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    req = requests.get(url_distance + 'origins=' + start +
                       '&destinations=' + fin + '&key=' + api_key)
    values = req.json()
    return("%s: %s" % (values['destination_addresses'][0], values['rows'][0]['elements'][0]['distance']['text']))


def nearby_locations(place):
    api_key = 'AIzaSyBbwM-62klXAknNAhMWEZ-MVlpfUFYFYko'
    url_place = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    r = requests.get(url_place + 'query=' + place + '&key=' + api_key)
    x = r.json()
    return(x['results'])


def dist(start, place):
    location_array = []
    data = nearby_locations(place)
    for i in range(len(data)):
        fin = data[i]['formatted_address']
        location_array.append(distance(start, fin))
    return(location_array)


#function to get time to each location with distance to each location in an array.
if __name__ == "__main__":
    start = input("enter the start location boss :)")
    place = input("Enter a place boss :)")
    location_array = dist(start, place)
    for i in range(len(location_array)):
        print(location_array[i])
