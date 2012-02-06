# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainApp.ui'
#
# Created: Mon Jan 30 13:46:30 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainApp(object):
    def setupUi(self, mainApp):
        mainApp.setObjectName("mainApp")
        mainApp.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mainApp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 664, 531))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        mainApp.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_Archivo = QtGui.QMenu(self.menubar)
        self.menu_Archivo.setObjectName("menu_Archivo")
        self.menuEditar = QtGui.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        mainApp.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainApp)
        self.statusbar.setObjectName("statusbar")
        mainApp.setStatusBar(self.statusbar)
        self.action_Nuevo = QtGui.QAction(mainApp)
        self.action_Nuevo.setObjectName("action_Nuevo")
        self.menu_Archivo.addAction(self.action_Nuevo)
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())

        self.retranslateUi(mainApp)
        QtCore.QMetaObject.connectSlotsByName(mainApp)

    def retranslateUi(self, mainApp):
        mainApp.setWindowTitle(QtGui.QApplication.translate("mainApp", "Procesos Judiciales", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Archivo.setTitle(QtGui.QApplication.translate("mainApp", "&Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEditar.setTitle(QtGui.QApplication.translate("mainApp", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Nuevo.setText(QtGui.QApplication.translate("mainApp", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))

