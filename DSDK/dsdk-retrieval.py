import requests, xml.etree.ElementTree as ET

base_url = "https://sammlungen.ub.uni-frankfurt.de/oai"

verb = "ListRecords"
metadata_prefix = "oai_dc"
set_spec = "kolonialbibliothek"

resumption_token = None

f = open('ub-frankfurt.txt', 'w', encoding="utf-8")
f.write("Identifier; Jahr; Titel; Description; Publisher; Relation"  + '\n')

i = 1

while True:
    print(f"Seite {i}")
    if resumption_token:
        request_url = f'{base_url}?verb={verb}&resumptionToken={resumption_token}'
    else:
        request_url = f"{base_url}?verb={verb}&metadataPrefix={metadata_prefix}&set={set_spec}"

    response = requests.get(request_url)

    if response.status_code == 200:
        result = response.content.decode('utf-8')
        
        
        root = ET.fromstring(result)
        
        if root[1].text == "0":
            print("No record")
            
        else:
            ListRecords = root[2]
            
            for record in ListRecords:
                elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}date")
                if elementTag:
                    date = elementTag[0].text
                else:
                    date = "none"
                
                elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}description")
                if elementTag:
                    description = elementTag[0].text
                else:
                    descritpion = "none"
                
                elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}publisher")
                if elementTag:
                    publisher = elementTag[0].text
                else:
                    publisher = "none"
                    
                elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}title")
                if elementTag:
                    title = elementTag[0].text
                else:
                    title = "none"
                
                elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}relation")
                if elementTag:
                    relation = elementTag[0].text
                else:
                    relation = "none"
                
                
                elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}identifier")
                if elementTag:
                    identifier = elementTag[0].text
                else:
                    identifier = "none"
                
                entry = identifier + "; " + date + "; " + title + "; " + description + "; " + publisher + "; " + relation
                f.write(entry  + '\n')     
              
            
            element = ListRecords[len(ListRecords) - 1]
            resumption_token = element.text
            i = i + 1

       
        if resumption_token is None:
            break
        
    else:
        print(f"Fehler mit Status-Code: {response.status_code}")