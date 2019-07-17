from lib.sn import h

zodiaks=['Leo', 'Scorpio', 'Libra', 'Cancer', 'Aries', 'Taurus', 'Sagittarius', 'Capricorn', 'Aquarius', 'Virgo', 'Pisces']
def getRamalan(zodiak):
	if zodiak.title() in zodiaks:
		data=h.bs("http://gemintang.com/ramalan-bintang-setiap-hari/ramalan-{}-hari-ini/".format(zodiak))
		info=data.findAll("td",{"colspan":2})
		ramalan=info[1].text[8:].split(" \xa0")[0]
		hidup=ramalan.split(" Keuangan: ")[0]
		keuangan=ramalan.split("Keuangan: ")[1].split(" Asmara:")[0].capitalize()
		asmara=ramalan.split("Asmara: ")[1].capitalize()
		luckyn=info[2].findAll("td")[2].text[1:][:-1]
		h.pj({"zodiak":zodiak.title(),"ramalan":{"hidup":hidup,"keuangan":keuangan,"asmara":asmara,"nomorKeberuntungan":luckyn}})
	else:
		h.pj({"error":"Tidak ada zodiak {}. Zodiak yang tersedia hanya {}.".format(zodiak,", ".join(zodiaks))})

getRamalan("scorpio")