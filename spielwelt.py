import random
def welt_erstellen(n):
	welt=[]
	for i in range(0,n):
		welt.append([])
		for j in range(0,n):
			q = random.randint(0,1)
			if q == 1:
				welt[i].append(1)
			else:
				welt[i].append(" ")
			#welt[i].append(random.randint(0,1))
			
	return welt