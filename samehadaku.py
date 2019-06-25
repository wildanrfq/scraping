from lib.sn import *

data,no,animes=h.bs("https://samehadaku.tv"),1,[]
def getskuyliving():
	list,no="[ Samehadaku Update ]\n\n",1
	for anime in data.findAll("li",class_="post-item tie-standard"):
		link=anime.a.get("href")
		title=anime.a.get("title").split("Subtitle")[0]
		list+="{}. {}\n".format(no,title)
		no+=1
		animes.append({"title":title,"link":link})
	list+="\n[ Finish ]\nUntuk melihat link download anime, silahkan ketik nomor anime : "
	a=int(input(list))
	if a <= no:
		z=h.bs(animes[a-1]["link"]).find("div",class_="download-eps").findAll("li")
		links=[]
		for linkk in z:
			links.append({linkk.strong.text:[{"link":linkx.get("href"),"via":linkx.text} for linkx in linkk.findAll("a")][:5]})
		if len(links) >= 4:
			del links[0];del links[1]
		if len(links[0]) >= 5:
			links[0] = links[0][:5]
		print(json.dumps(links,indent=4))
	
getskuyliving()