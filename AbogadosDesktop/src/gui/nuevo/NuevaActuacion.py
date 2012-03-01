# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: harold
'''

from PySide import QtGui, QtCore
from gui.nuevo.NuevaActuacionScreen import Ui_NuevaActuacion
from core.Actuacion import Actuacion
from gui.ver.VerJuzgado import VerJuzgado
from gui.ListadoDialogo import ListadoDialogo
from gui.nuevo.NuevoCampo import NuevoCampo
from datetime import datetime
from gui.nuevo.NuevoJuzgado import NuevoJuzgado
from gui.GestorCampos import GestorCampos
from persistence.Persistence import Persistence
from gui.DialogoAuxiliar import DialogoAuxiliar
from gui import Util

class NuevaActuacion(QtGui.QDialog, Ui_NuevaActuacion):
    '''
    classdocs
    '''
    def __init__(self, actuacion = None, parent = None):
        super(NuevaActuacion, self).__init__(parent)
        self.__dirty = False
        
        if actuacion is not None and not isinstance(actuacion, Actuacion):
            raise TypeError("El objeto actuacion debe ser de la clase Actuacion")
 
        self.setupUi(self)
        self.__actuacion = actuacion
        self.__juzgado = None
        campos = []
                
        if actuacion is not None:
            self.setWindowTitle(unicode("Editar actuación"))
            self.groupBox.setTitle(unicode("Datos de la actuación:"))
            self.__juzgado = actuacion.getJuzgado()
            campos = actuacion.getCampos()
            self.txtDescripcion.setText(unicode(actuacion.getDescripcion()))
            self.lblJuzgado.setText(unicode(self.__juzgado.getNombre()))
            self.dteFecha.setDateTime(actuacion.getFecha())
            self.dteFechaProxima.setDateTime(actuacion.getFechaProxima())
        else:
            self.dteFecha.setDateTime(datetime.today())
            self.dteFechaProxima.setDateTime(datetime.today())
            self.lblJuzgado.setText(unicode("vacío"))
            
        self.__dialogo = DialogoAuxiliar(self)
        
        self.clickJuzgado()
        self.clickFecha()
        self.clickFechaProxima()
        
        cambiar = self.createAction("Cambiar", self.cambiarJuzgado)
        cambiar.setData(self.lblJuzgado)
        editar = self.createAction("Editar", self.editarJuzgado)
        editar.setData(self.lblJuzgado)
        
        self.lblJuzgado.addActions([cambiar, editar])
        
        self.__gestor = GestorCampos(campos = campos, formLayout = self.formLayout, parent = self,
                                     constante_de_edicion = NuevoCampo.ACTUACION, constante_de_creacion = ListadoDialogo.CAMPOACTUACION)
        self.btnAdd.clicked.connect(self.__gestor.addCampo)
        
        self.txtDescripcion.textChanged.connect(self.setDirty)
        self.dteFecha.dateTimeChanged.connect(self.setDirty)
        self.dteFechaProxima.dateTimeChanged.connect(self.setDirty)
        
    def getActuacion(self):
        return self.__actuacion
    
    def createAction(self, text, slot = None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action 
    
    def cambiarJuzgado(self):
        listado = ListadoDialogo(ListadoDialogo.JUZGADO, self)
        if listado.exec_():
            self.__juzgado = listado.getSelected()
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            self.__dirty = True
    
    def editarJuzgado(self):
        if self.__juzgado is not None and self.__juzgado.getId_juzgado() is not "1":
            dialogo = NuevoJuzgado(self.__juzgado, self)
            if dialogo.exec_():
                self.lblJuzgado.setText(self.__juzgado.getNombre())
                if isinstance(self.horizontal.itemAt(1).widget(), VerJuzgado):
                    self.horizontal.itemAt(1).widget().deleteLater()
                    vista = VerJuzgado(self.__juzgado, self)
                    self.horizontal.addWidget(vista)
        
    def accept(self):
        if len(self.txtDescripcion.text()) is 0:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("La descripción se considera obligatoria")
            message.exec_()
            self.txtDescripcion.setFocus()
        elif self.__juzgado is None or self.__juzgado.getId_juzgado() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El juzgado no se permite vacío")
            message.exec_()
            self.txtDescripcion.setFocus()
        elif self.__gestor.organizarCampos():
            self.guardar()
            
    def guardar(self):
        fecha = self.dteFecha.dateTime().toPython()
        fechaProxima = self.dteFechaProxima.dateTime().toPython()
        descripcion = self.txtDescripcion.text()
        if self.__actuacion is None:
            self.__actuacion = Actuacion(juzgado = self.__juzgado, fecha = fecha,
                                         fechaProxima = fechaProxima, descripcion = descripcion,
                                         campos = self.__gestor.getCampos())
        else:
            if self.__actuacion.getId_actuacion() is not None:
                camposNuevos = self.__gestor.getCamposNuevos()
                camposEliminados = self.__gestor.getCamposEliminados()
                try:
                    p = Persistence()
                    for campo in camposEliminados:
                        p.borrarCampoActuacion(campo)
                    for campo in camposNuevos:
                        p.guardarCampoActuacion(campo, self.__actuacion.getId_actuacion())
                except Exception, e:
                    print "guardar actuación -> " % e.args
            self.__actuacion.setDescripcion(descripcion)
            self.__actuacion.setFecha(fecha)
            self.__actuacion.setFechaProxima(fechaProxima)
            self.__actuacion.setCampos(self.__gestor.getCampos())
            self.__actuacion.setJuzgado(self.__juzgado)
        return QtGui.QDialog.accept(self)
        
    def clickJuzgado(self):
        dialogo = self.__dialogo
        widget = self
        lblJuzgado = self.lblJuzgado
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__juzgado is not None and widget.__juzgado.getId_juzgado() is not "1":
                    vista = VerJuzgado(widget.__juzgado, widget)
                    dialogo.setWidget(vista)
                else:
                    widget.cambiarJuzgado()
            return QtGui.QLabel.mousePressEvent(lblJuzgado, self)
            
        self.lblJuzgado.mousePressEvent = mousePressEvent
    
    def clickFecha(self):
        dialogo = self.__dialogo 
        dteFecha = self.dteFecha
        
        def focusInEvent(self):     
            calendar = QtGui.QCalendarWidget()
            calendar.setSelectedDate(dteFecha.dateTime().date())
            dialogo.setWidget(calendar)  
            
            selectionChanged = lambda:dteFecha.setDate(calendar.selectedDate())           
            calendar.selectionChanged.connect(selectionChanged)
                  
            return QtGui.QDateTimeEdit.focusInEvent(dteFecha, self)
        
        def dateChanged(date):
            calendar = dialogo.getWidget()
            calendar.setSelectedDate(date)        
            
        dteFecha.focusInEvent = focusInEvent
        dteFecha.dateChanged.connect(dateChanged)
        
    
    def clickFechaProxima(self):
        dialogo = self.__dialogo
        dteFecha = self.dteFechaProxima
        
        def focusInEvent(self):     
            calendar = QtGui.QCalendarWidget()
            calendar.setSelectedDate(dteFecha.dateTime().date())
            dialogo.setWidget(calendar) 
            
            selectionChanged = lambda:dteFecha.setDate(calendar.selectedDate())           
            calendar.selectionChanged.connect(selectionChanged)
                 
            return QtGui.QDateTimeEdit.focusInEvent(dteFecha, self)
        
        def dateChanged(date):
            calendar = dialogo.getWidget()
            calendar.setSelectedDate(date)        
            
        dteFecha.focusInEvent = focusInEvent
        dteFecha.dateChanged.connect(dateChanged)
        
    def reject(self):
        Util.reject(self, self.__dirty)
        
    def setDirty(self):
        sender = self.sender()
        if isinstance(sender, QtGui.QLineEdit):
            self.__dirty = True
            self.disconnect(sender, QtCore.SIGNAL("textEdited()"), self.setDirty)
        elif isinstance(sender, QtGui.QDateTimeEdit):
            self.__dirty = True
            self.disconnect(sender, QtCore.SIGNAL("dateTimeChanged()"), self.setDirty)
