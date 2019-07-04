from lib.sn import *

data,dataa=h.bsverif("https://turnbackhoax.id"),[]
def hoaxes():
	for hoax in data.findAll("div",class_="mh-loop-content mh-clearfix"):
		link=hoax.a.get("href");image=h.bs(link).figure.img.get("src")
		title=hoax.a.text[6:][:-4]
		tag=title[1:].split("]")[0]
		title=title.split("] ")[1]
		if title == title.upper():title=title.title()
		dataa.append({"tag":tag,"title":title,"link":link,"image":image})
	h.pj(dataa)

def getHoax(link):
	data=h.bsverif(link).find("div",class_="entry-content mh-clearfix")
	berita=data.text[5:][:-74]
	listimg=[image.get("src") for image in data.findAll("img")]
	h.pj({"berita":berita,"listImage":listimg})
	
getHoax("https://turnbackhoax.id/2019/07/04/salah-akhirnya-thoriq-ditemukan-dengan-selamat/")