from lib.sn import h;import json

def cariKost(query):
	data,dataa=h.bs("https://m.infokost.id/search?q={}&checkin=2019-07-07&type=kost&price_type=monthly&order=&price=0-50000000&ac=false".format(query)).find("div",class_="result-search"),[]
	try:
		niherror=data.find("div",class_="alert alert- margin-top-20 text-center").text
		h.pj({"error":"Pencarian kost {} tidak ditemukan.".format(query)})
	except:
		for kost in data.findAll("div",class_="box-search"):
			title=kost.h2.text
			kamarr=[]
			link=kost.a.get("href")
			alamat=kost.find("div",class_="box-address").text[17:][:-12]
			info=h.bs(link)
			images=[img.get("src") for img in info.find("div",class_="detail-images").findAll("img")]
			fulldesc="".join([desc.text[56:][:-29] for desc in info.findAll("div",class_="full-width")[-1:]])
			if fulldesc==" - ":fulldesc.replace(" ","")
			for kamar in info.find("div",class_="container-detail").findAll("div",class_="room-row"):
				kamarw=kamar.div.text[13:][:-8]
				fasilitas=[fas.text for fas in kamar.find("div",class_="row").findAll("p")]
				desc=kamar.find("div",class_="room-subtitle").text[14:].replace("                                    Deskripsi","").replace(" \n            ","\n").replace("                     ","").replace("                    ","")
				if desc.endswith("\n"):desc=desc[:-1]
				desc=desc.split("\n")
				harga=kamar.find("div",class_="right room-price-detail").text
				kamarr.append({"kamar":kamarw,"fasilitas":fasilitas,"desc":desc,"harga":harga})
			dataa.append({"title":title,"link":link,"images":images,"alamat":alamat,"fullDesc":fulldesc,"kamar":kamarr})
		h.pj(dataa)
def cariKost2(query):
	data,dataa=h.bs("https://m.infokost.id/search?q={}&checkin=2019-07-07&type=kost&price_type=monthly&order=&price=0-50000000&ac=false".format(query)).find("div",class_="result-search"),[]
	try:
		niherror=data.find("div",class_="alert alert- margin-top-20 text-center").text
		h.pj({"error":"Pencarian kost {} tidak ditemukan.".format(query)})
	except:
		for kost in data.findAll("div",class_="box-search"):
			title=kost.h2.text
			kamarr=[]
			link=kost.a.get("href")
			alamat=kost.find("div",class_="box-address").text[17:][:-12]
			info=h.bs(link)
			images=[img.get("src") for img in info.find("div",class_="detail-images").findAll("img")]
			fulldesc="".join([desc.text[56:][:-29] for desc in info.findAll("div",class_="full-width")[-1:]])
			if fulldesc==" - ":fulldesc.replace(" ","")
			for kamar in info.find("div",class_="container-detail").findAll("div",class_="room-row"):
				kamarw=kamar.div.text[13:][:-8]
				fasilitas=[fas.text for fas in kamar.find("div",class_="row").findAll("p")]
				desc=kamar.find("div",class_="room-subtitle").text[14:].replace("                                    Deskripsi","").replace(" \n            ","\n").replace("                     ","").replace("                    ","")
				if desc.endswith("\n"):desc=desc[:-1]
				desc=desc.split("\n")
				images=[img.get("src") for img in info.findAll("img",{"alt":kamarw})]
				harga=kamar.find("div",class_="right room-price-detail").text
				kamarr.append({"kamar":kamarw,"fasilitas":fasilitas,"desc":desc,"harga":harga})
			dataa.append({"title":title,"link":link,"images":images,"alamat":alamat,"fullDesc":fulldesc,"kamar":kamarr})
		return json.dumps(dataa)
				

			
			
cariKost("undip")
