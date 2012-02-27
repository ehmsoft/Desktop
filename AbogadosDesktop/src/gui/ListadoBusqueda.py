'''
Created on 27/02/2012

@author: harold
'''
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from Listado import Listado
from persistence.Persistence import Persistence
from core.Proceso import Proceso

class ListadoBusqueda(QDialog):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.lista = QListWidget(self)
        self.txtBuscar = QLineEdit(self)
        self.listaOriginal = Persistence().consultarProcesos()
        self.listadoActual = self.listaOriginal
        self.lista.addItems(self.listaOriginal)
        self.texto = None
        self.txtBuscar.textChanged.connect(self.changed)
        
    def filtro(self, elemento):
        demandante = elemento.getDemandante().getNombre().lower()
        demandado = elemento.getDemandado().getNombre().lower()
        juzgado = elemento.getJuzgado().getNombre().lower()
        radicado = elemento.getRadicado().lower()
        radicadoUnido = elemento.getRadicadoUnico().lower()
        categoria = elemento.getCategoria().getNombre().lower()
        notas = elemento.getNotas().lower()
        
        keywords = [demandante,demandado,juzgado,radicado,radicadoUnido,categoria,notas]
        self.texto.lower()
        for key in keywords:
            if self.texto in key:
                return True
            
        return False
        
    def changed(self):
        self.texto = self.txtBuscar.text()
        self.listadoActual = filter(self.filtro, self.listaOriginal)
        self.montarLista()
        
    def montarLista(self):
        for x in range(0,len(self.listadoActual)):
            self.lista.itemAt(0)
        self.lista.addItems(self.listadoActual)
        
app = QApplication(sys.argv)