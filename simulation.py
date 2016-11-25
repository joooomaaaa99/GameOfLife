import nachbarschaft,copy
def veraendere_die_welt(welt):
	welt2=copy.copy(welt)
	# FALLEEEEEEE!!!! Warum sollte man hier copy(welt) verwenden?
	l=len(welt) #davor -1
	for i in range (0,l):
		for k in range (0,l):
			anzahl=nachbarschaft.zaehle_nachbarn(i,k,welt,l)
			if anzahl <2:
				welt2[i][k]=" "
			elif anzahl >3:
				welt2[i][k]=" "
			elif anzahl ==3:
				welt2[i][k]=1
			elif anzahl ==2:
				welt2[i][k]=1
	
	return welt2
#welt = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
#welt=veraendere_die_welt(welt)	
#print (welt)
#input("WATIT")

				
				
		