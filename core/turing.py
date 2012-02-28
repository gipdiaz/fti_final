# -*- coding: UTF-8 -*-
#!/usr/bin/env python

######################################################

import sys
import cPickle

pr = sys.stdout.write
run = True
pausa = False
detener = False

######################################################

class Persistencia(object):
	
	#----------------------------------------------------#
	
	def __init__(self):
		pass
	
	#----------------------------------------------------#
	
	def cargar(self,file_nombre):
		manejador_fichero = open(file_nombre,'r')
		objeto = cPickle.load(manejador_fichero)
		manejador_fichero.close()
		return objeto

	#----------------------------------------------------#

	def guardar(self, objeto, nombre_fichero):
		manejador_fichero = open(nombre_fichero,'w')
		cPickle.dump(self, manejador_fichero)
		manejador_fichero.close()

######################################################

class TuringCintaException(Exception):
	def __init__(self, valor):
		Exception.__init__(self)
		self.valor = valor
	def __str__(self):
		return self.valor

######################################################

class Cinta:
	
	#----------------------------------------------------#
	
	def __init__(self, cadenaInicial=[], posInicial=0, blanco="_"):
		self.status = 0
		self.cinta = []
		self.pos = posInicial
		self.blanco = blanco
		self.cadenaInicial = cadenaInicial
		if len(cadenaInicial) > 0:
			for ch in cadenaInicial:
				self.cinta.append(ch)
		else:
			self.tape.append(blanco)

	#----------------------------------------------------#

	def reinit(self):
		self.__init__(self.cadenaInicial)
		
	#----------------------------------------------------#	

	def mover(self, char_chequeo, char_nuevo, direccion):
		# Solo D y I son las direcciones soportadas
		# Chequeo si el caracter en el cabezal es el buscado
		if char_chequeo != self.cinta[self.pos]:
			raise TuringCintaException ("Tape head doesn't match head character")
		
		# en este paso, el cabezal se encuentra sobre el caracter buscado.
		# se cambia el caracter del cabezal por el nuevo caracter
		self.cinta[self.pos] = char_nuevo
		
		if direccion == "I":
			self.mover_izq()
			self.status = self.status - 1
		elif direccion == "D":
			self.mover_der()
			self.status = self.status + 1
		elif direccion == "-":
			pass
		else: raise TuringCintaException ("La Direccion es Invalida")

	#----------------------------------------------------#

	def leer(self):
		""" retorna el caracter en el cabezal """
		return self.cinta[self.pos]

	#----------------------------------------------------#

	def mover_izq(self):
		if self.pos <= 0: 
			self.cinta.insert(-1, self.blanco)
			self.pos = 0
		else:
			self.pos += -1

	#----------------------------------------------------#

	def mover_der(self):
		self.pos += 1
		if self.pos >= len(self.cinta): self.cinta.append(self.blanco)

	#----------------------------------------------------#
	
	def mostrar(self):
		for ch in self.cinta:
			pr(ch)
		pr("\n"); pr(" "*self.pos + "^"); pr("\n")

	def mostrar_2(self,main_window,j):
		cad = "<p><span style=color:#736F6E;><B>Paso "+ str(j) +" = " + "</B></span>" + "<span style=color:blue;>"
		i = 0
		for ch in self.cinta:
			if i == self.status:
				ch = "</span><span style=color:red;>" + ch + "</span><span style=color:blue;>"
			i = i + 1
			cad = cad + ch
		cad = cad + "</span></p>"
		main_window.imprimir(cad)

# LOGICA DE LA MAQUINA DE TURING
"""
Se utiliza diccionario para la la estructura de programa para la MT
    Los pasos del Algoritmo:
	1. Revise para ver si la longitud de la cadena es cero y si estamos en un estado final
	2. Si el "estado actual" se encuentra en los estados finales lansa un Acepto
	3. Si el "estado actual" no se encuentra en los estados finales lansa un Error
	4. Chequea el caracter del cabezal
	5. Si el caracter del cabezal no esta en el diccionario y en el estado actual lansa un Error.
	6. Recupera desde el diccionario el estado destino, char_out y el movimiento
	7. Setea el estado actual al nuevo estado
	8. Escribe en la cinta y mueve el cabezal

Program: (El diccionario)
    [estado][char_in] --> [(estado_destino, char_out, movimiento)]
"""

