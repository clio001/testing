#This file retrieves keywords (Schlagwoerter) from the K10plus library catalogue

import requests, csv, xml.etree.ElementTree as ET, pandas as pd

global ppnList
ppnList = []
cleanList = []

def createOutputFile():
    f = open('sw-physischePPNs-117467.csv', 'a')
    f.write("DigitalePPN, PhysischePPN, ddc5010, lcc5030, rvk5090, bk5301, loc5500, sw5550, gab5570" + '\n')

def importPPNs():
    ppn_df = pd.read_csv('117467physischeUnddigitalePPNs.csv')

    i = 0
    while i < len(ppn_df):
        ppnList.append(ppn_df.loc[i, 'physischePPN'])
        i = i + 1
    
    for element in ppnList:
        cleanElement = element.replace("PPN", "")
        cleanList.append(cleanElement)
    
    print("Clean list created.")
    
        
    
def getData():
    ppn_df = pd.read_csv('117467physischeUnddigitalePPNs.csv')
    digiPPN = ""
    
    i = 0
    while i < len(ppn_df):
        ppn = ppn_df.loc[i, 'physischePPN'].replace("PPN", "")
        digiPPN = ppn_df.loc[i, 'PPN']
        
        url = f"http://sru.k10plus.de/gvk7?version=1.1&operation=searchRetrieve&query=pica.ppn={ppn}&maximumRecords=300&recordSchema=picaxml"
        response = requests.get(url)
        data = response.content.decode('utf-8')
        
        parseData(data, ppn, digiPPN)
        
        i = i + 1

    print("""

Keyword retrieval complete!""")


def parseData(data, ppn, digiPPN):
    ddc5010 = ""
    lcc5030 = ""
    rvk5090 = ""
    bk5301 = ""
    loc5500 = ""
    sw5550 = ""
    gab5570 = ""

    root = ET.fromstring(data)
    
    f = open('sw-physischePPNs-117467.csv', 'a')
    
    if root[1].text == "0":
        row = f"{digiPPN}, PPN{ppn}, , , , , , , "
        f.write(row + '\n')
        
    else:
        record = root[2][0][2][0]

        for datafield in record:
            if datafield.attrib['tag'] == "045F":
                for subfield in datafield:
                    if subfield.attrib['code'] == "a":
                        ddc5010 = subfield.text
                
            if datafield.attrib['tag'] == "045A":
                for subfield in datafield:
                    if subfield.attrib['code'] == "a":
                        lcc5030 = subfield.text
         
            if datafield.attrib['tag'] == "045R":
                for subfield in datafield:
                    if subfield.attrib['code'] == "a":
                        rvk5090 = subfield.text
                
            if datafield.attrib['tag'] == "045Q":
                for subfield in datafield:
                    if subfield.attrib['code'] == "j":
                        bk5301 = subfield.text
            
            if datafield.attrib['tag'] == "044A":
                for subfield in datafield:
                    if subfield.attrib['code'] == "a":
                        loc5500 = subfield.text
    
            if datafield.attrib['tag'] == "044K":
                for subfield in datafield:
                    if subfield.attrib['code'] == "a":
                        sw5550 = subfield.text

            if datafield.attrib['tag'] == "044S":
                for subfield in datafield:
                    if subfield.attrib['code'] == "a":
                        loc5500 = subfield.text
    
    
        row = f"{digiPPN}, PPN{ppn}, {ddc5010}, {lcc5030}, {rvk5090}, {bk5301}, {loc5500}, {sw5550}, {gab5570}"
        f.write(row + '\n')


createOutputFile()
getData()