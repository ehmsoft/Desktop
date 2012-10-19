# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/exportarCSVDialog.ui'
#
# Created: Fri Oct 19 09:59:33 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ExportarCSVDialog(object):
    def setupUi(self, ExportarCSVDialog):
        ExportarCSVDialog.setObjectName("ExportarCSVDialog")
        ExportarCSVDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ExportarCSVDialog.resize(321, 347)
        self.gridLayout = QtGui.QGridLayout(ExportarCSVDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(ExportarCSVDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rdProcesos = QtGui.QRadioButton(self.groupBox)
        self.rdProcesos.setChecked(True)
        self.rdProcesos.setObjectName("rdProcesos")
        self.verticalLayout.addWidget(self.rdProcesos)
        self.rdDemandantes = QtGui.QRadioButton(self.groupBox)
        self.rdDemandantes.setObjectName("rdDemandantes")
        self.verticalLayout.addWidget(self.rdDemandantes)
        self.rdDemandados = QtGui.QRadioButton(self.groupBox)
        self.rdDemandados.setObjectName("rdDemandados")
        self.verticalLayout.addWidget(self.rdDemandados)
        self.rdJuzgados = QtGui.QRadioButton(self.groupBox)
        self.rdJuzgados.setObjectName("rdJuzgados")
        self.verticalLayout.addWidget(self.rdJuzgados)
        self.rdActuaciones = QtGui.QRadioButton(self.groupBox)
        self.rdActuaciones.setObjectName("rdActuaciones")
        self.verticalLayout.addWidget(self.rdActuaciones)
        self.rdActuacionesCriticas = QtGui.QRadioButton(self.groupBox)
        self.rdActuacionesCriticas.setObjectName("rdActuacionesCriticas")
        self.verticalLayout.addWidget(self.rdActuacionesCriticas)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ExportarCSVDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rdCSV = QtGui.QRadioButton(self.groupBox_2)
        self.rdCSV.setChecked(True)
        self.rdCSV.setObjectName("rdCSV")
        self.verticalLayout_2.addWidget(self.rdCSV)
        self.rdTab = QtGui.QRadioButton(self.groupBox_2)
        self.rdTab.setObjectName("rdTab")
        self.verticalLayout_2.addWidget(self.rdTab)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.buttonBox = QtGui.QDialogButtonBox(ExportarCSVDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(ExportarCSVDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ExportarCSVDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ExportarCSVDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportarCSVDialog)

    def retranslateUi(self, ExportarCSVDialog):
        ExportarCSVDialog.setWindowTitle(QtGui.QApplication.translate("ExportarCSVDialog", "Exportar a CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ExportarCSVDialog", "¿Qué desea Exportar?", None, QtGui.QApplication.UnicodeUTF8))
        self.rdProcesos.setText(QtGui.QApplication.translate("ExportarCSVDialog", "Procesos", None, QtGui.QApplication.UnicodeUTF8))
        self.rdDemandantes.setText(QtGui.QApplication.translate("ExportarCSVDialog", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.rdDemandados.setText(QtGui.QApplication.translate("ExportarCSVDialog", "Contrapartes", None, QtGui.QApplication.UnicodeUTF8))
        self.rdJuzgados.setText(QtGui.QApplication.translate("ExportarCSVDialog", "Juzgados", None, QtGui.QApplication.UnicodeUTF8))
        self.rdActuaciones.setText(QtGui.QApplication.translate("ExportarCSVDialog", "Actuaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.rdActuacionesCriticas.setText(QtGui.QApplication.translate("ExportarCSVDialog", "Eventos Próximos", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ExportarCSVDialog", "Formato", None, QtGui.QApplication.UnicodeUTF8))
        self.rdCSV.setText(QtGui.QApplication.translate("ExportarCSVDialog", "Valores Separados por Comas", None, QtGui.QApplication.UnicodeUTF8))
        self.rdTab.setText(QtGui.QApplication.translate("ExportarCSVDialog", "Valores Separados por Tabulaciones", None, QtGui.QApplication.UnicodeUTF8))

