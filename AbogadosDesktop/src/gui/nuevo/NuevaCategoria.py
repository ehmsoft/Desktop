# -*- coding: utf-8 -*-
'''
Created on 24/01/2012

@author: esteban
'''

from PySide.QtGui import QDialog, QMessageBox
from PySide.QtCore import SIGNAL
from NuevaCategoriaScreen import Ui_NuevaCategoria
from core.Categoria import Categoria
from persistence.Persistence import Persistence
from gui import Util
import sqlite3

class NuevaCategoria(QDialog, Ui_NuevaCategoria):
    def __init__(self, categoria=None, parent=None):
        super(NuevaCategoria, self).__init__(parent)
        self.__dirty = False
        self.__categoria = categoria
        self.setupUi(self)        
        if self.__categoria is not None:
            self.setWindowTitle(u"Editar categoría")
            self.groupBox.setTitle(u"Datos de la categoría:")
            self.txtCategoria.setText(self.__categoria.getDescripcion())
            
        self.txtCategoria.textChanged.connect(self.setDirty)
            
        
    def getCategoria(self):
        return self.__categoria
    
    def __guardar(self):
        guardar = True
        p = Persistence()
        if self.__categoria is None:
            categoria = Categoria()
            categoria.setDescripcion(self.txtCategoria.text())
            self.__categoria = categoria
        else:
            self.__categoria.setDescripcion(self.txtCategoria.text())
            guardar = False        
        try:
            if guardar:
                p.guardarCategoria(categoria)
            else:
                p.actualizarCategoria(self.__categoria)
        except sqlite3.IntegrityError:
            if guardar:
                self.__categoria = None
            QMessageBox.information(self, 'Error', 'El elemento ya existe')
        else:
            return QDialog.accept(self)

    
    def accept(self):
        if self.txtCategoria.text().__len__() == 0 :
            QMessageBox.warning(self, 'Campo obligatorio', u'La descripción se considera obligatoria')
            self.txtCategoria.setFocus()                 
        else:
            self.__guardar()
            
    def reject(self):
        Util.reject(self, self.__dirty)
        
    def setDirty(self):
        self.__dirty = True
        self.disconnect(self.txtCategoria, SIGNAL("textChanged()"), self.setDirty)
