#12/03/2021
#Reuse
import If_No_council as counc
import sqlite3
import requests,json
import openpyxl

excel_files = ['HackLboro_-_Team_2_-_Database.xlsx']

for file in excel_files:

    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['Activities']



def displayReuseMethod(material):

    activitytext = []

    activities = []
    activity = ""

    
    if(material.lower() == "scrap wood"):

        activities.append(worksheet['B2'].value)

    elif(material.lower() == "glue"):

        activities.append(worksheet['B3'].value)
                
    elif(material.lower() == "paper"):

        activities.append(worksheet['B4'].value)

    elif(material.lower() == "cardboard"):

        activities.append(worksheet['B5'].value)

    elif(material.lower() == "metal"):

        activities.append(worksheet['B6'].value)

    elif(material.lower() == "plastic bottles"):

        activities.append(worksheet['B7'].value)

    elif(material.lower() == "textiles"):

        activities.append(worksheet['B8'].value)   

    for i in range(0, len(activities)):
        activity = (activity + activities[i] + "\n")
    print(activity)
    return activity

def locateNearbyCharities():
    
    place = ("Charity Near Me")

    charities = ""

    x = counc.nearby_locations(place)
    charitylist = []
    dlist = []
    
    for i in range(len(x)):
        charitylist.append(x[i]['name'])
    
    start = input("Enter Your Postcode : ")
    for l in range(len(x)):
            fin = x[l]['formatted_address']
            dlist.append(str(counc.distance(start,fin)))
    for item in dlist:
        print(item)
 
    return charitylist

if __name__ == "__main__":
    
    locateNearbyCharities()
