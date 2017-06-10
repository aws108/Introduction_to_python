
#asigna un valor a las frutas
frutas = {'manzanas':1.60,'peras':1.90,'bananas':0.95}
print frutas
print '\n'

#anyade una fruta mas. len se usa para obtener la longitud,
#es decir, para conocer la cantidad de frutas que hay
frutas['naranjas']=2.50
print '\n'

#del borra 'naranjas'. El bucle mediante keys() devuelve la lista con
#todas las frutas menos con naranjas
del frutas['naranjas']
for x in frutas.keys():
	print x
print '\n'

#Escribe el valor de las frutas
for x in frutas.values():
	print x
print '\n'

#El bucle recorre las clave valor de la lista de frutas y las devuelve
#Se veran por pantalla una lista de claves/valor
for (clave,valor) in frutas.items():
	print clave+' '+str(valor)+'-' 
print '\n'

#Borra el diccionario de frutas
frutas.clear()
print frutas
