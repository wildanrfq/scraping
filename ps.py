from lib.sn import h

url="https://play.google.com"
def findApps(query):
	data,dataa=h.bs(url+"/store/search?q={}&c=apps".format(query)),[]
	for app in data.findAll("div",class_="Vpfmgd"):
		image=app.img.get("data-src")
		infoo=app.findAll("a")[2]
		link=url+infoo.get("href")
		title=infoo.text
		developer=app.find("a",class_="mnKHRc").text
		desc=app.find("div",class_="b8cIId f5NCO").text
		info=h.bs(link)
		rated="{}/5 ({})".format(app.find("div",{"role":"img"}).get("aria-label").split(" ")[1].split(" ")[0],info.findAll("span",class_="")[2].text)
		genre=info.find("a",{"itemprop":"genre"}).text
		rating=info.find("img",class_="T75of E1GfKc").get("alt").split(" ")[1]
		fulldesc=info.find("meta",{"itemprop":"description"}).get("content")
		email=info.find("a",class_="hrTbp euBY6b").text
		version=info.findAll("span",class_="htlgb")[6].text
		dataa.append({"title":title,"link":link,"image":image,"developer":developer,"shortDesc":desc,"rated":rated,"rating":rating,"genre":genre,"version":version,"fullDesc":fulldesc,"emailDev":email})
	h.pj(dataa)
findApps("pubg")