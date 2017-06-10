#!/usr/bin/python

##Todos los números divisibles de los siguientes numeros

numero=1
sortir = False

while sortir==False:
	if numero%15==0 and numero%16==0 and numero%26==0:
		print numero
		#sortir=True
	else:
		
		if numero>10000:
			sortir=True
			
	numero=numero+1
print "Un numero divisible entre 15, 16 i 26: "
if numero>10000:
	print "No l'he trobat"
else:
	print numero
