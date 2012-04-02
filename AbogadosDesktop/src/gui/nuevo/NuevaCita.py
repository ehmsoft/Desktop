# -*- coding: utf-8 -*-
'''
Created on 27/03/2012

@author: harold
'''
from PySide import QtCore, QtGui
from NuevaCitaScreen import Ui_Cita
from datetime import datetime
from core.CitaCalendario import CitaCalendario
from persistence.Persistence import Persistence

class NuevaCita(QtGui.QDialog, Ui_Cita):
    def __init__(self,actuacion = None, cita = None,parent = None):
        super(NuevaCita, self).__init__(parent)
        self.setupUi(self)
        self.cita = cita
        self.fecha.setDateTime(datetime.today())
        self.actuacion = actuacion
        self.checkBox.stateChanged.connect(self.checkBoxChanged)
        
        if cita == None:
            self.checkBox.setChecked(False)
            self.checkBoxChanged(False)        
            self.fecha.setDateTime(self.actuacion.getFechaProxima())
            self.descripcion.setText(self.actuacion.getDescripcion())
        else:
            self.checkBox.setChecked(cita.isAlarma())
            self.checkBoxChanged(cita.isAlarma())
            self.descripcion.setText(self.cita.getDescripcion())
            self.fecha.setDateTime(self.cita.getFecha())
            ant = self.transAnticipacion(self.cita.getAnticipacion())
            self.comboAnticipacion.setCurrentIndex(self.comboAnticipacion.findText(ant[1]))
            self.spinAnticipacion.setValue(ant[0])
        
    def checkBoxChanged(self, check):
        if not check:
            self.spinAnticipacion.setEnabled(False)
            self.comboAnticipacion.setEnabled(False)
        else:
            self.spinAnticipacion.setEnabled(True)
            self.comboAnticipacion.setEnabled(True)
            
    def setFecha(self, date):
        self.fecha.setDate(date)            
            
    def getAnticipacion(self):
        escala = self.comboAnticipacion.currentText()
        ant = self.spinAnticipacion.value()
        if escala == 'minutos':
            return ant * 60
        elif escala == 'horas':
            return ant * 3600
        elif escala == unicode('días'):
            return ant * 86400
        else:
            raise TypeError('Error en valores')
        
    def transAnticipacion(self, ant):
        if ant < 3600:
            return (ant / 60, 'minutos')
        elif ant < 86400:
            return (ant / 3600, 'horas')
        else:
            return (ant / 86400, unicode('días'))
        
    def guardar(self):
        fecha = self.fecha.dateTime().toPython()
        anticipacion = self.getAnticipacion()
        descripcion = self.descripcion.text()
        alarma = self.checkBox.isChecked()
        if self.cita == None:
            self.cita = CitaCalendario(fecha = fecha, anticipacion = anticipacion, 
                                       descripcion = descripcion, alarma = alarma, 
                                       id_cita = None, id_actuacion = self.actuacion.getId_actuacion(), uid = '')
        else:
            self.cita.setFecha(fecha)
            self.cita.setAnticipacion(anticipacion)
            self.cita.setAlarma(alarma)
            self.cita.setDescripcion(descripcion)
        try:
            p = Persistence()
            if self.cita.getId_cita() == None:
                p.guardarCitaCalendario(self.cita)
            else:
                p.actualizarCitaCalendario(self.cita)
            return QtGui.QDialog.accept(self)
        except Exception, e:
            print e
            return QtGui.QDialog.reject(self)

            
    def accept(self):
        self.guardar()
            
    def getCita(self):
        return self.cita