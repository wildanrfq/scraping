from lib.sn import *;import datetime as _dt;from humanfriendly import *
data,dataa=h.bs("https://www.goal.com/id/berita/jadwal-siaran-langsung-sepakbola/1qomojcjyge9n1nr2voxutdc1n").find("div",class_="body"),[]
hari=["Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu","Minggu"]

def jadwal():
	for kompetisii in data.findAll("a",{"target":"_blank"}):
		info=h.bs(kompetisii.get("href"))
		infox=kompetisii.text.split(" | ")
		jam=infox[0]
		pertandingan=infox[1]
		channel=infox[2]
		if channel.endswith(" "):
			channel=channel[:-1]
		infoo=info.title.text.split(",")
		kompetisi=infoo[2].split(" | ")[0][1:]
		try:
			dt=infoo[1][1:].split("/")
			dt=[format_number(dt2) for dt2 in dt]
			brp=_dt.date(int("20"+str(dt[2])),int(dt[1]),int(dt[0]))
			day=hari[brp.weekday()]
			month=h.tr(_dt.date(int("20"+str(dt[2])),int(dt[1]),int(dt[0])).strftime("%B"),"en","id")
			brp=str(brp).split("-")
			datee="{}, {} {} {}".format(day,dt[0],month,brp[0])
		except:
			dt=info.find("time",{"data-dateformat":"dateShort"}).text.split("/")
			dt=[format_number(dt2) for dt2 in dt]
			brp=_dt.date(int("20"+str(dt[2])),int(dt[1]),int(dt[0]))
			day=hari[brp.weekday()]
			month=h.tr(_dt.date(int("20"+str(dt[2])),int(dt[1]),int(dt[0])).strftime("%B"),"en","id")
			brp=str(brp).split("-")
			datee="{}, {} {} {}".format(day,dt[0],month,brp[0])
		dataa.append({"pertandingan":pertandingan,"kompetisi":kompetisi,"tanggal":datee,"jam":jam,"channel":channel})
	h.pj(dataa)
jadwal()
	
