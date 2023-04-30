import xml.etree.ElementTree as ET
import requests

#Define base URL
global baseURL
baseURL = "https://sru.gbv.de/opac-de-1?version=1.1&operation=searchRetrieve&maximumRecords=100&recordSchema=picaxml&query=pica.xppn%3D"

#Open file containing PPNs and create PPN list
print("""
      Schlagwort und verwandte Begriffe Retrieval
      - - - - - - - - - - - - - - - - - - - - - -
      """)
path = input('Pfad oder Dateiname eingeben: ')
f = open(path)
lines = f.readlines()
global ppnList 
ppnList = []
for line in lines:
    ppnList.append(line.split('\n')[0])

print("""
      PPN-Liste:
      """)
for e in ppnList:
    print(e)
global data

#API fetch
def getData(baseURL, ppnList):
    for ppn in ppnList:
        url = f"{baseURL}{ppn}"
        print("""
      URL:
      """)
        print(url)
        response = requests.get(url)
        data = response.content
        print(f"status: {response}")
        parseXML(data)
    
#Parse XML
def parseXML(data):
    root = ET.fromstring(data)

    for child in root[2][0][2][0]:
        if child.attrib['tag'] == "021A":
            print(f"Titel: {child[0].text}")
        
        if child.attrib['tag'] == "028A":
            for e in child:
                if e.attrib['code'] == "A":
                    print(f"Autor*in: {e.text}")
                        
        if child.attrib['tag'] == "044A":
            for e in child:
                print(e.tag)
           
getData(baseURL, ppnList)