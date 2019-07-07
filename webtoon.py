from lib.sn import *;from progress.bar import *;from humanfriendly import format_size as fn;from datetime import datetime,date
from googletrans import *
import os,shutil,urllib.request,requests

hariini=datetime.now().strftime("%A").upper()
hari={"sen":"Senin","sel":"Selasa","rab":"Rabu","kam":"Kamis","jum":"Jum'at","sab":"Sabtu","min":"Minggu"}
data=h.bs("https://m.webtoons.com/id/dailySchedule?webtoon-platform-redirect=true").find("div",class_="daily_section _list_"+hariini)
datetoday=str(date.today()).split("-")
hariini="{}, {}".format(Translator().translate(hariini.title(),dest="id",src="en").text,"{} {} {}".format(datetoday[2],Translator().translate(datetime.today().strftime("%B"),dest="id",src="en").text,datetoday[0]));dataa={hariini:[]}
def getWebtoonToday():
	for webtun in data.findAll("li"):
		link=webtun.a.get("href")
		image=webtun.img.get("src").replace("webtoo","swebtoo").split("?")[0]
		info=[dan.text for dan in webtun.findAll("p")]
		genre=info[0].title()
		title=info[1]
		author=info[2]
		status=info[3]
		likes=info[4][4:].replace("M","jt")
		webtoon=h.bs(link)
		desc=webtoon.find("p",class_="summary").text
		infoo=webtoon.findAll("em",class_="cnt")
		rating,subs=infoo[1].text,infoo[0].text
		updatedays=webtoon.find("p",class_="day_info").text[9:]
		if "," in updatedays:
			updatedays=updatedays.split(", ")
			updatedays=", ".join([hari[day.lower()] for day in updatedays])
		else:updatedays=updatedays.title()
		dataa[hariini].append({"title":title,"link":link,"image":image,"author":author,"genre":genre,"likes":likes,"description":desc,"subscribers":subs,"updateDays":updatedays})
	h.pj(dataa)
	

def getEpsWebtoon(link):
	##### HANYA MENGAMBIL 9 EPISODE #####
	webtoon,eps=h.bs(link),[]
	infox=webtoon.find("ul",{"id":"_listUl"}).findAll("li")
	for ep in infox:
		titlee=ep.img.get("alt")
		linkk=ep.a.get("href")
		likess=ep.find("span",class_="like_area _likeitArea").text[4:]
		date=" ".join(ep.find("span",class_="date").text.split(" ")[::-1])
		eps.append({"episode":titlee,"link":linkk,"like":likess,"date":date})
	h.pj(eps)
	
def getComicWebtoon(linkepisode):
	webtun,comics,no,size=h.bs(linkepisode),{"size":0,"c":[]},1,0
	images=webtun.find("div",{"id":"_imageList"})
	titlee=webtun.find("meta",{"property":"og:title"}).get("content")
	for comic in images.findAll("img"):
		image=comic.get("data-url").replace("webtoo","swebtoo")
		title="gambar-{}.jpg".format(no)
		no+=1
		size+=int(requests.get(image).headers["Content-Length"])
		comics["c"].append({"image":image,"title":title})
	comics["size"] = fn(size)
	folder=os.getcwd()+"/"+titlee+"/"
	try:os.mkdir(titlee)
	except FileExistsError:
		shutil.rmtree(folder)
		os.mkdir(folder)
	print("""Judul Webtoon : {}
Total Gambar Yang Akan Didownload : {}
Total Ukuran Gambar Yang Akan Didownload : {}
Disimpan di : {}""".format(titlee,len(comics["c"]),comics["size"],os.getcwd()+"/"+titlee+"/"))
	while True:
		jwb=input("""Lanjutkan Mendownload Webtoon?
    
Jawaban [y/n (exit)] = """).lower()
		if jwb == "y":
			pb=IncrementalBar("Downloading...",max=len(comics["c"]))
			for comicc in comics["c"]:
				urllib.request.urlretrieve(comicc["image"],folder+comicc["title"])
				pb.next()
			pb.finish()
			print("Success Download Webtoon {} !".format(titlee))
			break
		elif jwb == "n":sys.exit("Gagal Mendownload Webtoon {} !".format(titlee));shutil.rmtree(folder)
		else:print("Pilihan Anda Salah!")

def searchWebtoon(webtun):
	print("Coming Soon :)")
	
	
getWebtoonToday()