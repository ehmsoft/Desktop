# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevaActuacion.ui'
#
# Created: Wed Feb 15 11:37:56 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NuevaActuacion(object):
    def setupUi(self, NuevaActuacion):
        NuevaActuacion.setObjectName("NuevaActuacion")
        NuevaActuacion.resize(302, 205)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NuevaActuacion.sizePolicy().hasHeightForWidth())
        NuevaActuacion.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(NuevaActuacion)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(NuevaActuacion)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lblDescripcion = QtGui.QLabel(self.groupBox)
        self.lblDescripcion.setObjectName("lblDescripcion")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblDescripcion)
        self.txtDescripcion = QtGui.QLineEdit(self.groupBox)
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtDescripcion)
        self.lblJuzgado_2 = QtGui.QLabel(self.groupBox)
        self.lblJuzgado_2.setObjectName("lblJuzgado_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblJuzgado_2)
        self.lblJuzgado = QtGui.QLabel(self.groupBox)
        self.lblJuzgado.setCursor(QtCore.Qt.PointingHandCursor)
        self.lblJuzgado.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lblJuzgado.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lblJuzgado.setObjectName("lblJuzgado")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lblJuzgado)
        self.lblFecha = QtGui.QLabel(self.groupBox)
        self.lblFecha.setObjectName("lblFecha")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblFecha)
        self.dteFecha = QtGui.QDateTimeEdit(self.groupBox)
        self.dteFecha.setObjectName("dteFecha")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dteFecha)
        self.lblFechaProxima = QtGui.QLabel(self.groupBox)
        self.lblFechaProxima.setObjectName("lblFechaProxima")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblFechaProxima)
        self.dteFechaProxima = QtGui.QDateTimeEdit(self.groupBox)
        self.dteFechaProxima.setObjectName("dteFechaProxima")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dteFechaProxima)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.btnAdd = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout_2.addWidget(self.btnAdd, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.line = QtGui.QFrame(NuevaActuacion)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.buttonBox = QtGui.QDialogButtonBox(NuevaActuacion)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.lblDescripcion.setBuddy(self.txtDescripcion)
        self.lblFecha.setBuddy(self.dteFecha)
        self.lblFechaProxima.setBuddy(self.dteFechaProxima)

        self.retranslateUi(NuevaActuacion)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NuevaActuacion.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NuevaActuacion.reject)
        QtCore.QMetaObject.connectSlotsByName(NuevaActuacion)

    def retranslateUi(self, NuevaActuacion):
        NuevaActuacion.setWindowTitle(QtGui.QApplication.translate("NuevaActuacion", "Nueva actuación", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NuevaActuacion", "Ingrese los datos de la nueva actuación", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDescripcion.setText(QtGui.QApplication.translate("NuevaActuacion", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.lblJuzgado_2.setText(QtGui.QApplication.translate("NuevaActuacion", "Juzgado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblJuzgado.setText(QtGui.QApplication.translate("NuevaActuacion", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFecha.setText(QtGui.QApplication.translate("NuevaActuacion", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFechaProxima.setText(QtGui.QApplication.translate("NuevaActuacion", "Fecha próxima:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("NuevaActuacion", "+", None, QtGui.QApplication.UnicodeUTF8))

