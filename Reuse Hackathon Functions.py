#12/03/2021
#Written By: Callum Wilkinson
#Reuse

import sqlite3

#file = database

#engine = create_engine('sqlite://', echo = False)

activ = open("activities.txt", "r");

def displayReuseMethod(material):

    activitytext = [];
    activitytext = activ.readlines();

    activities = [];
    activity = "";
    
    if(material[0].lower() == "wood"):

        activities.append(activitytext[0]);
        
    elif(material[0].lower() == "glue"):

        activites.append(activitytext[1]);

    elif(material[0].lower() == "plastic"):

        activities.append(...);

    elif(material[0].lower() == "metal"):

        activites.append(...);

        

    for i in range(0, len(activities)):

        activity = (activity + activities[i] + "\n");

    print(activity);


    

    return activity;

    


"""def locateNearbyCharities():

    str charitynames = [];

    



    return charitynames;


"""

displayReuseMethod(["wood"]);
