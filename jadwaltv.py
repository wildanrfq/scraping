from lib.sn import *
from datetime import *

channels=["antv","gtv","indosiar","inewstv","kompastv","mnctv","metrotv","nettv","rcti","sctv","rtv","trans7","transtv"]
jam=str(datetime.now().time()).split(":");jam="{}:{}".format(jam[0],jam[1])
def getJadwalTV(channel):
	if channel.lower() in channels:
		data,dataa=h.bs("https://www.jadwaltv.net/channel/"+channel).tbody,[]
		for jadwal in data.findAll("tr")[1:]:
			info=jadwal.findAll("td")
			dataa.append("{} - {}".format(info[0].text.replace("WIB"," WIB"),info[1].text.title()))
		h.pj(dataa)
	else:h.pj({"error":"Channel yang dituju salah! Daftar Channel yang tersedia: "+", ".join([ch.upper() for ch in channels])})

def getJadwalTVNow():
	data,dataa=h.bs("https://www.jadwaltv.net/channel/acara-tv-nasional-saat-ini").tbody,{"jam":jam,"jadwalTV":[]}
	for jadwal in data.findAll("tr")[1:]:
		info=" - ".join([x.text for x in jadwal.findAll("td")])
		dataa["jadwalTV"].append(info.replace("WIB"," WIB"))
	x="\n".join(dataa["jadwalTV"])
	dataa["jadwalTV"] = x
	h.pj(dataa)
	
getJadwalTVNow()