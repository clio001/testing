import requests
import json
import csv
import pandas as pd
import math

global List_cbs_SW, List_GND_IDs, termsList, baseURL
List_cbs_SW = []
List_GND_IDs = []
termsList = []
baseURL = "https://lobid.org/gnd/"

#Import CBS Metadata
def getCBSData():
    cbsData_df = pd.read_csv('example.txt', sep='\t')
    length = len(cbsData_df)
    
    i = 0
    while i < length:
        List_cbs_SW.append(cbsData_df.loc[i, 'Schlagwort'])
        i = i + 1
    getIDsFromExport(List_cbs_SW)    

#Extract GND IDs from CBS export
def getIDsFromExport(List_cbs_SW):
    listID = []
    
    for SW in List_cbs_SW:
        splitElement = SW.rsplit(";")
        print(splitElement)
        for element in splitElement:
            listID.append(element)
        
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

#Print related data
def printRelatedTerms(data):
    termsList = data["variantName"]

    print(termsList)
        
getCBSData()

