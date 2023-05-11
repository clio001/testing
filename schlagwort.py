import requests
import csv

#Get GND IDs for keywords from file



    
    
#Get related keywords from GND via Lobid



def getRelatedKeywords():
    response = requests.get("https://lobid.org/gnd/search?q=*&format=json")
    data = response.json()
    print(data)

getRelatedKeywords()

#def parseData(data):
    
    
