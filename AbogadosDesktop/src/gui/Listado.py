'''
Created on 19/01/2012

@author: esteban
'''
from PySide.QtCore import *
from PySide.QtGui import *
from ItemListas import ItemListas
from types import ListType
from core.Persona import Persona
from core.Juzgado import Juzgado
from persistence.Persistence import Persistence


class Listado(QListWidget):
    def __init__(self,listaObjetos = [],parent = None):
        super(Listado,self).__init__(parent)
        
    
        if listaObjetos is None or len(listaObjetos) is 0:
                listaObjetos = [] 
              
        elif isinstance(listaObjetos[0], Persona):
            
            try:
                p= Persistence()
                vacio = p.consultarPersona("1", listaObjetos[0].getTipo())                
                listaObjetos.remove(vacio)
            except Exception,e:
                print e
        elif isinstance(listaObjetos[0], Juzgado):
            try:
                p= Persistence()
                vacio = p.consultarJuzgado("1")                
                listaObjetos.remove(vacio)
            except Exception,e:
                print e
        
        self.setMouseTracking(True)       
        if isinstance(listaObjetos, ListType):
            self.__listaObjetos = listaObjetos
                                      
            for objeto in listaObjetos:
                item = ItemListas(objeto)
                item.setToolTip(unicode(objeto))
                item.setStatusTip(unicode(objeto))
                self.addItem(item)
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def add(self,objeto):
        item = ItemListas(objeto)
        item.setToolTip(unicode(objeto))
        item.setStatusTip(unicode(objeto))
        self.addItem(item)
        
    def remove(self):        
        objeto = self.currentItem()
        if QMessageBox.question(self,"Eliminar","Desea eliminar "+objeto.text()+" ?",QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            self.takeItem(self.currentRow())
            return True
        else:
            return False
            
    def replace(self,new):
        item = self.currentItem()
        item.setObjeto(new)
        
    def getSelectedItem(self):
        return self.currentItem().getObjeto()
        


