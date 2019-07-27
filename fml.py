from lib.sn import h
import random

def randomFML():
	return h.pj({"fml":random.choice([fml.text.split(" FML")[0].replace("\n","") for fml in h.bs("https://www.fmylife.com/random").findAll("a",class_="article-link")])})

randomFML()