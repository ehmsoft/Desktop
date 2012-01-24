# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevaCategoria.ui'
#
# Created: Tue Jan 24 14:33:01 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.8
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NuevaCategoria(object):
    def setupUi(self, NuevaCategoria):
        NuevaCategoria.setObjectName("NuevaCategoria")
        NuevaCategoria.resize(408, 154)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NuevaCategoria.sizePolicy().hasHeightForWidth())
        NuevaCategoria.setSizePolicy(sizePolicy)
        NuevaCategoria.setMaximumSize(QtCore.QSize(16777215, 250))
        self.gridLayout = QtGui.QGridLayout(NuevaCategoria)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(NuevaCategoria)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(NuevaCategoria)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lbldescripcion = QtGui.QLabel(NuevaCategoria)
        self.lbldescripcion.setObjectName("lbldescripcion")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbldescripcion)
        self.txtCategoria = QtGui.QLineEdit(NuevaCategoria)
        self.txtCategoria.setObjectName("txtCategoria")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtCategoria)
        self.lblNotas = QtGui.QLabel(NuevaCategoria)
        self.lblNotas.setText("")
        self.lblNotas.setObjectName("lblNotas")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblNotas)
        self.gridLayout.addLayout(self.formLayout, 3, 0, 1, 1)
        self.line = QtGui.QFrame(NuevaCategoria)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.lbldescripcion.setBuddy(self.txtCategoria)

        self.retranslateUi(NuevaCategoria)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NuevaCategoria.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NuevaCategoria.reject)
        QtCore.QMetaObject.connectSlotsByName(NuevaCategoria)

    def retranslateUi(self, NuevaCategoria):
        NuevaCategoria.setWindowTitle(QtGui.QApplication.translate("NuevaCategoria", "Nueva categoria", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NuevaCategoria", "Ingrese la información de la nueva categoria:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbldescripcion.setText(QtGui.QApplication.translate("NuevaCategoria", "descripcion:", None, QtGui.QApplication.UnicodeUTF8))

