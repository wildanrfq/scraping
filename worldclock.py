from lib.sn import h;import time

wil,dan="https://www.timeanddate.com",[]

"""144 adalah total data world clock nya,
jadi kalo mau ngambil semua data harap bersabar :)"""

def getDetailWorldClock(maximum=144):
	start=time.time()
	data,dataa=h.bs(wil+"/worldclock/?sort=0").table,[]
	for clock in data.findAll("a")[:maximum]:dan.append(clock.text+"///"+wil+clock.get("href"))
	dan.sort()
	for clockk in dan:
		info=clockk.split("///")
		link=info[1]
		infoo=h.bs(link)
		time=infoo.find("span",class_="h1").text
		tz=infoo.find("span",{"id":"cta"});tz="{} ({})".format(tz.a.get("title"),tz.text)
		dt=infoo.find("span",{"id":"ctdat"}).text
		info2=[x.text.split(":  ")[1] for x in infoo.find("div",class_="five columns").findAll("p")]
		city,coun,ll,cur,lang,dial=info[0],info2[0],info2[1],info2[2],info2[3],info2[4].split(" - ")[0]
		dataa.append({"city":city,"link":link,"country":coun,"latLong":ll,"currency":cur,"language":lang,"dialCode":dial})
	h.pj(dataa)
	print("Execution time: {} seconds.".format(round(time.time() - start)))
		
def getSimpleWorldClock(maximum=144):
	start=time.time()
	data,dataa=h.bs(wil+"/worldclock/?sort=0").table,[]
	for clock in data.findAll("a")[:maximum]:dan.append(clock.text+"///"+wil+clock.get("href"))
	dan.sort()
	for clockk in dan:
		info=clockk.split("///");city,link=info[0],info[1]
		infoo=h.bs(link)
		dtime=infoo.find("span",{"id":"ctdat"}).text+", "+infoo.find("span",class_="h1").text
		dataa.append({"city":city,"datetime":dtime})
	h.pj(dataa)
	print("Execution time: {} seconds.".format(round(time.time() - start)))

getDetailWorldClock(10)
getSimpleWorldClock(10)