######################################################

class MaquinaTuring(Persistencia):
	
	#----------------------------------------------------#
	
	def __init__(self, conj_estados = None,alfabeto_entrada = None,estado_inicial = None,char_blanco = None,conj_estados_finales_aceptadores = None):
		if conj_estados != None:
			self.conj_estados = conj_estados
			self.alfabeto_entrada = alfabeto_entrada
			self.blanco = char_blanco
			self.conj_estados_finales_aceptadores = conj_estados_finales_aceptadores
			self.program = {}
			self.estado_inicial = estado_inicial
			self.estado = self.estado_inicial
			self.list_item = []
	
	#----------------------------------------------------#
	
	def reinit(self,cadena):
		self.lenStr = len(cadena)
		self.cinta = None
		self.cinta = Cinta(cadena,0,self.blanco)
		
	#----------------------------------------------------#	
	
	def getItems(self):
		return self.list_item
	
	#----------------------------------------------------#
	
	def getItems_qt(self):
		return self.list_item_qt
	
	#----------------------------------------------------#
		
	def agregarTransicion(self, estado, char_in, estado_destino, char_out, movimiento, item):
		self.list_item.append(item)
		#self.list_item_qt.append(item_qt)
		if not self.program.has_key(estado):
			self.program[estado] = {}

		tup = (estado_destino, char_out, movimiento)
		self.program[estado][char_in] = tup

	#----------------------------------------------------#

	#str(item.text(0)) , str(item.text(1)) , str(item.text(2)), str(item.text(3)), str(item.text(4))
	def borrarTransicion(self, estado, char_in, estado_destino, char_out, movimiento, item, item_qt):
		self.list_item.remove(item)
		#self.list_item_qt.remove(item_qt)
		if self.program.has_key(estado):
			#print "transicion a borrar", self.program[estado][char_in]
			#print "transiciones del estado antes", self.program[estado]
			aux = self.program[estado].pop(char_in)
			#self.program[estado] = aux.pop(char_in)
			#print "transiciones del estado despues", self.program[estado]
			
		"""
		if not self.program.has_key(estado):
			self.program[estado] = {}

		tup = (estado_destino, char_out, movimiento)
		self.program[estado][char_in] = tup
		"""

	#----------------------------------------------------#

	def paso(self):
		
		head = self.cinta.leer()
		# Pasos 1 - 3 """
		if self.lenStr == 0 and self.estado in self.conj_estados_finales_aceptadores: 
			#print "cadena vacia"
			return "Acepto"
		if self.estado in self.conj_estados_finales_aceptadores and head == self.blanco: 
			#print "estado acep"
			return "Acepto" 
		if self.estado not in self.program.keys(): return "Error"
		
		# Pasos 4 y 5 """
		#head = self.cinta.leer()
		#print "head = ", head
		if head not in self.program[self.estado].keys(): return "Error"
			
		# Pasos 6 y 7
		est = self.estado
		(estado_destino, char_out, movimiento) = self.program[self.estado][head]
		self.estado = estado_destino
		
		# Paso 8
		try:	
			self.cinta.mover(head, char_out, movimiento)
			return (est, head, estado_destino,char_out, movimiento)
		except TuringCintaException, s:
			pass
			#print s
	
	#----------------------------------------------------#

	def ejecutar(self):
		run = True
		while run:
			self.cinta.mostrar()
			aux = self.paso()
			if (aux == "Acepto") or (aux == "Error"):
				run = False
		#print aux
		return aux 

######################################################

if __name__ == "__main__":
	pass