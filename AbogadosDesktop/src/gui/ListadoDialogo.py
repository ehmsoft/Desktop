from PySide.QtCore import *
from PySide.QtGui import *
from persistence.Persistence import Persistence
from gui.Listado import Listado
import sys
from gui.ItemListas import ItemListas
from gui.NuevaPersona import NuevaPersona
from gui.NuevoJuzgado import NuevoJuzgado
from gui.NuevaCategoria import NuevaCategoria
from gui.NuevoCampo import NuevoCampo



        
class ListadoDialogo (QDialog):
    demandante = 1
    demandado = 2
    juzgado = 3
    categoria = 4
    campoProcesoPlantilla = 5
    campoJuzgado = 6
    campoActuacion = 7
    campoPersona = 8
    def __init__(self,tipo, parent=None):
        super(ListadoDialogo, self).__init__(parent)
        
        self.tipo = tipo
        self.__p = Persistence()
        
        
        if self.tipo is self.__class__.demandante:
            
            objetos= self.__p.consultarDemandantes()
            self.setWindowTitle('Seleccionar Demandante')
        elif self.tipo is self.__class__.demandado:
            objetos = self.__p.consultarDemandados()
            self.setWindowTitle('Seleccionar Demandado')
        elif self.tipo is self.__class__.juzgado:
            objetos = self.__p.consultarJuzgados()
            self.setWindowTitle('Seleccionar Juzgado')
        elif self.tipo is self.__class__.categoria:
            objetos = self.__p.consultarCategorias()
            self.setWindowTitle('Seleccionar categoria')
        elif self.tipo is self.__class__.campoProcesoPlantilla:
            objetos = self.__p.consultarAtributos()
            self.setWindowTitle('seleccione un campo')
        elif self.tipo is self.__class__.campoJuzgado:
            objetos = self.__p.consultarAtributosJuzgado()
            self.setWindowTitle('seleccione un campo')
        elif self.tipo is self.__class__.campoActuacion:
            objetos = self.__p.consultarAtributosActuacion()
            self.setWindowTitle('seleccione un campo')
        elif self.tipo is self.__class__.campoPersona:
            objetos = self.__p.consultarAtributosPersona()
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
        
        
    def click(self,item):
        self.selected = item.getObjeto()
        self.accept()
         
    def getSelected(self):
        return self.selected
    
    def button(self):
        if self.tipo is self.__class__.demandante:
            nuevaPersona = NuevaPersona(tipo = 1 ,parent = self)
            if nuevaPersona.exec_():
                demandante = nuevaPersona.getPersona()
                del(demandante[0])
                self.lista.add(demandante)
        elif self.tipo is self.__class__.demandado:
            nuevaPersona = NuevaPersona(tipo = 2, parent = self)
            if nuevaPersona.exec_():
                demandado =  nuevaPersona.getPersona()
                self.lista.add(demandado)
        elif self.tipo is self.__class__.juzgado:
            nuevoJuzgado = NuevoJuzgado(parent = self)
            if nuevoJuzgado.exec_():
                juzgado = nuevoJuzgado.getJuzgado()
                self.lista.add(juzgado)
        elif self.tipo is self.__class__.categoria:
            nuevaCategoria = NuevaCategoria(parent = self)
            if nuevaCategoria.exec_():
                categoria = nuevaCategoria.getCategoria()
                self.lista.add(categoria)
        elif self.tipo is self.__class__.campoPersona:
            nuevoCampoDemandante = NuevoCampo(tipo = NuevoCampo.persona, parent = self)
            if nuevoCampoDemandante.exec_():
                campoPersona = nuevoCampoDemandante.getCampo()
                self.lista.add(campoPersona)
        elif self.tipo is self.__class__.campoActuacion:
            nuevoCampoActuacion = NuevoCampo(tipo = NuevoCampo.actuacion, parent = self)
            if nuevoCampoActuacion.exec_():
                campoActuacion = nuevoCampoActuacion.getCampo()
                self.lista.add(campoActuacion)
        elif self.tipo is self.__class__.campoProcesoPlantilla:
            nuevoCampoPP = NuevoCampo(tipo = NuevoCampo.proceso, parent = self)
            if nuevoCampoPP.exec_():
                campoPP = nuevoCampoPP.getCampo()
                self.lista.add(campoPP)
        elif self.tipo is self.__class__.campoJuzgado:
            nuevoCampoJuzgado = NuevoCampo(tipo =  NuevoCampo.juzgado, parent = self)
            if nuevoCampoActuacion.exec_():
                campoJuzgado = nuevoCampoJuzgado.getCategoria()
                self.lista.add(campoJuzgado)
        
app = QApplication(sys.argv)  
form = ListadoDialogo(tipo = ListadoDialogo.demandante)
form.show()
app.exec_()
                    
            