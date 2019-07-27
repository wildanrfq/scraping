from lib.sn import *

def findLyrics(q):
	data,dataa=h.bs("https://search.azlyrics.com/search.php?q={}&w=songs&p=1".format(q)),[]
	for lyric in data.findAll("td",class_="text-left visitedlyr")[:10]:
		info=lyric.findAll("b")
		title=info[0].text;artist=info[1].text
		lyric=h.bs(lyric.a.get("href")).find("div",class_="col-xs-12 col-lg-8 text-center").findAll("div")[6].text[2:][:-1]
		dataa.append({"title":title,"artist":artist,"lyric":lyric})
	h.pj(dataa)
		
findLyrics("yellow")