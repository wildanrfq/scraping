from lib.sn import *

daerahs=json.loads(open("lib/js.json","r").read())
def jadwalSholat(daerah):
	daerah=daerah.title()
	if daerah in daerahs.keys():
		data=[waktu.text for waktu in h.bs("https://www.jadwalsholat.org/adzan/monthly.php?id="+daerahs[daerah]).find("tr",class_="table_highlight").findAll("td")[1:]]
		imsyak,subuh,dhuha,dzuhur,ashar,maghrib,isya=data[0],data[1],data[2],data[3],data[4],data[5],data[6]
		h.pj({"Imsyak":imsyak,"Subuh":subuh,"Dhuha":dhuha,"Dzuhur":dzuhur,"Ashar":ashar,"Maghrib":maghrib,"Isya":isya})
	else:
		h.pj({"error":"Daerah yang tersedia hanya: {}".format(", ".join(daerahs.keys()))})
	
	
jadwalSholat("kendal")