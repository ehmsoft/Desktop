# -*- coding: utf-8 -*-
'''
Created on 7/02/2012

@author: harold
'''

from PySide import QtGui, QtCore
from core.Proceso import Proceso
from gui.NuevoProcesoScreen import Ui_NuevoProceso
from copy import copy
from gui.ListadoDialogo import ListadoDialogo
from gui.NuevoCampo import NuevoCampo
from persistence.Persistence import Persistence
from gui.VerPersona import VerPersona
from gui.VerJuzgado import VerJuzgado
from datetime import datetime
from gui.NuevaPersona import NuevaPersona
from gui.NuevoJuzgado import NuevoJuzgado
from gui.NuevaCategoria import NuevaCategoria
from gui.NuevaActuacion import NuevaActuacion
from gui.VerActuacion import VerActuacion

class NuevoProceso(QtGui.QDialog, Ui_NuevoProceso):
    '''
    classdocs
    '''


    def __init__(self, proceso = None, parent = None):
        '''
        Constructor
        '''
        super(NuevoProceso, self).__init__(parent)
        if proceso is not None and not isinstance(proceso, Proceso):
            raise TypeError("El objeto proceso debe pertenecer a la clase Proceso")
        if proceso is not None:
            self.groupBox.setTitle("Datos del proceso:")
            self.setWindowTitle("Editar proceso")
            
        self.setupUi(self)
        self.__proceso = proceso
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.addCampo)
        self.connect(self.btnAdd_2, QtCore.SIGNAL("clicked()"), self.addActuacion)
        self.__campos = []
        self.__actuaciones = []
        self.__demandante = None
        self.__demandado = None
        self.__juzgado = None
        self.__categoria = None
        
        self.sbPrioridad.setRange(0, 10)        
        if self.__proceso is not None:
            self.__demandante = self.__proceso.getDemandante()
            self.__demandado = self.__proceso.getDemandado()
            self.__juzgado = self.__proceso.getJuzgado()
            self.__categoria = self.__proceso.getCategoria()
            self.__campos = copy(self.__proceso.getCampos())
            self.__actuaciones = copy(self.__proceso.getActuaciones())
            
            self.lblDemandante.setText(self.__demandante.getNombre())
            self.lblDemandado.setText(self.__demandado.getNombre())
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            self.lblCategoria.setText(self.__categoria.getNombre())
            self.txtRadicado.setText(self.__proceso.getRadicado())
            self.txtRadicadoUnico.setText(self.__proceso.getRadicadoUnico())
            self.txtTipo.setText(self.__proceso.getTipo())
            self.txtEstado.setText(self.__proceso.getEstado())
            self.sbPrioridad.setValue(self.__proceso.getPrioridad())
            self.dteFecha.setDateTime(self.__proceso.getFecha())
            self.txtNotas.setText(self.__proceso.getNotas())
        else:
            self.dteFecha.setDateTime(datetime.today())
            
        self.cargarCampos()
        self.cargarActuaciones()
                
        self.clickDemandante()
        self.clickDemandado()
        self.clickJuzgado()
        self.clickCategoria()
        self.clickFecha()
        
        cambiar = self.createAction("Cambiar", self.cambiarJuzgado)
        cambiar.setData(self.lblJuzgado)
        editar = self.createAction("Editar", self.editarJuzgado)
        editar.setData(self.lblJuzgado)
        
        self.lblJuzgado.addActions([cambiar, editar])
        
        cambiar = self.createAction("Cambiar", self.cambiarDemandante)
        cambiar.setData(self.lblDemandante)
        editar = self.createAction("Editar", self.editarDemandante)
        editar.setData(self.lblDemandante)
        
        self.lblDemandante.addActions([cambiar, editar])
        
        cambiar = self.createAction("Cambiar", self.cambiarDemandado)
        cambiar.setData(self.lblDemandado)
        editar = self.createAction("Editar", self.editarDemandado)
        editar.setData(self.lblDemandado)
        
        self.lblDemandado.addActions([cambiar, editar])
        
        cambiar = self.createAction("Cambiar", self.cambiarCategoria)
        cambiar.setData(self.lblCategoria)
        editar = self.createAction("Editar", self.editarCategoria)
        editar.setData(self.lblCategoria)
        
        self.lblCategoria.addActions([cambiar, editar])
                
    def clickDemandante(self):
        container = self.horizontalLayout 
        widget = self
        lblDemandante = self.lblDemandante
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__demandante is not None and widget.__demandante.getId_persona() is not "1":
                    if container.itemAt(1) is not None:
                        container.itemAt(1).widget().deleteLater()
                    vista = VerPersona(widget.__demandante, widget)
                    container.addWidget(vista)
                else:
                    widget.cambiarDemandante()
            return QtGui.QLabel.mousePressEvent(lblDemandante, self)
            
        self.lblDemandante.mousePressEvent = mousePressEvent
    
    def clickDemandado(self):
        container = self.horizontalLayout  
        widget = self
        lblDemandado = self.lblDemandado
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__demandado is not None and widget.__demandado.getId_persona() is not "1":
                    if container.itemAt(1) is not None:
                        container.itemAt(1).widget().deleteLater()
                    vista = VerPersona(widget.__demandado, widget)
                    container.addWidget(vista)
                else:
                    widget.cambiarDemandado()
            return QtGui.QLabel.mousePressEvent(lblDemandado, self)
            
        self.lblDemandado.mousePressEvent = mousePressEvent
    
    def clickJuzgado(self):
        container = self.horizontalLayout  
        widget = self
        lblJuzgado = self.lblJuzgado
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__juzgado is not None and widget.__juzgado.getId_juzgado() is not "1":
                    if container.itemAt(1) is not None:
                        container.itemAt(1).widget().deleteLater()
                    vista = VerJuzgado(widget.__juzgado, widget)
                    container.addWidget(vista)
                else:
                    widget.cambiarJuzgado()
            return QtGui.QLabel.mousePressEvent(lblJuzgado, self)
            
        self.lblJuzgado.mousePressEvent = mousePressEvent
    
    def clickCategoria(self):
        widget = self
        lblCategoria = self.lblCategoria
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                widget.cambiarCategoria()
            return QtGui.QLabel.mousePressEvent(lblCategoria, self)
            
        self.lblCategoria.mousePressEvent = mousePressEvent
    
    def clickFecha(self):
        container = self.horizontalLayout
        dteFecha = self.dteFecha
        
        def focusInEvent(self):
            if container.itemAt(1) is not None:
                container.itemAt(1).widget().deleteLater()       
            calendar = QtGui.QCalendarWidget()
            calendar.setSelectedDate(dteFecha.dateTime().date())
            container.addWidget(calendar)  
            
            selectionChanged = lambda:dteFecha.setDate(calendar.selectedDate())           
            calendar.selectionChanged.connect(selectionChanged)
                  
            return QtGui.QDateTimeEdit.focusInEvent(dteFecha, self)
        
        def dateChanged(date):
            calendar = container.itemAt(1).widget()
            calendar.setSelectedDate(date)        
            
        dteFecha.focusInEvent = focusInEvent
        dteFecha.dateChanged.connect(dateChanged)
    
    def cambiarDemandante(self):
        listado = ListadoDialogo(ListadoDialogo.DEMANDANTE, self)
        if listado.exec_():
            self.__demandante = listado.getSelected()
            self.lblDemandante.setText(self.__demandante.getNombre())
            if (self.horizontalLayout.count() < 2 or 
                isinstance(self.horizontalLayout.itemAt(1).widget(), VerPersona) or
                self.lblJuzgado.hasFocus()):
                if self.horizontalLayout.count() > 1:
                    self.horizontalLayout.itemAt(1).widget().deleteLater()
                vista = VerPersona(self.__demandante, self)
                self.horizontalLayout.addWidget(vista)
    
    def cambiarDemandado(self):
        listado = ListadoDialogo(ListadoDialogo.DEMANDADO, self)
        if listado.exec_():
            self.__demandado = listado.getSelected()
            self.lblDemandado.setText(self.__demandado.getNombre())
            if (self.horizontalLayout.count() < 2 or 
                isinstance(self.horizontalLayout.itemAt(1).widget(), VerPersona) or 
                self.lblDemandado.hasFocus()):
                if self.horizontalLayout.count() > 1:    
                    self.horizontalLayout.itemAt(1).widget().deleteLater()
                vista = VerPersona(self.__demandado, self)
                self.horizontalLayout.addWidget(vista)
    
    def cambiarJuzgado(self):
        listado = ListadoDialogo(ListadoDialogo.JUZGADO, self)
        if listado.exec_():
            self.__juzgado = listado.getSelected()
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            if (self.horizontalLayout.count() < 2 or 
                isinstance(self.horizontalLayout.itemAt(1).widget(), VerJuzgado) or 
                self.lblJuzgado.hasFocus()):
                if self.horizontalLayout.count() > 1:
                    self.horizontalLayout.itemAt(1).widget().deleteLater()
                vista = VerJuzgado(self.__juzgado, self)
                self.horizontalLayout.addWidget(vista)
    
    def cambiarCategoria(self):
        listado = ListadoDialogo(ListadoDialogo.CATEGORIA, self)
        if listado.exec_():
            self.__categoria = listado.getSelected()
            self.lblCategoria.setText(unicode(self.__categoria))
            
    def editarDemandante(self):
        if self.__demandante is not None and self.__demandante.getId_persona() is not "1":
            dialogo = NuevaPersona(persona = self.__demandante, parent = self)
            if dialogo.exec_():
                self.lblDemandante.setText(self.__demandante.getNombre())
                if (self.horizontalLayout.count() > 1 and 
                isinstance(self.horizontalLayout.itemAt(1).widget(), VerPersona)):
                    self.horizontalLayout.itemAt(1).widget().deleteLater()
                    vista = VerPersona(self.__demandante, self)
                    self.horizontalLayout.addWidget(vista)
    
    def editarDemandado(self):
        if self.__demandado is not None and self.__demandado.getId_persona() is not "1":
            dialogo = NuevaPersona(persona = self.__demandado, parent = self)
            if dialogo.exec_():
                self.lblDemandado.setText(self.__demandado.getNombre())
                if (self.horizontalLayout.count() > 1 and 
                isinstance(self.horizontalLayout.itemAt(1).widget(), VerPersona)):
                    self.horizontalLayout.itemAt(1).widget().deleteLater()
                    vista = VerPersona(self.__demandado, self)
                    self.horizontalLayout.addWidget(vista)
    
    def editarJuzgado(self):
        if self.__juzgado is not None and self.__juzgado.getId_juzgado() is not "1":
            dialogo = NuevoJuzgado(juzgado = self.__juzgado, parent = self)
            if dialogo.exec_():
                self.lblJuzgado.setText(self.__juzgado.getNombre())
                if (self.horizontalLayout.count() > 1 and 
                isinstance(self.horizontalLayout.itemAt(1).widget(), VerJuzgado)):
                    self.horizontalLayout.itemAt(1).widget().deleteLater()
                    vista = VerJuzgado(self.__juzgado, self)
                    self.horizontalLayout.addWidget(vista)
    
    def editarCategoria(self):
        if self.__categoria is not None and self.__categoria.getId_categoria() is not "1":
            dialogo = NuevaCategoria(self.__categoria, self)
            if dialogo.exec_():
                self.lblCategoria.setText(self.__categoria.getNombre())
                
    def accept(self):
        if self.__demandante is None or self.__demandante.getId_persona() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El demandante se considera obligatorio")
            message.exec_()
        elif self.__demandado is None or self.__demandado.getId_persona() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El demandado se considera obligatorio")
            message.exec_()
        elif self.__juzgado is None or self.__juzgado.getId_juzgado() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El juzgado se considera obligatorio")
            message.exec_()
        elif len(self.txtRadicado.text()) is 0:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El radicado se considera obligatorio")
            message.exec_()
            self.txtRadicado.setFocus()
        elif self.organizarCampos():
            self.guardar()
    
    def guardar(self):
        try:
            p = Persistence()
            demandante = self.__demandante
            demandado = self.__demandado
            fecha = self.dteFecha.dateTime().toPython()
            juzgado = self.__juzgado
            radicado = self.txtRadicado.text()
            radicadoUnico = self.txtRadicadoUnico.text()
            actuaciones = self.__actuaciones
            estado = self.txtEstado.text()
            categoria = self.__categoria
            tipo = self.txtTipo.text()
            notas = self.txtNotas.toPlainText()
            prioridad = self.sbPrioridad.value()
            campos = self.__campos
            if self.__proceso is None:
                proceso = Proceso(demandante = demandante, demandado = demandado, fecha = fecha, juzgado = juzgado,
                                  radicado = radicado, radicadoUnico = radicadoUnico, actuaciones = actuaciones,
                                  estado = estado, categoria = categoria, tipo = tipo, notas = notas,
                                  prioridad = prioridad, campos = campos)
                p.guardarProceso(proceso)
            else:
                actuacionesNuevas = self.actuacionesNuevas()
                if len(actuacionesNuevas) is not 0:
                    for actuacion in actuacionesNuevas:
                        p.guardarActuacion(actuacion, self.__proceso.getId_proceso())
                self.__proceso.setDemandante(demandante)
                self.__proceso.setDemandado(demandado)
                self.__proceso.setFecha(fecha)
                self.__proceso.setJuzgado(juzgado)
                self.__proceso.setRadicado(radicado)
                self.__proceso.setRadicadoUnico(radicadoUnico)
                self.__proceso.setActuaciones(actuaciones)
                self.__proceso.setEstado(estado)
                self.__proceso.setCategoria(categoria)
                self.__proceso.setTipo(tipo)
                self.__proceso.setNotas(notas)
                self.__proceso.setPrioridad(prioridad)
                self.__proceso.setCampos(campos)
                self.__p.actualizarProceso(proceso)
                p.actualizarProceso(self.__proceso)
        except Exception, e:
            print "Guardar proceso -> %s" % e
        finally:
            return QtGui.QDialog.accept(self)
                
    def getProceso(self):
        return self.__proceso
                
    def organizarCampos(self):
        count = 11
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
                    
        count = 11
        for campo in self.__campos:
            if campo is not None:
                item = self.formLayout.itemAt(count, QtGui.QFormLayout.FieldRole).widget()
                campo.setValor(item.text())
            count += 1
                        
        func = lambda x: x is not None and 1 or 0
        self.__campos = filter(func, self.__campos)
        
        if self.__proceso is not None:        
            camposObjeto = self.__persona.getCampos()
            
            for campoNuevo in self.__campos:
                if campoNuevo not in camposObjeto:
                    try:
                        p = Persistence()
                        p.guardarCampoPersonalizado(campoNuevo, self.__proceso.getId_proceso())
                    except Exception, e:
                        print e
            for campoViejo in camposObjeto:
                if campoViejo not in self.__campos:
                    try:
                        p = Persistence()
                        p.borrarCampoPersonalizado(campoViejo)
                    except Exception, e:
                        print e
            self.__persona.setCampos(self.__campos)
        return True
    
    def borrarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QtGui.QFormLayout.LabelRole)
        item = self.formLayout.itemAt(index, QtGui.QFormLayout.FieldRole)
        label.widget().deleteLater()
        item.widget().deleteLater()
        self.__campos[index - 11] = None
        
    def editarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QtGui.QFormLayout.LabelRole).widget()
        txtBox = self.formLayout.itemAt(index, QtGui.QFormLayout.FieldRole).widget()
        campo = self.__campos[index - 11]
        dialogo = NuevoCampo(NuevoCampo.PROCESO, campo, self)
        if dialogo.exec_():
            label.setText(unicode("%s:" % campo.getNombre()))
            if campo.getLongitudMax() is not 0:
                txtBox.setMaxLength(campo.getLongitudMax())
    
    def createAction(self, text, slot = None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action
    
    def cargarCampos(self):
        if len(self.__campos) is not 0:
            for campo in self.__campos:
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
                
    def addCampo(self):
        dialogo = ListadoDialogo(ListadoDialogo.CAMPOPROCESOP, self)                
        if dialogo.exec_():
            campo = dialogo.getSelected()
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
                
    def editarActuacion(self):
        index = self.verticalLayout.indexOf(self.sender().data())
        dialogo = NuevaActuacion(actuacion = self.__actuaciones[index], parent = self)
        if dialogo.exec_():
            vista = self.verticalLayout.itemAt(index).widget()
            vista.setActuacion(dialogo.getActuacion())
            
    
    def eliminarActuacion(self):
        index = self.verticalLayout.indexOf(self.sender().data())
        actuacion = self.__actuaciones[index]
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Question)
        message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        message.setDefaultButton(QtGui.QMessageBox.No)
        message.setText(unicode("¿Desea eliminar la actuación %s?" % unicode(actuacion)))
        ret = message.exec_()
        if ret == QtGui.QMessageBox.Yes:
            item = self.verticalLayout.takeAt(index)
            item.widget().deleteLater()            
            del(self.__actuaciones[index])
            self.verticalLayout.update()                
                
    def cargarActuaciones(self):
        if len(self.__actuaciones) is not 0:
            for actuacion in self.__actuaciones:
                vista = VerActuacion(actuacion = actuacion, parent = self)
                vista.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
                editar = self.createAction("Editar", self.editarActuacion)
                editar.setData(vista)
                eliminar = self.createAction("Eliminar", self.eliminarActuacion)
                eliminar.setData(vista)
                vista.addActions([editar, eliminar])
                self.verticalLayout.addWidget(vista)
                self.__actuaciones.append(actuacion)
    
    def addActuacion(self):
        dialogo = NuevaActuacion(parent = None)
        if dialogo.exec_():
            actuacion = dialogo.getActuacion()
            vista = VerActuacion(actuacion = actuacion, parent = self)
            vista.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
            editar = self.createAction("Editar", self.editarActuacion)
            editar.setData(vista)
            eliminar = self.createAction("Eliminar", self.eliminarActuacion)
            eliminar.setData(vista)
            vista.addActions([editar, eliminar])
            self.verticalLayout.addWidget(vista)
            self.__actuaciones.append(actuacion)
            
    def actuacionesNuevas(self):
        actuaciones = []
        if len(self.__actuaciones) is not 0:
            for actuacion in self.__actuaciones:
                if actuacion not in self.__proceso.getActuaciones():
                    actuaciones.append(actuacion)
        return actuaciones
                
import sys
app = QtGui.QApplication(sys.argv)
form = NuevoProceso(None, None)
form.show()
app.exec_()
