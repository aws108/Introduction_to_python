#keys()
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
lista=diccionario.keys()
print lista

#values()
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
lista=diccionario.values()
print lista

#items()
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
lista=diccionario.items()
print lista

#pop(clave,[valor])
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
valor=diccionario.pop('window')
print valor 
print diccionario

diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
valor=diccionario.pop('love','clave no encontrada')
print valor

#has_key(clave)
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
if diccionario.has_key('love'):
	print 'Si tiene la clave buscada'
else:
	print 'No existe la clave buscada'

#clear()
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
diccionario.clear()
print diccionario

#copy()
diccionario1={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
diccionario2=diccionario1.copy()
print diccionario2 
diccionario1['house']='xxxxx'
print diccionario2 

#popitem()
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
elemento=diccionario.popitem()
print elemento
print diccionario

#update(diccionario2)
diccionario1={'uno':'1','dos':'2','tres':'3333'}
diccionario2={'tres':'3','cuatro':'4','cinco':'5'}
diccionario1.update(diccionario2)
print diccionario1

#Borrado de elementos del diccionario
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
del diccionario['house']
print diccionario
#Modificacion y creacion de elementos del diccionario
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
diccionario['red']='colorado'
diccionario['blue']='azul'
print diccionario
#Conocer la cantidad de elementos actual
diccionario={'house':'casa','red':'rojo','bed':'cama','window':'ventana'}
print len(diccionario)
