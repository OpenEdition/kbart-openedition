import urllib.request
import json

URL = "https://bacon.abes.fr/list.json"
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

f=open(OUTPUT_FILE, "w+")
output = urllib.request.urlopen(URL)
output = json.load(output);
output = output["bacon"]["query"]["results"]
output = list(filter(lambda x: x["element"]["provider"] == PROVIDER, output))
output = list(filter(lambda x: not(x["element"]["package"] in EXCLUDED), output))
for package in output:
  line = package["element"]["package"]
  line = " * `"+line.replace("GLOBAL_EBOOKS-","").replace("-"," ").lower().capitalize()+" <https://bacon.abes.fr/package2kbart/"+PROVIDER+"_"+line+">`_ \n"
  f.write(line)
print("SUCCESS")
