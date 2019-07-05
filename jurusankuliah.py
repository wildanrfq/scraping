from lib.sn import *

def jurusan(jurusan):
	data,dataa=h.bs("https://www.youthmanual.com/cari-jurusan?src="+jurusan),[]
	try:
		tx=data.article.get("h3")
		h.pj({"error":"Jurusan {} tidak ditemukan.".format(jurusan)})
	except:
		for jurusann in data.findAll("div",class_="col-sm-6 col-md-4 m-bot-30"):
			link=jurusann.a.get("href")
			studi=jurusann.h3.text
			info=jurusann.findAll("p")
			data2=h.bs(link)
			kategori=info[0].text
			penjuruan=info[2].text
			pelajaran=info[4].text
			desc=data2.find("meta",{"name":"description"}).get("content")
			info2=data2.findAll("p",class_="ted")
			kenapa=info[1].text
			info3=data2.find("div",class_="col-md-7 col-md-pull-5")
			matkul=[mat.li.text[1:] for mat in info3.findAll("ul",class_="list_order")[:9]]+[mat.li.text[2:] for mat in info3.findAll("ul",class_="list_order")[9:]]
			karakter=[kar.li.text for kar in info3.findAll("ul",class_="list_4")]
			prospek=info2[2].text
			info4=data2.findAll("div",class_="col-md-12 clearfix")
			profesilulusan=[prof.text for prof in info4[6].findAll("h3")]
			kampus=["{} ({})".format(kam.text.split("\n")[0],sek.text) for kam,sek in zip(info4[7].findAll("h3")[1:],info4[7].findAll("small"))]
			jurusanterkait=[jur.text[1:] if jur.text.startswith(" ") else jur.text for jur in data2.find("div",class_="col-xs-12 hidden-md hidden-lg").findAll("h3")[1:]]
			dataa.append({"studi":studi,"link":link,"kategori":kategori,"penjuruan":penjuruan,"pelajaran":pelajaran,"description":desc,"kenapaMemilih":kenapa,"matkul":matkul,"karakter":karakter,"prospek":prospek,"profesiLulusan":profesilulusan,"jurusanTerkait":jurusanterkait,"kampus":kampus})
		h.pj(dataa)
		
def jurusans(jurusan): #Spesifik
	data,dataa=h.bs("https://www.youthmanual.com/cari-jurusan?src="+jurusan),[]
	try:
		tx=data.article.get("h3")
		h.pj({"error":"Jurusan {} yang spesifik tidak ditemukan.".format(jurusan)})
	except:
		for jurusann in data.findAll("div",class_="col-sm-6 col-md-4 m-bot-30"):
			if jurusan.title() == jurusann.h3.text:
				link=jurusann.a.get("href")
				studi=jurusann.h3.text
				info=jurusann.findAll("p")
				data2=h.bs(link)
				kategori=info[0].text
				penjuruan=info[2].text
				pelajaran=info[4].text
				desc=data2.find("meta",{"name":"description"}).get("content")
				info2=data2.findAll("p",class_="ted")
				kenapa=info[1].text
				info3=data2.find("div",class_="col-md-7 col-md-pull-5")
				matkul=[mat.li.text[1:] for mat in info3.findAll("ul",class_="list_order")[:9]]+[mat.li.text[2:] for mat in info3.findAll("ul",class_="list_order")[9:]]
				karakter=[kar.li.text for kar in info3.findAll("ul",class_="list_4")]
				prospek=info2[2].text
				info4=data2.findAll("div",class_="col-md-12 clearfix")
				profesilulusan=[prof.text for prof in info4[6].findAll("h3")]
				kampus=["{} ({})".format(kam.text.split("\n")[0],sek.text) for kam,sek in zip(info4[7].findAll("h3")[1:],info4[7].findAll("small"))]
				jurusanterkait=[jur.text[1:] if jur.text.startswith(" ") else jur.text for jur in data2.find("div",class_="col-xs-12 hidden-md hidden-lg").findAll("h3")[1:]]
				h.pj({"studi":studi,"link":link,"kategori":kategori,"penjuruan":penjuruan,"pelajaran":pelajaran,"description":desc,"kenapaMemilih":kenapa,"matkul":matkul,"karakter":karakter,"prospek":prospek,"profesiLulusan":profesilulusan,"jurusanTerkait":jurusanterkait,"kampus":kampus})
				break
			else:
				h.pj({"error":"Jurusan {} yang spesifik tidak ditemukan.".format(jurusan)})
				break
			

jurusans("stat")
