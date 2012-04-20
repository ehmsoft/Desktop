# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cita.ui'
#
# Created: Wed Mar 28 23:15:52 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Cita(object):
    def setupUi(self, Cita):
        Cita.setObjectName("Cita")
        Cita.resize(278, 181)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Cita.sizePolicy().hasHeightForWidth())
        Cita.setSizePolicy(sizePolicy)
        Cita.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Cita)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(Cita)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.descripcion = QtGui.QLineEdit(self.groupBox)
        self.descripcion.setObjectName("descripcion")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.descripcion)
        self.fecha = QtGui.QDateTimeEdit(self.groupBox)
        self.fecha.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.fecha.setCalendarPopup(True)
        self.fecha.setTimeSpec(QtCore.Qt.LocalTime)
        self.fecha.setObjectName("fecha")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fecha)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinAnticipacion = QtGui.QSpinBox(self.groupBox)
        self.spinAnticipacion.setProperty("value", 5)
        self.spinAnticipacion.setObjectName("spinAnticipacion")
        self.horizontalLayout.addWidget(self.spinAnticipacion)
        self.comboAnticipacion = QtGui.QComboBox(self.groupBox)
        self.comboAnticipacion.setObjectName("comboAnticipacion")
        self.comboAnticipacion.addItem("")
        self.comboAnticipacion.addItem("")
        self.comboAnticipacion.addItem("")
        self.horizontalLayout.addWidget(self.comboAnticipacion)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Cita)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Cita.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Cita.reject)
        QtCore.QMetaObject.connectSlotsByName(Cita)

    def retranslateUi(self, Cita):
        Cita.setWindowTitle(QtGui.QApplication.translate("Cita", "Cita", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Cita", "Cita", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Cita", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Cita", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Cita", "Anticipación:", None, QtGui.QApplication.UnicodeUTF8))
        self.fecha.setDisplayFormat(QtGui.QApplication.translate("Cita", "d MMM yyyy hh:mm:ss a", None, QtGui.QApplication.UnicodeUTF8))
        self.comboAnticipacion.setItemText(0, QtGui.QApplication.translate("Cita", "minutos", None, QtGui.QApplication.UnicodeUTF8))
        self.comboAnticipacion.setItemText(1, QtGui.QApplication.translate("Cita", "horas", None, QtGui.QApplication.UnicodeUTF8))
        self.comboAnticipacion.setItemText(2, QtGui.QApplication.translate("Cita", "días", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Cita", "alarma", None, QtGui.QApplication.UnicodeUTF8))

