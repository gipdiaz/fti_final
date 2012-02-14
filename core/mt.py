# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import sys
import cPickle

pr = sys.stdout.write

class Persistencia(object):
	#def nombre_clase(self):
	#	return str(self).split(' ')[0].split('.')[1]
	
	def cargar(self, nombre_fichero):
		manejador_fichero = open(nombre_fichero,'r')
		objeto = cPickle.load(manejador_fichero)
		manejador_fichero.close()
		return objeto

	def guardar(self, objeto, nombre_fichero):
		manejador_fichero = open(nombre_fichero,'w')
		cPickle.dump(self, manejador_fichero)
		manejador_fichero.close()

class TuringCintaException(Exception):
	""" Turing Cinta Exception """
	def __init__(self, valor):
		Exception.__init__(self)
		self.valor = valor
	def __str__(self):
		return self.valor

class TuringErrorException(Exception):
	""" Turing Error Exception """
	def __str__(self):
		return "Error"

class TuringAceptoException(Exception):
	""" Turing Accept Exception """
	def __str__(self):
		return "Acepto"

class MaquinaCinta:
	def __init__(self, cadenaInicial=[], posInicial=0, blanco="_"):
		""" La cinta usa una lista simple """
		self.cinta = []
		self.pos = posInicial
		self.blanco = blanco
		self.cadenaInicial = cadenaInicial
		if len(cadenaInicial) > 0:
			for ch in cadenaInicial:
				self.cinta.append(ch)
		else:
			self.tape.append(blanco)

	def reinit(self):
		self.__init__(self.cadenaInicial)

	def mover(self, char_chequeo, char_nuevo, direccion):
		""" Solo D y I son las direcciones soportadas """
		# check to see if the character under the head is what we need
		if char_chequeo != self.cinta[self.pos]:
			raise TuringCintaException ("Tape head doesn't match head character")
		
		# at this point the head is over the same character we are looking for
		#  change the head character to the new character
		self.cinta[self.pos] = char_nuevo
		
		if direccion == "I":
			self.mover_izq()
		elif direccion == "D":
			self.mover_der()
		else: raise TuringCintaException ("La Direccion es Invalida")
	
	def leer(self):
		""" retorna el caracter en el cabezal """
		return self.cinta[self.pos]
	
	def mover_izq(self):
		if self.pos <= 0: 
			self.cinta.insert(-1, self.blank)
			self.pos = 0
		else:
			self.pos += -1

	def mover_der(self):
		self.pos += 1
		if self.pos >= len(self.cinta): self.cinta.append(self.blanco)
	
	def mostrar(self):
		""" imprime la cinta """
		for ch in self.cinta:
			pr(ch)
		pr("\n"); pr(" "*self.pos + "^"); pr("\n")

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

Program Layout: (El diccionario)
    [estado][char_in] --> [(estado_destino, char_out, movimiento)]
"""

class MaquinaTuring(Persistencia):
	def __init__(self, cadenaInicial=" ",estadoInicial=0, estadoFinal=[], blanco="_"):
		self.blanco = blanco
		self.cinta = MaquinaCinta(cadenaInicial,0,self.blanco)
		self.estadoFinal = estadoFinal
		self.program = {}
		self.estadoInicial = estadoInicial
		self.estado = self.estadoInicial
		self.lenStr = len(cadenaInicial)
	
	def reinit(self):
		self.estado = self.estadoInicial
		self.cinta.reinit()
	
	def agregarTransicion(self, estado, char_in, estado_destino, char_out, movimiento):
		if not self.program.has_key(estado):
			self.program[estado] = {}

		tup = (estado_destino, char_out, movimiento)
		self.program[estado][char_in] = tup

	def paso(self):
		""" Pasos 1 - 3 """
		if self.lenStr == 0 and self.state in self.fstates: raise TuringAceptoException
		if self.estado in self.estadoFinal: raise TuringAceptoException 
		if self.estado not in self.program.keys(): raise TuringErrorException
		
		""" Pasos 4 y 5 """
		head = self.cinta.leer()
		if head not in self.program[self.estado].keys(): raise TuringErrorException
			
		""" Pasos 6 y 7 """
		# execute transition
		(estado_destino, char_out, movimiento) = self.program[self.estado][head]
		self.estado = estado_destino
		try:
			""" Paso 8 """
			self.cinta.mover(head, char_out, movimiento)
		except TuringCintaException, s:
			print s

	def ejecutar(self):
		try:
			while 1:
				m.cinta.mostrar()
				m.paso()
		except (TuringErrorException, TuringAceptoException), s:
			print s

if __name__ == "__main__":
	""" MaquinaTuring(Cadena,estado_inicial,estados_finales,caracter_blanco) """
	m = MaquinaTuring("ABBACCCCCCBCCCBCBBABBBBD",0,[2],"@")
	
	""" agregarTransicion(estado_origen,caracter_leido,estado_destino,caracter_escrito,movimiento) """
	m.agregarTransicion(0,'A',0,'A','D')
	m.agregarTransicion(0,'B',0,'A','D')
	m.agregarTransicion(0,'C',0,'B','I')
	m.agregarTransicion(0,'D',1,'D','D')
	m.agregarTransicion(1,'@',2,'@','I')

	
	m.ejecutar()
	
	
	#m.guardar(m, "file_1")
	#m.cargar("file_1")
	
	
	# cPickle
	#cPickle.dump(m, file)
	#m = cPickle.load(file)
