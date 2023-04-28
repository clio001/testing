import xml.etree.ElementTree as ET

tree = ET.parse('opac-de-1.xml')
root = tree.getroot()

for child in root[2][0][2][0]:
    if child.attrib['tag'] == "021A":
        print(f"Title: {child[0].text}")
    if child.attrib['tag'] == "028A":
        for e in child:
            if e.attrib['code'] == "D":
                print(f"Author: {e.text}")
            

