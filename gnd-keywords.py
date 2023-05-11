import requests
import json
import csv

global List_GND_IDs, termsList, baseURL
List_GND_IDs = []
termsList = []
baseURL = "https://lobid.org/gnd/"

#Extract GND IDs from CBS export
def getIDsFromExport():
    string = "Birma ; ID: gnd/4069500-1; Assam ; ID: gnd/4003249-8; Staatliches Museum für Völkerkunde München ; ID: gnd/2022507-6; Musikinstrument ; ID: gnd/4040851-6; Sammlung ; ID: gnd/4128844-0"	

    listID = string.rsplit(";")

    for element in listID:
        x = element.find("/")
        if x > -1:
            y = element[x + 1:len(element) + 8]
            List_GND_IDs.append(y)
            
    if List_GND_IDs == []:
        print("Kein Schlagwort gefunden")
    else:        
        print(f"Liste der Schlagwort GND IDs: {List_GND_IDs}")
        getRelatedTerms(baseURL, List_GND_IDs)

#Query GND for related terms with IDs from CBS exort
def getRelatedTerms(baseURL, List_GND_IDs):
    i = 1
    for ID in List_GND_IDs:
        url = baseURL + ID + ".json"
        print(f"""
Query #{i}: {url}""")
        i = i + 1
        response = requests.get(url)
        data = json.loads(response.content)
        printRelatedTerms(data)

def printRelatedTerms(data):
    termsList = data["preferredName"]

    for term in termsList:
        print(term)

getIDsFromExport()

