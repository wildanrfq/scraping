#Follow my IG @danrfq
#WibuDesu TOOLS by Wildan Rifqi

from bs4 import BeautifulSoup as bs
from requests import get
from lib.colors import *
import json,os

def elist(list,wildanganteng,thisiswrk):
	no,wrk=1,"[ {} ]\n\n".format(wildanganteng)
	for data in list:wrk+="{}. {}\n".format(str(no),data);no+=1
	wrk+="\n[ Finish ]\n\n"+thisiswrk
	return wrk
	
def shorturl(link):return get("https://is.gd/create.php?format=simple&url="+link).text

def menu():
	welcome = str(os.system("toilet -F gay WELCOME TO"))
	wibudesu = str(os.system("figlet -f big WibuDesu"))
	print("""╔══════════WibuDesu TOOLS═══════════╗
╠ {}Creator : Wildan Rifqi{}            ║
╠ {}Instagram : @danrfq{}               ║
╠ {}GitHub : {}https://github.com/danrfq{}{}║
╚══════════WibuDesu TOOLS═══════════╝""".format(colors.fg.green,colors.end,colors.fg.pink,colors.end,colors.fg.green,colors.underline,colors.end,colors.end))
	choice=int(input("""
╠ WibuDesu TOOLS Menu :
║
╠ 1. WibuDesu Popular 2019
╠ 2. WibuDesu Latest Update
╠ 3. WibuDesu Search Anime
╠ 99. Exit
╚════════════════════════
{}wibudesu (type the number){} >> """.format(colors.fg.lightblue,colors.end)))
	if choice == 1: 
		anime = int(input(elist([a["title"] for a in dataa["popular"]],"WibuDesu Popular 2019","{}wibudesu (anime information by number){} >> ".format(colors.fg.lightblue,colors.end))))
		if anime <= len(dataa["popular"]):
			info = dataa["popular"][anime-1]
			download = info["download"]
			print("""\n[ {} Info ]
			
Title: {}
Link: {}
Image: {}
Published: {}
Sinopsis: {}
Episodes: {}
Duration: {}
Genres: {}
Type: {}
Rating: {}
Download:
- 480p - {}: {}
- 720p - {}: {}
				
[ Finish ]""".format(info["title"],info["title"],info["link"],info["image"],info["published"],info["sinopsis"],info["episodes"],info["duration"],info["genres"],info["type"],info["rating"],download["480p"]["size"],download["480p"]["link"],download["720p"]["size"],download["720p"]["link"]))
	elif choice == 2: 
		anime = int(input(elist([a["title"] for a in dataa["latestUpdate"]],"WibuDesu Latest Update","{}wibudesu (anime information by number){} >> ".format(colors.fg.lightblue,colors.end))))
		if anime <= len(dataa["latestUpdate"]):
			info = dataa["latestUpdate"][anime-1]
			download = info["download"]
			print("""\n[ {} Info ]
			
Title: {}
Link: {}
Image: {}
Published: {}
Sinopsis: {}
Episodes: {}
Duration: {}
Genres: {}
Type: {}
Download:
- 480p - {}: {}
				
[ Finish ]""".format(info["title"],info["title"],info["link"],info["image"],info["published"],info["sinopsis"],info["episodes"],info["duration"],info["genres"],info["type"],download["480p"]["size"],download["480p"]["link"]))

	elif choice == 3:
		anime = input("{}wibudesu (type the anime title){} >> ".format(colors.fg.lightblue,colors.end))
		search = bs(get("https://wibudesu.com/?s={}&post_type=post".format(anime)).content, "html5lib")
		if search.p.text == "Hasil pencarian tidak ditemukan":
			print("Anime {}{}{} tidak ditemukan".format(colors.fg.red,anime,colors.end))
		else:
			for info in search.findAll("div",class_="detpost"):
				title = info.find("a")["title"]
				link = info.find("a")["href"]
				image = info.find("img")["data-lazy-src"]
				datax = bs(get(link).content, "html5lib")
				z=datax.find("div","info1").ul.findAll("li")
				published = z[0].text+", "+z[1].text.upper()
				infoo = datax.find("div",class_="lexot")
				txt = infoo.findAll("p")
				sinopsis = txt[0].text[11:]
				inffo = txt[1].text
				#Maaf untuk fitur search anime, saya hilangkan episodes, genres, sama type karna tiap anime ada yg ada episode nya, ada yg kaga :(
				sumber = txt[2].text.split("Sumber : ")[1]
				#Maaf cuma tersedia 480p, tiap link/anime ada yg 780p ada yg ngga jadi bingung:(
				_480p = txt[5]
				size480p = _480p.text.split("– ")[1].split("\n")[0]
				link480p = shorturl(_480p.a.get("href"))
				dataa["searchAnime"].append(
				{"title": title,
				"link": link, 
				"image": image,
				"published":published,
				"sinopsis":sinopsis,
				"episodes":episodes,
				"type":type,
				"genres":genres,
				"duration":duration,
				"download":{"480p":{"size":size480p,"link":link480p}}
				})
			anime = int(input(elist([a["title"] for a in dataa["searchAnime"]],"WibuDesu Search Anime","{}wibudesu (anime information by number){} >> ".format(colors.fg.lightblue,colors.end))))
			if anime <= len(dataa["searchAnime"]):
				info = dataa["searchAnime"][anime-1]
				download = info["download"]
				print("""\n[ {} Info ]
			
Title: {}
Link: {}
Image: {}
Published: {}
Sinopsis: {}
Episodes: {}
Duration: {}
Genres: {}
Type: {}
Download:
- 480p - {}: {}
				
[ Finish ]""".format(info["title"],info["title"],info["link"],info["image"],info["published"],info["sinopsis"],info["episodes"],info["duration"],info["genres"],info["type"],download["480p"]["size"],download["480p"]["link"]))
	elif choice == 99:
		print("Exit!")
	elif choice not in [1,2,3,99]:print("Yeeeee qymack!")
	
