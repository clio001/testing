import requests

response = requests.get("https://kvk.bibliothek.kit.edu/hylib-bin/kvk/nph-kvk2.cgi?maske=kvk-redesign&lang=de&title=KIT-Bibliothek%3A+Karlsruher+Virtueller+Katalog+KVK+%3A+Ergebnisanzeige&head=%2F%2Fkvk.bibliothek.kit.edu%2Fasset%2Fhtml%2Fhead.html&header=%2F%2Fkvk.bibliothek.kit.edu%2Fasset%2Fhtml%2Fheader.html&spacer=%2F%2Fkvk.bibliothek.kit.edu%2Fasset%2Fhtml%2Fspacer.html&footer=%2F%2Fkvk.bibliothek.kit.edu%2Fasset%2Fhtml%2Ffooter.html&css=none&input-charset=utf-8&ALL=&TI=Die+Musikinstrumente+Birmas+und+Assams+im+K.+Ethnographischen+Museum+zu+M%C3%BCnchen&AU=&CI=&ST=&PY=1917&SB=&SS=&PU=&searchDigitalMediaOnly=1&kataloge=K10PLUS&kataloge=BVB&kataloge=NRW&kataloge=HEBIS&kataloge=KOBV_SOLR&kataloge=DDB&ref=direct&client-js=yes&autosubmit")

print(response)