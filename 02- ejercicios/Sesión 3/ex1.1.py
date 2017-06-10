#! /user/bin/python
# -*- coding: utf-8 -*-
# > <
import random

#crei una llista amb 10 valors aleatoris entre 1 i 5.
lista = []
for x in range(1,11):
	valor = random.randint(1,5)
	lista.append(valor)
print "llista amb 10 valors aleatoris entre 1 i 5"
print lista 

#inserti un element al final amb el maxim valor de la llista
lista.insert(11,5)
print "Insertar al final el maxim valor de la llista"
print lista 	
	
#inserti un element al principi, amb la suma dels primers 5 elements
suma=0
print "Insertar ual principi amb la suma dels primers 5"
for x in range(0,5):
	suma=suma+lista[x]
lista.insert(0,suma)
print lista

#imprimeixi les vegades que apareix a la llista el valor de segon element
veces = 0
for i in lista:
   lista.count(lista[2])
   i=i+1
print("les vegades que apareix a la llista el valor de segon element", i)
   
