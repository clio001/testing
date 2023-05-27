import requests

base_url = "https://www.digishelf.de/oai"

verb = "ListRecords"
metadata_prefix = "oai_dc"
set_spec = "kolonialismus"

request_url = f"{base_url}?verb={verb}&metadataPrefix={metadata_prefix}&set={set_spec}"


response = requests.get('https://digishelf.de/oai?verb=ListRecords&metadataPrefix=oai_dc&set=kolonialismus')
if response.status_code == 200:
    result = response.content.decode('utf-8')
    f = open('ifa.txt', 'w')
    f.write(result)
    print(result)
else:
    print(f"Fehler mit Status-Code: {response.status_code}")