from scr import *
import random

def waifuwednesday():
	data,dataa=Helper.bsoup("http://jurnalotaku.com/tag/waifu-wednesday/",True),[]
	for info in data.findAll("div",class_="article-wrapper article-tb m-tb"):
		link=info.a.get("href")
		image=info.img.get("src")
		waifu=info.img.get("alt").split("[Waifu Wednesday] ")[1]
		#reason=Helper.bsoup(link,True).find("div",class_="meta-content").h2.text.split("+ ")[1]
		dataa.append({"waifu":waifu,"image":image})
	result=random.choice(dataa)
	Helper.baguskan(result)
	
def husbandofriday():
	data,dataa=Helper.bsoup("http://jurnalotaku.com/tag/husbando-friday/",True),[]
	for info in data.findAll("div",class_="article-wrapper article-tb m-tb"):
		link=info.a.get("href")
		image=info.img.get("src")
		waifu=info.img.get("alt").split("[Husbando Friday] ")[1]
		#reason=Helper.bsoup(link,True).find("div",class_="meta-content").h2.text.split("+ ")[1]
		dataa.append({"waifu":waifu,"image":image})
	result=random.choice(dataa)
	Helper.baguskan(result)

try:waifuwednesday()
except IndexError:waifuwednesday()
try:husbandofriday()
except IndexError:husbandofriday()