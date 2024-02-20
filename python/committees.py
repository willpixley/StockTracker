import json

#  returns dictionary with format "last name of house member": [committee1, committee2, etc.]
def getHouseCommittee():
    with open('SenateCommittees.json', 'r') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data



    

#  returns dictionary with format "last name of senator": [committee1, committee2, etc.]
def getSenateCommittee(): # gets committees of the senate 
    with open('SenateCommittees.json', 'r') as json_file:
        loaded_data = json.load(json_file)

    return loaded_data 
    

