# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verPersona.ui'
#
# Created: Wed Jan 25 10:47:55 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VerPersona(object):
    def setupUi(self, VerPersona):
        VerPersona.setObjectName("VerPersona")
        VerPersona.resize(366, 222)
        self.gridLayout = QtGui.QGridLayout(VerPersona)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(VerPersona)
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
        self.lbl2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl2.sizePolicy().hasHeightForWidth())
        self.lbl2.setSizePolicy(sizePolicy)
        self.lbl2.setObjectName("lbl2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbl2)
        self.lbl3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl3.sizePolicy().hasHeightForWidth())
        self.lbl3.setSizePolicy(sizePolicy)
        self.lbl3.setObjectName("lbl3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl3)
        self.lbl4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl4.sizePolicy().hasHeightForWidth())
        self.lbl4.setSizePolicy(sizePolicy)
        self.lbl4.setObjectName("lbl4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl4)
        self.lbl5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl5.sizePolicy().hasHeightForWidth())
        self.lbl5.setSizePolicy(sizePolicy)
        self.lbl5.setObjectName("lbl5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbl5)
        self.lbl6 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl6.sizePolicy().hasHeightForWidth())
        self.lbl6.setSizePolicy(sizePolicy)
        self.lbl6.setObjectName("lbl6")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.lbl6)
        self.lblNombre = QtGui.QLabel(self.groupBox)
        self.lblNombre.setText("")
        self.lblNombre.setObjectName("lblNombre")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblNombre)
        self.lblCedula = QtGui.QLabel(self.groupBox)
        self.lblCedula.setText("")
        self.lblCedula.setObjectName("lblCedula")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lblCedula)
        self.lblTelefono = QtGui.QLabel(self.groupBox)
        self.lblTelefono.setText("")
        self.lblTelefono.setObjectName("lblTelefono")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lblTelefono)
        self.lblDireccion = QtGui.QLabel(self.groupBox)
        self.lblDireccion.setText("")
        self.lblDireccion.setObjectName("lblDireccion")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lblDireccion)
        self.lblCorreo = QtGui.QLabel(self.groupBox)
        self.lblCorreo.setText("")
        self.lblCorreo.setObjectName("lblCorreo")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lblCorreo)
        self.lblNotas = QtGui.QLabel(self.groupBox)
        self.lblNotas.setText("")
        self.lblNotas.setObjectName("lblNotas")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lblNotas)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(VerPersona)
        QtCore.QMetaObject.connectSlotsByName(VerPersona)

    def retranslateUi(self, VerPersona):
        VerPersona.setWindowTitle(QtGui.QApplication.translate("VerPersona", "Ver Persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl1.setText(QtGui.QApplication.translate("VerPersona", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl2.setText(QtGui.QApplication.translate("VerPersona", "Cédula:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl3.setText(QtGui.QApplication.translate("VerPersona", "Teléfono:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl4.setText(QtGui.QApplication.translate("VerPersona", "Dirección:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl5.setText(QtGui.QApplication.translate("VerPersona", "Correo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl6.setText(QtGui.QApplication.translate("VerPersona", "Notas:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setToolTip(QtGui.QApplication.translate("VerPersona", "El nombre de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setStatusTip(QtGui.QApplication.translate("VerPersona", "El nombre de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCedula.setToolTip(QtGui.QApplication.translate("VerPersona", "La cédula de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCedula.setStatusTip(QtGui.QApplication.translate("VerPersona", "La cédula de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTelefono.setToolTip(QtGui.QApplication.translate("VerPersona", "El teléfono de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTelefono.setStatusTip(QtGui.QApplication.translate("VerPersona", "El teléfono de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDireccion.setToolTip(QtGui.QApplication.translate("VerPersona", "La dirección de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDireccion.setStatusTip(QtGui.QApplication.translate("VerPersona", "La dirección de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCorreo.setToolTip(QtGui.QApplication.translate("VerPersona", "El correo de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCorreo.setStatusTip(QtGui.QApplication.translate("VerPersona", "El correo de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNotas.setToolTip(QtGui.QApplication.translate("VerPersona", "Notas acerca de la persona", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNotas.setStatusTip(QtGui.QApplication.translate("VerPersona", "Notas acerca de la persona", None, QtGui.QApplication.UnicodeUTF8))
