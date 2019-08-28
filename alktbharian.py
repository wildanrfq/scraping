from lib.sn import *

dataz=h.bs('https://www.bible.com/id/verse-of-the-day')
image = dataz.find("meta",{"property":"og:image"}).get("content")
isi = dataz.find("meta",{"name":"description"}).get("content")[:-1]
link=dataz.find("meta", {"property":"og:url"}).get("content")
ayat=h.bs(link).title.text.split(" - ")[1].split(" | ")[0]
print(json.dumps({"ayat": ayat, "isi": isi, "link":link, "image": image}, indent=4, sort_keys=False))
