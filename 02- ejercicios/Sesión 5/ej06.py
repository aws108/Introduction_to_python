# -*- coding: utf-8 -*-

fichero = open("nuevo.txt", "w")

for i in range(1,5):
	texto = "Linea %i \n" %i
	fichero.write(texto)

print "Se ha escrito un fichero"

fichero.close()
