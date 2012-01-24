'''
Created on 19/01/2012

@author: esteban
'''
from PySide.QtCore import *
from PySide.QtGui import *
from ItemListas import ItemListas
from types import ListType

class Listado(QListWidget):
    def __init__(self,listaObjetos = [],parent = None):
        super(Listado,self).__init__(parent)
        
        if listaObjetos is None:
                listaObjetos = []        
        if isinstance(listaObjetos, ListType):
            self.__listaObjetos = listaObjetos
                                      
            for objeto in listaObjetos:
                item = ItemListas(objeto)
                self.addItem(item)
            self.itemClicked.connect(self.prueba)
        else:
            raise TypeError('Tipo de dato no admitido')
        
        
        
    def prueba(self,item):
        self.remove()
        
    def click(self,item):
        return item.getObjeto()
        
    def add(self,objeto):
        self.addItem(ItemListas(objeto))
        
    def remove(self):        
        objeto = self.currentItem()
        if QMessageBox.question(self,"Eliminar","Desea eliminar "+objeto.text()+" ?",QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            self.takeItem(self.currentRow())
            
    def replace(self,new):
        item = self.currentItem()
        item.setObjeto(new)
        


