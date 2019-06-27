from lib.sn import *
from urllib.parse import quote

def alkitabcari(q):
	dataz,dataa=h.bs('https://www.bible.com/id/search/bible?q='+quote(q)),[]
	for wildan in dataz.findAll("li", {"class": "reference"}):
		ayat=wildan.a.text
		link="https://bible.com"+wildan.a.get("href")
		isi=wildan.p.text.replace("\n","")
		dataa.append({"ayat":ayat,"isi": isi, "link":link})
	return h.pj(dataa)
	
print(alkitabcari("ayam"))