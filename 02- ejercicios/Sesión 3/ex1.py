import random

#Crear una lista con 30 valores aleatorios comprendidos entre 1 y 300

lista = []

for x in range(1,50):
	valor = random.randint(1,300)
	lista.append(valor)
print lista 
print '\n'

#Borrar el primer y ultimo elemento de la lista
del lista[0]
del lista[-1]
print lista
print '\n'

#inserti un element al principi, amb la suma dels primers 5 elements
suma=0
for x in range(1,len(lista)):
	suma=suma+lista[x]
lista.append(suma)
print lista
print '\n'

#Insertar un elemento entre el primero y el segundo elemento de la lista con el valor 125.
lista.insert(1,125)
print lista


