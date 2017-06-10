# -*- coding: utf-8 -*-

class Animal:
	"""Clase base poara mostrar la herencia"""
	
	def __init__(self, nombre, patas):
		self.nombre = nombre
		self.patas = patas
		
	def saluda(self):
		print "El animal llamado "+str(self.nombre) + " saluda"

class Perro(Animal):
	"""Clase hija para mostrar la herencia"""
	#No hacemos nada
	
	pass
	
mi_mascota = Perro("Rufo", 4)
mi_mascota.saluda()
