# -*- coding: utf-8 -*-

'''
Created on 25/01/2012

@author: harold
'''

from PySide import QtGui, QtCore
from NuevoJuzgadoScreen import Ui_NuevoJuzgado
from core.Juzgado import Juzgado
from persistence.Persistence import Persistence
from gui.ListadoDialogo import ListadoDialogo
from NuevoCampo import NuevoCampo
from gui.GestorCampos import GestorCampos
from gui import Util
import sqlite3

class NuevoJuzgado(QtGui.QDialog, Ui_NuevoJuzgado):
    '''
    classdocs
    '''
    
    def __init__(self, juzgado=None, parent=None):
        '''
        Constructor
        '''
        super(NuevoJuzgado, self).__init__(parent)
        self.__dirty = False
        
        if juzgado is not None and not isinstance(juzgado, Juzgado):
            raise TypeError("El objeto juzgado debe ser de la clase Juzgado")
        
        self.__juzgado = juzgado
        self.setupUi(self)
        
        campos = []
                
        if self.__juzgado is not None:
            self.setWindowTitle(u"Editar juzgado")
            self.groupBox.setTitle(u"Datos del juzgado:")
            campos = juzgado.getCampos()
            self.txtNombre.setText(self.__juzgado.getNombre())
            self.txtDireccion.setText(self.__juzgado.getDireccion())
            self.txtCiudad.setText(self.__juzgado.getCiudad())
            self.txtTelefono.setText(self.__juzgado.getTelefono())
            self.txtTipo.setText(self.__juzgado.getTipo())
            
        self.__gestor = GestorCampos(campos=campos, formLayout=self.formLayout, parent=self,
                                     constante_de_edicion=NuevoCampo.JUZGADO, constante_de_creacion=ListadoDialogo.CAMPOJUZGADO)
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.__gestor.addCampo)
        
        self.txtNombre.textChanged.connect(self.setDirty)
        self.txtCiudad.textChanged.connect(self.setDirty)
        self.txtDireccion.textChanged.connect(self.setDirty) 
        self.txtTelefono.textChanged.connect(self.setDirty) 
        self.txtTipo.textChanged.connect(self.setDirty)
          
    def getJuzgado(self):
        return self.__juzgado
    
    def __guardar(self):
        guardar = True
        p = Persistence()
        nombre = self.txtNombre.text()
        direccion = self.txtDireccion.text()
        telefono = self.txtTelefono.text()
        ciudad = self.txtCiudad.text()
        tipo = self.txtTipo.text()
        campos = self.__gestor.getCampos()
        if not self.__juzgado:
            self.__juzgado = Juzgado(nombre=nombre, ciudad=ciudad, direccion=direccion, telefono=telefono, tipo=tipo, campos=campos)                
        else:
            camposNuevos = self.__gestor.getCamposNuevos()
            camposEliminados = self.__gestor.getCamposEliminados()
            for campo in camposEliminados:
                p.borrarCampoJuzgado(campo)
            for campo in camposNuevos:
                p.guardarCampoJuzgado(campo, self.__juzgado.getId_juzgado())
            self.__juzgado.setNombre(nombre)
            self.__juzgado.setDireccion(direccion)
            self.__juzgado.setCiudad(ciudad)
            self.__juzgado.setTelefono(telefono)
            self.__juzgado.setTipo(tipo)
            self.__juzgado.setCampos(campos)
            guardar = False                    
        try:
            if guardar:
                p.guardarJuzgado(self.__juzgado)
            else:
                p.actualizarJuzgado(self.__juzgado) 
        except sqlite3.IntegrityError:
            if guardar:
                self.__juzgado = None
            QtGui.QMessageBox.information(self, 'Error', 'El elemento ya existe')
        else:
            return QtGui.QDialog.accept(self)
            
    def accept(self):
        if self.txtNombre.text().__len__() == 0 or self.txtNombre.text() == " ":
            QtGui.QMessageBox.warning(self, 'Cambo obligatorio', 'El nombre se considera obligatorio')
            self.txtNombre.setFocus()
        elif not len(self.txtTelefono.text()):
            ret = QtGui.QMessageBox.question(self, 'Pregunta', u'¿Desea guardar sin agregar un teléfono?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if ret == QtGui.QMessageBox.No:
                self.txtTelefono.setFocus()
            elif self.__gestor.organizarCampos():
                self.__guardar()            
        elif self.__gestor.organizarCampos():
            self.__guardar()
            
    def reject(self):
        Util.reject(self, self.__dirty)
            
    def setDirty(self):
        self.__dirty = True
        self.disconnect(self.sender(), QtCore.SIGNAL("textEdited()"), self.setDirty)
