# -*- coding: utf-8 -*-
'''
Created on 27/02/2012

@author: harold
'''
from PySide import QtGui
from Listado import Listado
from core.Proceso import Proceso
from core.Plantilla import Plantilla
from core.Persona import Persona
from core.Juzgado import Juzgado
from core.Actuacion import Actuacion
from core.Categoria import Categoria
from core.CampoPersonalizado import CampoPersonalizado
import resources

class ListadoBusqueda(Listado):
    '''
    classdocs
    '''

    def __init__(self, listado = [], parent = None):
        '''
        Constructor
        '''
        super(ListadoBusqueda, self).__init__(listado, parent)
        
        self.listaOriginal = listado
        self.listadoActual = self.listaOriginal
        self.buscar = CampoBusqueda()
        self.buscar.show()
                
        self.texto = None
        self.buscar.getTextEdit().textChanged.connect(self.__changed)
        self.buscar.getButton().clicked.connect(self.__click)
        
    def __filtro(self, elemento):
        for key in self.__getKeyWords(elemento):
            if key is not None and self.texto in key.lower():
                return True
            
        return False
    
    def __getKeyWords(self, elemento):
        if isinstance(elemento, Proceso):
            demandante = elemento.getDemandante().getNombre()
            demandado = elemento.getDemandado().getNombre()
            juzgado = elemento.getJuzgado().getNombre()
            radicado = elemento.getRadicado()
            radicadoUnido = elemento.getRadicadoUnico()
            categoria = elemento.getCategoria().getDescripcion()
            notas = elemento.getNotas()
            
            return [demandante, demandado, juzgado, radicado, radicadoUnido, categoria, notas]
        elif isinstance(elemento, Plantilla):
            demandante = elemento.getDemandante().getNombre()
            demandado = elemento.getDemandado().getNombre()
            juzgado = elemento.getJuzgado().getNombre()
            radicado = elemento.getRadicado()
            radicadoUnido = elemento.getRadicadoUnico()
            categoria = elemento.getCategoria().getDescripcion()
            notas = elemento.getNotas()
            
            return [demandante, demandado, juzgado, radicado, radicadoUnido, categoria, notas]
        elif isinstance(elemento, Persona):
            nombre = elemento.getNombre()
            telefono = elemento.getTelefono()
            cedula = elemento.getId()
            
            return [nombre, telefono, cedula]
        elif isinstance(elemento, Juzgado):
            nombre = elemento.getNombre()
            telefono = elemento.getTelefono()
            ciudad = elemento.getCiudad()
            tipo = elemento.getTipo()
            
            return [nombre, telefono, ciudad, tipo]
        elif isinstance(elemento, Actuacion):
            descripcion = elemento.getDescripcion()
            date = elemento.getFechaProxima().date()
            
            fechaProxima1 = '{:%d %m %Y}'.format(date)
            fechaProxima2 = '{:%d%m%Y}'.format(date)
            fechaProxima3 = '{:%d-%m-%Y}'.format(date)
            fechaProxima4 = '{:%d/%m/%Y}'.format(date)
            
            juzgado = elemento.getJuzgado().getNombre()
            
            return [descripcion, fechaProxima1, fechaProxima2, fechaProxima3, fechaProxima4, juzgado]
        elif isinstance(elemento, Categoria):
            return [elemento.getDescripcion()]
        elif isinstance(elemento, CampoPersonalizado):
            return [elemento.getNombre()]
        else: 
            return [unicode(elemento)]            
                
    def __changed(self, text):
        self.texto = text.lower()
        #self.listadoActual = filter(self.__filtro, self.listaOriginal)
        self.listadoActual = (x for x  in self.listaOriginal if self.__filtro(x))
        self.__montarLista()
        
    def __click(self):
        texto = self.buscar.getTextEdit().text()
        self.__changed(texto)
        
    def getSearchField(self):
        self.buscar.show()
        return self.buscar
        
    def __montarLista(self):
        while self.count() > 0:
            self.takeItem(0)
        self.addItems(self.listadoActual)
    
    def showSearchField(self):
        self.buscar.show()
        
class CampoBusqueda(QtGui.QWidget):
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(CampoBusqueda, self).__init__(parent)
        iconoBuscar = QtGui.QIcon(':/images/iconoBuscar.png')
        buscar = QtGui.QHBoxLayout(self)
        self.txtBuscar = QtGui.QLineEdit(self)
        self.btnBuscar = QtGui.QPushButton(self)
        self.btnBuscar.setFlat(True)
        self.btnBuscar.setIcon(iconoBuscar)
        buscar.addWidget(self.txtBuscar)
        buscar.addWidget(self.btnBuscar)
        
    def getTextEdit(self):
        return self.txtBuscar
    
    def getButton(self):
        return self.btnBuscar

import sys
from persistence.Persistence import Persistence

lista = Persistence().consultarProcesos()
app = QtGui.QApplication(sys.argv)
form = ListadoBusqueda(lista, None)
form.show()
form.getSearchField()
app.exec_()
