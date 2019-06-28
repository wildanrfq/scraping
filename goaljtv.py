from lib.sn import *;import datetime
data,dataa=h.bs("https://www.goal.com/id/berita/jadwal-siaran-langsung-sepakbola/1qomojcjyge9n1nr2voxutdc1n").find("div",class_="body"),[]
hari=["Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu","Minggu"]

def jadwal():
	for kompetisii in data.findAll("a",{"target":"_blank"}):
		info=h.bs(kompetisii.get("href"))
		infox=kompetisii.text.split(" | ")
		jam=infox[0]
		pertandingan=infox[1]
		channel=infox[2]
		infoo=info.title.text.split(",")
		kompetisi=infoo[2].split(" | ")[0][1:]
		try:
			dt=infoo[1][1:].split("/")
			day=hari[datetime.date(int(dt[0]),int(dt[1]),int(dt[2])).weekday()]
			month=h.tr(datetime.date(int(dt[0]),int(dt[1]),int(dt[2])).strftime("%B"),"en","id")
			datee="{}, {} {} 20{}".format(day, dt[0],month,dt[2])
		except:
			dt=info.find("time",{"data-dateformat":"monthDay"}).text[2:].split("/")
			day=hari[datetime.date(int(dt[0]),int(dt[1]),int(dt[2])).weekday()]
			month=h.tr(datetime.date(int(dt[0]),int(dt[1]),int(dt[2])).strftime("%B"),"en","id")
			datee="{}, {} {} 20{}".format(day, dt[0],month,dt[2])
		dataa.append({"pertandingan":pertandingan,"kompetisi":kompetisi,"tanggal":datee,"jam":jam,"channel":channel})
	h.pj(dataa)
jadwal()
	