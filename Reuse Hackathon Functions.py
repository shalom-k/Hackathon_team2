#12/03/2021
#Reuse

import sqlite3
import requests,json
import openpyxl

excel_files = ['HackLboro_-_Team_2_-_Database.xlsx']

for file in excel_files:

    workbook = openpyxl.load_workbook(file);
    worksheet = workbook['Activities']



def displayReuseMethod(material):

    activitytext = [];

    activities = [];
    activity = "";

    
    if(material.lower() == "scrap wood"):

        activities.append(worksheet['B2'].value);

    elif(material.lower() == "glue"):

        activities.append(worksheet['B3'].value);
                
    elif(material.lower() == "paper"):

        activities.append(worksheet['B4'].value);

    elif(material.lower() == "cardboard"):

        activities.append(worksheet['B5'].value);

    elif(material.lower() == "metal"):

        activities.append(worksheet['B6'].value);

    elif(material.lower() == "plastic bottles"):

        activities.append(worksheet['B7'].value);

    elif(material.lower() == "textiles"):

        activities.append(worksheet['B8'].value);


        

    for i in range(0, len(activities)):

        activity = (activity + activities[i] + "\n");

    print(activity);


    

    return activity;
    
def nearby_locations(place):
    
    api_key = 'AIzaSyBbwM-62klXAknNAhMWEZ-MVlpfUFYFYko'
    url_place = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    r = requests.get(url_place + 'query=' + place +'&key=' + api_key)
    x = r.json()
    data = x['results'] 
    return(x['results'])

def distance(start,fin):

    api_key = 'AIzaSyBbwM-62klXAknNAhMWEZ-MVlpfUFYFYko'
    url_distance='https://maps.googleapis.com/maps/api/distancematrix/json?'
    req = requests.get(url_distance + 'origins=' + start + '&destinations=' + fin +'&key=' + api_key)
    values=req.json()
    #can change this print statement to a return statement to release the data onto GUI
    print("%s: %s to %s: %s is %s away and would take %s"%(values['destination_addresses'][0],fin,values['origin_addresses'][0],start,values['rows'][0]['elements'][0]['distance']['text'],values['rows'][0]['elements'][0]['duration']['text']))
    return("%s: %s to %s: %s is %s away and would take %s"%(values['destination_addresses'][0],fin,values['origin_addresses'][0],start,values['rows'][0]['elements'][0]['distance']['text'],values['rows'][0]['elements'][0]['duration']['text']))

def locateNearbyCharities():
    
    place = ("Charity Near Me")


    charities = "";

    x = nearby_locations(place)
    charitylist = []
    dlist = []
    
    for i in range(len(x)):
        charitylist.append(x[i]['name'])

    print(charitylist)

    start = input("Enter Your Postcode : ")

    for l in range(len(charitylist)):

        dlist.append(distance(start,charitylist[l]));

    

    return charitylist;

if __name__ == "__main__":
    
    locateNearbyCharities();
