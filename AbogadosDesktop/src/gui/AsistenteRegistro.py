# -*- coding: utf-8 -*-
'''
Created on 09/08/2012

@author: elfotografo007
'''
from PySide import QtGui
from gui.AsistenteRegistroScreen import Ui_WizardRegistro
from gui.DialogoEspera import DialogoEspera

import sys
from gui.HiloActivacion import HiloActivacion

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
            try:
                self.hilo = HiloActivacion()
                self.hilo.correo = correo
                self.hilo.pet = 'activar'
                self.hilo.finished.connect(self.hiloTerminado)
                self.dialogo = DialogoEspera()
                self.hilo.start()
                self.dialogo.exec_()
            except:
                QtGui.QMessageBox.warning(self, "Error", u"Ha ocurrido un problema verificando la activación de la aplicación, esta se cerrará. Por favor vuelva a iniciarla.\nSi el problema persiste contacte a soporte@ehmsoft.com")
                sys.exit(0)
            self.__correo = correo
            return self.__valid
        
    def hiloTerminado(self):
        QtGui.QMessageBox.warning(self,"Info", self.hilo.respuesta)
        self.__valid = self.hilo.flag
        self.dialogo.hide()
        
    def isValid(self):
        return self.__valid
    
    def getCorreo(self):
        return self.__correo

