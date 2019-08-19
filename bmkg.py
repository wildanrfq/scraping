from lib.sn import h

data=h.bsverif("https://www.bmkg.go.id/warning.bmkg").findAll("section")[1]

def getInfo():

	info=data.ul.findAll("li")

	title=data.h3.text

	waktu=data.h5.text

	magnitudo=info[0].text.split("Magnitudo")[0]

	kedalaman=info[1].text.split("Keda")[0]

	koordinat=info[2].text.replace("LS","LS - ")

	infoo=data.find("div",class_="col-12").findAll("p")

	infoo[3].span.decompose();infoo[1].span.decompose();infoo[2].span.decompose()

	infox=infoo[0].text

	lokasi=infoo[1].text

	arahan=infoo[2].text

	saran=infoo[3].text

	shakemap=data.find("a",class_="tombol shakemap").get("href")

	h.pj({"title":title,"shakemap":shakemap,"waktu":waktu,"magnitudo":magnitudo,"kedalaman":kedalaman,"koordinat":koordinat,"info":infox,"lokasi":lokasi,"arahan":arahan,"saranBMKG":saran})

	

getInfo()
