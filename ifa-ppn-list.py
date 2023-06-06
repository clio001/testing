import xml.etree.ElementTree as ET

f = open('ifa-201-ppns.txt', 'a')
f.write('PPN; SetSpecification; Title; Creator; Subject; Publisher; Date; Identifier' + '\n')

tree = ET.parse('ifa.txt')
root = tree.getroot()

ListRecords = root[2]

for record in ListRecords:
    ppn = record[0][0].text
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

    f.write(ppn +"; " + setSpec +"; " + str(title.encode()).replace("b'", "").replace("'", "") +"; " + str(creator.encode()).replace("b'", "").replace("'", "") + "; " + subject + "; " + str(publisher.encode()).replace("b'", "").replace("'", "") + "; " + date + "; " + identifier + '\n')


print(f"{len(ListRecords)} Records")

