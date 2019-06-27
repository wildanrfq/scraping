from lib.sn import *

dataz=h.bs('https://awsubs.tv')
dataa=[]
for info in dataz.findAll("div", class_="rld"):
	image = info.img.get("src")
	link = info.a["href"]
	title = info.a["title"]
	anime=h.bs(link)
	infoa=anime.find("table",class_="listinfo").findAll("td")
	type=infoa[1].text
	status=infoa[2].text
	episodes=infoa[3].text
	genre=infoa[5].text
	duration=infoa[6].text
	wkwk=anime.find("div",class_="bxcl").ul.findAll("li")
	linkdl=[{"title":x.a.text,"link":x.a.get("href"),"date":x.find("span",class_="dt").text} for x in wkwk]
	dataa.append({"title": title, "link": link, "image": image,"type":type,"status":status,"episodes":episodes,"genre":genre,"duration":duration,"download":linkdl})
	
h.pj(dataa)