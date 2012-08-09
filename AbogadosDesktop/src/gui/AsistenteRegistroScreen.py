# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asistenteRegistro.ui'
#
# Created: Fri Aug  3 17:20:20 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_WizardRegistro(object):
    def setupUi(self, WizardRegistro):
        WizardRegistro.setObjectName("WizardRegistro")
        WizardRegistro.resize(672, 515)
        self.bienvenida = QtGui.QWizardPage()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bienvenida.sizePolicy().hasHeightForWidth())
        self.bienvenida.setSizePolicy(sizePolicy)
        self.bienvenida.setObjectName("bienvenida")
        self.label = QtGui.QLabel(self.bienvenida)
        self.label.setGeometry(QtCore.QRect(0, -10, 449, 101))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        WizardRegistro.addPage(self.bienvenida)
        self.registro = QtGui.QWizardPage()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registro.sizePolicy().hasHeightForWidth())
        self.registro.setSizePolicy(sizePolicy)
        self.registro.setObjectName("registro")
        self.widget = QtGui.QWidget(self.registro)
        self.widget.setGeometry(QtCore.QRect(10, 10, 421, 50))
        self.widget.setObjectName("widget")
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(6, 8, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtCorreo = QtGui.QLineEdit(self.widget)
        self.txtCorreo.setMinimumSize(QtCore.QSize(250, 0))
        self.txtCorreo.setText("")
        self.txtCorreo.setPlaceholderText("")
        self.txtCorreo.setObjectName("txtCorreo")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtCorreo)
        WizardRegistro.addPage(self.registro)

        self.retranslateUi(WizardRegistro)
        QtCore.QMetaObject.connectSlotsByName(WizardRegistro)

    def retranslateUi(self, WizardRegistro):
        WizardRegistro.setWindowTitle(QtGui.QApplication.translate("WizardRegistro", "Asistente Activación", None, QtGui.QApplication.UnicodeUTF8))
        self.bienvenida.setTitle(QtGui.QApplication.translate("WizardRegistro", "Bienvenido", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WizardRegistro", "Gracias por confiar en ehmSoftware. Este asistente lo guiará para activar la copia del software adquirido. Para continuar es necesaria una conexión a internet. Cuando esté listo para proceder haga click en \"Siguiente\" ", None, QtGui.QApplication.UnicodeUTF8))
        self.registro.setTitle(QtGui.QApplication.translate("WizardRegistro", "Registro", None, QtGui.QApplication.UnicodeUTF8))
        self.registro.setSubTitle(QtGui.QApplication.translate("WizardRegistro", "Por favor llene los campos a continuación:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WizardRegistro", "Correo:", None, QtGui.QApplication.UnicodeUTF8))

