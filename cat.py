from lib.sn import h
import random

def catOfTheDay():
	data=h.bs("http://www.funnycatpix.com/")
	title=h.bs(data.base.get("href")+data.a.get("href")).title.text
	cat=data.base.get("href")+data.img.get("src")
	h.pj({"title":title,"image":cat})

def randomFunnyCatVideo():
	data,dataa=h.bs("http://www.catsvscancer.org/section/video/"),[]
	for vids in data.findAll("div",class_="video-btn-wrapper"):
		vid=h.bs(vids.a.get("href"))
		title=vid.h3.text[:-1]
		link=vid.iframe.get("src")
		if "facebook" in link:
			x=link.split("href=")[1].split("&show")[0]
			link=h.bs("https://www.videofk.com/facebook-video-download/search?url={}&select=facebook".format(x))
			link=link.findAll("a")[9].get("href")
		else:
			id=link.split("embed/")[1].split("?")[0]
			link=h.ytmp4(id)
		dataa.append({"title":title,"video":link})
	h.pj(random.choice(dataa))
	
def randomFunnyCatPictures():
	data,dataa=h.bs("https://funnycatsite.com"),[]
	for cat in data.main.findAll("img"):
		image=data.base.get("href")+cat.get("src").replace("thumbs","pictures").replace("_s","").lower()
		title=cat.get("alt")
		dataa.append({"title":title,"image":image})
	h.pj(random.choice(dataa))
		
catOfTheDay()
randomFunnyCatVideos()
randomFunnyCatPictures()