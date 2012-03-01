# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevoCampo.ui'
#
# Created: Thu Jan 26 15:18:03 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.8
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NuevoCampo(object):
    def setupUi(self, NuevoCampo):
        NuevoCampo.setObjectName("NuevoCampo")
        NuevoCampo.resize(407, 181)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NuevoCampo.sizePolicy().hasHeightForWidth())
        NuevoCampo.setSizePolicy(sizePolicy)
        NuevoCampo.setMaximumSize(QtCore.QSize(16777215, 181))
        self.gridLayout = QtGui.QGridLayout(NuevoCampo)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(NuevoCampo)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.line = QtGui.QFrame(NuevoCampo)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(NuevoCampo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lblNombre = QtGui.QLabel(self.groupBox)
        self.lblNombre.setObjectName("lblNombre")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblNombre)
        self.txtNombre = QtGui.QLineEdit(self.groupBox)
        self.txtNombre.setObjectName("txtNombre")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtNombre)
        self.lblLongMax = QtGui.QLabel(self.groupBox)
        self.lblLongMax.setObjectName("lblLongMax")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblLongMax)
        self.lblLongMin = QtGui.QLabel(self.groupBox)
        self.lblLongMin.setObjectName("lblLongMin")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblLongMin)
        self.sbLongMax = QtGui.QSpinBox(self.groupBox)
        self.sbLongMax.setObjectName("sbLongMax")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sbLongMax)
        self.sbLongMin = QtGui.QSpinBox(self.groupBox)
        self.sbLongMin.setObjectName("sbLongMin")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sbLongMin)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.cbObligatorio = QtGui.QCheckBox(self.groupBox)
        self.cbObligatorio.setObjectName("cbObligatorio")
        self.gridLayout_2.addWidget(self.cbObligatorio, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.lblNombre.setBuddy(self.txtNombre)

        self.retranslateUi(NuevoCampo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NuevoCampo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NuevoCampo.reject)
        QtCore.QMetaObject.connectSlotsByName(NuevoCampo)

    def retranslateUi(self, NuevoCampo):
        NuevoCampo.setWindowTitle(QtGui.QApplication.translate("NuevoCampo", "Nuevo campo personalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NuevoCampo", "Ingrese la información del nuevo campo personalizado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setText(QtGui.QApplication.translate("NuevoCampo", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLongMax.setText(QtGui.QApplication.translate("NuevoCampo", "Longitud máxima:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLongMin.setText(QtGui.QApplication.translate("NuevoCampo", "Longitud mínima:", None, QtGui.QApplication.UnicodeUTF8))
        self.sbLongMax.setToolTip(QtGui.QApplication.translate("NuevoCampo", "El valor 0 se usa si no se quiere limiar con este parámetro", None, QtGui.QApplication.UnicodeUTF8))
        self.sbLongMin.setToolTip(QtGui.QApplication.translate("NuevoCampo", "El valor 0 se usa si no se quiere limiar con este parámetro", None, QtGui.QApplication.UnicodeUTF8))
        self.cbObligatorio.setToolTip(QtGui.QApplication.translate("NuevoCampo", "Si el campo al ser agregado a algún elemento debe tener siempre o no un valor", None, QtGui.QApplication.UnicodeUTF8))
        self.cbObligatorio.setText(QtGui.QApplication.translate("NuevoCampo", "Obligatorio", None, QtGui.QApplication.UnicodeUTF8))

