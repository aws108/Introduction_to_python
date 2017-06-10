# -*- coding: utf-8 -*-

#Abrimos el fichero en modo lectura

fichero = open("lista.txt", "r")

contenido = fichero.read(2)

print contenido

fichero.close()
