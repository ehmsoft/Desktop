# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: harold
'''

from PySide import QtGui, QtCore
from gui.NuevaActuacionScreen import Ui_NuevaActuacion
from persistence.Persistence import Persistence
from core.Juzgado import Juzgado
from core.Actuacion import Actuacion
from datetime import datetime
from gui.VerJuzgado import VerJuzgado
from gui.ListadoDialogo import ListadoDialogo
from gui.NuevoCampo import NuevoCampo

class NuevaActuacion(QtGui.QDialog, Ui_NuevaActuacion):
    '''
    classdocs
    '''


    def __init__(self, actuacion = None, id_proceso = None, parent = None):
        super(NuevaActuacion, self).__init__(parent)
        
        if actuacion is None and id_proceso is None:
            raise TypeError("Para crear una actuación debe pasar el argumento id_proceso")
        if actuacion is not None and not isinstance(actuacion, Actuacion):
            raise TypeError("El objeto actuacion debe ser de la clase Actuacion")
        
        
        self.setupUi(self)
        self.__actuacion = actuacion
        self.__idProceso = id_proceso
        self.__juzgado = None
        self.__campos = []
                
        if actuacion is not None:
            self.__juzgado = actuacion.getJuzgado()
            self.__campos = actuacion.getCampos()
            self.txtDescripcion.setText(unicode(actuacion.getDescripcion()))
            self.lblJuzgado.setText(unicode(self.__juzgado.getNombre()))
            self.dteFecha.setDateTime(actuacion.getFecha())
            self.dteFechaProxima.setDateTime(actuacion.getFechaProxima())
            
        if self.__campos is not None and self.__campos != []:
            for campo in self.__campos:
                self.addCampo(campo)
        
        self.clickJuzgado()
        self.clickFecha()
        self.clickFechaProxima()
        
    def clickJuzgado(self):
        container = self.horizontal  
        widget = self
        lblJuzgado = self.lblJuzgado
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if container.itemAt(1) is not None:
                    container.itemAt(1).widget().deleteLater()
                if widget.__juzgado.getId_juzgado is not "1":
                    vista = VerJuzgado(widget.__juzgado, widget)
                    container.addWidget(vista)
            return QtGui.QLabel.mousePressEvent(lblJuzgado,self)
            
        self.lblJuzgado.mousePressEvent = mousePressEvent
    
    def clickFecha(self):
        container = self.horizontal  
        dteFecha = self.dteFecha
        
        def focusInEvent(self):
            if container.itemAt(1) is not None:
                container.itemAt(1).widget().deleteLater()       
            calendar = QtGui.QCalendarWidget()
            calendar.setSelectedDate(dteFecha.dateTime().date())
            container.addWidget(calendar)  
            
            selectionChanged = lambda:dteFecha.setDate(calendar.selectedDate())           
            calendar.selectionChanged.connect(selectionChanged)
                  
            return QtGui.QDateTimeEdit.focusInEvent(dteFecha,self)
        
        def dateChanged(date):
            calendar = container.itemAt(1).widget()
            calendar.setSelectedDate(date)        
            
        dteFecha.focusInEvent = focusInEvent
        dteFecha.dateChanged.connect(dateChanged)
        
    
    def clickFechaProxima(self):
        container = self.horizontal  
        dteFecha = self.dteFechaProxima
        
        def focusInEvent(self):
            if container.itemAt(1) is not None:
                container.itemAt(1).widget().deleteLater()       
            calendar = QtGui.QCalendarWidget()
            calendar.setSelectedDate(dteFecha.dateTime().date())
            container.addWidget(calendar)   
            
            selectionChanged = lambda:dteFecha.setDate(calendar.selectedDate())           
            calendar.selectionChanged.connect(selectionChanged)
                 
            return QtGui.QDateTimeEdit.focusInEvent(dteFecha,self)
        
        def dateChanged(date):
            calendar = container.itemAt(1).widget()
            calendar.setSelectedDate(date)        
            
        dteFecha.focusInEvent = focusInEvent
        dteFecha.dateChanged.connect(dateChanged)
        
    def organizarCampos(self):
        count = 4
        for campo in self.__campos:
            if campo is not None:
                item = self.formLayout.itemAt(count, QtGui.QFormLayout.FieldRole).widget()
                
                message = QtGui.QMessageBox()
                message.setIcon(QtGui.QMessageBox.Warning)
                
                if campo.isObligatorio() and len(item.text()) is 0:
                    message.setText("El campo %s es obligatorio" % campo.getNombre())
                    message.exec_()
                    return False
                elif campo.getLongitudMax() is not 0 and len(item.text()) > campo.getLongitudMax():
                    message.setText(unicode("La longitud máxima del campo %s es de %i caracteres" % (campo.getNombre(), campo.getLongitudMax())))
                    message.exec_()
                    return False
                elif campo.getLongitudMin() is not 0 and len(item.text()) < campo.getLongitudMin():
                    message.setText(unicode("La longitud mínima del campo %s es de %i caracteres" % (campo.getNombre(), campo.getLongitudMin())))
                    message.exec_()
                    return False
                count += 1
                    
        count = 4
        for campo in self.__campos:
            if campo is not None:
                item = self.formLayout.itemAt(count, QtGui.QFormLayout.FieldRole).widget()
                campo.setValor(item.text())
            count += 1
                        
        func = lambda x: x is not None and 1 or 0
        self.__campos = filter(func, self.__campos)
        
        if self.__actuacion is not None:        
            camposObjeto = self.__actuacion.getCampos()
            
            for campoNuevo in self.__campos:
                if campoNuevo not in camposObjeto:
                    try:
                        p = Persistence()
                        p.guardarCampoJuzgado(campoNuevo, self.__actuacion.getId_actuacion())
                    except Exception, e:
                        print e
            for campoViejo in camposObjeto:
                if campoViejo not in self.__campos:
                    try:
                        p = Persistence()
                        p.borrarCampoJuzgado(campoViejo)
                    except Exception, e:
                        print e
            self.__actuacion.setCampos(self.__campos)
        return True
        
    def borrarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QtGui.QFormLayout.LabelRole)
        item = self.formLayout.itemAt(index, QtGui.QFormLayout.FieldRole)
        label.widget().deleteLater()
        item.widget().deleteLater()
        self.__campos[index - 4] = None
        
    def editarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QtGui.QFormLayout.LabelRole).widget()
        txtBox = self.formLayout.itemAt(index, QtGui.QFormLayout.FieldRole).widget()
        campo = self.__campos[index - 4]
        dialogo = NuevoCampo(NuevoCampo.actuacion, campo, self)
        if dialogo.exec_():
            label.setText("%s:" % campo.getNombre())
            if campo.getLongitudMax() is not 0:
                txtBox.setMaxLength(campo.getLongitudMax())
    
    def createAction(self, text, slot = None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action
        
    def addCampo(self, campo = None):
        if campo is not None:
            if campo in self.__campos:
                message = QtGui.QMessageBox()
                message.setIcon(QtGui.QMessageBox.Warning)
                message.setText("El campo ya se encuentra")
                message.exec_()
            else:
                label = QtGui.QLabel()
                label.setText("%s:" % campo.getNombre())
                txtBox = QtGui.QLineEdit()
                txtBox.setText(campo.getValor())
                if campo.getLongitudMax() is not 0:
                    txtBox.setMaxLength(campo.getLongitudMax())
                
                txtBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
                
                eliminar = self.createAction('Eliminar', self.borrarElemento)
                eliminar.setData(txtBox)
                editar = self.createAction("Editar", self.editarElemento)
                editar.setData(txtBox)
                
                txtBox.addActions([eliminar, editar])
                self.formLayout.addRow(label, txtBox)
                self.__campos.append(campo)
        else:
            dialogo = ListadoDialogo(ListadoDialogo.campoActuacion, self)
            if dialogo.exec_():
                campo = dialogo.getSelected()
                self.addCampo(campo)

import sys 

fecha = datetime(2012, 1, 1, 14, 15, 16, 0, None)
fechaProxima = datetime(2011, 2, 2, 15, 16, 17, 0, None)

juzgado = Juzgado(nombre = "Juzgado", ciudad = "Pereira", direccion = "calle", telefono = "3333333",tipo = "De familia")
actuacion = Actuacion(juzgado = juzgado,fecha = fecha,fechaProxima = fechaProxima,descripcion = "Actuación")
           
app = QtGui.QApplication(sys.argv)
form = NuevaActuacion(actuacion)
form.show()
app.exec_()
        