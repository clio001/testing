import requests, xml.etree.ElementTree as ET

base_url = "https://www.digi-hub.de/viewer/oai"

verb = "ListRecords"
metadata_prefix = "oai_dc"
set_spec = "allgemeinerbestand"

resumption_token = None

f = open('evifa-allg-bestand.txt', 'a')
f.write('KOBV; SetSpecification; Title; Creator; Subject; Publisher; Date; Identifier' + '\n')


i = 1

while True:
    print(f"Page {i}")
    if resumption_token:
        request_url = f'{base_url}?verb={verb}&resumptionToken={resumption_token}'
    else:
        request_url = f"{base_url}?verb={verb}&metadataPrefix={metadata_prefix}&set={set_spec}"

    response = requests.get(request_url)

    if response.status_code == 200:
        result = response.content.decode('utf-8')
        
        root = ET.fromstring(result)
        
        ListRecords = root[2]

        for record in ListRecords:
            kobv = record[0][0].text
            setSpec = record[0][2].text

            elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}title")
            if elementTag:
                title = elementTag[0].text
            else:
                title = "none"
            
            elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}creator")
            if elementTag:
                creator = elementTag[0].text
            else:
                creator = "none"
            
            elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}subject")
            if elementTag:
                subject = elementTag[0].text
            else:
                subject = "none"
            
            elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}publisher")
            if elementTag:
                publisher = elementTag[0].text
            else:
                publisher = "none"
            
            elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}date")
            if elementTag:
                date = elementTag[0].text
            else:
                date = "none"
            
            elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}identifier")
            if elementTag:
                identifier = elementTag[0].text
            else:
                identifier = "none"
                
            f = open('evifa-allg-bestand.txt', 'a')
            f.write(kobv +"; " + setSpec +"; " + str(title.encode()).replace("b'", "").replace("'", "") +"; " + str(creator.encode()).replace("b'", "").replace("'", "") + "; " + subject + "; " + str(publisher.encode()).replace("b'", "").replace("'", "") + "; " + date + "; " + identifier + '\n')   
            
        if root[1].text == "0":
            print("No record")
            
        else:
            ListRecords = root[2]
            element = ListRecords[len(ListRecords) - 1]
            resumption_token = element.text
            if resumption_token == "":
                print("No resumption token.")
            else:
                print(f"Resumption token: {resumption_token}"  + "\n")
            
            i = i + 1

    
        if resumption_token is None:
            break
        
    else:
        print(f"Fehler mit Status-Code: {response.status_code}")