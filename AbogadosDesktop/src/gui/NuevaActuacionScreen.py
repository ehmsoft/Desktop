# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevaActuacion.ui'
#
# Created: Wed Feb  1 10:49:07 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.8
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NuevaActuacion(object):
    def setupUi(self, NuevaActuacion):
        NuevaActuacion.setObjectName("NuevaActuacion")
        NuevaActuacion.resize(302, 180)
        self.gridLayout_4 = QtGui.QGridLayout(NuevaActuacion)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontal = QtGui.QHBoxLayout()
        self.horizontal.setObjectName("horizontal")
        self.groupBox = QtGui.QGroupBox(NuevaActuacion)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtDescripcion = QtGui.QLineEdit(self.groupBox)
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtDescripcion)
        self.lblJuzgado = QtGui.QLabel(self.groupBox)
        self.lblJuzgado.setObjectName("lblJuzgado")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lblJuzgado)
        self.dteFecha = QtGui.QDateTimeEdit(self.groupBox)
        self.dteFecha.setObjectName("dteFecha")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.dteFecha)
        self.dteFechaProxima = QtGui.QDateTimeEdit(self.groupBox)
        self.dteFechaProxima.setObjectName("dteFechaProxima")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.dteFechaProxima)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.horizontal.addWidget(self.groupBox)
        self.gridLayout_3.addLayout(self.horizontal, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtGui.QFrame(NuevaActuacion)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(NuevaActuacion)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.label.setBuddy(self.txtDescripcion)
        self.label_3.setBuddy(self.dteFecha)
        self.label_4.setBuddy(self.dteFechaProxima)

        self.retranslateUi(NuevaActuacion)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NuevaActuacion.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NuevaActuacion.reject)
        QtCore.QMetaObject.connectSlotsByName(NuevaActuacion)

    def retranslateUi(self, NuevaActuacion):
        NuevaActuacion.setWindowTitle(QtGui.QApplication.translate("NuevaActuacion", "Actuación", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NuevaActuacion", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NuevaActuacion", "Juzgado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NuevaActuacion", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NuevaActuacion", "Fecha próxima:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblJuzgado.setText(QtGui.QApplication.translate("NuevaActuacion", "Ninguno", None, QtGui.QApplication.UnicodeUTF8))

