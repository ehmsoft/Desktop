# -*- coding: utf-8 -*-
'''
Created on 30/03/2012

@author: harold
'''
from core.Singleton import Singleton
from PySide import QtGui, QtCore
from persistence.Persistence import Persistence
from datetime import datetime
from datetime import timedelta
from core.Preferencias import Preferencias
from gui.Preferencias_GUI import Preferencias_GUI
from core.GestorCorreo import enviarCorreo

class GestorCitas(object):
    __metaclass__ = Singleton
    
    def __init__(self, tray,parent=None):
        self.timer = []
        self.tray = tray
        self.parent = parent
        
    def actualizarCitas(self):
        self.__detenerCitas()
        self.__cargarCitas()
        
    def __detenerCitas(self):
        for t in self.timer:
            t.stop()
        del self.timer[:]
    
    def __cargarCitas(self):
        try:
            p = Persistence()
            citas = p.consultarCitasCalendario()
            for cita in citas:
                if cita.isAlarma() and cita.getFecha() + timedelta(0, cita.getAnticipacion()) > datetime.today():
                    t = QtCore.QTimer(self.parent)
                    self.timer.append(t)
                    t.setSingleShot(True)
                    t.timeout.connect(lambda : self.__seCumpleCita(cita))
                    delta = cita.getFecha() - datetime.today()
                    tiempo = (delta.total_seconds() - cita.getAnticipacion()) * 1000
                    t.start(tiempo)
        except Exception as e:
            print e
                
    
    def __seCumpleCita(self, cita):
        preferencias = Preferencias()
        tipoAlarma = preferencias.getTipoAlarma()
        if tipoAlarma & Preferencias_GUI.MENSAJE_CORREO == Preferencias_GUI.MENSAJE_CORREO:
            enviarCorreo(cita, preferencias.getCorreo())
        if tipoAlarma & Preferencias_GUI.MENSAJE_ICONO == Preferencias_GUI.MENSAJE_ICONO:
            self.tray.showMessage(u'Notificación de cita' + cita.getDescripcion(), unicode(cita))
        if tipoAlarma & Preferencias_GUI.MENSAJE_EMERGENTE == Preferencias_GUI.MENSAJE_EMERGENTE:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("Se cumple la cita:\n" + unicode(cita))
            message.exec_()