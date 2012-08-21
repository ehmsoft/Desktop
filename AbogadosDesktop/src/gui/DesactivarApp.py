# -*- coding: utf-8 -*-
'''
Created on 21/08/2012

@author: elfotografo007
'''
from PySide import QtGui
from persistence.Persistence import Persistence
from gui.DialogoEspera import DialogoEspera
from gui.HiloActivacion import HiloActivacion
import sys
class DesactivarApp(object):
    def __init__(self, carpeta, parent = None):
        self.__persistence = Persistence(carpeta)
        self.parent = parent
    
    def desactivarAplicacion(self):
        confirmar = QtGui.QMessageBox.question(self.parent, u"Confirmar desactivación", u"Si procede no podrá utilizar la aplicación. ¿Seguro que desea desactivar la aplicación?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if confirmar == QtGui.QMessageBox.Yes:
            self.dialogo = DialogoEspera()
            try:
                correo = self.__persistence.consultarPreferencia(10402)
            except:
                QtGui.QMessageBox.warning(self.parent, "Error", u"Ha ocurrido un problema desactivando la aplicación. Por favor vuelva a intentar.\nSi el problema persiste contacte a soporte@ehmsoft.com")

            self.hilo = HiloActivacion()
            self.hilo.correo = correo
            self.hilo.pet = 'desactivar'
            self.hilo.finished.connect(self.hiloTerminado)
            self.dialogo = DialogoEspera()
            try:
                self.hilo.start()
                self.dialogo.exec_()
            except:
                QtGui.QMessageBox.warning(self.parent, "Error", u"Ha ocurrido un problema verificando la activación de la aplicación, esta se cerrará. Por favor vuelva a iniciarla.\nSi el problema persiste contacte a soporte@ehmsoft.com")
                sys.exit(0)
            if self.flag:
                try:
                    self.__persistence.actualizarPreferencia(998, 0)
                except Exception as e:
                    QtGui.QMessageBox.warning(self.parent, "Error", u"Ha ocurrido un problema desactivando la aplicación. Por favor vuelva a intentar.\nSi el problema persiste contacte a soporte@ehmsoft.com")
                    print e
            sys.exit(0)
            
    def hiloTerminado(self):
        QtGui.QMessageBox.warning(self.parent,"Info", self.hilo.respuesta)
        self.flag = self.hilo.flag
        self.dialogo.hide()