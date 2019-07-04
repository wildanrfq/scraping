from lib.sn import h

url="https://m.karir.com"
def loker():
	data,dataa=h.bs(url+"/search").find("ul",class_="opportunities-list"),[]
	for ker in data.findAll("li",class_="opportunity opportunity-search-click"):
		perusahaan=ker.h3.text
		link=url+ker.get("data-url")
		profesi=ker.h2.text.title()
		if profesi.endswith(" "):profesi=profesi[:-1]
		gaji=ker.find("span",class_="tdd-salary").text
		lokasi=ker.find("div",class_="tdd-location").text
		info=h.bs(link)
		infoo=info.findAll("div",class_="bm-opportunity-stat__value")
		pengalaman=infoo[2].text
		jobfunction=infoo[1].text
		levelkarir=infoo[3].text
		edukasi=infoo[4].text
		info2=info.findAll("section",class_="b-matte__content")
		desc=info2[0].text
		req=info2[1].text
		dataa.append({"perusahaan":perusahaan,"link":link,"profesi":profesi,"gaji":gaji,"lokasi":lokasi,"pengalaman":pengalaman,"jobFunction":jobfunction,"levelKarir":levelkarir,"edukasi":edukasi,"desc":desc,"syarat":req})
	h.pj(dataa)
loker()