import pandas as pd

systemstelle = "U"
titel = "afrika"
start = 5230 # Start-Signatur
ende = 6458 # End-Signatur
quelldatei = "kart-u-historische-karten.txt"
dateiname = f"kart-u-{start}-{ende}-{titel}.csv" # Dateiname der Zieldatei

sgnList = []

treffer = 0

print(f"""
- - - - - - - - - - - -
Signatur-Retrieval aus der Historischen Systematik der SBB-Kartenabteilung

Systemstelle: Kart. {systemstelle}
Signaturbereich: {systemstelle} {start} - {systemstelle} {ende}
- - - - - - - - - - - -
""")

while start < ende:
    sgnList.append(systemstelle + " " + str(start))
    start = start + 1
    
# Erstelle Ziel-Datei
datei = open(dateiname, 'a', encoding="utf-8")
datei.write("PPN" + "; " + "EPN" + "; " + "Jahr" + "; " + "Titel+Zusatz" +"; " +  "Verfasser" + "; " + "Ort+Verlag" + "; " + "Umfang" + "; " +  "Basisklassifikation"+"; " +  "Schlagwort" + "; " + "ExKommentar4802" +"; " + "Schlagwort6800" + "; " + "Abrufzeichen8600"+ "; " + "Signatur" + "; " + "Standort" + "; " + "URL")


# Lies CBS-Export in 'karten_df' Datenframe von Pandas
karten_df = pd.read_csv(quelldatei, sep="\t")

# Ersetze NaN in Tabelle mit eigenem Text
karten_df["Signatur"] = karten_df["Signatur"].fillna("k.a.")

# Schleife, um zu überprüfen, ob gesuchte Signaturen sich in der Spalte Signaturen des Dataframes 'karten_df' befinden

for index, row in karten_df.iterrows():
    print("Exemplare: ", index, end="\r")
    for sgn in sgnList:
        if str(sgn) in karten_df.loc[index, "Signatur"]:
            treffer = treffer + 1
            
            PPN = karten_df.loc[index, "PPN"]
            EPN = karten_df.loc[index, "EPN"]
            Jahr =  karten_df.loc[index, "Jahr"]
            TitelZusatz = karten_df.loc[index, "Titel+Zusatz"]
            Verfasser = karten_df.loc[index, "Verfasser"]
            OrtVerlag = karten_df.loc[index, "Ort+Verlag"]
            Umfang = karten_df.loc[index, "Umfang"]
            Basisklassifikation = karten_df.loc[index, "Basisklassifikation"]
            Schlagwort = karten_df.loc[index, "Schlagwort"]
            ExKommentar = karten_df.loc[index, "ExKommentar4802"]
            SchlagwortLokal = karten_df.loc[index, "Schlagwort6800"]
            Abrufzeichen = karten_df.loc[index, "Abrufzeichen8600"]
            Signatur = karten_df.loc[index, "Signatur"]
            Standort = karten_df.loc[index, "Standort"]
            URL = karten_df.loc[index, "URL"]
            
            datei.write(str(PPN) + "; " + str(EPN) + "; " + str(Jahr) + "; " + str(TitelZusatz) + "; " + str(Verfasser) + "; " + str(OrtVerlag) + "; " + str(Umfang) + "; " + str(Basisklassifikation) + "; " + str(Schlagwort) + "; " + str(ExKommentar) + "; " + str(SchlagwortLokal) + "; " + str(Abrufzeichen) + "; " + str(Signatur) + "; " + str(Standort) + "; " + str(URL) + "\n")
        else:
            continue

print(f"""

- - - - - - - - - - - -
Abfrage abgeschlossen!

{treffer} Titel in {dateiname} gespeichert.
""")