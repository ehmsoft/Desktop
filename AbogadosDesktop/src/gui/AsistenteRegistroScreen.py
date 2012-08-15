# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/asistenteRegistro.ui'
#
# Created: Wed Aug 15 17:11:55 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_WizardRegistro(object):
    def setupUi(self, WizardRegistro):
        WizardRegistro.setObjectName("WizardRegistro")
        WizardRegistro.resize(699, 542)
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
        self.terminos = QtGui.QWizardPage()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminos.sizePolicy().hasHeightForWidth())
        self.terminos.setSizePolicy(sizePolicy)
        self.terminos.setObjectName("terminos")
        self.verticalLayout = QtGui.QVBoxLayout(self.terminos)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtGui.QTextBrowser(self.terminos)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        WizardRegistro.addPage(self.terminos)
        self.registro = QtGui.QWizardPage()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registro.sizePolicy().hasHeightForWidth())
        self.registro.setSizePolicy(sizePolicy)
        self.registro.setObjectName("registro")
        self.layoutWidget = QtGui.QWidget(self.registro)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(6, 8, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtCorreo = QtGui.QLineEdit(self.layoutWidget)
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
        self.terminos.setTitle(QtGui.QApplication.translate("WizardRegistro", "Términos y Condiciones", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("WizardRegistro", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AVISO IMPORTANTE: Antes de descargar, instalar, copiar o utilizar el software lea los siguientes términos y condiciones: ehmSoftware es el propietario del software y del soporte físico. ehmSoftware concede este software bajo una licencia exclusivamente de uso a una persona natural o jurídica. Disponiendo de ésta, la instalación podrá realizarse solamente en un dispositivo o computadora, el cual está permitido cambiarlo, para esto debe eliminar por completo la instalación en el dispositivo anterior y contactar a ehmSoftware. Para que el software funcione correctamente se debe cumplir con los requisitos mínimos especificados por ehmSoftware.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ehmSoftware no se hará responsable por pérdidas, daños, reclamaciones o costes de cualquier naturaleza, incluyendo cualquier daño consecuente, indirecto o secundario, ni de cualquier pérdida de beneficios o ganancias, daños que resulten de la interrupción del negocio, daño personal o incumplimiento de cualquier deber de diligencia o reclamaciones de terceros, del mismo modo no garantiza que el software este libre de errores y se recomienda que en el caso de que éstos se presente sean reportados a soporte@ehmsoft.com para realizar el seguimiento de los mismos y tomar medidas para su corrección en el menor tiempo posible. ehmSoftware se reserva todos los derechos que no se le conceden expresamente a usted en este documento y puede retirar la licencia de uso si usted no cumple con los términos y condiciones. Si usted presiona el botón Siguiente indica que ha leído, comprendido y está de acuerdo con todos los términos y condiciones expuestos en el presente documento así como con la licencia exclusivamente de uso del software. Si no está de acuerdo presione el botón Cancelar, destruya todas las copias del software que tenga en su poder y póngase en contacto con ehmSoftware.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.registro.setTitle(QtGui.QApplication.translate("WizardRegistro", "Registro", None, QtGui.QApplication.UnicodeUTF8))
        self.registro.setSubTitle(QtGui.QApplication.translate("WizardRegistro", "Por favor llene los campos a continuación:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WizardRegistro", "Correo:", None, QtGui.QApplication.UnicodeUTF8))

