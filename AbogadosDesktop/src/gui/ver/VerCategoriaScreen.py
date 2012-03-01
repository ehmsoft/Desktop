# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verCategoria.ui'
#
# Created: Thu Jan 26 08:29:32 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VerCategoria(object):
    def setupUi(self, VerCategoria):
        VerCategoria.setObjectName("VerCategoria")
        VerCategoria.resize(312, 80)
        self.gridLayout = QtGui.QGridLayout(VerCategoria)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(VerCategoria)
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
        self.lbl4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl4.sizePolicy().hasHeightForWidth())
        self.lbl4.setSizePolicy(sizePolicy)
        self.lbl4.setObjectName("lbl4")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl4)
        self.lblDescripcion = QtGui.QLabel(self.groupBox)
        self.lblDescripcion.setText("")
        self.lblDescripcion.setObjectName("lblDescripcion")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblDescripcion)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(VerCategoria)
        QtCore.QMetaObject.connectSlotsByName(VerCategoria)

    def retranslateUi(self, VerCategoria):
        VerCategoria.setWindowTitle(QtGui.QApplication.translate("VerCategoria", "Ver Categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl4.setText(QtGui.QApplication.translate("VerCategoria", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDescripcion.setToolTip(QtGui.QApplication.translate("VerCategoria", "La descripción de la categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDescripcion.setStatusTip(QtGui.QApplication.translate("VerCategoria", "La descripción de la categoría", None, QtGui.QApplication.UnicodeUTF8))

