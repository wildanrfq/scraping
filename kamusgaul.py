from lib.sn import *

def kataHariIni():
	data=h.bs("https://kitabgaul.com/words")
	kata=data.find("div",class_="word").text
	deff=data.find("div",class_="definition").text
	ex=str(data.find("div",class_="example").span)[6:][:-7].replace("<br/>","\n").replace("<a href=\"/word/a\">A</a>","A").replace("<a href=\"/word/b\">B</a>","B")
	h.pj({"kata":kata,"definisi":deff,"contoh":ex})
	
def cariKata(q):
	data,dataa=h.bs("https://kitabgaul.com/word/{}?kw={}".format(q,q)),[]
	err=data.find("div",class_="para").text
	if "Maaf" not in err:
		for kataa in data.findAll("div",class_="entryDetail"):
			kata=data.find("div",class_="word").text
			deff=data.find("div",class_="definition").text
			ex=str(data.find("div",class_="example").span)[6:][:-7].replace("<br/>","\n").replace("<a href=\"/word/a\">A</a>","A").replace("<a href=\"/word/b\">B</a>","B")
			dataa.append({"kata":kata,"definisi":deff,"contoh":ex})
		if len(dataa) == 1:
			for x in dataa:h.pj(x)
		else:h.pj(dataa)
	else:h.pj({"error":"Kata {} tidak ditemukan.".format(q)})

kataHariIni()
cariKata("anjay")