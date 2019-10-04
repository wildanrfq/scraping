from lib.sn import h

zodiaks=['Leo', 'Scorpio', 'Libra', 'Cancer', 'Aries', 'Taurus', 'Sagittarius', 'Capricorn', 'Aquarius', 'Virgo', 'Pisces']
def getRamalan(zodiak):
	if zodiak.title() in zodiaks:
		data=h.bs("http://gemintang.com/ramalan-bintang-setiap-hari/ramalan-{}-hari-ini/".format(zodiak))
		info=data.findAll("td",{"colspan":2})[1]
		ramalan=info.text[8:].split(".  \n")[0]+"."
		luckyn=data.findAll("table")[1].findAll("tr")[1].td.text[1:][:-1]
		h.pj({"zodiak":zodiak.title(),"ramalan":ramalan,"nomorKeberuntungan":luckyn})
	else:
		h.pj({"error":"Tidak ada zodiak {}. Zodiak yang tersedia hanya {}.".format(zodiak,", ".join(zodiaks))})

getRamalan("scorpio")