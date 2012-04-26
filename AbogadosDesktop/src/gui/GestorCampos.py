# -*- coding: utf-8 -*-
'''
Created on 10/02/2012

@author: harold
'''
from PySide import QtGui, QtCore
from nuevo.NuevoCampo import NuevoCampo
from copy import copy
from gui.ListadoDialogo import ListadoDialogo

class GestorCampos(object):
    '''
    classdocs
    '''


    def __init__(self, campos, formLayout, parent, constante_de_edicion, constante_de_creacion):
        '''
        Constructor
        '''
        self.__count = formLayout.rowCount()
        self.__campos = copy(campos)
        self.__camposOriginales = copy(campos)
        self.__formLayout = formLayout
        self.__parent = parent
        self.__constanteEdicion = constante_de_edicion
        self.__constanteCreacion = constante_de_creacion
        self.__camposNuevos = []
        self.__camposEliminados = []
        
        self.__cargarCampos()
        
    def getCampos(self):
        return self.__campos
    
    def getCamposNuevos(self):
        return self.__camposNuevos
    
    def getCamposEliminados(self):
        return self.__camposEliminados
    
    def __filtro(self, campo):
        if campo is None:
            return False
        else:
            return True        
        
    def organizarCampos(self, validar=True):
        count = self.__count
        for campo in self.__campos:
            if campo is not None:
                item = self.__formLayout.itemAt(count + self.__campos.index(campo), QtGui.QFormLayout.FieldRole).widget()
                
                message = QtGui.QMessageBox()
                message.setIcon(QtGui.QMessageBox.Warning)
                
                if validar and campo.isObligatorio() and len(item.text()) is 0:
                    message.setText("El campo %s es obligatorio" % campo.getNombre())
                    message.exec_()
                    item.setFocus()
                    return False
                elif validar and campo.getLongitudMax() is not 0 and len(item.text()) > campo.getLongitudMax():
                    message.setText(u'La longitud máxima del campo {0} es de {1} caracteres'.format(campo.getNombre(), campo.getLongitudMax()))
                    message.exec_()
                    return False
                    item.setFocus()
                elif validar and campo.getLongitudMin() is not 0 and len(item.text()) < campo.getLongitudMin():
                    message.setText(u'La longitud mínima del campo {0} es de {1} caracteres'.format(campo.getNombre(), campo.getLongitudMin()))
                    message.exec_()
                    return False
                    item.setFocus()
                    
        for campo in self.__campos:
            if campo is not None:
                item = self.__formLayout.itemAt(count + self.__campos.index(campo), QtGui.QFormLayout.FieldRole).widget()
                campo.setValor(item.text())
                        
        func = lambda x: x is not None
        self.__campos = filter(func, self.__campos)
        
        camposObjeto = self.__camposOriginales
        
        for campoNuevo in self.__campos:
            if campoNuevo not in camposObjeto:
                self.__camposNuevos.append(campoNuevo)
        for campoViejo in camposObjeto:
            if campoViejo not in self.__campos:
                self.__camposEliminados.append(campoViejo)

        return True
    
    def __borrarElemento(self):
        txtField = self.__parent.focusWidget()
        index = self.__formLayout.getWidgetPosition(txtField)[0]
        label = self.__formLayout.itemAt(index, QtGui.QFormLayout.LabelRole).widget()
        label.deleteLater()
        txtField.deleteLater()
        self.__campos[index - self.__count] = None
        
    def __editarElemento(self):
        txtField = self.__parent.focusWidget()
        index = self.__formLayout.getWidgetPosition(txtField)[0]
        label = self.__formLayout.itemAt(index, QtGui.QFormLayout.LabelRole).widget()
        campo = self.__campos[index - self.__count]
        dialogo = NuevoCampo(self.__constanteEdicion, campo, self.__parent)
        if dialogo.exec_():
            label.setText(unicode("%s:" % campo.getNombre()))
            if campo.getLongitudMax() is not 0:
                txtField.setMaxLength(campo.getLongitudMax())
            else:
                txtField.setMaxLength(32767)
    
    def addCampo(self, campo=None):
        if campo is None:
            dialogo = ListadoDialogo(tipo=self.__constanteCreacion, parent=self.__parent)
            if dialogo.exec_():
                self.addCampo(dialogo.getSelected())
        else:
            if self.existe(campo, self.__campos):
                message = QtGui.QMessageBox()
                message.setIcon(QtGui.QMessageBox.Warning)
                message.setText("El campo ya se encuentra")
                message.exec_()
            else:
                label = QtGui.QLabel()
                label.setText("%s:" % campo.getNombre())
                txtBox = QtGui.QLineEdit()
                txtBox.setText(campo.getValor())
                if campo.getLongitudMax() is not 0:
                    txtBox.setMaxLength(campo.getLongitudMax())
                
                txtBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
                
                eliminar = self.__createAction('Eliminar', self.__borrarElemento)
                eliminar.setData(txtBox)
                editar = self.__createAction("Editar", self.__editarElemento)
                editar.setData(txtBox)
                
                txtBox.addActions([eliminar, editar])
                self.__formLayout.addRow(label, txtBox)
                self.__campos.append(campo)
                txtBox.textEdited.connect(self.__parent.setDirty)
                
    def existe(self, campo, lista):
        for c in lista:
            if c is not None:
                if c.getId_atributo() == campo.getId_atributo():
                    return True
        return False
            
    def __cargarCampos(self):
        for campo in self.__campos:
            label = QtGui.QLabel()
            label.setText("%s:" % campo.getNombre())
            txtBox = QtGui.QLineEdit()
            txtBox.setText(campo.getValor())
            if campo.getLongitudMax() is not 0:
                txtBox.setMaxLength(campo.getLongitudMax())
            
            txtBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
            
            eliminar = self.__createAction('Eliminar', self.__borrarElemento)
            eliminar.setData(txtBox)
            editar = self.__createAction("Editar", self.__editarElemento)
            editar.setData(txtBox)
            
            txtBox.addActions([eliminar, editar])
            self.__formLayout.addRow(label, txtBox)
            txtBox.textEdited.connect(self.__parent.setDirty)   
            
    def __createAction(self, text, slot=None):
        action = QtGui.QAction(text, self.__formLayout)
        if slot is not None:
            self.__formLayout.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action
