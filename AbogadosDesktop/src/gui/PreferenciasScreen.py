# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferencias.ui'
#
# Created: Wed Apr 11 16:17:05 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.8
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(368, 497)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cantidadEventosSpin = QtGui.QSpinBox(self.layoutWidget)
        self.cantidadEventosSpin.setObjectName("cantidadEventosSpin")
        self.horizontalLayout.addWidget(self.cantidadEventosSpin)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(98, 18, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.alarmaMenEmergente = QtGui.QCheckBox(self.layoutWidget)
        self.alarmaMenEmergente.setObjectName("alarmaMenEmergente")
        self.verticalLayout_2.addWidget(self.alarmaMenEmergente)
        self.alarmaIcono = QtGui.QCheckBox(self.layoutWidget)
        self.alarmaIcono.setObjectName("alarmaIcono")
        self.verticalLayout_2.addWidget(self.alarmaIcono)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(98, 28, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cantCopiaSegSpin = QtGui.QSpinBox(self.layoutWidget)
        self.cantCopiaSegSpin.setObjectName("cantCopiaSegSpin")
        self.horizontalLayout_3.addWidget(self.cantCopiaSegSpin)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.BorrarEventosBtn = QtGui.QPushButton(self.layoutWidget)
        self.BorrarEventosBtn.setObjectName("BorrarEventosBtn")
        self.horizontalLayout_4.addWidget(self.BorrarEventosBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.OrdenArribaBtn = QtGui.QPushButton(self.layoutWidget)
        self.OrdenArribaBtn.setObjectName("OrdenArribaBtn")
        self.verticalLayout_5.addWidget(self.OrdenArribaBtn)
        self.OrdenAbajoBtn = QtGui.QPushButton(self.layoutWidget)
        self.OrdenAbajoBtn.setObjectName("OrdenAbajoBtn")
        self.verticalLayout_5.addWidget(self.OrdenAbajoBtn)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.OrdenRestablecerBtn = QtGui.QPushButton(self.layoutWidget)
        self.OrdenRestablecerBtn.setObjectName("OrdenRestablecerBtn")
        self.verticalLayout_5.addWidget(self.OrdenRestablecerBtn)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.listaMainApp = QtGui.QListWidget(self.layoutWidget)
        self.listaMainApp.setObjectName("listaMainApp")
        self.horizontalLayout_8.addWidget(self.listaMainApp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtGui.QSpacerItem(218, 18, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.GuardarBtn = QtGui.QPushButton(self.layoutWidget)
        self.GuardarBtn.setObjectName("GuardarBtn")
        self.horizontalLayout_5.addWidget(self.GuardarBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Cantidad de eventos proximos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Tipo de alarma:", None, QtGui.QApplication.UnicodeUTF8))
        self.alarmaMenEmergente.setText(QtGui.QApplication.translate("Form", "Mensaje emergente", None, QtGui.QApplication.UnicodeUTF8))
        self.alarmaIcono.setText(QtGui.QApplication.translate("Form", "Icono de notificacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Cantidad de copias de seguriadad guardadas:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Borrar eventos vencidos:", None, QtGui.QApplication.UnicodeUTF8))
        self.BorrarEventosBtn.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Orden del menu:", None, QtGui.QApplication.UnicodeUTF8))
        self.OrdenArribaBtn.setText(QtGui.QApplication.translate("Form", "Arriba", None, QtGui.QApplication.UnicodeUTF8))
        self.OrdenAbajoBtn.setText(QtGui.QApplication.translate("Form", "Abajo", None, QtGui.QApplication.UnicodeUTF8))
        self.OrdenRestablecerBtn.setText(QtGui.QApplication.translate("Form", "Restablecer", None, QtGui.QApplication.UnicodeUTF8))
        self.GuardarBtn.setText(QtGui.QApplication.translate("Form", "Guardar", None, QtGui.QApplication.UnicodeUTF8))

