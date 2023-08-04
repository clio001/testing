import requests, xml.etree.ElementTree as ET

base_url = "https://oai.sbb.berlin/"

verb = "ListRecords"
metadata_prefix = "oai_dc"
set_spec = "afrikanische.handschriften"

resumption_token = None

f = open('afrikanischhand.txt', 'w', encoding="utf-8")
f.write("PPN; Jahr; Titel; Publisher"  + '\n')

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
                    if date == "13XX" or "18XX" or date == "186X" or date == "19XX" or date == "17XX" or 1799 < int(date) < 1934:
                        elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}title")
                        if elementTag:
                            title = elementTag[0].text
                            title
                        else:
                            title = "none"
                        
                        elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}publisher")
                        if elementTag:
                            publisher = elementTag[0].text
                        else:
                            publisher = "none"
                        
                        elementTag = record.findall(".//{http://purl.org/dc/elements/1.1/}identifier")
                        if elementTag:
                            identifier = elementTag[0].text
                        else:
                            identifier = "none"
                        
                        entry = identifier + "; " + date + "; " + title + "; " + publisher
                        f.write(entry  + '\n')
            
                    else:
                        continue
                
                        
                   
            
            element = ListRecords[len(ListRecords) - 1]
            resumption_token = element.text
            i = i + 1

       
        if resumption_token is None:
            break
        
    else:
        print(f"Fehler mit Status-Code: {response.status_code}")