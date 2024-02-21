import json
import os

#  returns dictionary with format "last name of house member": [committee1, committee2, etc.]
def getHouseCommittee():
    filepath = os.path.join("json_files", "HouseCommittees.json")
    with open(filepath, 'r') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data

def getFullCommittees():
    filepath = os.path.join("json_files", "FullCommittees.json")
    with open(filepath, 'r') as json_file:
        fullCommittees = json.load(json_file)
    return fullCommittees
    

#  returns dictionary with format "last name of senator": [committee1, committee2, etc.]
def getSenateCommittee(): # gets committees of the senate 
    filepath = os.path.join("json_files", "SenateCommittees.json")
    with open(filepath, 'r') as json_file:
        loaded_data = json.load(json_file)

    return loaded_data 
    

