import xml.etree.ElementTree as ET, requests

response = requests.get("https://oai.sbb.berlin/?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:digital.staatsbibliothek-berlin.de:PPN867445300")

xml = response.content



in_context = [
        {
          "id": "1",
          "creator": "Heinrich Barth",
          "recordTitle": "Reisen im südlichen Sahel",
          "pubYear": "1858",
          "pubPlace": "Berlin",
          "recordSchema": "oai_dc",
          "institutionRecord": xml,
          "imgUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/TIMBUKTU-EINZUG.jpg/220px-TIMBUKTU-EINZUG.jpg"
        },
                {
          "id": "2",
          "creator": "Bruno Hassenstein",
          "recordTitle": "Brief an Heinrich Barth",
          "pubYear": "1856",
          "pubPlace": "Berlin",
          "recordSchema": "ead",
          "institutionRecord": "ead",
          "imgUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/TIMBUKTU-EINZUG.jpg/220px-TIMBUKTU-EINZUG.jpg"
        },

      ]




recordXml = ET.fromstring(xml)
elementTag = recordXml.findall(".//{http://purl.org/dc/elements/1.1/}title")
if elementTag:
    schemaTitle = elementTag[0].text
else:
    schemaTitle = "keine Angabe"   

for element in in_context:
#include record schema check       
    
    
    print("Item: " + element["id"])
    print("- - - - - - - - - - - - - - - - - - -")
    print("Creator: " + element["creator"])
    print("Title: " + schemaTitle)
    print("Place: " + element["pubPlace"])
    print("Year: " + element["pubYear"])
    print("Schema: ")
    print("\n")