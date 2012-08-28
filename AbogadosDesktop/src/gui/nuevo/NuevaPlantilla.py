# -*- coding: utf-8 -*-
'''
Created on 14/02/2012

@author: harold
'''

from core.Plantilla import Plantilla
from NuevaPlantillaScreen import Ui_NuevaPlantilla
from PySide import QtCore, QtGui
from core.Categoria import Categoria
from gui.GestorCampos import GestorCampos
from NuevoCampo import NuevoCampo
from gui.ListadoDialogo import ListadoDialogo
from gui.ver.VerPersona import VerPersona
from gui.ver.VerJuzgado import VerJuzgado
from NuevaPersona import NuevaPersona
from NuevoJuzgado import NuevoJuzgado
from NuevaCategoria import NuevaCategoria
from persistence.Persistence import Persistence
from gui.DialogoAuxiliar import DialogoAuxiliar
from gui import Util

class NuevaPlantilla(QtGui.QDialog, Ui_NuevaPlantilla):
    '''
    classdocs
    '''

    def __init__(self, plantilla = None, parent = None):
        '''
        Constructor
        '''
        super(NuevaPlantilla, self).__init__(parent)
        self.__dirty = False
        self.setupUi(self)
        if plantilla is not None and not isinstance(plantilla, Plantilla):
            raise TypeError("El objeto plantilla debe pertenecer a la clase Plantilla")
        if plantilla is not None:
            self.groupBox.setTitle("Datos de la plantilla:")
            self.setWindowTitle("Editar plantilla")
            
        self.__plantilla = plantilla
        campos = []
        self.__demandante = None
        self.__demandado = None
        self.__juzgado = None
        self.__categoria = Categoria("Ninguna", "1")
        
        self.sbPrioridad.setRange(0, 10)        
        if self.__plantilla is not None:
            self.__demandante = self.__plantilla.getDemandante()
            self.__demandado = self.__plantilla.getDemandado()
            self.__juzgado = self.__plantilla.getJuzgado()
            self.__categoria = self.__plantilla.getCategoria()
            campos = self.__plantilla.getCampos()
            
            self.txtNombre.setText(self.__plantilla.getNombre())
            self.lblDemandante.setText(self.__demandante.getNombre())
            self.lblDemandado.setText(self.__demandado.getNombre())
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            self.lblCategoria.setText(self.__categoria.getDescripcion())
            self.txtRadicado.setText(self.__plantilla.getRadicado())
            self.txtRadicadoUnico.setText(self.__plantilla.getRadicadoUnico())
            self.txtTipo.setText(self.__plantilla.getTipo())
            self.txtEstado.setText(self.__plantilla.getEstado())
            self.sbPrioridad.setValue(self.__plantilla.getPrioridad())
            self.txtNotas.setText(self.__plantilla.getNotas())
            
        self.__dialogo = DialogoAuxiliar(self)
                            
        self.__clickDemandante()
        self.__clickDemandado()
        self.__clickJuzgado()
        self.__clickCategoria()
        
        cambiar = self.__createAction("Cambiar", self.__cambiarJuzgado)
        cambiar.setData(self.lblJuzgado)
        editar = self.__createAction("Editar", self.__editarJuzgado)
        editar.setData(self.lblJuzgado)
        
        self.lblJuzgado.addActions([cambiar, editar])
        
        cambiar = self.__createAction("Cambiar", self.__cambiarDemandante)
        cambiar.setData(self.lblDemandante)
        editar = self.__createAction("Editar", self.__editarDemandante)
        editar.setData(self.lblDemandante)
        
        self.lblDemandante.addActions([cambiar, editar])
        
        cambiar = self.__createAction("Cambiar", self.__cambiarDemandado)
        cambiar.setData(self.lblDemandado)
        editar = self.__createAction("Editar", self.__editarDemandado)
        editar.setData(self.lblDemandado)
        
        self.lblDemandado.addActions([cambiar, editar])
        
        cambiar = self.__createAction("Cambiar", self.__cambiarCategoria)
        cambiar.setData(self.lblCategoria)
        editar = self.__createAction("Editar", self.__editarCategoria)
        editar.setData(self.lblCategoria)
        
        self.lblCategoria.addActions([cambiar, editar])
        
        self.__gestor = GestorCampos(campos = campos, formLayout = self.formLayout, parent = self,
                                     constante_de_edicion = NuevoCampo.PROCESO, constante_de_creacion = ListadoDialogo.CAMPOPROCESOP)
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.__gestor.addCampo)
        
        self.txtRadicado.textChanged.connect(self.setDirty)
        self.txtRadicadoUnico.textChanged.connect(self.setDirty)
        self.txtTipo.textChanged.connect(self.setDirty)
        self.txtEstado.textChanged.connect(self.setDirty)
        self.sbPrioridad.valueChanged.connect(self.setDirty)
        self.txtNombre.textChanged.connect(self.setDirty)
                
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
            dialogo = NuevaPersona(persona = self.__demandante, parent = self)
            if dialogo.exec_():
                self.lblDemandante.setText(self.__demandante.getNombre())
                if (isinstance(self.__dialogo.getWidget(), VerPersona)):
                    vista = VerPersona(self.__demandante, self)
                    self.__dialogo.setWidget(vista)
            del(dialogo)
    
    def __editarDemandado(self):
        if self.__demandado is not None and self.__demandado.getId_persona() is not "1":
            dialogo = NuevaPersona(persona = self.__demandado, parent = self)
            if dialogo.exec_():
                self.lblDemandado.setText(self.__demandado.getNombre())
                if (isinstance(self.__dialogo.getWidget(), VerPersona)):
                    vista = VerPersona(self.__demandado, self)
                    self.__dialogo.setWidget(vista)
            del(dialogo)
    
    def __editarJuzgado(self):
        if self.__juzgado is not None and self.__juzgado.getId_juzgado() is not "1":
            dialogo = NuevoJuzgado(juzgado = self.__juzgado, parent = self)
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
                
    def __createAction(self, text, slot = None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action 
                
    def accept(self):
        if len(self.txtNombre.text()):
            self.__gestor.organizarCampos(False)
            self.__guardar()
        else:
            QtGui.QMessageBox.information(self, 'Error', u'No se permite el nombre vacío')
            self.txtNombre.setFocus()
    
    def __guardar(self):
        del(self.__dialogo)
        try:
            p = Persistence()
            nombre = self.txtNombre.text()
            demandante = self.__demandante
            demandado = self.__demandado
            juzgado = self.__juzgado
            radicado = self.txtRadicado.text()
            radicadoUnico = self.txtRadicadoUnico.text()
            estado = self.txtEstado.text()
            categoria = self.__categoria
            tipo = self.txtTipo.text()
            notas = self.txtNotas.toPlainText()
            prioridad = self.sbPrioridad.value()
            campos = self.__gestor.getCampos()
            if self.__plantilla is None:
                plantilla = Plantilla(nombre = nombre, demandante = demandante, demandado = demandado,
                                      juzgado = juzgado, radicado = radicado, radicadoUnico = radicadoUnico,
                                      estado = estado, categoria = categoria, tipo = tipo, notas = notas,
                                      campos = campos, prioridad = prioridad)
                p.guardarPlantilla(plantilla)
                self.__plantilla = plantilla
            else:
                camposNuevos = self.__gestor.getCamposNuevos()
                camposEliminados = self.__gestor.getCamposEliminados()
                for campo in camposEliminados:
                    p.borrarCampoPersonalizado(campo)
                for campo in camposNuevos:
                    p.guardarCampoPersonalizado(campo, self.__plantilla.getId_proceso())
                self.__plantilla.setNombre(nombre)
                self.__plantilla.setDemandante(demandante)
                self.__plantilla.setDemandado(demandado)
                self.__plantilla.setJuzgado(juzgado)
                self.__plantilla.setRadicado(radicado)
                self.__plantilla.setRadicadoUnico(radicadoUnico)
                self.__plantilla.setEstado(estado)
                self.__plantilla.setCategoria(categoria)
                self.__plantilla.setTipo(tipo)
                self.__plantilla.setNotas(notas)
                self.__plantilla.setPrioridad(prioridad)
                self.__plantilla.setCampos(campos)
                p.actualizarPlantilla(self.__plantilla)
        except Exception, e:
            print "Guardar plantilla -> %s con %s" % (e, e.args)
        finally:
            return QtGui.QDialog.accept(self)
                
    def getPlantilla(self):
        return self.__plantilla
    
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