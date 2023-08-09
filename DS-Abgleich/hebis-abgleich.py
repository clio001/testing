import requests

response = requests.get("http://sru.hebis.de/sru/DB=2.1?query=pica.ppn+%3D+%22501231862%22&version=1.1&operation=searchRetrieve&recordSchema=picaxml&maximumRecords=10")

result = response.content.decode('utf-8')
print(result)