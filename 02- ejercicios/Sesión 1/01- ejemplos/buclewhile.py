#!/usr/bin/python

numero=1
sortir = False

while sortir==False:
	if numero%15==0 and numero%16==0 and numero%26==0:
		sortir=True
	else:
		numero=numero+1
		if numero>10000:
			sortir=True
print "Un numero divisible entre 15, 16 i 26: "
if numero>10000:
	print "No l'he trobat"
else:
	print numero
