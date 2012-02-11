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
from gui.NuevoCampo import NuevoCampo
from gui.GestorCampos import GestorCampos


class NuevoJuzgado(QtGui.QDialog, Ui_NuevoJuzgado):
    '''
    classdocs
    '''
    
    def __init__(self, juzgado = None, parent = None):
        '''
        Constructor
        '''
        super(NuevoJuzgado, self).__init__(parent)
        
        if juzgado is not None and not isinstance(juzgado, Juzgado):
            raise TypeError("El objeto juzgado debe ser de la clase Juzgado")
        
        self.__juzgado = juzgado
        self.setupUi(self)
        
        campos = []
                
        if self.__juzgado is not None:
            campos = juzgado.getCampos()
            self.txtNombre.setText(self.__juzgado.getNombre())
            self.txtDireccion.setText(self.__juzgado.getDireccion())
            self.txtCiudad.setText(self.__juzgado.getCiudad())
            self.txtTelefono.setText(self.__juzgado.getTelefono())
            self.txtTipo.setText(self.__juzgado.getTipo())
            
        self.__gestor = GestorCampos(campos = campos, formLayout = self.formLayout, parent = self,
                                     constante_de_edicion = NuevoCampo.JUZGADO, constante_de_creacion = ListadoDialogo.CAMPOJUZGADO)
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.__gestor.addCampo)  
            
    def getJuzgado(self):
        return self.__juzgado
    
    def guardar(self):
        try:
            p = Persistence()
            if self.__juzgado is None:
                juzgado = Juzgado()
                juzgado.setNombre(self.txtNombre.text())
                juzgado.setDireccion(self.txtDireccion.text())
                juzgado.setCiudad(self.txtCiudad.text())
                juzgado.setTelefono(self.txtTelefono.text())
                juzgado.setTipo(self.txtTipo.text())
                juzgado.setCampos(self.__gestor.getCampos())
                
                p.guardarJuzgado(juzgado)
                self.__juzgado = juzgado
            else:
                camposNuevos = self.__gestor.getCamposNuevos()
                camposEliminados = self.__gestor.getCamposEliminados()
                for campo in camposEliminados:
                    p.borrarCampoJuzgado(campo)
                for campo in camposNuevos:
                    p.guardarCampoJuzgado(campo, self.__juzgado.getId_juzgado())
                self.__juzgado.setNombre(self.txtNombre.text())
                self.__juzgado.setDireccion(self.txtDireccion.text())
                self.__juzgado.setCiudad(self.txtCiudad.text())
                self.__juzgado.setTelefono(self.txtTelefono.text())
                self.__juzgado.setTipo(self.txtTipo.text())
                self.__juzgado.setCampos(self.__gestor.getCampos())
                p.actualizarJuzgado(self.__juzgado)                    
        except Exception, e:
            print e
        finally:
            return QtGui.QDialog.accept(self)
            
    def accept(self):
        if self.txtNombre.text().__len__() == 0 or self.txtNombre.text() == " ":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El nombre se considera obligatorio")
            message.exec_()
            self.txtNombre.setFocus()
        elif self.txtTelefono.text().__len__() == 0 or self.txtTelefono.text() == " ":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Question)
            message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            message.setDefaultButton(QtGui.QMessageBox.No)
            message.setText(unicode("¿Desea guardar sin agregar un teléfono?"))
            ret = message.exec_()
            if ret == QtGui.QMessageBox.Yes:
                self.guardar()
            else:
                self.txtTelefono.setFocus()            
        elif self.__gestor.organizarCampos():
            self.guardar()
