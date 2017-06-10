# -*- coding: utf-8 -*-

fichero = open("nuevo.txt", "w")

fichero.write("1234567890")

fichero.seek(5)

fichero.write("XXX")

fichero.close()
