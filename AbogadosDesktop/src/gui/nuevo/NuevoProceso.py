# -*- coding: utf-8 -*-
'''
Created on 7/02/2012

@author: harold
'''

from PySide import QtGui, QtCore
from core.Proceso import Proceso
from gui.nuevo.NuevoProcesoScreen import Ui_NuevoProceso
from copy import copy
from gui.ListadoDialogo import ListadoDialogo
from NuevoCampo import NuevoCampo
from persistence.Persistence import Persistence
from gui.ver.VerPersona import VerPersona
from gui.ver.VerJuzgado import VerJuzgado
from datetime import datetime
from NuevaPersona import NuevaPersona
from NuevoJuzgado import NuevoJuzgado
from NuevaCategoria import NuevaCategoria
from NuevaActuacion import NuevaActuacion
from gui.ver.VerActuacion import VerActuacion
from gui.GestorCampos import GestorCampos
from core.Categoria import Categoria
from gui.DialogoAuxiliar import DialogoAuxiliar
from core.Plantilla import Plantilla
from gui import Util

class NuevoProceso(QtGui.QDialog, Ui_NuevoProceso):
    '''
    classdocs
    '''


    def __init__(self, proceso=None, plantilla=None, parent=None):
        '''
        Constructor
        '''
        super(NuevoProceso, self).__init__(parent)
        self.__dirty = False
        self.setupUi(self)
        if proceso is not None and plantilla is not None:
            raise TypeError("Solo se puede enviar el argumento plantilla o proceso sólo")
        if proceso is not None and not isinstance(proceso, Proceso):
            raise TypeError("El objeto proceso debe pertenecer a la clase Proceso")
        if plantilla is not None and not isinstance(plantilla, Plantilla):
            raise TypeError("El objeto plantilla debe pertenecer a la clase Plantilla")
        if proceso is not None:
            self.groupBox.setTitle("Datos del proceso:")
            self.setWindowTitle("Editar proceso")
            
        self.__proceso = proceso
        self.connect(self.btnAdd_2, QtCore.SIGNAL("clicked()"), self.addActuacion)
        campos = []
        self.__actuaciones = []
        self.__demandante = None
        self.__demandado = None
        self.__juzgado = None
        self.__categoria = Categoria("Ninguna", "1")
        
        self.sbPrioridad.setRange(0, 10)        
        if self.__proceso is not None:
            self.__demandante = self.__proceso.getDemandante()
            self.__demandado = self.__proceso.getDemandado()
            self.__juzgado = self.__proceso.getJuzgado()
            self.__categoria = self.__proceso.getCategoria()
            campos = self.__proceso.getCampos()
            self.__actuaciones = copy(self.__proceso.getActuaciones())
            
            self.lblDemandante.setText(self.__demandante.getNombre())
            self.lblDemandado.setText(self.__demandado.getNombre())
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            self.lblCategoria.setText(self.__categoria.getDescripcion())
            self.txtRadicado.setText(self.__proceso.getRadicado())
            self.txtRadicadoUnico.setText(self.__proceso.getRadicadoUnico())
            self.txtTipo.setText(self.__proceso.getTipo())
            self.txtEstado.setText(self.__proceso.getEstado())
            self.sbPrioridad.setValue(self.__proceso.getPrioridad())
            self.dteFecha.setDateTime(self.__proceso.getFecha())
            self.txtNotas.setText(self.__proceso.getNotas())
        elif plantilla is not None:
            self.__demandante = plantilla.getDemandante()
            self.__demandado = plantilla.getDemandado()
            self.__juzgado = plantilla.getJuzgado()
            self.__categoria = plantilla.getCategoria()
            campos = plantilla.getCampos()
            
            self.lblDemandante.setText(self.__demandante.getNombre())
            self.lblDemandado.setText(self.__demandado.getNombre())
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            self.lblCategoria.setText(self.__categoria.getDescripcion())
            self.txtRadicado.setText(plantilla.getRadicado())
            self.txtRadicadoUnico.setText(plantilla.getRadicadoUnico())
            self.txtTipo.setText(plantilla.getTipo())
            self.txtEstado.setText(plantilla.getEstado())
            self.sbPrioridad.setValue(plantilla.getPrioridad())
            self.txtNotas.setText(plantilla.getNotas())
        else:
            self.dteFecha.setDateTime(datetime.today())
            
        self.cargarActuaciones()
        
        self.__dialogo = DialogoAuxiliar(self)
                
        self.__clickDemandante()
        self.__clickDemandado()
        self.__clickJuzgado()
        self.__clickCategoria()
        self.__clickFecha()
        
        cambiar = self.createAction("Cambiar", self.__cambiarJuzgado)
        cambiar.setData(self.lblJuzgado)
        editar = self.createAction("Editar", self.__editarJuzgado)
        editar.setData(self.lblJuzgado)
        
        self.lblJuzgado.addActions([cambiar, editar])
        
        cambiar = self.createAction("Cambiar", self.__cambiarDemandante)
        cambiar.setData(self.lblDemandante)
        editar = self.createAction("Editar", self.__editarDemandante)
        editar.setData(self.lblDemandante)
        
        self.lblDemandante.addActions([cambiar, editar])
        
        cambiar = self.createAction("Cambiar", self.__cambiarDemandado)
        cambiar.setData(self.lblDemandado)
        editar = self.createAction("Editar", self.__editarDemandado)
        editar.setData(self.lblDemandado)
        
        self.lblDemandado.addActions([cambiar, editar])
        
        cambiar = self.createAction("Cambiar", self.__cambiarCategoria)
        cambiar.setData(self.lblCategoria)
        editar = self.createAction("Editar", self.__editarCategoria)
        editar.setData(self.lblCategoria)
        
        self.lblCategoria.addActions([cambiar, editar])
        
        self.__gestor = GestorCampos(campos=campos, formLayout=self.formLayout, parent=self,
                                     constante_de_edicion=NuevoCampo.PROCESO, constante_de_creacion=ListadoDialogo.CAMPOPROCESOP)
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.__gestor.addCampo)
        self.txtRadicado.textChanged.connect(self.setDirty)
        self.txtRadicadoUnico.textChanged.connect(self.setDirty)
        self.txtTipo.textChanged.connect(self.setDirty)
        self.txtEstado.textChanged.connect(self.setDirty)
        self.sbPrioridad.valueChanged.connect(self.setDirty)
        self.dteFecha.dateTimeChanged.connect(self.setDirty)
                
    def __clickDemandante(self):
        dialogo = self.__dialogo
        widget = self
        lblDemandante = self.lblDemandante
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__demandante is not None and widget.__demandante.getId_persona() is not "1":
                    vista = VerPersona(widget.__demandante, widget)
                    dialogo.setWidget(vista)
                else:
                    widget.__cambiarDemandante()
            return QtGui.QLabel.mousePressEvent(lblDemandante, self)
            
        self.lblDemandante.mousePressEvent = mousePressEvent
    
    def __clickDemandado(self):
        dialogo = self.__dialogo 
        widget = self
        lblDemandado = self.lblDemandado
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__demandado is not None and widget.__demandado.getId_persona() is not "1":
                    vista = VerPersona(widget.__demandado, widget)
                    dialogo.setWidget(vista)
                else:
                    widget.__cambiarDemandado()
            return QtGui.QLabel.mousePressEvent(lblDemandado, self)
            
        self.lblDemandado.mousePressEvent = mousePressEvent
    
    def __clickJuzgado(self):
        dialogo = self.__dialogo 
        widget = self
        lblJuzgado = self.lblJuzgado
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__juzgado is not None and widget.__juzgado.getId_juzgado() is not "1":
                    vista = VerJuzgado(widget.__juzgado, widget)
                    dialogo.setWidget(vista)
                else:
                    widget.__cambiarJuzgado()
            return QtGui.QLabel.mousePressEvent(lblJuzgado, self)
            
        self.lblJuzgado.mousePressEvent = mousePressEvent
    
    def __clickCategoria(self):
        widget = self
        lblCategoria = self.lblCategoria
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                widget.__cambiarCategoria()
            return QtGui.QLabel.mousePressEvent(lblCategoria, self)
            
        self.lblCategoria.mousePressEvent = mousePressEvent
    
    def __clickFecha(self):
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
    
    def __cambiarDemandante(self):
        listado = ListadoDialogo(ListadoDialogo.DEMANDANTE, self)
        if listado.exec_():
            self.__demandante = listado.getSelected()
            self.lblDemandante.setText(self.__demandante.getNombre())
            vista = VerPersona(self.__demandante, self)
            self.__dialogo.setWidget(vista)
            self.__dirty = True
        del(listado)
    
    def __cambiarDemandado(self):
        listado = ListadoDialogo(ListadoDialogo.DEMANDADO, self)
        if listado.exec_():
            self.__demandado = listado.getSelected()
            self.lblDemandado.setText(self.__demandado.getNombre())
            vista = VerPersona(self.__demandado, self)
            self.__dialogo.setWidget(vista)
            self.__dirty = True
        del(listado)
    
    def __cambiarJuzgado(self):
        listado = ListadoDialogo(ListadoDialogo.JUZGADO, self)
        if listado.exec_():
            self.__juzgado = listado.getSelected()
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            vista = VerJuzgado(self.__juzgado, self)
            self.__dialogo.setWidget(vista)
            self.__dirty = True
        del(listado)
    
    def __cambiarCategoria(self):
        listado = ListadoDialogo(ListadoDialogo.CATEGORIA, self)
        if listado.exec_():
            self.__categoria = listado.getSelected()
            self.lblCategoria.setText(unicode(self.__categoria))
            self.__dirty = True
        del(listado)
            
    def __editarDemandante(self):
        if self.__demandante is not None and self.__demandante.getId_persona() is not "1":
            dialogo = NuevaPersona(persona=self.__demandante, parent=self)
            if dialogo.exec_():
                self.lblDemandante.setText(self.__demandante.getNombre())
                if (isinstance(self.__dialogo.getWidget(), VerPersona)):
                    vista = VerPersona(self.__demandante, self)
                    self.__dialogo.setWidget(vista)
            del(dialogo)
    
    def __editarDemandado(self):
        if self.__demandado is not None and self.__demandado.getId_persona() is not "1":
            dialogo = NuevaPersona(persona=self.__demandado, parent=self)
            if dialogo.exec_():
                self.lblDemandado.setText(self.__demandado.getNombre())
                if (isinstance(self.__dialogo.getWidget(), VerPersona)):
                    vista = VerPersona(self.__demandado, self)
                    self.__dialogo.setWidget(vista)
            del(dialogo)
    
    def __editarJuzgado(self):
        if self.__juzgado is not None and self.__juzgado.getId_juzgado() is not "1":
            dialogo = NuevoJuzgado(juzgado=self.__juzgado, parent=self)
            if dialogo.exec_():
                self.lblJuzgado.setText(self.__juzgado.getNombre())
                if (isinstance(self.__dialogo.getWidget(), VerJuzgado)):
                    vista = VerJuzgado(self.__juzgado, self)
                    self.__dialogo.setWidget(vista)
            del(dialogo)
    
    def __editarCategoria(self):
        if self.__categoria is not None and self.__categoria.getId_categoria() is not "1":
            dialogo = NuevaCategoria(self.__categoria, self)
            if dialogo.exec_():
                self.lblCategoria.setText(self.__categoria.getNombre())
            del(dialogo)
                
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
        elif self.__gestor.organizarCampos():
            self.__guardar()
    
    def __guardar(self):
        del(self.__dialogo)
        try:
            self.organizarActuaciones()
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
            campos = self.__gestor.getCampos()
            if self.__proceso is None:
                proceso = Proceso(demandante=demandante, demandado=demandado, fecha=fecha, juzgado=juzgado,
                                  radicado=radicado, radicadoUnico=radicadoUnico, actuaciones=actuaciones,
                                  estado=estado, categoria=categoria, tipo=tipo, notas=notas,
                                  prioridad=prioridad, campos=campos)
                p.guardarProceso(proceso)
                self.__proceso = proceso
            else:
                camposNuevos = self.__gestor.getCamposNuevos()
                camposEliminados = self.__gestor.getCamposEliminados()
                for campo in camposEliminados:
                    p.borrarCampoPersonalizado(campo)
                for campo in camposNuevos:
                    p.guardarCampoPersonalizado(campo, self.__proceso.getId_proceso())
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
                p.actualizarProceso(self.__proceso)
        except Exception, e:
            print "Guardar proceso -> %s con %s" % (e, e.args)
        finally:
            return QtGui.QDialog.accept(self)
                
    def getProceso(self):
        return self.__proceso
    
    def createAction(self, text, slot=None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action 
    
    def organizarActuaciones(self):
        if self.__proceso is not None:
            actuacionesOriginales = self.__proceso.getActuaciones()
            actuaciones = self.__actuaciones
            
            try:
                p = Persistence()
                for nuevaActuacion in actuaciones:
                    if nuevaActuacion not in actuacionesOriginales:
                        p.guardarActuacion(nuevaActuacion, self.__proceso.getId_proceso())
                for viejaActuacion in actuacionesOriginales:
                    if viejaActuacion not in actuaciones:
                        p.borrarActuacion(viejaActuacion)
            except Exception, e:
                print "organizarActuaciones -> %s" % e                    
                
    def editarActuacion(self):
        index = self.verticalLayout.indexOf(self.sender().data())
        dialogo = NuevaActuacion(actuacion=self.__actuaciones[index], parent=self)
        if dialogo.exec_():
            self.verticalLayout.itemAt(index).widget().deleteLater()
            vista = VerActuacion(dialogo.getActuacion(), self)
            self.verticalLayout.insertWidget(index, vista)
            if self.__proceso is not None:
                self.__dirty = True
        del(dialogo)
            
    
    def eliminarActuacion(self):
        index = self.verticalLayout.indexOf(self.sender().data())
        actuacion = self.__actuaciones[index]
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Question)
        message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        message.setDefaultButton(QtGui.QMessageBox.No)
        message.setText(u'¿Desea eliminar la actuación {0}?'.format(actuacion))
        ret = message.exec_()
        if ret == QtGui.QMessageBox.Yes:
            item = self.verticalLayout.takeAt(index)
            item.widget().deleteLater()            
            del(self.__actuaciones[index])
            self.verticalLayout.update()
            self.__dirty = True       
        del(message)         
                
    def cargarActuaciones(self):
        if len(self.__actuaciones) is not 0:
            for actuacion in self.__actuaciones:
                vista = VerActuacion(actuacion=actuacion, parent=self)
                vista.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
                editar = self.createAction("Editar", self.editarActuacion)
                editar.setData(vista)
                eliminar = self.createAction("Eliminar", self.eliminarActuacion)
                eliminar.setData(vista)
                vista.addActions([editar, eliminar])
                self.verticalLayout.addWidget(vista)
    
    def addActuacion(self, actuacion=None):
        if actuacion is None:
            dialogo = NuevaActuacion(parent=self)
            if dialogo.exec_():
                actuacion = dialogo.getActuacion()
                self.addActuacion(actuacion)
            del(dialogo)
        else:
            vista = VerActuacion(actuacion=actuacion, parent=self)
            vista.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
            editar = self.createAction("Editar", self.editarActuacion)
            editar.setData(vista)
            eliminar = self.createAction("Eliminar", self.eliminarActuacion)
            eliminar.setData(vista)
            vista.addActions([editar, eliminar])
            self.verticalLayout.addWidget(vista)
            self.__actuaciones.append(actuacion)
            self.__dirty = True
        
    def reject(self):
        Util.reject(self, self.__dirty)
            
    def setDirty(self):
        sender = self.sender()
        if isinstance(sender, QtGui.QLineEdit) or isinstance(sender, QtGui.QTextEdit):
            self.__dirty = True
            self.disconnect(sender, QtCore.SIGNAL("textChanged()"), self.setDirty)
        elif isinstance(sender, QtGui.QDateTimeEdit):
            self.__dirty = True
            self.disconnect(sender, QtCore.SIGNAL("dateTimeChanded()"), self.setDirty)
