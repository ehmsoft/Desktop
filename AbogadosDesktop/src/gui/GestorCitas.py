# -*- coding: utf-8 -*-
'''
Created on 30/03/2012

@author: harold
'''
from core.Singleton import Singleton
from PySide import QtGui, QtCore
from persistence.Persistence import Persistence
from datetime import datetime
class GestorCitas(object):
    __metaclass__ = Singleton
    
    def __init__(self, parent = None):
        self.timer = []
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
                if cita.getFecha() > datetime.today():
                    t = QtCore.QTimer(self.parent)
                    self.timer.append(t)
                    t.setSingleShot(True)
                    t.timeout.connect(lambda : self.__seCumpleCita(cita))
                    date = cita.getFecha()
                    delta = date - datetime.today()
                    tiempo = delta.seconds * 1000 + delta.microseconds / 1000
                    t.start(tiempo)
        except Exception as e:
            print e
                
    
    def __seCumpleCita(self, cita):
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Warning)
        message.setText("Se cumple la cita:\n" + unicode(cita))
        message.exec_()