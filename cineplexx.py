from lib.sn import *

url="https://m.21cineplex.com/"
def cineplex(chc):
	dataa=[]
	if chc=="nowplaying":data=h.bs(url)
	elif chc=="comingsoon":data=h.bs(url+"gui.coming_soon.php")
	for film in data.findAll("div",class_="grid_movie"):
		link=url+film.a.get("href")
		title=film.find("div",class_="title").text.title()
		dimensi=film.span.text
		try:rating=film.findAll("a")[1].text
		except:rating="-"
		data2=h.bs(link)
		genre=data2.findAll("div",class_="col-xs-8 col-sm-11 col-md-11")[1].text.replace('                                    ',"").replace('                                ','')
		if genre.endswith(" "):genre=genre[:-1]
		poster=data2.find("img",class_="img-responsive pull-left gap-left").get("src")
		trailer=data2.findAll("button")[4].get("onclick").split("'")[1].split("'")[0]
		sinopsis=data2.find("p",{"id":"description"}).text
		info=data2.findAll("p")
		producer=info[7].text
		if producer.startswith(" "):producer=producer[1:]
		director=info[9].text
		writer=info[11].text
		casts=info[13].text
		distributor=info[15].text
		if len(info) == 17 and info[17].get("href") != "":
			linkmovie=info[17].get("href")
		else:linkmovie="-"
		dataa.append({"title":title,"distributor":distributor,"poster":poster,"genre":genre,"dimensi":dimensi,"rating":rating,"sinopsis":sinopsis,"producer":producer,"director":director,"writer":writer,"casts":casts,"sinopsis":sinopsis,"link":link,"linkmovie":linkmovie})
	h.pj(dataa)
cineplex("comingsoon")