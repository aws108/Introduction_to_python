# -*- coding: utf-8 -*-

fichero = open("lista.txt", "r")

lista_lineas = fichero.readlines()

print lista_lineas[4]
print lista_lineas[3]
print lista_lineas[1]

fichero.close()
