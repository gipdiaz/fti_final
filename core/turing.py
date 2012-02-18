# -*- coding: UTF-8 -*-
#!/usr/bin/env python

#-----------------------------------------------------------------#

import sys
import cPickle

pr = sys.stdout.write
run = False
pausa = False
detener = False

#-----------------------------------------------------------------#

class Persistencia(object):
    #def nombre_clase(self):
    #    return str(self).split(' ')[0].split('.')[1]
    def __init__(self):
        pass
    def cargar(self, nombre_fichero):
        manejador_fichero = open(nombre_fichero,'r')
        objeto = cPickle.load(manejador_fichero)
        manejador_fichero.close()
        return objeto

    def guardar(self, objeto, nombre_fichero):
        manejador_fichero = open(nombre_fichero,'w')
        cPickle.dump(self, manejador_fichero)
        manejador_fichero.close()

#-----------------------------------------------------------------#

class TuringCintaException(Exception):
	def __init__(self, valor):
		Exception.__init__(self)
		self.valor = valor
	def __str__(self):
		return self.valor

#-----------------------------------------------------------------#

class TuringErrorException(Exception):
	def __str__(self):
		return "Se produjo un Error"

#-----------------------------------------------------------------#

class TuringAceptoException(Exception):
	def __str__(self):
		return "Finalizo la Maquina correctamente"

#-----------------------------------------------------------------#

class Cinta:
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

#-----------------------------------------------------------------#

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
#-----------------------------------------------------------------#

class MaquinaTuring(Persistencia):
	def __init__(self, conj_estados,alfabeto_entrada,alfabeto_cinta,estado_inicial,char_blanco,cadena,conj_estados_finales_aceptadores):
		self.blanco = char_blanco
		#self.cinta_1 = cinta_1
		#self.cinta_2 = cinta_2
		self.cinta = Cinta(cadena,0,self.blanco)
		self.conj_estados_finales_aceptadores = conj_estados_finales_aceptadores
		self.program = {}
		self.estado_inicial = estado_inicial
		self.estado = self.estado_inicial
		self.lenStr = len(cadena)
	
	def reinit(self):
		self.estado = self.estado_inicial
		self.cinta.reinit()
	
	def agregarTransicion(self, estado, char_in, estado_destino, char_out, movimiento):
		if not self.program.has_key(estado):
			self.program[estado] = {}

		tup = (estado_destino, char_out, movimiento)
		self.program[estado][char_in] = tup

	def paso(self):
		""" Pasos 1 - 3 """
		if self.lenStr == 0 and self.estado in self.conj_estados_finales_aceptadores: raise TuringAceptoException
		if self.estado in self.conj_estados_finales_aceptadores: raise TuringAceptoException 
		if self.estado not in self.program.keys(): raise TuringErrorException
		
		""" Pasos 4 y 5 """
		head = self.cinta.leer()
		if head not in self.program[self.estado].keys(): raise TuringErrorException
			
		""" Pasos 6 y 7 """
		# ejecutar la transcision
		(estado_destino, char_out, movimiento) = self.program[self.estado][head]
		self.estado = estado_destino
		try:
			""" Paso 8 """
			self.cinta.mover(head, char_out, movimiento)
		except TuringCintaException, s:
			print s

	def ejecutar(self):
		try:
			while run:
				self.cinta.mostrar()
				self.paso()
		except (TuringErrorException, TuringAceptoException), s:
			print s

#-----------------------------------------------------------------#

class Manejador():
	def __init__(self):
		pass
	def inicio(self):
		global run, pausa, detener
		run = False
		pausa = False
		detener = False
				
	def run(self,mt):
		
		
		try:
			# Maquina run
			while run:
				mt.cinta.mostrar()
				mt.paso()
				if detener == True:
					break
		except (TuringErrorException, TuringAceptoException), s:
			print s
		# Maquina detenida	
		print "Maquina de Turing Detenida" 	

#-----------------------------------------------------------------#

if __name__ == "__main__":
	
	### Definicion de los componentes de la Maquina de Turing ###
	
	# Q = conjunto de estados	
	conj_estados = [0,1,2]
	# E = alfabeto de entrada
	alfabeto_entrada = ['A','B','C','D']
	# R = alfabeto de cinta
	alfabeto_cinta = alfabeto_entrada + ['Der','Izq']
	# s = estado inicial
	estado_inicial = 0
	# b = simbolo blanco
	char_blanco = "@"
	# cadena
	cadena = "ABBACCCCCCBCCCBCBBABBBBD"
	# F = conjunto de estados finales aceptadores
	conj_estados_finales_aceptadores = [2]
	# Creacion de la Maquina de Turing completa
	mt = MaquinaTuring(conj_estados,alfabeto_entrada,alfabeto_cinta,estado_inicial,char_blanco,cadena,conj_estados_finales_aceptadores)
	# El metodo agregarTransicion(estado_origen,caracter_leido,estado_destino,caracter_escrito,movimiento)
	mt.agregarTransicion(0,'A',0,'A','D')
	mt.agregarTransicion(0,'B',0,'A','D')
	mt.agregarTransicion(0,'C',0,'B','I')
	mt.agregarTransicion(0,'D',1,'D','D')
	mt.agregarTransicion(1,'@',2,'@','I')
	# Crear el Manejador
	manejador = Manejador()
	# Ejecutar el Manejador
	manejador.inicio()
	manejador.run(mt)

	# ejecutar la maquina
	#mt.ejecutar()
		
	#m.guardar(m, "file_1")
	#m.cargar("file_1")