# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verJuzgado.ui'
#
# Created: Thu Feb  2 15:43:50 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VerJuzgado(object):
    def setupUi(self, VerJuzgado):
        VerJuzgado.setObjectName("VerJuzgado")
        VerJuzgado.resize(381, 190)
        self.gridLayout = QtGui.QGridLayout(VerJuzgado)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(VerJuzgado)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(-1, -1, 10, -1)
        self.formLayout.setObjectName("formLayout")
        self.lbl1 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl1.sizePolicy().hasHeightForWidth())
        self.lbl1.setSizePolicy(sizePolicy)
        self.lbl1.setObjectName("lbl1")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl1)
        self.lblNombre = QtGui.QLabel(self.groupBox)
        self.lblNombre.setText("")
        self.lblNombre.setObjectName("lblNombre")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblNombre)
        self.lbl2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl2.sizePolicy().hasHeightForWidth())
        self.lbl2.setSizePolicy(sizePolicy)
        self.lbl2.setObjectName("lbl2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbl2)
        self.lblCiudad = QtGui.QLabel(self.groupBox)
        self.lblCiudad.setText("")
        self.lblCiudad.setObjectName("lblCiudad")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lblCiudad)
        self.lbl3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl3.sizePolicy().hasHeightForWidth())
        self.lbl3.setSizePolicy(sizePolicy)
        self.lbl3.setObjectName("lbl3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl3)
        self.lblTelefono = QtGui.QLabel(self.groupBox)
        self.lblTelefono.setText("")
        self.lblTelefono.setObjectName("lblTelefono")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lblTelefono)
        self.lbl4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl4.sizePolicy().hasHeightForWidth())
        self.lbl4.setSizePolicy(sizePolicy)
        self.lbl4.setObjectName("lbl4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl4)
        self.lblDireccion = QtGui.QLabel(self.groupBox)
        self.lblDireccion.setText("")
        self.lblDireccion.setObjectName("lblDireccion")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lblDireccion)
        self.lbl5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl5.sizePolicy().hasHeightForWidth())
        self.lbl5.setSizePolicy(sizePolicy)
        self.lbl5.setObjectName("lbl5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbl5)
        self.lblTipo = QtGui.QLabel(self.groupBox)
        self.lblTipo.setText("")
        self.lblTipo.setObjectName("lblTipo")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lblTipo)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(VerJuzgado)
        QtCore.QMetaObject.connectSlotsByName(VerJuzgado)

    def retranslateUi(self, VerJuzgado):
        VerJuzgado.setWindowTitle(QtGui.QApplication.translate("VerJuzgado", "Ver Juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl1.setText(QtGui.QApplication.translate("VerJuzgado", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setToolTip(QtGui.QApplication.translate("VerJuzgado", "El nombre del juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setStatusTip(QtGui.QApplication.translate("VerJuzgado", "El nombre del juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl2.setText(QtGui.QApplication.translate("VerJuzgado", "Ciudad:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCiudad.setToolTip(QtGui.QApplication.translate("VerJuzgado", "La ciudad del juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCiudad.setStatusTip(QtGui.QApplication.translate("VerJuzgado", "La ciudad del juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl3.setText(QtGui.QApplication.translate("VerJuzgado", "Teléfono:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTelefono.setToolTip(QtGui.QApplication.translate("VerJuzgado", "El teléfono del juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTelefono.setStatusTip(QtGui.QApplication.translate("VerJuzgado", "El teléfono del juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl4.setText(QtGui.QApplication.translate("VerJuzgado", "Dirección:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDireccion.setToolTip(QtGui.QApplication.translate("VerJuzgado", "La dirección del juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDireccion.setStatusTip(QtGui.QApplication.translate("VerJuzgado", "La dirección del juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl5.setText(QtGui.QApplication.translate("VerJuzgado", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipo.setToolTip(QtGui.QApplication.translate("VerJuzgado", "El tipo de juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipo.setStatusTip(QtGui.QApplication.translate("VerJuzgado", "El tipo de juzgado", None, QtGui.QApplication.UnicodeUTF8))
