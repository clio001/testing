import xml.etree.ElementTree as ET
import requests


#Build URL
baseURL = 'https://sru.gbv.de/opac-de-1?version=1.1&operation=searchRetrieve&maximumRecords=100&recordSchema=picaxml&query=pica.xppn%3D'
ppn = "798833505"
url = baseURL + ppn
global data

#API fetch
def getData(url):
    response = requests.get(url)
    data = response.content
    print(f"status: {response}")
    print(f"PPN: {ppn}")
    parseXML(data)
    

#Parse XML
def parseXML(data):
    root = ET.fromstring(data)

    for child in root[2][0][2][0]:
        if child.attrib['tag'] == "021A":
            print(f"Title: {child[0].text}")
        
            
        if child.attrib['tag'] == "028A":
            for e in child:
                if e.attrib['code'] == "A":
                    print(f"Author: {e.text}")
            else:
                print("Author: 028A does not exist")
                        
        if child.attrib['tag'] == "044A":
            for e in child:
                print(e.tag)
           
getData(url)