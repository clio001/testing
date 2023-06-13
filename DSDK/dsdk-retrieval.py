import requests, xml.etree.ElementTree as ET

def parseData():
    f = open('dsdk.txt')
    content = f.read()
    data = content.encode()
    x = data.decode()
    print(x)
      
    root = ET.fromstring(data)
    
    record = root[2]
    print(record)

    


#FETCH DSDK RECORDS

def getData():
    url = "https://sru.k10plus.de/gvk?version=1.1&operation=searchRetrieve&query=pica.lsw=Digitale%20Sammlung%20Deutscher%20Kolonialismus&maximumRecords=600&recordSchema=picaxml&startRecord=601"
    response = requests.get(url)
    data = response.content.decode('utf-8')
    writeData(data)
    
def writeData(data):
    f = open('dsdk-1.txt', 'w')
    f.write(str(data.encode()))
    f.close()
   
#getData()
parseData()
    