# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri Feb 17 23:04:57 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Sharpness.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayoutWidget = QtGui.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 621, 101))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.EstadosLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.EstadosLabel.setObjectName(_fromUtf8("EstadosLabel"))
        self.gridLayout.addWidget(self.EstadosLabel, 0, 0, 1, 1)
        self.EstadosText = QtGui.QTextEdit(self.gridLayoutWidget)
        self.EstadosText.setObjectName(_fromUtf8("EstadosText"))
        self.gridLayout.addWidget(self.EstadosText, 0, 1, 1, 1)
        self.SimbBlancoLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.SimbBlancoLabel.setObjectName(_fromUtf8("SimbBlancoLabel"))
        self.gridLayout.addWidget(self.SimbBlancoLabel, 0, 2, 1, 1)
        self.SimbBlancoText = QtGui.QTextEdit(self.gridLayoutWidget)
        self.SimbBlancoText.setObjectName(_fromUtf8("SimbBlancoText"))
        self.gridLayout.addWidget(self.SimbBlancoText, 0, 3, 1, 1)
        self.AlfabetoLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.AlfabetoLabel.setObjectName(_fromUtf8("AlfabetoLabel"))
        self.gridLayout.addWidget(self.AlfabetoLabel, 1, 0, 1, 1)
        self.AlfabetoText = QtGui.QTextEdit(self.gridLayoutWidget)
        self.AlfabetoText.setObjectName(_fromUtf8("AlfabetoText"))
        self.gridLayout.addWidget(self.AlfabetoText, 1, 1, 1, 1)
        self.EstadoIniLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.EstadoIniLabel.setObjectName(_fromUtf8("EstadoIniLabel"))
        self.gridLayout.addWidget(self.EstadoIniLabel, 1, 2, 1, 1)
        self.EstadoIniComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.EstadoIniComboBox.setObjectName(_fromUtf8("EstadoIniComboBox"))
        self.gridLayout.addWidget(self.EstadoIniComboBox, 1, 3, 1, 1)
        self.EstadosAcepLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.EstadosAcepLabel.setObjectName(_fromUtf8("EstadosAcepLabel"))
        self.gridLayout.addWidget(self.EstadosAcepLabel, 2, 0, 1, 1)
        self.EstadosAcepText = QtGui.QTextEdit(self.gridLayoutWidget)
        self.EstadosAcepText.setObjectName(_fromUtf8("EstadosAcepText"))
        self.gridLayout.addWidget(self.EstadosAcepText, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setEnabled(False)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 200, 621, 172))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.CintatextBrowser = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.CintatextBrowser.setObjectName(_fromUtf8("CintatextBrowser"))
        self.gridLayout_2.addWidget(self.CintatextBrowser, 0, 2, 1, 1)
        self.transcisionesWidget = QtGui.QTreeWidget(self.gridLayoutWidget_2)
        self.transcisionesWidget.setObjectName(_fromUtf8("transcisionesWidget"))
        self.transcisionesWidget.header().setDefaultSectionSize(40)
        self.transcisionesWidget.header().setMinimumSectionSize(15)
        self.gridLayout_2.addWidget(self.transcisionesWidget, 0, 0, 1, 1)
        self.BorrarTransicionBoton = QtGui.QToolButton(self.gridLayoutWidget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BorrarTransicionBoton.setIcon(icon1)
        self.BorrarTransicionBoton.setIconSize(QtCore.QSize(24, 24))
        self.BorrarTransicionBoton.setObjectName(_fromUtf8("BorrarTransicionBoton"))
        self.gridLayout_2.addWidget(self.BorrarTransicionBoton, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.widget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(-1, 99, 621, 101))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.TranscisionLabel = QtGui.QLabel(self.gridLayoutWidget_3)
        self.TranscisionLabel.setObjectName(_fromUtf8("TranscisionLabel"))
        self.gridLayout_3.addWidget(self.TranscisionLabel, 1, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout_3.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout_3.addWidget(self.comboBox_3, 1, 3, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.gridLayout_3.addWidget(self.comboBox_4, 1, 4, 1, 1)
        self.comboBox_5 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.gridLayout_3.addWidget(self.comboBox_5, 1, 5, 1, 1)
        self.AgregarTransicionBoton = QtGui.QToolButton(self.gridLayoutWidget_3)
        self.AgregarTransicionBoton.setSizeIncrement(QtCore.QSize(32, 32))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AgregarTransicionBoton.setIcon(icon2)
        self.AgregarTransicionBoton.setIconSize(QtCore.QSize(24, 24))
        self.AgregarTransicionBoton.setObjectName(_fromUtf8("AgregarTransicionBoton"))
        self.gridLayout_3.addWidget(self.AgregarTransicionBoton, 1, 6, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.QiLabel = QtGui.QLabel(self.gridLayoutWidget_3)
        self.QiLabel.setObjectName(_fromUtf8("QiLabel"))
        self.gridLayout_3.addWidget(self.QiLabel, 2, 1, 1, 1)
        self.SiLabel = QtGui.QLabel(self.gridLayoutWidget_3)
        self.SiLabel.setObjectName(_fromUtf8("SiLabel"))
        self.gridLayout_3.addWidget(self.SiLabel, 2, 2, 1, 1)
        self.QjLabel = QtGui.QLabel(self.gridLayoutWidget_3)
        self.QjLabel.setObjectName(_fromUtf8("QjLabel"))
        self.gridLayout_3.addWidget(self.QjLabel, 2, 3, 1, 1)
        self.SjLabel = QtGui.QLabel(self.gridLayoutWidget_3)
        self.SjLabel.setObjectName(_fromUtf8("SjLabel"))
        self.gridLayout_3.addWidget(self.SjLabel, 2, 4, 1, 1)
        self.MovLabel = QtGui.QLabel(self.gridLayoutWidget_3)
        self.MovLabel.setObjectName(_fromUtf8("MovLabel"))
        self.gridLayout_3.addWidget(self.MovLabel, 2, 5, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbrir = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrir.setIcon(icon3)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionNueva = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/New file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNueva.setIcon(icon4)
        self.actionNueva.setObjectName(_fromUtf8("actionNueva"))
        self.actionGuardar = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGuardar.setIcon(icon5)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionSalir = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon6)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionEjecutar = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEjecutar.setIcon(icon7)
        self.actionEjecutar.setObjectName(_fromUtf8("actionEjecutar"))
        self.actionPausar = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Stop playing.png")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.actionPausar.setIcon(icon8)
        self.actionPausar.setObjectName(_fromUtf8("actionPausar"))
        self.actionDetener = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDetener.setIcon(icon9)
        self.actionDetener.setObjectName(_fromUtf8("actionDetener"))
        self.actionCerrar = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/iconos/Close folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCerrar.setIcon(icon10)
        self.actionCerrar.setObjectName(_fromUtf8("actionCerrar"))
        self.actionCargar = QtGui.QAction(MainWindow)
        self.actionCargar.setIcon(icon2)
        self.actionCargar.setObjectName(_fromUtf8("actionCargar"))
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNueva)
        self.toolBar.addAction(self.actionAbrir)
        self.toolBar.addAction(self.actionGuardar)
        self.toolBar.addAction(self.actionCerrar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEjecutar)
        self.toolBar.addAction(self.actionPausar)
        self.toolBar.addAction(self.actionDetener)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SIMTUR - Simulador Maquina de Turing", None, QtGui.QApplication.UnicodeUTF8))
        self.EstadosLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Estados</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SimbBlancoLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Simb. Blanco</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.AlfabetoLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Alfabeto</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.EstadoIniLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Estado Ini.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.EstadosAcepLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Estados Acep.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.transcisionesWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Qi", None, QtGui.QApplication.UnicodeUTF8))
        self.transcisionesWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Si", None, QtGui.QApplication.UnicodeUTF8))
        self.transcisionesWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Qj", None, QtGui.QApplication.UnicodeUTF8))
        self.transcisionesWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Sj", None, QtGui.QApplication.UnicodeUTF8))
        self.transcisionesWidget.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Mov", None, QtGui.QApplication.UnicodeUTF8))
        self.BorrarTransicionBoton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Borrar</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Transicion</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BorrarTransicionBoton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TranscisionLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Agregar</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Transicion</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.AgregarTransicionBoton.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Agregar </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Transicion</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.AgregarTransicionBoton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.QiLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Q</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">i</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SiLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">S</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">i</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.QjLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Q</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">j</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SjLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">S<span style=\" vertical-align:sub;\">j</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.MovLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Mov</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setToolTip(QtGui.QApplication.translate("MainWindow", "Abrir Maquina Turing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva.setText(QtGui.QApplication.translate("MainWindow", "Nueva", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva.setToolTip(QtGui.QApplication.translate("MainWindow", "Nueva Maquina Turing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setText(QtGui.QApplication.translate("MainWindow", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setToolTip(QtGui.QApplication.translate("MainWindow", "Guardar Maquina Turing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setToolTip(QtGui.QApplication.translate("MainWindow", "Salir del Simulador", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEjecutar.setText(QtGui.QApplication.translate("MainWindow", "Ejecutar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEjecutar.setToolTip(QtGui.QApplication.translate("MainWindow", "Ejecutar Maquina Turing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPausar.setText(QtGui.QApplication.translate("MainWindow", "Pausar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPausar.setToolTip(QtGui.QApplication.translate("MainWindow", "Pausar Maquina Turing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDetener.setText(QtGui.QApplication.translate("MainWindow", "Detener", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDetener.setToolTip(QtGui.QApplication.translate("MainWindow", "Detener Maquina Turing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerrar.setText(QtGui.QApplication.translate("MainWindow", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerrar.setToolTip(QtGui.QApplication.translate("MainWindow", "Cerrar Maquina Turing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar.setText(QtGui.QApplication.translate("MainWindow", "Cargar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCargar.setToolTip(QtGui.QApplication.translate("MainWindow", "Cargar Transicion", None, QtGui.QApplication.UnicodeUTF8))

import qrc_resources_rc
