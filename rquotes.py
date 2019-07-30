from lib.sn import h

def getRandomQuotes():
	data,dataa=h.bs("https://best-quotations.com/tyxaio.php"),[]
	for q in data.findAll("td",class_="quote"):
		quote=q.b.text
		wil=q.a.text
		if "," in wil:au=wil.split(",")[0]
		else:au=wil
		quote=quote[:-2]+"." if quote.endswith("  .") else quote
		categ=", ".join([c.text for c in q.findAll("li")])
		dataa.append({"quote":quote,"author":au,"category":categ})
	h.pj(h.rc(dataa))
		
getRandomQuotes()