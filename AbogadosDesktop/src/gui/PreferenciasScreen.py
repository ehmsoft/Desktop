# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferencias.ui'
#
# Created: Wed Aug 15 10:13:43 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Preferencias(object):
    def setupUi(self, Preferencias):
        Preferencias.setObjectName("Preferencias")
        Preferencias.resize(334, 261)
        self.verticalLayout = QtGui.QVBoxLayout(Preferencias)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(Preferencias)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbEmergente = QtGui.QCheckBox(self.groupBox)
        self.cbEmergente.setObjectName("cbEmergente")
        self.verticalLayout_3.addWidget(self.cbEmergente)
        self.cbNotificacion = QtGui.QCheckBox(self.groupBox)
        self.cbNotificacion.setObjectName("cbNotificacion")
        self.verticalLayout_3.addWidget(self.cbNotificacion)
        self.cbCorreo = QtGui.QCheckBox(self.groupBox)
        self.cbCorreo.setObjectName("cbCorreo")
        self.verticalLayout_3.addWidget(self.cbCorreo)
        self.txtCorreo = QtGui.QLineEdit(self.groupBox)
        self.txtCorreo.setEnabled(False)
        self.txtCorreo.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.txtCorreo.setObjectName("txtCorreo")
        self.verticalLayout_3.addWidget(self.txtCorreo)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Preferencias)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.sbCantidadEventos = QtGui.QSpinBox(self.groupBox_2)
        self.sbCantidadEventos.setObjectName("sbCantidadEventos")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.sbCantidadEventos)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.btnEventosVencidos = QtGui.QPushButton(self.groupBox_2)
        self.btnEventosVencidos.setObjectName("btnEventosVencidos")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.btnEventosVencidos)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnGuardar = QtGui.QPushButton(Preferencias)
        self.btnGuardar.setObjectName("btnGuardar")
        self.horizontalLayout.addWidget(self.btnGuardar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Preferencias)
        QtCore.QMetaObject.connectSlotsByName(Preferencias)

    def retranslateUi(self, Preferencias):
        Preferencias.setWindowTitle(QtGui.QApplication.translate("Preferencias", "Preferencias", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Preferencias", "Tipo de alarma", None, QtGui.QApplication.UnicodeUTF8))
        self.cbEmergente.setText(QtGui.QApplication.translate("Preferencias", "Mensaje emergente", None, QtGui.QApplication.UnicodeUTF8))
        self.cbNotificacion.setText(QtGui.QApplication.translate("Preferencias", "Mensaje en el icono de notificación", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCorreo.setText(QtGui.QApplication.translate("Preferencias", "Correo electrónico", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Preferencias", "Eventos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Preferencias", "Cantidad de eventos próximos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Preferencias", "Borrar eventos vencidos:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEventosVencidos.setText(QtGui.QApplication.translate("Preferencias", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGuardar.setText(QtGui.QApplication.translate("Preferencias", "Guardar", None, QtGui.QApplication.UnicodeUTF8))

