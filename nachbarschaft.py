
def check(x,y,welt,l):
	if x==l or y==l:
		return 0
	if welt[x][y]==1:
		# print(x,y)
		return 1
	else: 
		return 0 #Wenn kein Wert da ist
		
	
def zaehle_nachbarn(x,y,welt,l):
	anzahl=0
	anzahl=anzahl+check(x+1,y,welt,l)
	anzahl=anzahl+check(x+1,y+1,welt,l)
	anzahl=anzahl+check(x+1,y-1,welt,l)
	
	anzahl=anzahl+check(x,y+1,welt,l)
	anzahl=anzahl+check(x,y-1,welt,l)
	
	anzahl=anzahl+check(x-1,y,welt,l)
	anzahl=anzahl+check(x-1,y+1,welt,l)
	anzahl=anzahl+check(x-1,y-1,welt,l)

	return anzahl
	
