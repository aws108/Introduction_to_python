# -*- coding: utf-8 -*-

un_texto = "Hola mundo"
otro_texto = "Adios mundo"

fichero = open("nuevo.txt", "w")

fichero.write(un_texto)
fichero.write(otro_texto)

print "Se ha escrito un fichero"
fichero.close()
