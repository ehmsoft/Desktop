# -*- coding: utf-8 -*-
'''
Created on 09/08/2012

@author: elfotografo007
'''
from PySide import QtGui
from gui.AsistenteRegistroScreen import Ui_WizardRegistro
from gui.DialogoEspera import DialogoEspera


class AsistenteRegistro(QtGui.QWizard, Ui_WizardRegistro):
    def __init__(self, parent=None):
        super(AsistenteRegistro, self).__init__(parent)
        self.setupUi(self)
        self.registro.validatePage = self.validatePage
        self.__valid = False
        self.__correo = None
        
    def validatePage(self):
        correo = self.txtCorreo.text()
        if correo == "":
            QtGui.QMessageBox.warning(self, "Advertencia", u"El campo correo no puede estar vacío")
            return False
        else:
            dialogo = DialogoEspera()
            flag, respuesta = dialogo.iniciarActivacion(correo)
            QtGui.QMessageBox.warning(self,"Info", respuesta)
            self.__valid = flag
            self.__correo = correo
            return flag
    
    def isValid(self):
        return self.__valid
    
    def getCorreo(self):
        return self.__correo
