import requests,json

start = input("enter the start location boss :)")
place = input("Enter a place boss :)")

#find distance between 2 points
def distance(start,fin):
    api_key = 'AIzaSyBbwM-62klXAknNAhMWEZ-MVlpfUFYFYko'
    url_distance='https://maps.googleapis.com/maps/api/distancematrix/json?'
    req = requests.get(url_distance + 'origins=' + start + '&destinations=' + fin +'&key=' + api_key)
    values=req.json()
    #can change this print statement to a return statement to release the data onto GUI
    print("%s: %s to %s: %s is %s away and would take %s"%(values['destination_addresses'][0],fin,values['origin_addresses'][0],start,values['rows'][0]['elements'][0]['distance']['text'],values['rows'][0]['elements'][0]['duration']['text']))
def nearby_locations(place):
    api_key = 'AIzaSyBbwM-62klXAknNAhMWEZ-MVlpfUFYFYko'
    url_place = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    r = requests.get(url_place + 'query=' + place +'&key=' + api_key)
    x = r.json()
    #data = x['results'] 
    return(x['results'])
def dist(start,place):
    data = nearby_locations(place)
    for i in range(len(data)):
        fin=data[i]['formatted_address']
        distance(start,fin)
        print(data[i]['name'])

#function to get time to each location :)
dist(start,place)

