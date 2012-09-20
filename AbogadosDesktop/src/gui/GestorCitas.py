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
from core.GestorCorreo import Correo

class GestorCitas(object):
    __metaclass__ = Singleton
    
    def __init__(self, tray,parent=None):
        self.tray = tray
        self.parent = parent
        self.citas = []
        self.timer = []
        self.callback = None
        
    def actualizarCitas(self):
        self.__detenerCitas()
        self.__cargarCitas()
        
    def registrarCallBack(self, callback):
        self.callback = callback
        
    def retirarCallBack(self):
        self.callback = None
        
    def __detenerCitas(self):
        for t in self.timer:
            t.stop()
        del self.timer[:]
        del self.citas[:]
    
    def __cargarCitas(self):
        try:
            p = Persistence()
            citas = p.consultarCitasCalendario()
            for cita in citas:
                if cita.isAlarma() and cita.getFecha() - timedelta(0, cita.getAnticipacion()) > datetime.today():
                    timer = QtCore.QTimer(self.parent)
                    timer.setSingleShot(True)
                    timer.timeout.connect(self.__seCumpleCita)
                    delta = cita.getFecha() - datetime.today()
                    tiempo = (delta.total_seconds() - cita.getAnticipacion()) * 1000
                    #print 'Cita: '+ cita.getDescripcion() + '\n Anticipación: ' + unicode(tiempo)
                    self.citas.append(cita)
                    timer.start(tiempo)
                    self.timer.append(timer)
                    
        except Exception as e:
            print e                
    
    def __seCumpleCita(self):
        if len(self.citas):
            cita = self.citas.pop(0)
            if self.callback:
                self.callback()
            preferencias = Preferencias()
            tipoAlarma = preferencias.getTipoAlarma()
            if tipoAlarma & Preferencias_GUI.MENSAJE_CORREO == Preferencias_GUI.MENSAJE_CORREO:
                try:
                    correo = Correo(self.parent)
                    correo.cita = cita
                    correo.correo = preferencias.getCorreoNotificacion()
                    correo.start()
                except Exception as e:
                    print e.message
                    QtGui.QMessageBox.information(self.parent, 'Error', u"Error al enviar correo electrónico de notificación de una cita. Por favor verifique su conexión a internet e intente de nuevo. Si el problema persiste por favor comuníquese con nuestro personal de soporte técnico: soporte@ehmsoft.com")
            if tipoAlarma & Preferencias_GUI.MENSAJE_ICONO == Preferencias_GUI.MENSAJE_ICONO:
                self.tray.showMessage(u'Notificación de cita' + cita.getDescripcion(), unicode(cita))
            if tipoAlarma & Preferencias_GUI.MENSAJE_EMERGENTE == Preferencias_GUI.MENSAJE_EMERGENTE:
                message = QtGui.QMessageBox()
                message.setIcon(QtGui.QMessageBox.Warning)
                message.setText("Se cumple la cita:\n" + unicode(cita))
                message.exec_()