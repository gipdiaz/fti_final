#! /usr/bin/python2 
# -*- coding: utf-8 -*-

import os,sys
from PyQt4 import QtCore,QtGui
from gui.window import Ui_MainWindow
from gui.dialog import Ui_Dialog
from core.turing import MaquinaTuring

######################################################

class Vars():
    file_name = "default"
    PATH_ACTUAL = os.path.abspath("") + os.sep + "maquinas" + os.sep
    paso = 1
    run = True
    
######################################################
    
class FileDialog(QtGui.QFileDialog):
    
    #----------------------------------------------------#
    
    def __init__(self):
        "" ""
        QtGui.QFileDialog.__init__(self)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setOption(self.DontUseNativeDialog, True) 

    #----------------------------------------------------#

    def abrir(self):
        self.nombreArchivo = str(self.getOpenFileName(self,"", Vars.PATH_ACTUAL + Vars.file_name,"Archivos - Maquina Turing Config (*.mtc)","", self.DontUseNativeDialog))
        print self.nombreArchivo
        if self.nombreArchivo == "":
            return "None"
        else:
            return self.nombreArchivo
      
    #----------------------------------------------------#  
        
    def guardar(self):
        Vars.file_name = str(self.getSaveFileName(self,"", Vars.PATH_ACTUAL, "Archivos - Maquina Turing Config (*.mtc)","", self.DontUseNativeDialog)) + ".mtc"
        if self.nombreArchivo == "":
            return "None"
        else:
            return self.nombreArchivo

######################################################

class MainWindow(QtGui.QMainWindow):
    
    #----------------------------------------------------#
    
    def __init__(self):
        "" ""
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.transcisionesWidget
    
    #----------------------------------------------------#
    
    def nueva(self):
        
        # set objetos "enable"
        self.ui.EstadosText.setEnabled(True)
        self.ui.EstadosText.setToolTip("'a,b,c' sino 'a b c'")
        self.ui.EstadosText.clear()
        self.ui.AlfabetoText.setEnabled(True)
        self.ui.AlfabetoText.setToolTip("'1,2,3' sino '1 2 3'")
        self.ui.AlfabetoText.clear()
        self.ui.EstadosAcepText.setEnabled(True)
        self.ui.EstadosAcepText.setToolTip("'a,b,c' sino 'a b c'")
        self.ui.EstadosAcepText.clear()
        self.ui.SimbBlancoText.setEnabled(True)
        self.ui.SimbBlancoText.setToolTip("'@' sino '#' sino '&' sino 'Cualquier caracter'")
        self.ui.SimbBlancoText.clear()
        self.ui.EstadoIniText.setEnabled(True)
        self.ui.EstadoIniText.setToolTip("'a' sino 'b' sino 'c'")
        self.ui.EstadoIniText.clear()
                
        # set objetos "disable"
        self.ui.comboBox.setEnabled(False)
        self.ui.comboBox_2.setEnabled(False)
        self.ui.comboBox_3.setEnabled(False)
        self.ui.comboBox_4.setEnabled(False)
        self.ui.comboBox_5.setEnabled(False)
        self.ui.transcisionesWidget.setEnabled(False)
        self.ui.transcisionesWidget.clear()
        self.ui.CintatextBrowser.setEnabled(False)
        self.ui.CintatextBrowser.clear()
        self.ui.AgregarTransicionBoton.setEnabled(False)
        self.ui.BorrarTransicionBoton.setEnabled(False)
        
        # set el estado de los botones de la interfaz
        self.ui.actionNueva.setDisabled(False)
        self.ui.actionAbrir.setDisabled(False)
        self.ui.actionCerrar.setDisabled(True)
        self.ui.actionGuardar.setDisabled(True)
        self.ui.actionEjecutar.setDisabled(True)
        self.ui.actionPaso.setDisabled(True)
        self.ui.actionDetener.setDisabled(True)
        self.ui.actionCargar.setDisabled(True)
        
    #----------------------------------------------------#
    
    def mostrar(self,msj):
        self.ui.CintatextBrowser.setText(msj)
    
    #----------------------------------------------------#
    
    def imprimir(self,msj):
        self.ui.CintatextBrowser.append(msj)
        self.ui.CintatextBrowser.show()
        
        #self.ui.CintatextBrowser.append(msj)
        #self.ui.CintatextBrowser.setVisible(True)
        #self.ui.CintatextBrowser.append(msj)
     
    #----------------------------------------------------#
        
    def activarTransicion(self,datos):
        self.ui.comboBox.setEnabled(True)
        self.ui.comboBox_2.setEnabled(True)
        self.ui.comboBox_3.setEnabled(True)
        self.ui.comboBox_4.setEnabled(True)
        self.ui.comboBox_5.setEnabled(True)
        self.ui.transcisionesWidget.setEnabled(True)
        self.ui.CintatextBrowser.setEnabled(True)
        self.ui.AgregarTransicionBoton.setEnabled(True)
        self.ui.BorrarTransicionBoton.setEnabled(True)
        
        self.ui.comboBox.addItems(datos.conj_estados)
        self.ui.comboBox_2.addItems(datos.alfabeto_entrada + [datos.char_blanco])
        self.ui.comboBox_3.addItems(datos.conj_estados)
        self.ui.comboBox_4.addItems(datos.alfabeto_entrada + [datos.char_blanco])
        self.ui.comboBox_5.addItems(['D','I'])
    
    #----------------------------------------------------#
        
    def desactivarCargaDatos(self):
        self.ui.EstadosText.setEnabled(False)
        self.ui.AlfabetoText.setEnabled(False)
        self.ui.EstadosAcepText.setEnabled(False)
        self.ui.SimbBlancoText.setEnabled(False)
        self.ui.EstadoIniText.setEnabled(False)
   
