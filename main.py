### Aufgaben
# Module anzeige, simulation, nachbarschaft
#	für simulation muss man das Modul nachbarschaft einbinden
#	bei anzeige soll die Welt mit Tabulatoren getrennt ohne Klammern schachbrettartig angezeigt werden
#	bei nachbarschaft ist fast nichts mehr zu tun; die Hauptfunktion soll "zaehle_nachbarn()" sein
# main anpassen
# 	Komentare
# 	Benutzerinteraktion, Variablen abfragen
# 	Außerdem: Warum kann man plötzlich Sonderzeichen benutzen?


import os,time

'''
******************************
***			ANPASSEN 	******
******************************
'''
n=30
t=10000
delay=0.05
'''
	***************************
'''
import spielwelt,anzeige,simulation
# welt=spielwelt.welt_erstellen(n)
welt=spielwelt.welt_importieren()
for step in range(0,t):
	os.system('cls')
	anzeige.zeige_die_welt_wie_sie_ist(welt)
	welt=simulation.veraendere_die_welt(welt)
	time.sleep(delay)
input ("\n\n---Return drücken---")