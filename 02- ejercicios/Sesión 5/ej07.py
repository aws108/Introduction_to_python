# -*- coding: utf-8 -*-

mi_lista = ["Primera","Segunda","Tercera"]

fichero = open("nuevo.txt","w")

fichero.writelines(mi_lista)

fichero.close()
