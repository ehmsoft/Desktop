# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verCampoPersonalizado.ui'
#
# Created: Thu Jan 26 07:39:48 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VerCampoPersonalizado(object):
    def setupUi(self, VerCampoPersonalizado):
        VerCampoPersonalizado.setObjectName("VerCampoPersonalizado")
        VerCampoPersonalizado.resize(381, 190)
        self.gridLayout = QtGui.QGridLayout(VerCampoPersonalizado)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(VerCampoPersonalizado)
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
        self.lblValor = QtGui.QLabel(self.groupBox)
        self.lblValor.setText("")
        self.lblValor.setObjectName("lblValor")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lblValor)
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
        self.lblLongitudMax = QtGui.QLabel(self.groupBox)
        self.lblLongitudMax.setText("")
        self.lblLongitudMax.setObjectName("lblLongitudMax")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lblLongitudMax)
        self.lbl5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl5.sizePolicy().hasHeightForWidth())
        self.lbl5.setSizePolicy(sizePolicy)
        self.lbl5.setObjectName("lbl5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbl5)
        self.lblLongitudMin = QtGui.QLabel(self.groupBox)
        self.lblLongitudMin.setText("")
        self.lblLongitudMin.setObjectName("lblLongitudMin")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lblLongitudMin)
        self.chkObligatorio = QtGui.QCheckBox(self.groupBox)
        self.chkObligatorio.setEnabled(False)
        self.chkObligatorio.setWhatsThis("")
        self.chkObligatorio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkObligatorio.setText("")
        self.chkObligatorio.setChecked(False)
        self.chkObligatorio.setObjectName("chkObligatorio")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.chkObligatorio)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(VerCampoPersonalizado)
        QtCore.QMetaObject.connectSlotsByName(VerCampoPersonalizado)

    def retranslateUi(self, VerCampoPersonalizado):
        VerCampoPersonalizado.setWindowTitle(QtGui.QApplication.translate("VerCampoPersonalizado", "Ver Campo Personalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl1.setText(QtGui.QApplication.translate("VerCampoPersonalizado", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setToolTip(QtGui.QApplication.translate("VerCampoPersonalizado", "El nombre del campo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setStatusTip(QtGui.QApplication.translate("VerCampoPersonalizado", "El nombre del campo", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl2.setText(QtGui.QApplication.translate("VerCampoPersonalizado", "Valor:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblValor.setToolTip(QtGui.QApplication.translate("VerCampoPersonalizado", "El valor que tiene el campo", None, QtGui.QApplication.UnicodeUTF8))
        self.lblValor.setStatusTip(QtGui.QApplication.translate("VerCampoPersonalizado", "El valor que tiene el campo", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl3.setText(QtGui.QApplication.translate("VerCampoPersonalizado", "Obligatorio:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl4.setText(QtGui.QApplication.translate("VerCampoPersonalizado", "Longitud Máx:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLongitudMax.setToolTip(QtGui.QApplication.translate("VerCampoPersonalizado", "Longitud Máxima de caracteres. 0 es ilimitado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLongitudMax.setStatusTip(QtGui.QApplication.translate("VerCampoPersonalizado", "Longitud Máxima de caracteres. 0 es ilimitado", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl5.setText(QtGui.QApplication.translate("VerCampoPersonalizado", "Longitud Mín:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLongitudMin.setToolTip(QtGui.QApplication.translate("VerCampoPersonalizado", "Longitud Mínima de caracteres. 0 es ilimitado", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLongitudMin.setStatusTip(QtGui.QApplication.translate("VerCampoPersonalizado", "Longitud Mínima de caracteres. 0 es ilimitado", None, QtGui.QApplication.UnicodeUTF8))
        self.chkObligatorio.setToolTip(QtGui.QApplication.translate("VerCampoPersonalizado", "Indica si el campo es obligatorio", None, QtGui.QApplication.UnicodeUTF8))
        self.chkObligatorio.setStatusTip(QtGui.QApplication.translate("VerCampoPersonalizado", "Indica si el campo es obligatorio", None, QtGui.QApplication.UnicodeUTF8))

