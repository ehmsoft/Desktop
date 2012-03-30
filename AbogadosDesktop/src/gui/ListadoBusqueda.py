# -*- coding: utf-8 -*-
'''
Created on 27/02/2012

@author: harold
'''
from PySide import QtGui, QtCore
from Listado import Listado
from core.Proceso import Proceso
from core.Plantilla import Plantilla
from core.Persona import Persona
from core.Juzgado import Juzgado
from core.Actuacion import Actuacion
from core.Categoria import Categoria
from core.CampoPersonalizado import CampoPersonalizado
import resources
from gui.ItemListas import ItemListas
from persistence.Persistence import Persistence

class ListadoBusqueda(Listado):
    '''
    classdocs
    '''

    def __init__(self, listado = [], parent = None):
        '''
        Constructor
        '''
        super(ListadoBusqueda, self).__init__(listado, parent)
        self.listaRespaldo = listado
        self.listaOriginal = listado
        self.listadoActual = self.listaOriginal
        if len(listado) != 0:
            if isinstance(listado[0], Proceso) or isinstance(listado[0], Plantilla):
                self.buscar= CampoBusqueda(self, combo=True)
            else:
                self.buscar = CampoBusqueda(self)
        else:
            self.buscar = CampoBusqueda(self)
        self.buscar.hide()
        self.texto = None
        self.buscar.getTextEdit().textChanged.connect(self.__changed)
        self.buscar.getButton().clicked.connect(self.__click)
        self.buscar.getCombo().currentIndexChanged.connect(self.__comboChanged)
        
    def __filtro(self, elemento, filtrarCategoria = False):
        for key in self.__getKeyWords(elemento, filtrarCategoria):
            if key is not None and self.texto in key.lower():
                return True
            
        return False
    
    def __getKeyWords(self, elemento, filtrarCategoria = False):
        if isinstance(elemento, Proceso):
            demandante = elemento.getDemandante().getNombre()
            demandado = elemento.getDemandado().getNombre()
            juzgado = elemento.getJuzgado().getNombre()
            radicado = elemento.getRadicado()
            radicadoUnido = elemento.getRadicadoUnico()
            categoria = elemento.getCategoria().getDescripcion()
            notas = elemento.getNotas()
            if filtrarCategoria:
                return [categoria]
            else:
                return [demandante, demandado, juzgado, radicado, radicadoUnido, categoria, notas]
        elif isinstance(elemento, Plantilla):
            demandante = elemento.getDemandante().getNombre()
            demandado = elemento.getDemandado().getNombre()
            juzgado = elemento.getJuzgado().getNombre()
            radicado = elemento.getRadicado()
            radicadoUnido = elemento.getRadicadoUnico()
            categoria = elemento.getCategoria().getDescripcion()
            notas = elemento.getNotas()
            if filtrarCategoria:
                return [categoria]
            else:
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
        self.listadoActual = [x for x  in self.listaOriginal if self.__filtro(x)]
        self.__montarLista()
        
    def __click(self):
        texto = self.buscar.getTextEdit().text()
        self.__changed(texto)
        
    def __comboChanged(self, index):
        itemtext = self.buscar.getCombo().itemText(index)
        if ( itemtext == 'Todas'):
            self.listaOriginal = self.listaRespaldo
            self.__click()
        else:
            self.texto=itemtext.lower()
            self.listaOriginal = [x for x  in self.listaRespaldo if self.__filtro(x, filtrarCategoria=True)]
            self.listadoActual = self.listaOriginal
            self.__click()

        
    def getSearchField(self):
        self.buscar.show()
        return self.buscar
        
    def __montarLista(self):
        while self.count() > 0:
            self.takeItem(0)
        self.addItems(self.listadoActual)
        if self.count():
            self.setCurrentRow(0)
        else:
            self.emit(QtCore.SIGNAL("listaCeros()"))
    
    def showSearchField(self):
        self.buscar.show()
        
        
    def add(self, objeto):
        Listado.add(self, objeto)
        self.listaOriginal.append(objeto)
        self.listaRespaldo.append(objeto)
        
    def remove(self):
        objeto = self.currentItem()
        if QtGui.QMessageBox.question(self,"Eliminar","Desea eliminar "+objeto.text()+" ?",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
            self.takeItem(self.currentRow())
            del self.listaOriginal[self.listaOriginal.index(objeto.getObjeto())]
            del self.listaRespaldo[self.listaRespaldo.index(objeto.getObjeto())]
            self.__click()
            return True
        else:
            return False
        
class CampoBusqueda(QtGui.QWidget):
    def __init__(self, parent = None, combo= False):
        '''
        Constructor
        '''
        super(CampoBusqueda, self).__init__(parent)
        iconoBuscar = QtGui.QIcon(':/images/iconoBuscar.png')
        buscar = QtGui.QHBoxLayout(self)
        self.txtBuscar = QtGui.QLineEdit(self)
        self.btnBuscar = QtGui.QPushButton()
        self.btnBuscar.setFlat(True)
        self.btnBuscar.setIcon(iconoBuscar)
        self.comboBuscar = QtGui.QComboBox()
        buscar.addWidget(self.txtBuscar)
        if combo:
            buscar.addWidget(self.comboBuscar)
            self.llenarCombo()
        else:
            buscar.addWidget(self.btnBuscar)
        self.setLayout(buscar)
        
    def getTextEdit(self):
        return self.txtBuscar
    
    def getButton(self):
        return self.btnBuscar
    
    def getCombo(self):
        return self.comboBuscar
    
    def llenarCombo(self):
        items = ['Todas']
        categorias = Persistence().consultarCategorias()
        items += [categoria.getDescripcion() for categoria in categorias]
        while(self.comboBuscar.count()):
            self.comboBuscar.removeItem(0)
        self.comboBuscar.addItems(items)
        self.comboBuscar.setCurrentIndex(0)
