import bs4,requests,json,pafy
mozhdr={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
class h:
	def shorturl(link):return requests.get("http://4h.net/api.php?url="+link).text
	def bsverif(link,hdr):
		if hdr == False:return bs4.BeautifulSoup(requests.get(link,verify=False).content, "html5lib")
		else:return bs4.BeautifulSoup(requests.get(link,verify=False,headers=mozhdr).content, "html5lib")
	def bs(link,hdr=True):
		if hdr == False:return bs4.BeautifulSoup(requests.get(link).content, "html5lib")
		else:return bs4.BeautifulSoup(requests.get(link,headers=mozhdr).content, "html5lib")
	def pbs(link):return print(bs4.BeautifulSoup(requests.get(link).content,"html5lib").prettify())
	def pbs2(link):return bs4.BeautifulSoup(requests.get(link).content,"html5lib").prettify()
	def baguskan(jsonnya):return print(json.dumps(jsonnya,indent=4))
	def loadskan(jsonnya):return json.loads(jsonnya)
	def ytmp4(id):return pafy.new(id,basic=False).videostreams[-1].url
	def elist(list,wildanganteng,thisiswrk):
		no,wrk=1,"[ {} ]\n\n".format(wildanganteng)
		for data in list:wrk+="{}. {}\n".format(str(no),data);no+=1
		wrk+="\n[ Finish ]\n\n"+thisiswrk
		return wrk