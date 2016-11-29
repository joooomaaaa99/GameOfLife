import random
def welt_erstellen(n):
	welt=[]
	for i in range(0,n):
		welt.append([])
		for j in range(0,n):
			x=random.randint(0,1)
			if x==0:
				x=" "
			else:
				x="1"
			welt[i].append(x)
	return welt
def welt_importieren():
	datei = open("input.csv")
	welt=[]
	for zeile in datei.readlines():
		zeile=zeile.replace("0"," ")
		welt.append(zeile.split(";"))
	datei.close()
	return welt