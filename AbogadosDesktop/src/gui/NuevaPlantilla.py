'''
Created on 14/02/2012

@author: harold
'''

from core.Plantilla import Plantilla
from NuevaPlantillaScreen import Ui_NuevaPlantilla
from PySide import QtCore, QtGui
from core.Categoria import Categoria
from GestorCampos import GestorCampos
from NuevoCampo import NuevoCampo
from ListadoDialogo import ListadoDialogo
from VerPersona import VerPersona
from VerJuzgado import VerJuzgado
from NuevaPersona import NuevaPersona
from NuevoJuzgado import NuevoJuzgado
from NuevaCategoria import NuevaCategoria
from persistence.Persistence import Persistence

class NuevaPlantilla(QtGui.QDialog, Ui_NuevaPlantilla):
    '''
    classdocs
    '''

    def __init__(self, plantilla = None, parent = None):
        '''
        Constructor
        '''
        super(NuevaPlantilla, self).__init__(parent)
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
                            
        self.clickDemandante()
        self.clickDemandado()
        self.clickJuzgado()
        self.clickCategoria()
        
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
        
        self.__gestor = GestorCampos(campos = campos, formLayout = self.formLayout, parent = self,
                                     constante_de_edicion = NuevoCampo.PROCESO, constante_de_creacion = ListadoDialogo.CAMPOPROCESOP)
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.__gestor.addCampo)
                
    def clickDemandante(self):
        container = self.horizontalLayout 
        widget = self
        lblDemandante = self.lblDemandante
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__demandante is not None and widget.__demandante.getId_persona() is not "1":
                    if container.count() > 1:
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
                    if container.count() > 1:
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
                    if container.count() > 1:
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
                
    def createAction(self, text, slot = None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action 
                
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
            self.guardar()
    
    def guardar(self):
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