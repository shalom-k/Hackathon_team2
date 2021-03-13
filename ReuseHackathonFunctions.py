#12/03/2021
#Reuse
import If_No_council as counc
import sqlite3
import requests
import json
import openpyxl

excel_files = ['HackLboro_-_Team_2_-_Database.xlsx']

for file in excel_files:

    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['Activities']

def getTotalMaterials():
    materials = []
    for i in range(2,9):
        materials.append(worksheet['A' + str(i)].value)
    return materials


def displayReuseMethod(material):

    activitytext = []

    activities = []
    activity = ""

    if(material.lower() == "wood"):

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
    return activity


def locateNearbyCharities(start):

    place = ("Charity Near " + start)

    charities = ""

    x = counc.nearby_locations(place)
    charitylist = []
    dlist = []

    for i in range(len(x)):
        charitylist.append(x[i]['name'])

    for l in range(len(x)):
        fin = x[l]['formatted_address']
        dlist.append(str(counc.distance(start, fin)))
    for item in dlist:
        print(item)
    

    new_arr = []
    for i in range(len(charitylist)):
      new_arr.append(charitylist[i]+dlist[i])

    return new_arr
    


if __name__ == "__main__":

    i = 5
    #print(locateNearbyCharities("PE29 2EB"))
    #displayReuseMethod("wood")
    
