
import json
import pymongo
from pymongo import MongoClient

# Open GeoJSON File
with open("/home/rj/Documents/Rancho/RanchoGeoJson.geojson") as jsonFile:
    data = json.load(jsonFile)

# Connect to MongoDB Database and Rancho SOV Collection
cluster = MongoClient("mongodb+srv://rj:Hapkido123@cluster0.iiuhn.mongodb.net/?retryWrites=true&w=majority")
db = cluster["IE"]
Rancho = db["Rancho SOV"]


# Iterate through precincts
for x in range(len(data["features"])):

     # Get precinct info from GeoJSON file
     precinctNum = data["features"][x]["properties"]["PRECINCT"]

     # Format string to match database
     precinctStr = str(precinctNum)

     print (precinctStr)

     # Get record from database that matches precinct
     ranchoRec = Rancho.find_one({"Precinct Num": precinctStr})


     try:
          data["features"][x]["properties"]["FLOYD E CLARK"] = ranchoRec["FLOYD E CLARK"]
          data["features"][x]["properties"]["ROSE STEPHENS OLMSTED"] = ranchoRec["ROSE STEPHENS OLMSTED"]
          data["features"][x]["properties"]["ASHLEY STICKLER"] = ranchoRec["ASHLEY STICKLER"]
          data["features"][x]["properties"]["MARY HANNAH"] = ranchoRec["MARY HANNAH"]
          data["features"][x]["properties"]["LAWRENCE HENDERSON"] = ranchoRec["LAWRENCE HENDERSON"]
          data["features"][x]["properties"]["ERICK JIMENEZ"] = ranchoRec["ERICK JIMENEZ"]
          data["features"][x]["properties"]["Write-in"] = ranchoRec["Write-in"]
          data["features"][x]["properties"]["Total"] = ranchoRec["Total"]
     except:
          print("Error on: " + precinctStr)
          pass



with open("/home/rj/Documents/Rancho/RanchoGeoJsonOutput.geojson", "w") as jsonFile:
     json.dump(data, jsonFile, indent=2)



