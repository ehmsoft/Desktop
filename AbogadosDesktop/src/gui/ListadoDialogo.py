# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
from persistence.Persistence import Persistence
from gui.ListadoBusqueda import ListadoBusqueda

        
class ListadoDialogo (QDialog):
    DEMANDANTE = 1
    DEMANDADO = 2
    JUZGADO = 3
    CATEGORIA = 4
    CAMPOPROCESOP = 5 # constante que indica el campo personalizado de procesos y plantillas
    CAMPOJUZGADO = 6
    CAMPOACTUACION = 7
    CAMPODEMANDANTE = 8
    CAMPODEMANDADO = 9
    PROCESO = 10
    PLANTILLA = 11
    
    def __init__(self, tipo, parent = None):
        super(ListadoDialogo, self).__init__(parent)
        
        self.__tipo = tipo
        self.__p = Persistence()
        self.__editado = []
        self.__eliminado = []
        self.__agregado = []
        if self.__tipo is self.__class__.DEMANDANTE:
            objetos = self.__p.consultarDemandantes()
            self.setWindowTitle('Seleccionar Demandante')
        elif self.__tipo is self.__class__.DEMANDADO:
            objetos = self.__p.consultarDemandados()
            self.setWindowTitle('Seleccionar Demandado')
        elif self.__tipo is self.__class__.JUZGADO:
            objetos = self.__p.consultarJuzgados()
            self.setWindowTitle('Seleccionar Juzgado')
        elif self.__tipo is self.__class__.CATEGORIA:
            objetos = self.__p.consultarCategorias()
            self.setWindowTitle('Seleccionar categoría')
        elif self.__tipo is self.__class__.CAMPOPROCESOP:
            objetos = self.__p.consultarAtributos()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is self.__class__.CAMPOJUZGADO:
            objetos = self.__p.consultarAtributosJuzgado()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is self.__class__.CAMPOACTUACION:
            objetos = self.__p.consultarAtributosActuacion()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is self.__class__.CAMPODEMANDANTE:
            objetos = self.__p.consultarAtributosPersona()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is self.__class__.CAMPODEMANDADO:
            objetos = self.__p.consultarAtributosPersona()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is self.__class__.PROCESO:
            objetos = self.__p.consultarProcesos()
            self.setWindowTitle('seleccione un proceso')
        elif self.__tipo is self.__class__.PLANTILLA:
            objetos = self.__p.consultarPlantillas()
            self.setWindowTitle('Seleccione una plantilla')
            
        groupBox = QGroupBox("Seleccione un elemento")           
        self.lista = ListadoBusqueda(objetos)
        btnAgregar = QPushButton('+')
        layout = QVBoxLayout()
        layoutBox = QVBoxLayout() 
        buttonlayout = QHBoxLayout()
        buttonlayout.addStretch()
        layout.addWidget(self.lista.getSearchField())
        layout.addWidget(self.lista)
        buttonlayout.addWidget(btnAgregar)
        groupBox.setLayout(layout)
        layoutBox.addWidget(groupBox)
        layoutBox.addLayout(buttonlayout)
        self.setLayout(layoutBox)
        self.lista.itemClicked.connect(self.click)
        self.connect(btnAgregar, SIGNAL("clicked()"), self.button)
        self.lista.setContextMenuPolicy(Qt.ActionsContextMenu)
        
        actionEliminar = self.__createAction("Eliminar", self.eliminar)
        actionAgregar = self.__createAction("Agregar", self.button)
        actionEditar = self.__createAction("Editar", self.editar)
        self.lista.addAction(actionEliminar)
        self.lista.addAction(actionAgregar)
        self.lista.addAction(actionEditar)
        
    def click(self, item):
        self.selected = item.getObjeto()
        self.accept()
        
    
    def getSelected(self):
        return self.selected
    
    def button(self):
        from gui.nuevo.NuevoJuzgado import NuevoJuzgado
        from gui.nuevo.NuevaPersona import NuevaPersona
        from gui.nuevo.NuevaCategoria import NuevaCategoria
        from gui.nuevo.NuevoCampo import NuevoCampo
        from gui.nuevo.NuevoProceso import NuevoProceso
        from gui.nuevo.NuevaPlantilla import NuevaPlantilla
        
        if self.__tipo is self.__class__.DEMANDANTE:
            nuevaPersona = NuevaPersona(tipo = 1 , parent = self)
            if nuevaPersona.exec_():
                demandante = nuevaPersona.getPersona()
                self.lista.add(demandante)
                self.__agregado.append(demandante)
        elif self.__tipo is self.__class__.DEMANDADO:
            nuevaPersona = NuevaPersona(tipo = 2, parent = self)
            if nuevaPersona.exec_():
                demandado = nuevaPersona.getPersona()
                self.lista.add(demandado)
                self.__agregado.append(demandado)
        elif self.__tipo is self.__class__.JUZGADO:
            nuevoJuzgado = NuevoJuzgado(parent = self)
            if nuevoJuzgado.exec_():
                juzgado = nuevoJuzgado.getJuzgado()
                self.lista.add(juzgado)
                self.__agregado.append(juzgado)
        elif self.__tipo is self.__class__.CATEGORIA:
            nuevaCategoria = NuevaCategoria(parent = self)
            if nuevaCategoria.exec_():
                categoria = nuevaCategoria.getCategoria()
                self.lista.add(categoria)
                self.__agregado.append(categoria)
        elif self.__tipo is self.__class__.CAMPODEMANDANTE:
            nuevoCampoDemandante = NuevoCampo(tipo = NuevoCampo.PERSONA, parent = self)
            if nuevoCampoDemandante.exec_():
                campoPersona = nuevoCampoDemandante.getCampo()
                self.lista.add(campoPersona)
                self.__agregado.append(campoPersona)
        elif self.__tipo is self.__class__.CAMPODEMANDADO:
            nuevoCampoDemandado = NuevoCampo(tipo = NuevoCampo.PERSONA, parent = self)
            if nuevoCampoDemandado.exec_():
                campoPersona = nuevoCampoDemandado.getCampo()
                self.lista.add(campoPersona)
                self.__agregado.append(campoPersona)        
        elif self.__tipo is self.__class__.CAMPOACTUACION:
            nuevoCampoActuacion = NuevoCampo(tipo = NuevoCampo.ACTUACION, parent = self)
            if nuevoCampoActuacion.exec_():
                campoActuacion = nuevoCampoActuacion.getCampo()
                self.lista.add(campoActuacion)
                self.__agregado.append(campoActuacion)
        elif self.__tipo is self.__class__.CAMPOPROCESOP:
            nuevoCampoPP = NuevoCampo(tipo = NuevoCampo.PROCESO, parent = self)
            if nuevoCampoPP.exec_():
                campoPP = nuevoCampoPP.getCampo()
                self.lista.add(campoPP)
                self.__agregado.append(campoPP)
        elif self.__tipo is self.__class__.CAMPOJUZGADO:
            nuevoCampoJuzgado = NuevoCampo(tipo = NuevoCampo.JUZGADO, parent = self)
            if nuevoCampoJuzgado.exec_():
                campoJuzgado = nuevoCampoJuzgado.getCampo()
                self.lista.add(campoJuzgado)
                self.__agregado.append(campoJuzgado)
        elif self.__tipo is self.__class__.PROCESO:
            nuevoProceso = NuevoProceso(parent=self)
            if nuevoProceso.exec_():
                proceso = nuevoProceso.getProceso()
                self.lista.add(proceso)
                self.__agregado.append(proceso)
        elif self.__tipo is self.__class__.PLANTILLA:
            nuevaPlantilla = NuevaPlantilla(parent=self)
            if nuevaPlantilla.exec_():
                plantilla = nuevaPlantilla.getPlantilla()
                self.lista.add(plantilla)
                self.__agregado.append(plantilla)
        
                
    
    
    def __createAction(self, text, slot = None, shortcut = None, icon = None, tip = None, checkable = False, signal = "triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon("./images/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action       
    
    def eliminar(self):
        objeto = self.lista.currentItem().getObjeto()
        if self.__tipo is self.__class__.DEMANDANTE:
            self.__p.borrarPersona(objeto)
            self.__eliminado.append(objeto)                    
        elif self.__tipo is self.__class__.DEMANDADO:
            self.__p.borrarPersona(objeto)
            self.__eliminado.append(objeto)             
        elif self.__tipo is self.__class__.JUZGADO:
            self.__p.borrarJuzgado(objeto)
            self.__eliminado.append(objeto)             
        elif self.__tipo is self.__class__.CATEGORIA:
            self.__p.borrarCategoria(objeto)
            self.__eliminado.append(objeto)             
        elif self.__tipo is self.__class__.CAMPODEMANDANTE:
            self.__p.borrarCampoDemandante(objeto)
            self.__eliminado.append(objeto)    
        elif self.__tipo is self.__class__.CAMPODEMANDADO:
            self.__p.borrarCampoDemandado(objeto)
            self.__eliminado.append(objeto) 
        elif self.__tipo is self.__class__.CAMPOACTUACION:
            self.__p.borrarCampoActuacion(objeto)
            self.__eliminado.append(objeto) 
        elif self.__tipo is self.__class__.CAMPOPROCESOP:
            self.__p.borrarCampoPersonalizado(objeto)
            self.__eliminado.append(objeto) 
        elif self.__tipo is self.__class__.CAMPOJUZGADO:
            self.__p.borrarCampoJuzgado(objeto)
            self.__eliminado.append(objeto)
        elif self.__tipo is self.__class__.PROCESO:
            self.__p.borrarProceso(objeto)
            self.__eliminado.append(objeto)
        elif self.__tipo is self.__class__.PLANTILLA:
            self.__p.borrarPlantilla(objeto)
            self.__eliminado.append(objeto) 
        self.lista.remove()
            
        
    def editar(self):
        from gui.nuevo.NuevoJuzgado import NuevoJuzgado
        from gui.nuevo.NuevaPersona import NuevaPersona
        from gui.nuevo.NuevaCategoria import NuevaCategoria
        from gui.nuevo.NuevoCampo import NuevoCampo
        from gui.nuevo.NuevoProceso import NuevoProceso
        from gui.nuevo.NuevaPlantilla import NuevaPlantilla
        if self.__tipo is self.__class__.DEMANDANTE:
            nuevaPersona = NuevaPersona(persona = self.lista.currentItem().getObjeto(), tipo = 1 , parent = self)
            if nuevaPersona.exec_():
                demandante = nuevaPersona.getPersona()
                self.lista.replace(demandante)
                self.__editado.append(demandante)
        elif self.__tipo is self.__class__.DEMANDADO:
            nuevaPersona = NuevaPersona(persona = self.lista.currentItem().getObjeto(), tipo = 2, parent = self)
            if nuevaPersona.exec_():
                demandado = nuevaPersona.getPersona()
                self.lista.replace(demandado)
                self.__editado.append(demandado)
        elif self.__tipo is self.__class__.JUZGADO:
            nuevoJuzgado = NuevoJuzgado(juzgado = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoJuzgado.exec_():
                juzgado = nuevoJuzgado.getJuzgado()
                self.lista.replace(juzgado)
                self.__editado.append(juzgado)
        elif self.__tipo is self.__class__.CATEGORIA:
            nuevaCategoria = NuevaCategoria(categoria = self.lista.currentItem().getObjeto(), parent = self)
            if nuevaCategoria.exec_():
                categoria = nuevaCategoria.getCategoria()
                self.lista.replace(categoria)
                self.__editado.append(categoria)
        elif self.__tipo is self.__class__.CAMPODEMANDANTE:
            nuevoCampoDemandante = NuevoCampo(tipo = NuevoCampo.PERSONA, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoDemandante.exec_():
                campoPersona = nuevoCampoDemandante.getCampo()
                self.lista.replace(campoPersona)
                self.__editado.append(campoPersona)
        elif self.__tipo is self.__class__.CAMPODEMANDADO:
            nuevoCampoDemandado = NuevoCampo(tipo = NuevoCampo.PERSONA, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoDemandado.exec_():
                campoPersona = nuevoCampoDemandado.getCampo()
                self.lista.replace(campoPersona)
                self.__editado.append(campoPersona)        
        elif self.__tipo is self.__class__.CAMPOACTUACION:
            nuevoCampoActuacion = NuevoCampo(tipo = NuevoCampo.ACTUACION, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoActuacion.exec_():
                campoActuacion = nuevoCampoActuacion.getCampo()
                self.lista.replace(campoActuacion)
                self.__editado.append(campoActuacion)
        elif self.__tipo is self.__class__.CAMPOPROCESOP:
            nuevoCampoPP = NuevoCampo(tipo = NuevoCampo.PROCESO, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoPP.exec_():
                campoPP = nuevoCampoPP.getCampo()
                self.lista.replace(campoPP)
                self.__editado.append(campoPP)
        elif self.__tipo is self.__class__.CAMPOJUZGADO:
            nuevoCampoJuzgado = NuevoCampo(tipo = NuevoCampo.JUZGADO, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoJuzgado.exec_():
                campoJuzgado = nuevoCampoJuzgado.getCampo()
                self.lista.replace(campoJuzgado)
                self.__editado.append(campoJuzgado)
        elif self.__tipo is self.__class__.PROCESO:
            nuevoProceso = NuevoProceso(proceso = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoProceso.exec_():
                proceso = nuevoProceso.getProceso()
                self.lista.replace(proceso)
                self.__editado.append(proceso)
        elif self.__tipo is self.__class__.PLANTILLA:
            nuevaPlantilla = NuevaPlantilla(pantilla = self.lista.currentItem().getObjeto(), parent = self)
            if nuevaPlantilla.exec_():
                plantilla = nuevaPlantilla.getProceso()
                self.lista.replace(plantilla)
                self.__editado.append(plantilla)

    def getEditados(self):
        return self.__editado
    def getEliminados(self):
        return self.__eliminado
    def getAgregados(self):
        return self.__agregado