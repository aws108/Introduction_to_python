# -*- coding: utf-8 -*-

fichero = open("lista.txt", "r")

line = fichero.readline()
while line!="":
	print line
	line = fichero.readline()
fichero.close()

