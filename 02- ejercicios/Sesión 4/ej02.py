# -*- coding: utf-8 -*-


class Producto:
	"Ejemplo de clase con la cantidad y el precio de un prodducto"
	
	def __init__(self, producto, precio, unidades):
		self.producto = producto
		self.precio = precio
		self.unidades = unidades
		
	def __costo_total__(self):
		costo = self.precio * self.unidades
		return costo
		
	def nuevo_precio(self, precio):
		self.precio = precio
	
	def agrega(self,cantidad):
		self.unidades = self.unidades + cantidad
		
	def saca(self, cantidad):
		if cantidad <=self.unidades:
			self.unidades = self.unidades - cantidad
		else:
			print "No hay suficientes"
			
	def informe(self):
		print "Productos: " + self.producto
		print "Precio" + str(self.precio)
		print "Unidades" + str(self.unidades)
		print "Precio total" +str(self.__costo_total__())
		
mi_producto1 = Producto("Pantalon",100,6)
mi_producto2 = Producto("camiseta",50,5)


print mi_producto1.precio
print mi_producto2.unidades

mi_producto2.agrega(5)
print mi_producto2.unidades

mi_producto2.informe()

mi_producto2.__costo_total()
