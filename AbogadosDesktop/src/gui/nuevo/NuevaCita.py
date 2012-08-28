# -*- coding: utf-8 -*-
'''
Created on 27/03/2012

@author: harold
'''
from PySide import QtGui
from NuevaCitaScreen import Ui_Cita
from core.CitaCalendario import CitaCalendario
from persistence.Persistence import Persistence
from gui.GestorCitas import GestorCitas

class NuevaCita(QtGui.QDialog, Ui_Cita):
    def __init__(self, actuacion=None, cita=None, fecha=None, parent=None, isGuardar = True):
        super(NuevaCita, self).__init__(parent)
        self.setupUi(self)
        self.isGuardar = isGuardar
        self.cita = cita
        self.actuacion = actuacion
        self.checkBox.stateChanged.connect(self.checkBoxChanged)
          
        if cita != None:
            self.checkBox.setChecked(cita.isAlarma())
            self.checkBoxChanged(cita.isAlarma())
            self.descripcion.setText(self.cita.getDescripcion())
            self.fecha.setDateTime(self.cita.getFecha())
            ant = self.transAnticipacion(self.cita.getAnticipacion())
            self.comboAnticipacion.setCurrentIndex(self.comboAnticipacion.findText(ant[1]))
            self.spinAnticipacion.setValue(ant[0])        
        elif actuacion != None:
            self.checkBox.setChecked(False)
            self.checkBoxChanged(False)        
            self.fecha.setDateTime(self.actuacion.getFechaProxima())
            self.descripcion.setText(self.actuacion.getDescripcion())
        elif fecha != None:
            self.fecha.setDateTime(fecha)
            self.checkBox.setChecked(False)
            self.checkBoxChanged(False) 
        else:
            raise TypeError('Todos los argumentos no pueden ser vacíos')

        
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
        elif escala == u'días':
            return ant * 86400
        else:
            raise TypeError('Error en valores')
        
    def transAnticipacion(self, ant):
        if ant < 3600:
            return (ant / 60, 'minutos')
        elif ant < 86400:
            return (ant / 3600, 'horas')
        else:
            return (ant / 86400, u'días')
        
    def guardar(self):
        fecha = self.fecha.dateTime().toPython()
        anticipacion = self.getAnticipacion()
        descripcion = self.descripcion.text()
        alarma = self.checkBox.isChecked()
        if not self.cita:
            if self.isGuardar:
                id_actuacion = self.actuacion.getId_actuacion()
            else:
                id_actuacion = None
            self.cita = CitaCalendario(fecha=fecha, anticipacion=anticipacion,
                                       descripcion=descripcion, alarma=alarma,
                                       id_cita=None, id_actuacion=id_actuacion, uid='')
        else:
            self.cita.setFecha(fecha)
            self.cita.setAnticipacion(anticipacion)
            self.cita.setAlarma(alarma)
            self.cita.setDescripcion(descripcion)
        if self.isGuardar or self.cita:
            self.guardarEnBD()
        else:
            return QtGui.QDialog.accept(self)
            
    def guardarEnBD(self):
        try:
            p = Persistence()
            if self.cita.getId_cita() == None:
                p.guardarCitaCalendario(self.cita)
            else:
                p.actualizarCitaCalendario(self.cita)
            return QtGui.QDialog.accept(self)
            gestor = GestorCitas()
            gestor.actualizarCitas()
        except Exception, e:
            print e
            return QtGui.QDialog.reject(self)
            
    def accept(self):
        if len(self.descripcion.text()):
            self.guardar()
        else:
            QtGui.QMessageBox.information(self, 'Error', u'La descripción no se permite vacía')
            
    def getCita(self):
        return self.cita
