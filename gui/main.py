#! /usr/bin/python2 
# -*- coding: utf-8 -*-

import os,sys
from PyQt4 import QtCore,QtGui
from gui import Ui_MainWindow
from gui import Ui_Dialog
#from pixmapItem import PixmapItem
#from sceneView import SceneView
#from graph import Graph

class Main(QtGui.QMainWindow):
    
    def __init__(self):
        "" ""
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.transcisionesWidget
        #self.ui.actionAbrir.activate(self.abrir)
        
        QtCore.QObject.connect(self.ui.actionAbrir, QtCore.SIGNAL(("activated()")), self.abrir)
        
        #self.ui.actionAbrir.activate()
        """   
        
        self.ui.scene = SceneView()
        self.ui.scene.setSceneRect(0,0,700,300)
        self.ui.graphicsView.setScene(self.ui.scene)
        self.ui.pushButton_3.clicked.connect(self.showFileDialog)
        self.ui.pushButton_2.clicked.connect(self.showNetworkDialog)        
        self.ui.pushButton_5.clicked.connect(self.showAbout)
        self.ui.pushButton_6.clicked.connect(self.showQuit)
        self.ui.graphicsView.show()
    
        self.fileNames = None
        """
    #---##---## ---##---##---##---##---##---##---##---##---##---##---##---##
        
    def abrir(self):
        #self.ui.EstadoIniLabel.setText("Funciona")
        self.ui.CintatextBrowser.setTextBackgroundColor(QtGui.QColor.fromRgb(12,233,47))
        self.ui.CintatextBrowser.setAcceptRichText(True)
        #self.ui.CintatextBrowser.setAlignment("Center")
        i=1
        while i<20:
            self.ui.CintatextBrowser.append("APPEND")
            i = i+1
        

        
        
        #self.ui.CintatextBrowser.setText("VAMOS FUNCIONA")
        #self.ui.CintatextBrowser.setText("VAMOS FUNCIONA 2")
        #self.ui.CintatextBrowser.setLineWidth(25)
        #self.ui.CintatextBrowser.scroll(5, 5)
        #self.ui.CintatextBrowser.setAcceptRichText(True)
        #QtGui.QColor(1)
        #self.ui.CintatextBrowser.setTextBackgroundColor(QtGui.QColor.fromRgb(12,233,47))
        #self.ui.CintatextBrowser.setText()
        #("VAMOS CARAJO FUNCIONA!!")
        #self.ui.CintatextBrowser.setText("VAMOS CARAJO FUNCIONA!!")
        #self.ui.CintatextBrowser.setText("VAMOS CARAJO FUNCIONA!!")
    """
    def showQuit(self):
        "" ""        
        reply = QtGui.QMessageBox.question(self, 'Message',
        "<font color=white> Are you sure to quit? </font>", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QtCore.QCoreApplication.instance().quit()           

    #---##---## ---##---##---##---##---##---##---##---##---##---##---##---##
    
    def showAbout(self):
        "" ""
        box = QtGui.QMessageBox.about(self,"my about","<font color=white> This is my about </font>")
        
    #---##---## ---##---##---##---##---##---##---##---##---##---##---##---##

    def showFileDialog(self):
        dialog = QtGui.QFileDialog() 
        self.fileNames = dialog.getOpenFileNames(self,"Open Image", os.getcwd() , "Image Files (*.png *.jpg *.bmp)")
        
        posx = posy = 10
        for i in self.fileNames:
            pix = QtGui.QPixmap(i)
            sca = PixmapItem(pix.scaledToWidth(80), i)
            sca.setFlags(QtGui.QGraphicsItem.ItemIsSelectable| QtGui.QGraphicsItem.ItemIsMovable)
            self.ui.scene.addItem(sca)
            if (self.ui.graphicsView.width() < posx + 100 ):
                 posy = 100; posx = 10
         
            sca.setPos(posx,posy)
            posx+=100     
            
    #---##---## ---##---##---##---##---##---##---##---##---##---##---##---##      
                          
    def showNetworkDialog(self):
        "" ""
        
        items = self.ui.scene.items()
        self.fileNames = [str(f) for f in self.fileNames] #para pasar de QString a una lista
        for i in items:
            if (not i.isVisible()):
                self.fileNames.remove(i.path)
        print self.fileNames        
        
        self.ui.scene.clear()
        myNetwork = Graph(17, 23,"../../data/matrizPesos.xls") #TODO pedirlo por ui
        myNetwork.show(self.ui.scene)
        """
######################################################

def main():
    app = QtGui.QApplication(sys.argv)
    #app.setStyleSheet(_fromUtf8("background-image:url(t.jpg);"))
    window=Main()
    window.show()    
    sys.exit(app.exec_())

######################################################

if __name__ == "__main__":
     main()