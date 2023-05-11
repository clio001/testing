import requests
import json
import csv

string = "Reise, id/gnd: 123456; Welt, id/gnd: 345678"

listID = string.rsplit(";")
print(listID)
for element in listID:
    x = element.find(":")
    y = element[x + 2:len(element)+8]
    print(y)


#IMPORT GND IDs
def getGNDIDs():
    f = open('example.txt')
    tsv_file = csv.reader(f, delimiter="\t")

    for line in tsv_file:
        print(line)

#GND QUERY
url = "https://lobid.org/gnd/4073624-6.json"

def getRelatedTerms(url):
    response = requests.get(url)
    data = json.loads(response.content)
    printRelatedTerms(data)

def printRelatedTerms(data):
    termsList = data["relatedTerm"]

    for term in termsList:
        print(term['label'])

#getGNDIDs()
#getRelatedTerms(url)
