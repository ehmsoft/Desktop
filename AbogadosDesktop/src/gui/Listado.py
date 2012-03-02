# -*- coding: utf-8 -*-
'''
Created on 19/01/2012

@author: esteban
'''
from PySide import QtGui
from ItemListas import ItemListas
from core.Persona import Persona
from core.Juzgado import Juzgado
from persistence.Persistence import Persistence


class Listado(QtGui.QListWidget):
    def __init__(self, listaObjetos = [], parent = None):
        super(Listado, self).__init__(parent)
        
    
        if listaObjetos is None or len(listaObjetos) is 0:
            listaObjetos = [] 
              
        elif isinstance(listaObjetos[0], Persona):            
            try:
                p = Persistence()
                vacio = p.consultarPersona("1", listaObjetos[0].getTipo())                
                listaObjetos.remove(vacio)
            except Exception, e:
                print e
        elif isinstance(listaObjetos[0], Juzgado):
            try:
                p = Persistence()
                vacio = p.consultarJuzgado("1")                
                listaObjetos.remove(vacio)
            except Exception, e:
                print e
        
        self.setMouseTracking(True)       
        self.addItems(listaObjetos)
        
    def addItems(self, items):                              
        for objeto in items:
            item = ItemListas(objeto)
            #item.setToolTip(unicode(objeto))
            #item.setStatusTip(unicode(objeto))
            self.addItem(item)
        
    def add(self, objeto):
        item = ItemListas(objeto)
        #item.setToolTip(unicode(objeto))
        #item.setStatusTip(unicode(objeto))
        self.addItem(item)
        
    def remove(self):        
        objeto = self.currentItem()
        pregunta = QtGui.QMessageBox.question(self, "Eliminar", "¿Desea eliminar %s?" % objeto.text(), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        pregunta.setDefaultButton(QtGui.QMessageBox.No)
        ret = pregunta.exec_()
        if ret == QtGui.QMessageBox.Yes:
            self.takeItem(self.currentRow())
            return True
        else:
            return False
            
    def replace(self, new):
        item = self.currentItem()
        item.setObjeto(new)
        
    def getSelectedItem(self):
        return self.currentItem().getObjeto()
