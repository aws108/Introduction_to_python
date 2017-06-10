# -*- coding: utf-8 -*-

class Producto:
	"Ejemplo de clase con la cantidad y el precio de un prodducto"
	
	def __init__(self, producto, precio, unidades):
		self.producto = "corbata"
		self.precio = 35
		self.unidades = 67
		
	def costo_total(self):
		costo = self.precio * self.unidades
		return costo
		
mi_objeto_producto = Producto(producto,precio,unidades)

print mi_objeto_producto.producto
print mi_objeto_producto.precio
print mi_objeto_producto.unidades
print mi_objeto_producto.costo_total()
