import json
import pymongo
from pymongo import MongoClient

# Open GeoJSON File
with open("/home/rj/Documents/Rancho/test.geojson") as jsonFile:
    data = json.load(jsonFile)

# Connect to MongoDB Database and Rancho SOV Collection

try:
    cluster = MongoClient("mongodb+srv://rj:Hapkido123@cluster0.iiuhn.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["IE"]
    Rancho = db["Rancho SOV"]
    print("Connected to MongoDB ------------")
except:
    print("Can't Connect to MongoDB!")

# Iterate through precincts
for x in range(len(data["features"])):

    # Get precinct info from GeoJSON file
    precinctNum = data["features"][x]["properties"]["PRECINCT"]

    # Format string to match database
    precinctStr = str(precinctNum)

    # print (precinctStr)

    # Get record from database that matches precinct
    ranchoRec = Rancho.find_one({"Precinct Num": precinctStr})

    try:
        data["features"][x]["properties"]["CLARK"] = ranchoRec["FLOYD E CLARK"]
        data["features"][x]["properties"]["OLMSTED"] = ranchoRec["ROSE STEPHENS OLMSTED"]
        data["features"][x]["properties"]["STICKLER"] = ranchoRec["ASHLEY STICKLER"]
        data["features"][x]["properties"]["HANNAH"] = ranchoRec["MARY HANNAH"]
        data["features"][x]["properties"]["HENDERSON"] = ranchoRec["LAWRENCE HENDERSON"]
        data["features"][x]["properties"]["JIMENEZ"] = ranchoRec["ERICK JIMENEZ"]
        data["features"][x]["properties"]["Write-in"] = ranchoRec["Write-in"]
        data["features"][x]["properties"]["Total"] = ranchoRec["Total"]


    except:
        # print("Find Error on: " + precinctStr)
        pass

    try:
        totalData = data["features"][x]["properties"]["Total"]
        clarkData = data["features"][x]["properties"]["CLARK"]

        clarkPercent = int(round((int(clarkData) / int(totalData) * 100), 0))

        myquery = {"Precinct Num": precinctStr}
        newvalues = {"$set": {"votePercentage": clarkPercent}}

        Rancho.update_one(myquery, newvalues)



    except:
        print("Data Error" + " - " + precinctStr + " - " + clarkData + " - " + totalData)
        clarkPercent = 0
        myquery = {"Precinct Num": precinctStr}
        newvalues = {"$set": {"votePercentage": 0}}
        Rancho.update_one(myquery, newvalues)
        pass

    print(clarkPercent)
# with open("/home/rj/Documents/Rancho/RanchoGeoJsonOutput.geojson", "w") as jsonFile:
#      json.dump(data, jsonFile, indent=2)
