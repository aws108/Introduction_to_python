#islower()
cadena='ana'
if cadena.islower():
	print 'La cadena '+cadena+ ' esta toda en minusculas'
	
#isdigit()
cadena='120'
if cadena.isdigit():
	print 'Todos los caracteres de la cadena son numeros'
	
#isalpha()
cadena='Hola mundo'
if cadena.isalpha():
	print 'Todos los caracteres de la cadena son del alfaberto'
else:
	print 'No todos los caracteres de la cadena son del alfabeto'
	
#isspace()
cadena= '  '
if cadena.isspace():
	print 'Todos los caracteres de la cadena son espacios en blanco'
	
#isalnum()
cadena='cordoba2008'
if cadena.isalnum():
	print 'Todos los caracteres son numeros o alfabeticos'
	
#find('cadena',[inicio],[fin])
cadena='esto es una prueba y es solo eso'
pos=cadena.find('es')
print pos

cadena='esto es una prueba y es solo eso'
pos=cadena.find('es',5)
print pos

#rfind('cadena',[inicio],[fin])
cadena='esto es una prueba y es solo eso'
pos=cadena.rfind('es')
print pos

#count('cadena',[inicio],[fin])
cadena='esto es una prueba y es solo eso'
cant=cadena.count('es')
print cant

#replace('cadena1','cadena2',[maximo])
cadena1='esto es una prueba y es solo eso'
cadena2=cadena1.replace('es','ES')
print cadena2 

#split('caracter separador',[maximo])
cadena='esto es una prueba y es solo eso'
lista=cadena.split(' ')
print lista
print len(lista)
lista=cadena.split(' ',2)
print lista
print len(lista)

#rsplit('caracter separador',[maximo])
cadena='esto es una prueba y es solo eso'
lista=cadena.rsplit(' ')
print lista
print len(lista)
lista=cadena.rsplit(' ',2)
print lista
print len(lista)

#splitlines()
mensaje="""Primer linea
Segunda linea
Tercer linea
Cuarta linea"""
lista=mensaje.splitlines()
print lista

#swapcase()
cadena1='Sistema de Facturacion'
cadena2=cadena1.swapcase()
print cadena2

#rjust(ancho,caracter de relleno)
cadena='200'
cadena2=cadena.rjust(5,'$')
print cadena2

#ljust(ancho,caracter de relleno)
cadena='200'
cadena2=cadena.ljust(5,'$')
print cadena2

#center(ancho,caracter de relleno)
cadena='200'
cadena2=cadena.center(5,'$')
print cadena2
