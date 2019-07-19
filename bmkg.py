from lib.sn import h

data=h.bsverif("https://www.bmkg.go.id/warning.bmkg")
def getInfo():
	image=data.find("img",class_="img-responsive").get("src")
	maps=data.find("a",class_="more").get("href")
	info=data.find("div",class_="col-xs-6 gempabumi-detail no-padding").findAll("li")
	waktu=info[0].text
	title=data.h3.text
	magnitudo=info[1].text
	kedalaman=info[2].text
	koordinat=info[3].text
	lokasi=info[4].text
	tsunami=info[5].text
	h.pj({"title":title,"image":image,"waktu":waktu,"magnitudo":magnitudo,"kedalaman":kedalaman,"koordinat":koordinat,"tsunami":tsunami,"lokasi":lokasi,"maps":maps})
	
getInfo()