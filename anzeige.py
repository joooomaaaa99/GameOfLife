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