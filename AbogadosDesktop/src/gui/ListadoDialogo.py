from PySide.QtCore import *
from PySide.QtGui import *
from persistence.Persistence import Persistence
from gui.Listado import Listado

        
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
    
    def __init__(self,tipo, parent=None):
        super(ListadoDialogo, self).__init__(parent)
        
        self.tipo = tipo
        self.p = Persistence()
        
        
        if self.tipo is self.__class__.DEMANDANTE:
            
            objetos= self.p.consultarDemandantes()
            self.setWindowTitle('Seleccionar Demandante')
        elif self.tipo is self.__class__.DEMANDADO:
            objetos = self.p.consultarDemandados()
            self.setWindowTitle('Seleccionar Demandado')
        elif self.tipo is self.__class__.JUZGADO:
            objetos = self.p.consultarJuzgados()
            self.setWindowTitle('Seleccionar Juzgado')
        elif self.tipo is self.__class__.CATEGORIA:
            objetos = self.p.consultarCategorias()
            self.setWindowTitle('Seleccionar categoria')
        elif self.tipo is self.__class__.CAMPOPROCESOP:
            objetos = self.p.consultarAtributos()
            self.setWindowTitle('seleccione un campo')
        elif self.tipo is self.__class__.CAMPOJUZGADO:
            objetos = self.p.consultarAtributosJuzgado()
            self.setWindowTitle('seleccione un campo')
        elif self.tipo is self.__class__.CAMPOACTUACION:
            objetos = self.p.consultarAtributosActuacion()
            self.setWindowTitle('seleccione un campo')
        elif self.tipo is self.__class__.CAMPODEMANDANTE:
            objetos = self.p.consultarAtributosPersona()
            self.setWindowTitle('seleccione un campo')
        elif self.tipo is self.__class__.CAMPODEMANDADO:
            objetos = self.p.consultarAtributosPersona()
            self.setWindowTitle('seleccione un campo')
                   
        self.lista = Listado(objetos)
        btnAgregar = QPushButton('+')
        layout = QVBoxLayout()
        buttonlayout = QHBoxLayout()
        buttonlayout.addStretch()
        layout.addWidget(self.lista)
        buttonlayout.addWidget(btnAgregar)
        layout.addLayout(buttonlayout)
        self.setLayout(layout)
        self.lista.itemClicked.connect(self.click)
        self.connect(btnAgregar,SIGNAL("clicked()"),self.button)
        self.lista.setContextMenuPolicy(Qt.ActionsContextMenu)
        
        actionEliminar = self.createAction("Eliminar", self.eliminar)
        actionAgregar = self.createAction("Agregar", self.button)
        actionEditar = self.createAction("Editar",self.editar)
        self.lista.addAction(actionEliminar)
        self.lista.addAction(actionAgregar)
        self.lista.addAction(actionEditar)
        
    def click(self,item):
        self.selected = item.getObjeto()
        self.accept()
    
    def getSelected(self):
        return self.selected
    
    def button(self):
        from gui.NuevoJuzgado import NuevoJuzgado
        from gui.NuevaPersona import NuevaPersona
        from gui.NuevaCategoria import NuevaCategoria
        from gui.NuevoCampo import NuevoCampo
        if self.tipo is self.__class__.DEMANDANTE:
            nuevaPersona = NuevaPersona(tipo = 1 ,parent = self)
            if nuevaPersona.exec_():
                demandante = nuevaPersona.getPersona()
                self.lista.add(demandante)
        elif self.tipo is self.__class__.DEMANDADO:
            nuevaPersona = NuevaPersona(tipo = 2, parent = self)
            if nuevaPersona.exec_():
                demandado =  nuevaPersona.getPersona()
                self.lista.add(demandado)
        elif self.tipo is self.__class__.JUZGADO:
            nuevoJuzgado = NuevoJuzgado(parent = self)
            if nuevoJuzgado.exec_():
                juzgado = nuevoJuzgado.getJuzgado()
                self.lista.add(juzgado)
        elif self.tipo is self.__class__.CATEGORIA:
            nuevaCategoria = NuevaCategoria(parent = self)
            if nuevaCategoria.exec_():
                categoria = nuevaCategoria.getCategoria()
                self.lista.add(categoria)
        elif self.tipo is self.__class__.CAMPODEMANDANTE:
            nuevoCampoDemandante = NuevoCampo(tipo = NuevoCampo.persona, parent = self)
            if nuevoCampoDemandante.exec_():
                campoPersona = nuevoCampoDemandante.getCampo()
                self.lista.add(campoPersona)
        elif self.tipo is self.__class__.CAMPODEMANDADO:
            nuevoCampoDemandado = NuevoCampo(tipo = NuevoCampo.persona, parent = self)
            if nuevoCampoDemandado.exec_():
                campoPersona = nuevoCampoDemandado.getCampo()
                self.lista.add(campoPersona)        
        elif self.tipo is self.__class__.CAMPOACTUACION:
            nuevoCampoActuacion = NuevoCampo(tipo = NuevoCampo.actuacion, parent = self)
            if nuevoCampoActuacion.exec_():
                campoActuacion = nuevoCampoActuacion.getCampo()
                self.lista.add(campoActuacion)
        elif self.tipo is self.__class__.CAMPOPROCESOP:
            nuevoCampoPP = NuevoCampo(tipo = NuevoCampo.proceso, parent = self)
            if nuevoCampoPP.exec_():
                campoPP = nuevoCampoPP.getCampo()
                self.lista.add(campoPP)
        elif self.tipo is self.__class__.CAMPOJUZGADO:
            nuevoCampoJuzgado = NuevoCampo(tipo =  NuevoCampo.juzgado, parent = self)
            if nuevoCampoJuzgado.exec_():
                campoJuzgado = nuevoCampoJuzgado.getCampo()
                self.lista.add(campoJuzgado)
    
    
    def createAction(self, text, slot= None, shortcut = None, icon = None, tip = None, checkable = False, signal = "triggered()"):
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
                     
        if self.tipo is self.__class__.DEMANDANTE:
            self.p.borrarPersona(self.lista.currentItem().getObjeto())                    
        elif self.tipo is self.__class__.DEMANDADO:
            self.p.borrarPersona(self.lista.currentItem().getObjeto())            
        elif self.tipo is self.__class__.JUZGADO:
            self.p.borrarJuzgado(self.lista.currentItem().getObjeto())            
        elif self.tipo is self.__class__.CATEGORIA:
            self.p.borrarCategoria(self.lista.currentItem().getObjeto())            
        elif self.tipo is self.__class__.CAMPODEMANDANTE:
            self.p.borrarCampoDemandante(self.lista.currentItem().getObjeto())   
        elif self.tipo is self.__class__.CAMPODEMANDADO:
            self.p.borrarCampoDemandado(self.lista.currentItem().getObjeto())
        elif self.tipo is self.__class__.CAMPOACTUACION:
            self.p.borrarCampoActuacion(self.lista.currentItem().getObjeto())
        elif self.tipo is self.__class__.CAMPOPROCESOP:
            self.p.borrarCampoPersonalizado(self.lista.currentItem().getObjeto())
        elif self.tipo is self.__class__.CAMPOJUZGADO:
            self.p.borrarCampoJuzgado(self.lista.currentItem().getObjeto())
        self.lista.remove()
            
        
    def editar(self):
        from gui.NuevoJuzgado import NuevoJuzgado
        from gui.NuevaPersona import NuevaPersona
        from gui.NuevaCategoria import NuevaCategoria
        from gui.NuevoCampo import NuevoCampo
        if self.tipo is self.__class__.DEMANDANTE:
            nuevaPersona = NuevaPersona(persona = self.lista.currentItem().getObjeto(), tipo = 1 ,parent = self)
            if nuevaPersona.exec_():
                demandante = nuevaPersona.getPersona()
                self.lista.replace(demandante)
        elif self.tipo is self.__class__.DEMANDADO:
            nuevaPersona = NuevaPersona(persona = self.lista.currentItem().getObjeto(), tipo = 2, parent = self)
            if nuevaPersona.exec_():
                demandado =  nuevaPersona.getPersona()
                self.lista.replace(demandado)
        elif self.tipo is self.__class__.JUZGADO:
            nuevoJuzgado = NuevoJuzgado(juzgado = self.lista.currentItem().getObjeto(), parent = self)
            if nuevoJuzgado.exec_():
                juzgado = nuevoJuzgado.getJuzgado()
                self.lista.replace(juzgado)
        elif self.tipo is self.__class__.CATEGORIA:
            nuevaCategoria = NuevaCategoria(categoria=self.lista.currentItem().getObjeto(),parent = self)
            if nuevaCategoria.exec_():
                categoria = nuevaCategoria.getCategoria()
                self.lista.replace(categoria)
        elif self.tipo is self.__class__.CAMPODEMANDANTE:
            nuevoCampoDemandante = NuevoCampo(tipo = NuevoCampo.persona,campo=self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoDemandante.exec_():
                campoPersona = nuevoCampoDemandante.getCampo()
                self.lista.replace(campoPersona)
        elif self.tipo is self.__class__.CAMPODEMANDADO:
            nuevoCampoDemandado = NuevoCampo(tipo = NuevoCampo.persona,campo=self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoDemandado.exec_():
                campoPersona = nuevoCampoDemandado.getCampo()
                self.lista.replace(campoPersona)        
        elif self.tipo is self.__class__.CAMPOACTUACION:
            nuevoCampoActuacion = NuevoCampo(tipo = NuevoCampo.actuacion,campo=self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoActuacion.exec_():
                campoActuacion = nuevoCampoActuacion.getCampo()
                self.lista.replace(campoActuacion)
        elif self.tipo is self.__class__.CAMPOPROCESOP:
            nuevoCampoPP = NuevoCampo(tipo = NuevoCampo.proceso,campo=self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoPP.exec_():
                campoPP = nuevoCampoPP.getCampo()
                self.lista.replace(campoPP)
        elif self.tipo is self.__class__.CAMPOJUZGADO:
            nuevoCampoJuzgado = NuevoCampo(tipo =  NuevoCampo.juzgado,campo=self.lista.currentItem().getObjeto(), parent = self)
            if nuevoCampoActuacion.exec_():
                campoJuzgado = nuevoCampoJuzgado.getCategoria()
                self.lista.replace(campoJuzgado)
                
