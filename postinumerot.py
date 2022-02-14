# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.

import json
import urllib.request

def postinumerot_func(postitmp): 

    with urllib.request.urlopen("https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json") as response:
        html = response.read()

    data = json.loads(html)
    city = postitmp.upper()
    nrot = [k for k,v in data.items() if v == city]
    nrot.sort()
    try:
        print("Postinumerot: " + ', '.join(nrot))
    except:
        print("Tuntematon postitoimipaikka")

    return nrot