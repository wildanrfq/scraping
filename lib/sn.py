import bs4,requests,json,pafy,googletrans,urllib;from datetime import *
mozhdr,z,harii={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"},{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"},["Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu","Minggu"]
class h:
	jam=str(datetime.now().time()).split(".")[0][:-3]
	hari=harii[datetime.today().weekday()]
	tanggal=datetime.today().date();tanggal="{} {} {}".format(tanggal.day,googletrans.Translator().translate(datetime.now().strftime("%B"),dest="id",src="en").text,tanggal.year)
	def shorturl(link):return requests.get("https://api-ssl.bitly.com/v3/shorten?access_token={}&longUrl={}".format(requests.get("https://md5.pinasthika.com/api/decrypt?value=4ad62d27a08d8b794c867408fdfbc5ea").json()["result"],link)).json()["data"]["url"]
	def bsverif(link,hdr=True):
		if hdr == False:return bs4.BeautifulSoup(requests.get(link,verify=False).content, "html5lib")
		else:return bs4.BeautifulSoup(requests.get(link,verify=False,headers=mozhdr).content, "html5lib")
	def bs(link,hdr=True):
		if hdr == False:return bs4.BeautifulSoup(requests.get(link).content, "html5lib")
		else:return bs4.BeautifulSoup(requests.get(link,headers=z).content, "html5lib")
	def pbs(link):return print(bs4.BeautifulSoup(requests.get(link,headers=mozhdr).content,"html5lib").prettify())
	def pbs2(link):return bs4.BeautifulSoup(requests.get(link).content,"html5lib").prettify()
	def pj(jsonnya):print(json.dumps(jsonnya,indent=4,ensure_ascii=False))
	def lj(jsonnya):return json.loads(jsonnya)
	def ytmp4(id):return pafy.new(id,basic=False).videostreams[-1].url
	def elist(list,start,end):
		no,wrk=1,"[ {} ]\n\n".format(start)
		for data in list:wrk+="{}. {}\n".format(str(no),data);no+=1
		wrk+="\n[ Finish ]\n\n"+end
		return wrk
	def tr(txt,dr,ke):return googletrans.Translator().translate(txt,dest=ke,src=dr).text
	def w(f,t):
		with open (f,"w") as x:x.write(str(t))
	def dl(l,f):
		urllib.request.urlretrieve(l,f)
