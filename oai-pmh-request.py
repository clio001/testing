import requests, xml.etree.ElementTree as ET

base_url = "https://www.digishelf.de/oai"

verb = "ListRecords"
metadata_prefix = "oai_dc"
set_spec = "kolonialismus"

resumption_token = None

i = 1

while True:
    print(i)
    if resumption_token:
        request_url = f'{base_url}?verb={verb}&resumptionToken={resumption_token}'
    else:
        request_url = f"{base_url}?verb={verb}&metadataPrefix={metadata_prefix}&set={set_spec}"

    response = requests.get(request_url)

    if response.status_code == 200:
        result = response.content.decode('utf-8')
        f = open('ifa.txt', 'a')
        f.write(result)
        print(result)
        
        root = ET.fromstring(result)
        
        if root[1].text == "0":
            print("No record")
            
        else:
            ListRecords = root[2]
            element = ListRecords[len(ListRecords) - 1]
            resumption_token = element.text
            i = i + 1

       
        if resumption_token is None:
            break
        
    else:
        print(f"Fehler mit Status-Code: {response.status_code}")