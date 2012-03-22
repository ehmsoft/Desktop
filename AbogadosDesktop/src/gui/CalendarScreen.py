# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created: Thu Mar 22 16:43:12 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.resize(538, 224)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Calendar)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lista = QtGui.QListWidget(Calendar)
        self.lista.setLayoutMode(QtGui.QListView.SinglePass)
        self.lista.setViewMode(QtGui.QListView.ListMode)
        self.lista.setModelColumn(0)
        self.lista.setObjectName("lista")
        self.verticalLayout.addWidget(self.lista)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnAgregar = QtGui.QPushButton(Calendar)
        self.btnAgregar.setObjectName("btnAgregar")
        self.horizontalLayout_3.addWidget(self.btnAgregar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        Calendar.setWindowTitle(QtGui.QApplication.translate("Calendar", "Calendario", None, QtGui.QApplication.UnicodeUTF8))
        self.lista.setSortingEnabled(False)
        self.btnAgregar.setText(QtGui.QApplication.translate("Calendar", "Agregar", None, QtGui.QApplication.UnicodeUTF8))

