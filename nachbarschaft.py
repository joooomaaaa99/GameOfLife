
def check(x,y,welt,n):
	if x>=n:
		x=0
	if y>=n:
		y=0
	if welt[x][y]=="1":
		# print(x,y)
		return 1
	else: return 0
	
def zaehle_nachbarn(x,y,welt,n):
	anzahl=0
	anzahl=anzahl+check(x+1,y,welt,n)
	anzahl=anzahl+check(x+1,y+1,welt,n)
	anzahl=anzahl+check(x+1,y-1,welt,n)
	
	anzahl=anzahl+check(x,y+1,welt,n)
	anzahl=anzahl+check(x,y-1,welt,n)
	
	anzahl=anzahl+check(x-1,y,welt,n)
	anzahl=anzahl+check(x-1,y+1,welt,n)
	anzahl=anzahl+check(x-1,y-1,welt,n)

	return anzahl
	
