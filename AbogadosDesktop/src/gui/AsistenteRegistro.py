# -*- coding: utf-8 -*-
'''
Created on 09/08/2012

@author: elfotografo007
'''
from PySide import QtGui
from gui.AsistenteRegistroScreen import Ui_WizardRegistro
from gui.DialogoEspera import DialogoEspera
import sys

class AsistenteRegistro(QtGui.QWizard, Ui_WizardRegistro):
    def __init__(self, parent=None):
        super(AsistenteRegistro, self).__init__(parent)
        self.setupUi(self)
        self.registro.validatePage = self.validatePage
        self.__valid = False
        self.__correo = None
        self.setPixmap(QtGui.QWizard.BackgroundPixmap,QtGui.QPixmap(QtGui.QImage(':/images/bolita.png')))
        self.setPixmap(QtGui.QWizard.WatermarkPixmap,QtGui.QPixmap(QtGui.QImage(':/images/bolita.png')))
        
    def validatePage(self):
        correo = self.txtCorreo.text()
        if correo == "":
            QtGui.QMessageBox.warning(self, "Advertencia", u"El campo correo no puede estar vacío")
            return False
        else:
            dialogo = DialogoEspera()
            try:
                flag, respuesta = dialogo.iniciarActivacion(correo)
            except:
                QtGui.QMessageBox.warning(self, "Error", u"Ha ocurrido un problema verificando la activación de la aplicación, esta se cerrará. Por favor vuelva a iniciarla.\nSi el problema persiste contacte a soporte@ehmsoft.com")
                sys.exit(0)
            QtGui.QMessageBox.warning(self,"Info", respuesta)
            self.__valid = flag
            self.__correo = correo
            return flag
    
    def isValid(self):
        return self.__valid
    
    def getCorreo(self):
        return self.__correo
