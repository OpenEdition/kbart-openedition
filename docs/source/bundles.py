#le script fonctionne en exposant sur le web ce Gdoc : https://docs.google.com/spreadsheets/d/1cRGLuwb13Xnmy8G6v1S0p9X2L_ZVvay_S0sifS3Bwvg/edit#gid=1546125655 via la fonction publier sur le web
#a priori ces infos ne sont un secret pour personne
#seule la feuille "kbart equiv" est exposée

import urllib.request
import json

URL = "https://bacon.abes.fr/list.json"
NAMES_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS_tX7qEeulus9SsWYfmsXonbxOeSU2MiqHioVLF60elpz4IZDHZiO7NrusfhnssceKIJnykWQoXXfv/pub?gid=1546125655&single=true&output=csv"
PROVIDER = "OPENEDITION"
OUTPUT_FILE = "bundles.rst"
# excluded packages, we don't want them in the bundles list :
EXCLUDED = ["GLOBAL_ALLTITLES",
"GLOBAL_ALLJOURNALS",
"GLOBAL_ALLEBOOKS",
"GLOBAL_HYPOTHESES",
"GLOBAL_JOURNALS-OPENACCESS",
"GLOBAL_JOURNALS-OPENACCESS-FREEMIUM",
"GLOBAL_JOURNALS-WITH-EMBARGO-PERIOD",
"GLOBAL_EBOOKS-OPENACCESS",
"GLOBAL_EBOOKS-OPENACCESS-FREEMIUM",
"GLOBAL_EBOOKS-EXCLUSIVE-ACCESS",
"FRANCE_ISTEXBOOKS"]
names = {}
NAMES_URL = bytes.decode(urllib.request.urlopen(NAMES_URL).read()).replace("\r","").replace("(mois année)","").replace("(année)","").replace("(année semestre)","").split("\n")
for line in NAMES_URL:
  line = line.split(",")
  names[line[1]] = line[0]
f=open(OUTPUT_FILE, "w+")
output = urllib.request.urlopen(URL)
output = json.load(output)
output = output["bacon"]["query"]["results"]
output = list(filter(lambda x: x["element"]["provider"] == PROVIDER, output))
output = list(filter(lambda x: not(x["element"]["package"] in EXCLUDED), output))
for package in output:
  line = package["element"]["package"]
  try:
    line = " * `"+names[line.replace("GLOBAL_EBOOKS-","")]+" <https://bacon.abes.fr/package2kbart/"+PROVIDER+"_"+line+">`_ \n"
  except:
    line = " * `"+line.replace("GLOBAL_EBOOKS-","").replace("-"," ").lower().capitalize()+" <https://bacon.abes.fr/package2kbart/"+PROVIDER+"_"+line+">`_ \n"
  f.write(line)
print("SUCCESS")
