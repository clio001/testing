#This file retrieves keywords (Schlagwoerter) from the K10plus library catalogue

import requests, csv, xml.etree.ElementTree as ET, datetime

global ppnList, trefferList
ppnList = []
trefferList = []

def createFiles():
    file = open('trefferliste.txt', 'a')
    file.write(f"""TREFFERLISTE
Stand: {datetime.datetime.now()}\n\n""")
    
    noRecordFile = open('no-records.txt', 'a')
    noRecordFile.write(f"""KEINE ERGEBNISSE IN SRU-ABFRAGE
Stand: {datetime.datetime.now()}\n\n""")

def importData():
    f = open('test-ppns.txt')
    lines = f.readlines()
    for line in lines:
        ppnList.append(line.split('\n')[0])
        
    getData(ppnList)

def getData(ppnList):
    for ppn in ppnList:
        url = f"http://sru.k10plus.de/gvk7?version=1.1&operation=searchRetrieve&query=pica.ppn={ppn}&maximumRecords=300&recordSchema=picaxml"
        response = requests.get(url)
        data = response.content.decode('utf-8')
        parseData(data, ppn)


def parseData(data,ppn):
    root = ET.fromstring(data)
    if root[1].text == "0":
        noRecordFile = open('no-records.txt', 'a')
        noRecordFile.write(ppn + '\n')
        noRecordFile.close()
        
    else:
        record = root[2][0][2][0]
           
        for datafield in record:   
            if datafield.attrib['tag'] == "244Z":
                for subfield in datafield:
                    if subfield.attrib['code'] == "a":
                        if subfield.text == "Digitale Sammlung Deutscher Kolonialismus":
                            print(f"Treffer: PPN{ppn} in DSDK (244Z) gefunden")
                            file = open('trefferliste.txt', 'a')
                            file.write(ppn + '\n')
                            file.close()

createFiles()
importData()