dataz=bs(get('https://wibudesu.com').content, 'html5lib')
dataa={"popular":[],"latestUpdate":[],"searchAnime":[]}
for info in dataz.findAll("div", {"class": "zeeb3"}):
	title = info.find("a")["title"]
	link = info.find("a")["href"]
	image = info.find("img")["data-lazy-src"]
	datax = bs(get(link).content, "html5lib")
	z=datax.find("div","info1").ul.findAll("li")
	published = z[0].text+", "+z[1].text.upper()
	infoo = datax.find("div",class_="lexot")
	txt = infoo.findAll("p")
	sinopsis = txt[0].text[11:]
	inffo = txt[1].text
	episodes = inffo.split("Episodes: ")[1].split("\n")[0]
	type = inffo.split("Type: ")[1].split("\n")[0]
	genres = inffo.split("Genres: ")[1].split("\n")[0]
	duration = inffo.split("Duration: ")[1].split("\n")[0]
	rating = inffo.split("Rating: ")[1].split("\n")[0]
	sumber = txt[2].text.split("Sumber : ")[1]
	# Link Download menggunakan Google Drive
	_480p = txt[5]
	size480p = _480p.text.split("– ")[1].split("\n")[0]
	link480p = shorturl(_480p.a.get("href"))
	_720p = txt[6]
	size720p = _720p.text.split("– ")[1].split("\n")[0]
	link720p = shorturl(_720p.a.get("href"))
	dataa["popular"].append(
	{"title": title,
	"link": link, 
	"image": image,
	"published":published,
	"sinopsis":sinopsis,
	"episodes":episodes,
	"type":type,
	"genres":genres,
	"duration":duration,
	"rating":rating,
	"download":{"480p":{"size":size480p,"link":link480p},"720p":{"size":size720p,"link":link720p}}
	})
	
for info in dataz.findAll("div",class_="detpost"):
	title = info.find("a")["title"]
	link = info.find("a")["href"]
	image = info.find("img")["data-lazy-src"]
	datax = bs(get(link).content, "html5lib")
	z=datax.find("div","info1").ul.findAll("li")
	published = z[0].text+", "+z[1].text.upper()
	infoo = datax.find("div",class_="lexot")
	txt = infoo.findAll("p")
	sinopsis = txt[0].text[11:]
	inffo = txt[1].text
	episodes = inffo.split("Episodes: ")[1].split("\n")[0]
	type = inffo.split("Type: ")[1].split("\n")[0]
	genres = inffo.split("Genres: ")[1].split("\n")[0]
	sumber = txt[2].text.split("Sumber : ")[1]
	#Maaf cuma tersedia 480p, tiap link/anime ada yg 780p ada yg ngga jadi bingung:(
	_480p = txt[5]
	size480p = _480p.text.split("– ")[1].split("\n")[0]
	link480p = shorturl(_480p.a.get("href"))
	dataa["latestUpdate"].append(
	{"title": title,
	"link": link, 
	"image": image,
	"published":published,
	"sinopsis":sinopsis,
	"episodes":episodes,
	"type":type,
	"genres":genres,
	"duration":duration,
	"download":{"480p":{"size":size480p,"link":link480p}}
	})
	
#run tools
menu()