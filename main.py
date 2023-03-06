
import json
import pymongo
from pymongo import MongoClient

with open("/home/rj/Documents/Rancho/RanchoGeoJson.geojson") as jsonFile:
    data = json.load(jsonFile)




cluster = MongoClient("mongodb+srv://rj:Hapkido123@cluster0.iiuhn.mongodb.net/?retryWrites=true&w=majority")
db = cluster["IE"]
Rancho = db["Rancho SOV"]
#
#
# for x in range(len(data["features"])):
#     districtNum = data["features"][x]["properties"]["DISTRICT"]
#     rec = AD.find_one({"NumOnly": districtNum})
#
#     data["features"][x]["properties"]["Name"] = rec["Name"]
#     data["features"][x]["properties"]["RegVoters"] = rec["RegVoters"]
#     data["features"][x]["properties"]["Baseline"] = rec["Baseline"]
#     data["features"][x]["properties"]["Party"] = rec["Party"]
#     print(rec["Name"])
#     print("Distrtit: " + districtNum + " : " + "RecNum: " + str(x))
#     print(data["features"][x]["properties"]["Name"])
#     print(rec["RegVoters"])
#     print(data["features"][x]["properties"]["RegVoters"])
#     print("--- ")
#
# # In[5]:
#
#
# with open("/home/rj/GeoJSONFiles/CDFullOut.geojson", "w") as jsonFile:
#     json.dump(data, jsonFile, indent=2)
#
# # In[ ]:
#
#
# # In[ ]:



