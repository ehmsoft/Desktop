# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from persistence.Persistence import Persistence
from gui.Listado import Listado

        
class ListadoDialogo (QtGui.QDialog):
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
        if self.__tipo is ListadoDialogo.DEMANDANTE:
            objetos = self.__p.consultarDemandantes()
            self.setWindowTitle('Seleccionar Demandante')
        elif self.__tipo is ListadoDialogo.DEMANDADO:
            objetos = self.__p.consultarDemandados()
            self.setWindowTitle('Seleccionar Demandado')
        elif self.__tipo is ListadoDialogo.JUZGADO:
            objetos = self.__p.consultarJuzgados()
            self.setWindowTitle('Seleccionar Juzgado')
        elif self.__tipo is ListadoDialogo.CATEGORIA:
            objetos = self.__p.consultarCategorias()
            self.setWindowTitle('Seleccionar categoría')
        elif self.__tipo is ListadoDialogo.CAMPOPROCESOP:
            objetos = self.__p.consultarAtributos()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is ListadoDialogo.CAMPOJUZGADO:
            objetos = self.__p.consultarAtributosJuzgado()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is ListadoDialogo.CAMPOACTUACION:
            objetos = self.__p.consultarAtributosActuacion()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is ListadoDialogo.CAMPODEMANDANTE:
            objetos = self.__p.consultarAtributosPersona()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is ListadoDialogo.CAMPODEMANDADO:
            objetos = self.__p.consultarAtributosPersona()
            self.setWindowTitle('Seleccione un campo')
        elif self.__tipo is ListadoDialogo.PROCESO:
            objetos = self.__p.consultarProcesos()
            self.setWindowTitle('seleccione un proceso')
        elif self.__tipo is ListadoDialogo.PLANTILLA:
            objetos = self.__p.consultarPlantillas()
            self.setWindowTitle('Seleccione una plantilla')
            
        groupBox = QtGui.QGroupBox("Seleccione un elemento")           
        self.lista = Listado(objetos)
        btnAgregar = QtGui.QPushButton('+')
        layout = QtGui.QVBoxLayout()
        layoutBox = QtGui.QVBoxLayout() 
        buttonlayout = QtGui.QHBoxLayout()
        buttonlayout.addStretch()
        layout.addWidget(self.lista)
        buttonlayout.addWidget(btnAgregar)
        groupBox.setLayout(layout)
        layoutBox.addWidget(groupBox)
        layoutBox.addLayout(buttonlayout)
        self.setLayout(layoutBox)
        self.lista.itemClicked.connect(self.click)
        self.connect(btnAgregar, QtCore.SIGNAL("clicked()"), self.button)
        self.lista.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        
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
        from nuevo.NuevoJuzgado import NuevoJuzgado
        from nuevo.NuevaPersona import NuevaPersona
        from nuevo.NuevaCategoria import NuevaCategoria
        from nuevo.NuevoCampo import NuevoCampo
        from nuevo.NuevoProceso import NuevoProceso
        from nuevo.NuevaPlantilla import NuevaPlantilla
        
        if self.__tipo is ListadoDialogo.DEMANDANTE or self.__tipo is ListadoDialogo.DEMANDADO:
            nuevaPersona = NuevaPersona(tipo = 1 , parent = self)
            if nuevaPersona.exec_():
                persona = nuevaPersona.getPersona()
                self.lista.add(persona)
                self.__agregado.append(persona)
            del(nuevaPersona)
        elif self.__tipo is ListadoDialogo.JUZGADO:
            nuevoJuzgado = NuevoJuzgado(parent = self)
            if nuevoJuzgado.exec_():
                juzgado = nuevoJuzgado.getJuzgado()
                self.lista.add(juzgado)
                self.__agregado.append(juzgado)
            del(nuevoJuzgado)
        elif self.__tipo is ListadoDialogo.CATEGORIA:
            nuevaCategoria = NuevaCategoria(parent = self)
            if nuevaCategoria.exec_():
                categoria = nuevaCategoria.getCategoria()
                self.lista.add(categoria)
                self.__agregado.append(categoria)
            del(nuevaCategoria)
        elif self.__tipo is ListadoDialogo.CAMPODEMANDANTE:
            nuevoCampoDemandante = NuevoCampo(tipo = NuevoCampo.PERSONA, parent = self)
            if nuevoCampoDemandante.exec_():
                campoPersona = nuevoCampoDemandante.getCampo()
                self.lista.add(campoPersona)
                self.__agregado.append(campoPersona)
            del(nuevoCampoDemandante)
        elif self.__tipo is ListadoDialogo.CAMPODEMANDADO:
            nuevoCampoDemandado = NuevoCampo(tipo = NuevoCampo.PERSONA, parent = self)
            if nuevoCampoDemandado.exec_():
                campoPersona = nuevoCampoDemandado.getCampo()
                self.lista.add(campoPersona)
                self.__agregado.append(campoPersona) 
            del(nuevoCampoDemandado)       
        elif self.__tipo is ListadoDialogo.CAMPOACTUACION:
            nuevoCampoActuacion = NuevoCampo(tipo = NuevoCampo.ACTUACION, parent = self)
            if nuevoCampoActuacion.exec_():
                campoActuacion = nuevoCampoActuacion.getCampo()
                self.lista.add(campoActuacion)
                self.__agregado.append(campoActuacion)
            del(nuevoCampoActuacion)
        elif self.__tipo is ListadoDialogo.CAMPOPROCESOP:
            nuevoCampoPP = NuevoCampo(tipo = NuevoCampo.PROCESO, parent = self)
            if nuevoCampoPP.exec_():
                campoPP = nuevoCampoPP.getCampo()
                self.lista.add(campoPP)
                self.__agregado.append(campoPP)
            del(nuevoCampoPP)
        elif self.__tipo is ListadoDialogo.CAMPOJUZGADO:
            nuevoCampoJuzgado = NuevoCampo(tipo = NuevoCampo.JUZGADO, parent = self)
            if nuevoCampoJuzgado.exec_():
                campoJuzgado = nuevoCampoJuzgado.getCampo()
                self.lista.add(campoJuzgado)
                self.__agregado.append(campoJuzgado)
            del(nuevoCampoJuzgado)
        elif self.__tipo is ListadoDialogo.PROCESO:
            nuevoProceso = NuevoProceso(parent=self)
            if nuevoProceso.exec_():
                proceso = nuevoProceso.getProceso()
                self.lista.add(proceso)
                self.__agregado.append(proceso)
            del(nuevoProceso)
        elif self.__tipo is ListadoDialogo.PLANTILLA:
            nuevaPlantilla = NuevaPlantilla(parent=self)
            if nuevaPlantilla.exec_():
                plantilla = nuevaPlantilla.getPlantilla()
                self.lista.add(plantilla)
                self.__agregado.append(plantilla)
            del(nuevaPlantilla)
        
                
    
    
    def __createAction(self, text, slot = None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action       
    
    def eliminar(self):
        objeto = self.lista.currentItem().getObjeto()
        if self.__tipo is ListadoDialogo.DEMANDANTE:
            self.__p.borrarPersona(objeto)
            self.__eliminado.append(objeto)                    
        elif self.__tipo is ListadoDialogo.DEMANDADO:
            self.__p.borrarPersona(objeto)
            self.__eliminado.append(objeto)             
        elif self.__tipo is ListadoDialogo.JUZGADO:
            self.__p.borrarJuzgado(objeto)
            self.__eliminado.append(objeto)             
        elif self.__tipo is ListadoDialogo.CATEGORIA:
            self.__p.borrarCategoria(objeto)
            self.__eliminado.append(objeto)             
        elif self.__tipo is ListadoDialogo.CAMPODEMANDANTE:
            self.__p.borrarCampoDemandante(objeto)
            self.__eliminado.append(objeto)    
        elif self.__tipo is ListadoDialogo.CAMPODEMANDADO:
            self.__p.borrarCampoDemandado(objeto)
            self.__eliminado.append(objeto) 
        elif self.__tipo is ListadoDialogo.CAMPOACTUACION:
            self.__p.borrarCampoActuacion(objeto)
            self.__eliminado.append(objeto) 
        elif self.__tipo is ListadoDialogo.CAMPOPROCESOP:
            self.__p.borrarCampoPersonalizado(objeto)
            self.__eliminado.append(objeto) 
        elif self.__tipo is ListadoDialogo.CAMPOJUZGADO:
            self.__p.borrarCampoJuzgado(objeto)
            self.__eliminado.append(objeto)
        elif self.__tipo is ListadoDialogo.PROCESO:
            self.__p.borrarProceso(objeto)
            self.__eliminado.append(objeto)
        elif self.__tipo is ListadoDialogo.PLANTILLA:
            self.__p.borrarPlantilla(objeto)
            self.__eliminado.append(objeto) 
        self.lista.remove()
            
        
    def editar(self):
        from nuevo.NuevoJuzgado import NuevoJuzgado
        from nuevo.NuevaPersona import NuevaPersona
        from nuevo.NuevaCategoria import NuevaCategoria
        from nuevo.NuevoCampo import NuevoCampo
        from nuevo.NuevoProceso import NuevoProceso
        from nuevo.NuevaPlantilla import NuevaPlantilla
        if self.__tipo is ListadoDialogo.DEMANDANTE or self.__tipo is ListadoDialogo.DEMANDADO:
            nuevaPersona = NuevaPersona(persona = self.lista.currentItem().getObjeto(), tipo = 1 , parent = self)
            if nuevaPersona.exec_():
                persona = nuevaPersona.getPersona()
                self.lista.replace(persona)
                self.__editado.append(persona)
            del(nuevaPersona)
        elif self.__tipo is ListadoDialogo.JUZGADO:
            nuevoJuzgado = NuevoJuzgado(juzgado = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoJuzgado.exec_():
                juzgado = nuevoJuzgado.getJuzgado()
                self.lista.replace(juzgado)
                self.__editado.append(juzgado)
            del(nuevoJuzgado)
        elif self.__tipo is ListadoDialogo.CATEGORIA:
            nuevaCategoria = NuevaCategoria(categoria = self.lista.currentItem().getObjeto(), parent = self)
            if nuevaCategoria.exec_():
                categoria = nuevaCategoria.getCategoria()
                self.lista.replace(categoria)
                self.__editado.append(categoria)
            del(nuevaCategoria)
        elif self.__tipo is ListadoDialogo.CAMPODEMANDANTE:
            nuevoCampoDemandante = NuevoCampo(tipo = NuevoCampo.PERSONA, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoDemandante.exec_():
                campoPersona = nuevoCampoDemandante.getCampo()
                self.lista.replace(campoPersona)
                self.__editado.append(campoPersona)
            del(nuevoCampoDemandante)
        elif self.__tipo is ListadoDialogo.CAMPODEMANDADO:
            nuevoCampoDemandado = NuevoCampo(tipo = NuevoCampo.PERSONA, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoDemandado.exec_():
                campoPersona = nuevoCampoDemandado.getCampo()
                self.lista.replace(campoPersona)
                self.__editado.append(campoPersona)     
            del(nuevoCampoDemandado)   
        elif self.__tipo is ListadoDialogo.CAMPOACTUACION:
            nuevoCampoActuacion = NuevoCampo(tipo = NuevoCampo.ACTUACION, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoActuacion.exec_():
                campoActuacion = nuevoCampoActuacion.getCampo()
                self.lista.replace(campoActuacion)
                self.__editado.append(campoActuacion)
            del(nuevoCampoActuacion)
        elif self.__tipo is ListadoDialogo.CAMPOPROCESOP:
            nuevoCampoPP = NuevoCampo(tipo = NuevoCampo.PROCESO, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoPP.exec_():
                campoPP = nuevoCampoPP.getCampo()
                self.lista.replace(campoPP)
                self.__editado.append(campoPP)
            del(nuevoCampoPP)
        elif self.__tipo is ListadoDialogo.CAMPOJUZGADO:
            nuevoCampoJuzgado = NuevoCampo(tipo = NuevoCampo.JUZGADO, campo = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoJuzgado.exec_():
                campoJuzgado = nuevoCampoJuzgado.getCampo()
                self.lista.replace(campoJuzgado)
                self.__editado.append(campoJuzgado)
            del(nuevoCampoJuzgado)
        elif self.__tipo is ListadoDialogo.PROCESO:
            nuevoProceso = NuevoProceso(proceso = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoProceso.exec_():
                proceso = nuevoProceso.getProceso()
                self.lista.replace(proceso)
                self.__editado.append(proceso)
            del(nuevoProceso)
        elif self.__tipo is ListadoDialogo.PLANTILLA:
            nuevaPlantilla = NuevaPlantilla(pantilla = self.lista.currentItem().getObjeto(), parent = self)
            if nuevaPlantilla.exec_():
                plantilla = nuevaPlantilla.getProceso()
                self.lista.replace(plantilla)
                self.__editado.append(plantilla)
            del(nuevaPlantilla)

    def getEditados(self):
        return self.__editado
    def getEliminados(self):
        return self.__eliminado
    def getAgregados(self):
        return self.__agregado