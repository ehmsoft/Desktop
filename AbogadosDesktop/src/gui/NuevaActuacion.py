# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: harold
'''

from PySide import QtGui, QtCore
from gui.NuevaActuacionScreen import Ui_NuevaActuacion
from persistence.Persistence import Persistence
from core.Actuacion import Actuacion
from gui.VerJuzgado import VerJuzgado
from gui.ListadoDialogo import ListadoDialogo
from gui.NuevoCampo import NuevoCampo
from datetime import datetime
from gui.NuevoJuzgado import NuevoJuzgado

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
        else:
            self.setWindowTitle(unicode("Editar actuación"))
            self.groupBox.setTitle(unicode("Editar los datos de la actuación:"))
            self.dteFecha.setDateTime(datetime.today())
            self.dteFechaProxima.setDateTime(datetime.today())
            self.lblJuzgado.setText(unicode("vacío"))
            
        if self.__campos is not None and self.__campos != []:
            for campo in self.__campos:
                self.addCampo(campo)
        
        self.clickJuzgado()
        self.clickFecha()
        self.clickFechaProxima()
        self.btnAdd.clicked.connect(self.addCampo)
        
        cambiar = self.createAction("Cambiar", self.cambiarJuzgado)
        cambiar.setData(self.lblJuzgado)
        editar = self.createAction("Editar", self.editarJuzgado)
        editar.setData(self.lblJuzgado)
        
        self.lblJuzgado.addActions([cambiar,editar])
        
    def cambiarJuzgado(self):
        listado = ListadoDialogo(ListadoDialogo.juzgado, self)
        if listado.exec_():
            self.__juzgado = listado.getSelected()
            self.lblJuzgado.setText(self.__juzgado.getNombre())
    
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
        elif self.__juzgado.getId_juzgado() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El juzgado no se permite vacío")
            message.exec_()
            self.txtDescripcion.setFocus()
        elif self.organizarCampos():
            self.guardar()
            
    def guardar(self):
        try:
            p = Persistence()
            fecha = self.dteFecha.dateTime()
            fechaProxima = self.dteFechaProxima.dateTime()
            descripcion = self.txtDescripcion.text()
            if self.__actuacion is None:
                self.__actuacion = Actuacion(juzgado = self.__juzgado, fecha = fecha, 
                                             fechaProxima = fechaProxima, descripcion = descripcion, 
                                             campos = self.__campos)
                p.guardarActuacion(self.__actuacion)
            else:
                self.__actuacion.setDescripcion(descripcion)
                self.__actuacion.setFecha(fecha)
                self.__actuacion.setFechaProxima(fechaProxima)
                self.__actuacion.setCampos(self.__campos)
                p.actualizarActuacion(self.__actuacion)
        except Exception, e:
            print e
        return QtGui.QDialog.accept(self)
        
    def clickJuzgado(self):
        container = self.horizontal  
        widget = self
        lblJuzgado = self.lblJuzgado
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__juzgado is not None and widget.__juzgado.getId_juzgado() is not "1":
                    if container.itemAt(1) is not None:
                        container.itemAt(1).widget().deleteLater()
                    if widget.__juzgado is not None and widget.__juzgado.getId_juzgado is not "1":
                        vista = VerJuzgado(widget.__juzgado, widget)
                        container.addWidget(vista)
                else:
                    widget.cambiarJuzgado()
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