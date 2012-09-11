# -*- coding: utf-8 -*-
'''
Created on 26/03/2012

@author: elfotografo007
'''
from PySide.QtCore import *
from PySide.QtGui import *
from persistence.Persistence import Persistence
from gui.ListadoBusqueda import ListadoBusqueda

        
class ListadoDialogoMultipleSeleccion(QDialog):
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
        super(ListadoDialogoMultipleSeleccion, self).__init__(parent)
        
        self.__tipo = tipo
        self.__p = Persistence()
        self.__editado = []
        self.__eliminado = []
        self.__agregado = []
        if self.__tipo is self.__class__.DEMANDANTE:
            objetos = self.__p.consultarDemandantes()
            self.setWindowTitle('Seleccionar Demandantes')
        elif self.__tipo is self.__class__.DEMANDADO:
            objetos = self.__p.consultarDemandados()
            self.setWindowTitle('Seleccionar Demandados')
        elif self.__tipo is self.__class__.JUZGADO:
            objetos = self.__p.consultarJuzgados()
            self.setWindowTitle('Seleccionar Juzgados')
        elif self.__tipo is self.__class__.CATEGORIA:
            objetos = self.__p.consultarCategorias()
            self.setWindowTitle(u'Seleccionar categorías')
        elif self.__tipo is self.__class__.CAMPOPROCESOP:
            objetos = self.__p.consultarAtributos()
            self.setWindowTitle('Seleccione campos')
        elif self.__tipo is self.__class__.CAMPOJUZGADO:
            objetos = self.__p.consultarAtributosJuzgado()
            self.setWindowTitle('Seleccione campos')
        elif self.__tipo is self.__class__.CAMPOACTUACION:
            objetos = self.__p.consultarAtributosActuacion()
            self.setWindowTitle('Seleccione campos')
        elif self.__tipo is self.__class__.CAMPODEMANDANTE:
            objetos = self.__p.consultarAtributosPersona()
            self.setWindowTitle('Seleccione campos')
        elif self.__tipo is self.__class__.CAMPODEMANDADO:
            objetos = self.__p.consultarAtributosPersona()
            self.setWindowTitle('Seleccione campos')
        elif self.__tipo is self.__class__.PROCESO:
            objetos = self.__p.consultarProcesos()
            self.setWindowTitle('Seleccione procesos')
        elif self.__tipo is self.__class__.PLANTILLA:
            objetos = self.__p.consultarPlantillas()
            self.setWindowTitle('Seleccione plantillas')
            
        groupBox = QGroupBox("Seleccione uno o varios elementos")           
        self.lista = ListadoBusqueda(objetos)
        self.lista.setSelectionMode(QListWidget.MultiSelection)
        layout = QVBoxLayout()
        layoutBox = QVBoxLayout()
        btnSelTodo = QPushButton("Seleccionar Todo")
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        buttonlayout = QHBoxLayout()
        buttonlayout.addStretch()
        layout.addWidget(self.lista.getSearchField())
        layout.addWidget(self.lista)
        buttonlayout.addWidget(btnSelTodo)
        buttonlayout.addWidget(self.buttonBox)
        groupBox.setLayout(layout)
        layoutBox.addWidget(groupBox)
        layoutBox.addLayout(buttonlayout)
        self.setLayout(layoutBox)
        self.connect(self.buttonBox, SIGNAL("accepted()"), self.accept)
        self.connect(self.buttonBox, SIGNAL("rejected()"), self.reject)
        self.connect(btnSelTodo, SIGNAL("clicked()"), self.selTodo)
    
    def selTodo(self):
        self.lista.selectAll()
        
    def getSelected(self):
        selected = self.lista.selectedItems()
        return [objeto.getObjeto() for objeto in selected]