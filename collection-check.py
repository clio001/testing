#This file retrieves keywords (Schlagwoerter) from the K10plus library catalogue

import requests, csv, xml.etree.ElementTree as ET

global ppn, collection
ppn = "138694893"
collection = "Digitale%20Sammlung%20Deutscher%20Kolonialismus"

def getData(ppn):
    url = f"http://sru.k10plus.de/gvk7?version=1.1&operation=searchRetrieve&query=pica.lsw={collection}&recordSchema=picaxml"
    response = requests.get(url)
    data = response.content.decode('utf-8')
    parseData(data)


def parseData(data):
    root = ET.fromstring(data)
    record = root[2][0][2][0]
    
    swName = ""
        
    for datafield in record:
        if datafield.attrib['tag'] == "244Z":
            for subfield in datafield:
                if subfield.attrib['code'] == "a":
                    if subfield.text == "Digitale Sammlung Deutscher Kolonialismus":
                        print("Match")

        if datafield.attrib['tag'] == "003@":
            for subfield in datafield:
                if subfield.attrib['code'] == "0":
                    print(f"003Q: {subfield.text}")
                        
        if datafield.attrib['tag'] == "021A":
            for subfield in datafield:
                if subfield.attrib['code'] == "a":
                    print(f"021A: {subfield.text}")
              
        if datafield.attrib['tag'] == "028A":
            for subfield in datafield:
                if subfield.attrib['code'] == "D":
                    firstName = subfield.text
                if subfield.attrib['code'] == "A":
                    lastName = subfield.text
            print(f"028A: {firstName} {lastName}")

        if datafield.attrib['tag'] == "044K":
            for subfield in datafield:
                if subfield.attrib['code'] == "a":
                    swName = subfield.text
                if subfield.attrib['code'] == "7":
                    gnd = subfield.text
            print(f"044K: {swName} {gnd}")
            
        if datafield.attrib['tag'] == "045Q":
            for subfield in datafield:
                if subfield.attrib['code'] == "j":
                    print(f"045Q: {subfield.text}")

def writeData():
    continue

getData(ppn)