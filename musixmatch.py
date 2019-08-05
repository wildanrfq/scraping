from lib.sn import *

wil="https://www.musixmatch.com"
def findSong(q):
	data,dataa=h.bs(wil+"/search/"+q+"/tracks").find("div",class_="box-content"),[]
	for song in data.findAll("li",class_="showArtist showCoverart"):
		title=song.h2.text
		artist=song.h3.text
		link=wil+song.a.get("href")
		dataa.append({"title":title,"artist":artist,"link":link})
	h.pj(dataa)

def getLyric(link):
	return "\n".join([x.text for x in h.bs(link).findAll("p")[0:2]])
	
		
findSong("Rich Brian")
getLyric("https://www.musixmatch.com/lyrics/Rich-Brian-2/Dat-tick")