######################################################

class SimTur():
    
    #----------------------------------------------------#
    
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.main_window=MainWindow()
        self.main_window.show()
        self.main_window.nueva()
        self.file_dialog=FileDialog()
        self.setSignals() 
        self.conj_estados = []
        self.alfabeto_entrada = []
        self.estado_inicial = 0
        self.char_blanco = ""
        self.cadena = ""
        self.conj_estados_finales_aceptadores = []
        sys.exit(app.exec_())
    
    #----------------------------------------------------#
    
    def __reinit__(self, conj_estados, alfabeto_entrada, estado_inicial, char_blanco, conj_estados_finales_aceptadores):
        self.mt = MaquinaTuring(conj_estados, alfabeto_entrada, estado_inicial, char_blanco, conj_estados_finales_aceptadores) 
    
    #----------------------------------------------------#

    def ejecutar(self):
        if self.cadena != "":
            self.main_window.mostrar("")
            cad = "<span style=color:#736F6E;>" "<B>" + "... Iniciando la Maquina de Turing ..." + "</B>" "</span>"
            self.main_window.mostrar(cad)
            self.cadena = self.main_window.ui.CadenaText.toPlainText()
            self.mt.reinit(str(self.cadena))
            self.mt.estado = self.mt.estado_inicial
            run = True
            j = 1
            while run:
                self.mt.cinta.mostrar_2(self.main_window,j)
                aux = self.mt.paso()
                j = j + 1
                if (aux == "Acepto"):
                    aux = "<span style=color:#736F6E;>" "<B>" + "... Finalizo la Maquina de Turing ..." + "</B>" "</span>"
                    run = False
                if (aux == "Error"):
                    aux = "<span style=color:red;>" "<B>" + "... Ocurrio un Error ..." + "</B>" "</span>"
                    run = False
            self.main_window.imprimir(aux)
        else:
            msj = "<span style=color:red;>" + "Error : Ingrese una cadena" + "</span>"
            self.main_window.mostrar(msj)     
            
    #----------------------------------------------------#
    
    def pasoapaso(self):
        if self.cadena != "":
            # Verifico si es el inicio de la Maquina Turing
            if Vars.paso == 1:
                self.main_window.mostrar("")
                cad = "<span style=color:#736F6E;>" "<B>" + "... Iniciando la Maquina de Turing ..." + "</B>" "</span>"
                self.main_window.mostrar(cad)
                self.cadena = self.main_window.ui.CadenaText.toPlainText()
                self.mt.reinit(str(self.cadena))
                self.mt.estado = self.mt.estado_inicial
                Vars.run = True
            
            # Verifico sino termino la Maquina Turing
            if Vars.run == True:
                self.mt.cinta.mostrar_2(self.main_window,Vars.paso)
                aux = self.mt.paso()
                print Vars.paso, aux
                Vars.paso = Vars.paso + 1
                if (aux == "Acepto"):
                    aux = "<span style=color:#736F6E;>" "<B>" + "... Finalizo la Maquina de Turing ..." + "</B>" "</span>"
                    Vars.run = False
                if (aux == "Error"):
                    aux = "<span style=color:red;>" "<B>" + "... Ocurrio un Error ..." + "</B>" "</span>"
                    Vars.run = False
            if Vars.run == False:
                Vars.paso = 1
                self.main_window.imprimir(aux)
        else:
            msj = "<span style=color:red;>" + "Error : Ingrese una cadena" + "</span>"
            self.main_window.mostrar(msj)

    #----------------------------------------------------#
            
    def detener(self):
        Vars.paso = 1
        Vars.run = False
        self.main_window.ui.CintatextBrowser.clear()
        
            
    
    #----------------------------------------------------#
            
    def guardar(self):
        file_name = self.file_dialog.guardar()
        if file_name != "None":
            self.mt.guardar(self, file_name)
        
    #----------------------------------------------------#

    def abrir(self):
        self.limpiar()
        file_name = self.file_dialog.abrir()
        if file_name != "None":
            self.mt = MaquinaTuring()
            self.mt = self.mt.cargar(file_name)
            
            self.conj_estados = self.mt.conj_estados
            self.alfabeto_entrada = self.mt.alfabeto_entrada
            self.conj_estados_finales_aceptadores = self.mt.conj_estados_finales_aceptadores
            self.char_blanco = self.mt.blanco
            self.estado_inicial = self.mt.estado_inicial
            i=1
            aux = ""
            list_estados = []
            for i in self.conj_estados:
                if i != "[" and i != "]" and i != "," and i != "[" and i != "'" and i != " ":
                    aux = aux + i + " "
                    list_estados.append(i)
            self.conj_estados = aux
            i=1
            aux = ""
            list_estados_acep = []
            for i in self.conj_estados_finales_aceptadores:
                if i != "[" and i != "]" and i != "," and i != "[" and i != "'" and i != " ":
                    aux = aux + i
                    list_estados_acep.append(i)
            self.conj_estados_finales_aceptadores = aux
            i=1
            aux = ""
            list_alfabeto = []
            for i in self.alfabeto_entrada:
                if i != "[" and i != "]" and i != "," and i != "[" and i != "'" and i != " ":
                    aux = aux + i
                    list_alfabeto.append(i)
            self.alfabeto_entrada = aux
             
            self.main_window.ui.EstadoIniText.setText(self.estado_inicial)
            self.main_window.ui.AlfabetoText.setText(self.alfabeto_entrada)
            self.main_window.ui.EstadosAcepText.setText(self.conj_estados_finales_aceptadores)
            self.main_window.ui.EstadosText.setText(self.conj_estados)
            self.main_window.ui.SimbBlancoText.setText(self.char_blanco)
            
            list_items = self.mt.getItems()
            
            self.main_window.ui.transcisionesWidget.setColumnCount(5)
            self.main_window.ui.transcisionesWidget.setContentsMargins(1, 1, 1, 1)
            self.main_window.ui.transcisionesWidget.setAllColumnsShowFocus(True)
            self.main_window.ui.transcisionesWidget.setColumnWidth(0,55)
            self.main_window.ui.transcisionesWidget.setColumnWidth(1,55)
            self.main_window.ui.transcisionesWidget.setColumnWidth(2,55)
            self.main_window.ui.transcisionesWidget.setColumnWidth(3,55)
            self.main_window.ui.transcisionesWidget.setColumnWidth(4,55)
            
            i=0
            for i in list_items:
                item = QtGui.QTreeWidgetItem(i)
                
                self.main_window.ui.transcisionesWidget.addTopLevelItem(item)
            
            self.main_window.ui.actionNueva.setDisabled(False)
            self.main_window.ui.actionAbrir.setDisabled(False)
            self.main_window.ui.actionCerrar.setDisabled(False)
            self.main_window.ui.actionGuardar.setDisabled(False)
            self.main_window.ui.actionEjecutar.setDisabled(False)
            self.main_window.ui.actionPaso.setDisabled(False)
            self.main_window.ui.actionDetener.setDisabled(False)
            self.main_window.ui.actionCargar.setDisabled(False)
                  
    #----------------------------------------------------#
            
    def limpiar(self):
        self.main_window.ui.EstadosText.setEnabled(True)
        self.main_window.ui.EstadosText.setText("")
        self.main_window.ui.AlfabetoText.setEnabled(True)
        self.main_window.ui.AlfabetoText.setText("")
        self.main_window.ui.EstadosAcepText.setEnabled(True)
        self.main_window.ui.EstadosAcepText.setText("")
        self.main_window.ui.SimbBlancoText.setEnabled(True)
        self.main_window.ui.SimbBlancoText.setText("")
        self.main_window.ui.EstadoIniText.setEnabled(True)
        self.main_window.ui.EstadoIniText.setText("")
        self.main_window.ui.comboBox.setEnabled(True)
        self.main_window.ui.comboBox_2.setEnabled(True)
        self.main_window.ui.comboBox_3.setEnabled(True)
        self.main_window.ui.comboBox_4.setEnabled(True)
        self.main_window.ui.comboBox_5.setEnabled(True)
        self.main_window.ui.comboBox.clear()
        self.main_window.ui.comboBox_2.clear()
        self.main_window.ui.comboBox_3.clear()
        self.main_window.ui.comboBox_4.clear()
        self.main_window.ui.comboBox_5.clear()
        self.main_window.ui.transcisionesWidget.setEnabled(True)
        self.main_window.ui.transcisionesWidget.clear()
        self.main_window.ui.CintatextBrowser.setEnabled(True)
        self.main_window.ui.CintatextBrowser.clear()
        self.main_window.ui.AgregarTransicionBoton.setEnabled(True)
        self.main_window.ui.BorrarTransicionBoton.setEnabled(True)
        
    #----------------------------------------------------#     
    
    def setSignals(self):
        QtCore.QObject.connect(self.main_window.ui.actionAbrir, QtCore.SIGNAL(("activated()")), self.abrir)
        QtCore.QObject.connect(self.main_window.ui.actionGuardar, QtCore.SIGNAL(("activated()")), self.guardar)
        QtCore.QObject.connect(self.main_window.ui.actionNueva, QtCore.SIGNAL(("activated()")), self.main_window.nueva)
        QtCore.QObject.connect(self.main_window.ui.actionCerrar, QtCore.SIGNAL(("activated()")), self.main_window.nueva)
        QtCore.QObject.connect(self.main_window.ui.aceptarTuringBoton, QtCore.SIGNAL(("clicked()")), self.validarTuring)
        QtCore.QObject.connect(self.main_window.ui.AgregarTransicionBoton, QtCore.SIGNAL(("clicked()")), self.agregarTransicion)
        QtCore.QObject.connect(self.main_window.ui.actionEjecutar, QtCore.SIGNAL(("activated()")), self.ejecutar)
        QtCore.QObject.connect(self.main_window.ui.actionPaso, QtCore.SIGNAL(("activated()")), self.pasoapaso)
        QtCore.QObject.connect(self.main_window.ui.actionDetener, QtCore.SIGNAL(("activated()")), self.detener)
            
    #----------------------------------------------------#
            
    def validarTuring(self):
        carga_datos_flag = True
        self.main_window.mostrar("")
        
        # reset de variables
        self.conj_estados = []
        self.alfabeto_entrada = []
        self.char_blanco = ""
        self.conj_estados_finales_aceptadores = []
        self.estado_inicial = ""
        
        # verificacion del conjunto de estados
        conj_estados = self.main_window.ui.EstadosText.toPlainText()
        for i in conj_estados:
            i = str(i)
            if (i != ',') and (i != " ") and (i != "\t"):
                self.conj_estados.append(i)
                carga_datos_flag = carga_datos_flag and True
        
        # Verificacion del alfabeto de entrada
        alfabeto_entrada = self.main_window.ui.AlfabetoText.toPlainText()
        for i in alfabeto_entrada:
            i = str(i)
            if i in self.conj_estados:
                self.main_window.mostrar("Error en la carga del Alfabeto")
                self.main_window.ui.AlfabetoText.selectAll()
                self.main_window.ui.AlfabetoText.setFocus()
                carga_datos_flag = carga_datos_flag and False
                break
            if (i != ',') and (i != " ") and (i != "\t"):
                self.alfabeto_entrada.append(i)
                carga_datos_flag = carga_datos_flag and True   
        
        # Verificacion de estados aceptadores
        conj_estados_finales_aceptadores_2 = []
        conj_estados_finales_aceptadores_1 = self.main_window.ui.EstadosAcepText.toPlainText()
        for i in conj_estados_finales_aceptadores_1:
            i = str(i)
            if (i != ',') and (i != " ") and (i != "\t"):
                conj_estados_finales_aceptadores_2.append(i)
        for i in conj_estados_finales_aceptadores_2:
            if i in self.conj_estados:
                self.conj_estados_finales_aceptadores.append(i)
                carga_datos_flag = carga_datos_flag and True
            else:
                self.main_window.mostrar("Error en la carga de los Estados Aceptadores")
                self.main_window.ui.EstadosAcepText.selectAll()
                self.main_window.ui.EstadosAcepText.setFocus()
                carga_datos_flag = carga_datos_flag and False
                break
        
        char_blanco = self.main_window.ui.SimbBlancoText.toPlainText()
        if char_blanco in self.alfabeto_entrada:
            self.main_window.mostrar("Error en la carga del Simbolo Blanco")
            self.main_window.ui.SimbBlancoText.selectAll()
            self.main_window.ui.SimbBlancoText.setFocus()
            carga_datos_flag = carga_datos_flag and False
        else:
            self.char_blanco = char_blanco
            carga_datos_flag = carga_datos_flag and True
        
        estado_inicial = self.main_window.ui.EstadoIniText.toPlainText()
        if estado_inicial in self.conj_estados:
            self.estado_inicial = estado_inicial
            carga_datos_flag = carga_datos_flag and True
        else:
            self.main_window.mostrar("Error en la carga del Estado Inicial")
            self.main_window.ui.EstadoIniText.selectAll()
            self.main_window.ui.EstadoIniText.setFocus()
            carga_datos_flag = carga_datos_flag and False
        
        print "Conjunto de Estados: ", self.conj_estados
        print "Alfabeto: ", self.alfabeto_entrada
        print "Conjunto de Estados Aceptadores: ", self.conj_estados_finales_aceptadores
        print "Simbolo Blanco: ", self.char_blanco
        print "Estado Inicial: ", self.estado_inicial
        
        if carga_datos_flag == True:
            self.main_window.activarTransicion(self)
            self.main_window.desactivarCargaDatos()
            self.crearTuring()
            
            self.main_window.ui.actionNueva.setDisabled(False)
            self.main_window.ui.actionAbrir.setDisabled(False)
            self.main_window.ui.actionCerrar.setDisabled(False)
            self.main_window.ui.actionGuardar.setDisabled(False)
            self.main_window.ui.actionEjecutar.setDisabled(False)
            self.main_window.ui.actionPaso.setDisabled(False)
            self.main_window.ui.actionDetener.setDisabled(False)
            self.main_window.ui.actionCargar.setDisabled(False)
            self.main_window.ui.aceptarTuringBoton.setDisabled(True)
            
    #----------------------------------------------------#
    
    def crearTuring(self):
        self.__reinit__(str(self.conj_estados), str(self.alfabeto_entrada), str(self.estado_inicial), str(self.char_blanco), str(self.conj_estados_finales_aceptadores))
        
    #----------------------------------------------------#
    
    def agregarTransicion(self):
        transicion = [ str(self.main_window.ui.comboBox.currentText()) , str(self.main_window.ui.comboBox_2.currentText()) , str(self.main_window.ui.comboBox_3.currentText()), str(self.main_window.ui.comboBox_4.currentText()), str(self.main_window.ui.comboBox_5.currentText())]
        item = QtGui.QTreeWidgetItem(transicion)
        self.main_window.ui.transcisionesWidget.addTopLevelItem(item)
        self.mt.agregarTransicion(str(self.main_window.ui.comboBox.currentText()) , str(self.main_window.ui.comboBox_2.currentText()) , str(self.main_window.ui.comboBox_3.currentText()), str(self.main_window.ui.comboBox_4.currentText()), str(self.main_window.ui.comboBox_5.currentText()), transicion)
 
######################################################
 
if __name__ == "__main__":
    simtur = SimTur()