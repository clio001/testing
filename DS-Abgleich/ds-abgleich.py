# Version 0.0.1 (August 2023)
# https://oai.sbb.berlin
# Kontakt: john.woitkowitz@spk.sbb-berlin.de


import requests, xml.etree.ElementTree as ET, datetime

# Parameter fuer API-Abfrage
base_url = "https://oai.sbb.berlin/"

verb = "ListRecords"
metadata_prefix = "oai_dc"
set_spec = "all"

# Quelldatei oeffnen und PPNs in List einlesen
sourcefile = open('bestandsppns.txt', 'r')
lines = sourcefile.readlines()

ppnList = []
for line in lines:
    ppnList.append("PPN" + line.split('\n')[0])
    

# Erstelle Datei
date_and_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

filename = "ds-abgleich.csv"
f = open(filename, 'w', encoding="utf-8")
f.write("DigiPPN; PhysPPN; Resolver-URL; Sets; Jahr; Titel; AutorIn; Verlag" + '\n')

resumption_token = None
page = 1
numberRecords = 0
hits = 0



print("""
||||||||||||||||||||||||||||||||||||||||||||||

    Bestandsabgleich:
    Digitale Sammlungen der SBB

||||||||||||||||||||||||||||||||||||||||||||||

      """)

print(f"Set: {set_spec}")

print(f"Datei erstellt: {filename}")

print("""
Abgleich gestartet ...
""")

# API-Abfrage mit Resumption-Token
while True:
    print(f"Titel abgeglichen: {numberRecords}", end='\r')
    
    if resumption_token:
        request_url = f'{base_url}?verb={verb}&resumptionToken={resumption_token}'
    else:
        request_url = f"{base_url}?verb={verb}&metadataPrefix={metadata_prefix}&set={set_spec}"


    response = requests.get(request_url)
    result = response.content.decode('utf-8')
            
    root = ET.fromstring(result)
     
    if root[1].text == "0":
        print("Es wurden keine Eintraege gefunden.")
        
    else:
        ListRecords = root[2]
        
        numberRecords = numberRecords + len(ListRecords) - 1
        
        element = ListRecords[len(ListRecords) - 1]
        if "resumptionToken" in element.tag:
            resumption_token = element.text
        else:
            resumption_token = None
            print("""
Abgleich abgeschlossen!

Ergebnis:
- - - - - -""")
            print(f"Abgleiche: {numberRecords}")
            print(f"Treffer: {hits}")
            print("")
            break
                
        for record in ListRecords:
            
            setElements = record.findall(".//{http://www.openarchives.org/OAI/2.0/}setSpec")
            dsSets = ""
            for element in setElements:
                dsSets = dsSets + " " + element.text
            
            elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}identifier")
            for identifier in elementTag:
                if identifier.text in ppnList:
                    hits = hits + 1
                    print("---")
                    print("Treffer: " + str(identifier.text))
                    print("Sets: " + dsSets)
                    print("---")
                    physicalPPN = identifier.text
                    
                    listIDs = []
                    
                    for recordID in elementTag:
                        listIDs.append(recordID.text)
                        if "http" in recordID.text:
                            resolver_url = recordID.text
                        
                    digitalPPN = listIDs[0]
                    
                    elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}date")
                    if elementTag:
                        date = elementTag[0].text
                    else:
                        date = "kein Angabe"
                        
                    elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}title")
                    if elementTag:
                        title = elementTag[0].text
                    else:
                        title = "keine Angabe"     
                    
                    elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}creator")
                    if elementTag:
                        creator = elementTag[0].text
                    else:
                        creator = "keine Angabe"                 

                    elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}publisher")
                    if elementTag:
                        publisher = elementTag[0].text
                    else:
                        publisher = "keine Angabe"
                             
                    
                    entry = digitalPPN + "; " + physicalPPN + "; " + resolver_url + "; " + dsSets + "; " + date + "; " + title + "; " + creator + "; " + publisher + "; "
                    f.write(entry + '\n')
                    
                    break
            
            
        page = page + 1
        
        

         
