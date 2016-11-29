def zeige_die_welt_wie_sie_ist(welt):
	# print(welt)
	output_str="\nWelt\n"
	for i in range(0,len(welt)):
		line=list(map(str,welt[i]))
		# for entry in welt[i]:
			# entry=str(entry) 
		output_str=output_str+" ".join(line)+"\n"
	output_str+="\n---\n"
	print (output_str)
	


##Neue Anzeige mit GUI
class Kasten:
	def __init__(self, canvas, color,kaestchenbreite):
		self.canvas = canvas
		self.id = canvas.create_rectangle(x*kaestchenbreite, y*kaestchenbreite, kaestchenbreite,kaestchenbreite, fill=color)
	
	
def zeichnek(color, self, canvas): #Wenn 1
	kasten = Kasten(canvas, "green",kaestchenbreite)
def entfernek(color, self, canvas): #Wenn 0
	kasten = Kasten(canvas, "white",kaestchenbreite)

