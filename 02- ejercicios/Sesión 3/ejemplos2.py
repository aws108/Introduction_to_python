#append(elemento)
lista=['juan','ana','luis']
lista.append('carlos')
print lista

#extend(elementos)
lista=['juan','ana','luis']
lista.extend(['uno','dos'])
print lista

lista=['juan','ana','luis']
lista.append(['uno','dos'])
print lista 

#insert(posicion,elemento)
lista=['juan','ana','luis']
lista.insert(0,'carlos')
print lista

#pop([posicion])
lista=['juan','ana','luis','marcos']
elemento=lista.pop()
print elemento
print lista
print lista.pop(1)
print lista

#remove(elemento)
lista=['juan','ana','luis','marcos','ana']
lista.remove('ana')
print lista

#count(elemento)
lista=['juan','ana','luis','marcos','ana']
print lista.count('ana')

#index(elemento,[inicio],[fin])
lista=['juan','ana','luis','marcos','ana']
print lista.index('ana')

#sort()
lista=['juan','ana','luis','marcos','ana']
lista.sort()
print lista

#reverse()
lista=['juan','ana','luis','marcos','ana']
lista.reverse()
print lista

#Borrado de elementos de la lista
lista=['juan','ana','luis','marcos']
del lista[2]
print lista
#Si queremos borrar los elementos de la posicion 2 hasta la 3:
lista=['juan','ana','carlos','maria','pedro']
del lista[2:4]
print lista
#Si queremos borrar desde la 2 hasta el final:
lista=['juan','ana','carlos','maria','pedro']
del lista[2:]
print lista
#Si queremos borrar todos desde el principio hasta la posicion 3 sin incluirla:
lista=['juan','ana','carlos','maria','pedro']
del lista[:3]
print lista
#Si queremos ir borrando de a uno de por medio:
lista=['juan','ana','carlos','maria','pedro']
del lista[::2]
print lista
#Si necesitamos modificar el contenido de un nodo de la lista
lista=['juan','ana','luis','marcos']
lista[2]='xxxxx'
print lista

#Conocer la cantidad de elementos actual
#Se utiliza la funcion len():
lista=['juan','ana','luis','marcos']
print len(lista)
