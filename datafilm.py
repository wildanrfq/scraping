from lib.sn import h

def getData():
	data,dataa=h.bs("http://filmindonesia.or.id/movie/viewer").tbody,[]
	for film in data.findAll("tr"):
		r=film.td.text
		filmm=film.a
		link,title=filmm.get("href"),filmm.text
		pen=film.findAll("td")[-1].text
		dataa.append({"rank":r,"title":title,"link":link,"penonton":pen})
	h.pj(dataa)
	
getData()
	