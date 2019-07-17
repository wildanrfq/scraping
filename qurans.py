from lib.sn import h

def search(q):
	data,dataa=h.bs("https://alquran-indonesia.com/search.php?search="+q),[]
	for surat in data.findAll("div",class_="panel panel-default")[:10]:
		arabic=surat.p.text
		golongan=surat.find("div",class_="panel-heading").text[9:][:-7].split("/ ")[1].split(" (")[0]
		suratt="Q.S. {}: {}".format(surat.b.text[:-1],surat.find("div",class_="panel-heading").text[9:][:-7].split(":")[1].split(")")[0])
		arti=surat.find("div",class_="pull-left m-left-sm m-top-sm ltr").text[12:][:-11]
		latin=surat.find("div",class_="tab-pane fade latin").p.text[1:].replace("\n","").capitalize()
		latin=latin[:-1] if latin.endswith(" ") else latin
		audio=surat.find("button",{"id":"nextStep"}).get("data-selector")
		try:asbabun=surat.find("div",{"id":"message89"}).p.text
		except:asbabun="-"
		dataa.append({"surat":suratt,"golongan":golongan,"ayat":{"arabic":arabic,"latin":latin,"arti":arti,"audio":audio},"asbabunNuzul":asbabun})
	h.pj(dataa)
search("Muhammad")