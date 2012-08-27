# -*- coding: utf-8 -*-
'''
Created on 4/04/2012

@author: esteban
'''
from PreferenciasScreen import Ui_Preferencias
from PySide import QtGui
from core.Preferencias import Preferencias
from persistence.Persistence import Persistence
class Preferencias_GUI(QtGui.QWidget, Ui_Preferencias):
    
    MENSAJE_EMERGENTE = 0b1
    MENSAJE_ICONO = 0b10
    MENSAJE_CORREO = 0b100
    
    def __init__(self, parent=None):
        self.preferencia = Preferencias()
        super(Preferencias_GUI, self).__init__(parent)
        self.setupUi(self)
        
        self.cbCorreo.stateChanged.connect(self.configurarCheckCorreo)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnEventosVencidos.clicked.connect(self.borrarEventosVencidos)
        
        self.cargarPreferencias()
        
    def configurarCheckCorreo(self, state):
        if state:
            self.txtCorreo.setEnabled(True)
        else:
            self.txtCorreo.setEnabled(False)
            self.txtCorreo.clear()
            
    def borrarEventosVencidos(self):
        res = QtGui.QMessageBox.question(self, 'Confirme', u'¿Desea eliminar todos los eventos vencidos?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if res == QtGui.QMessageBox.Yes:
            Persistence().borrarEventosVencidos()    
    
    def cargarPreferencias(self):
        preferencias = Preferencias()
        tipoAlarma = preferencias.getTipoAlarma()
        if tipoAlarma & self.MENSAJE_EMERGENTE == self.MENSAJE_EMERGENTE:
            self.cbEmergente.setChecked(True)
        else:
            self.cbEmergente.setChecked(False)
        if tipoAlarma & self.MENSAJE_ICONO == self.MENSAJE_ICONO:
            self.cbNotificacion.setChecked(True)
        else:
            self.cbNotificacion.setChecked(False)
        if tipoAlarma & self.MENSAJE_CORREO == self.MENSAJE_CORREO:
            self.cbCorreo.setChecked(True)
            self.txtCorreo.setText(preferencias.getCorreo())
        else:
            self.cbCorreo.setChecked(False)
        self.sbCantidadEventos.setValue(preferencias.getCantidadEventos())
        
    def guardar(self):
        p = Preferencias()
        tipoAlarma = 0
        if self.cbEmergente.isChecked():
            tipoAlarma = tipoAlarma | self.MENSAJE_EMERGENTE
        if self.cbNotificacion.isChecked():
            tipoAlarma = tipoAlarma | self.MENSAJE_ICONO
        if self.cbCorreo.isChecked():
            tipoAlarma = tipoAlarma | self.MENSAJE_CORREO
        p.setTipoAlarma(tipoAlarma)
        if self.cbCorreo.isChecked():
            p.setCorreo(self.txtCorreo.text())
        else:
            p.setCorreo('')
        p.setCantidadEventos(self.sbCantidadEventos.value())      