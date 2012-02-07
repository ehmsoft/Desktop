# -*- coding: utf-8 -*-

'''
Created on 25/01/2012

@author: harold
'''

from PySide import QtGui, QtCore
from NuevoJuzgadoScreen import Ui_NuevoJuzgado
from core.Juzgado import Juzgado
from persistence.Persistence import Persistence
from copy import deepcopy
from gui.ListadoDialogo import ListadoDialogo
from gui.NuevoCampo import NuevoCampo

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
        self.connect(self.btnAdd,QtCore.SIGNAL("clicked()"),self.addCampo)
        
        self.__campos = []
                
        if self.__juzgado is not None:
            self.__campos = deepcopy(juzgado.getCampos())
            self.txtNombre.setText(self.__juzgado.getNombre())
            self.txtDireccion.setText(self.__juzgado.getDireccion())
            self.txtCiudad.setText(self.__juzgado.getCiudad())
            self.txtTelefono.setText(self.__juzgado.getTelefono())
            self.txtTipo.setText(self.__juzgado.getTipo())
            
        if self.__campos is not None and self.__campos != []:
            for campo in self.__campos:
                self.addCampo(campo)
  
            
            
    def getJuzgado(self):
        return self.__juzgado
    
    def organizarCampos(self):
        count = 5
        for campo in self.__campos:
            if campo is not None:
                item = self.formLayout.itemAt(count, QtGui.QFormLayout.FieldRole).widget()
                
                message = QtGui.QMessageBox()
                message.setIcon(QtGui.QMessageBox.Warning)
                
                if campo.isObligatorio() and len(item.text()) is 0:
                    message.setText("El campo %s es obligatorio" % campo.getNombre())
                    message.exec_()
                    return False
                elif campo.getLongitudMax() is not 0 and len(item.text()) > campo.getLongitudMax():
                    message.setText(unicode("La longitud máxima del campo %s es de %i caracteres" % (campo.getNombre(), campo.getLongitudMax())))
                    message.exec_()
                    return False
                elif campo.getLongitudMin() is not 0 and len(item.text()) < campo.getLongitudMin():
                    message.setText(unicode("La longitud mínima del campo %s es de %i caracteres" % (campo.getNombre(), campo.getLongitudMin())))
                    message.exec_()
                    return False
                count += 1
                    
        count = 5
        for campo in self.__campos:
            if campo is not None:
                item = self.formLayout.itemAt(count, QtGui.QFormLayout.FieldRole).widget()
                campo.setValor(item.text())
            count += 1
                        
        func = lambda x: x is not None and 1 or 0
        self.__campos = filter(func, self.__campos)
        
        if self.__juzgado is not None:        
            camposObjeto = self.__juzgado.getCampos()
            
            for campoNuevo in self.__campos:
                if campoNuevo not in camposObjeto:
                    try:
                        p = Persistence()
                        p.guardarCampoJuzgado(campoNuevo, self.__juzgado.getId_juzgado())
                    except Exception, e:
                        print e
            for campoViejo in camposObjeto:
                if campoViejo not in self.__campos:
                    try:
                        p = Persistence()
                        p.borrarCampoJuzgado(campoViejo)
                    except Exception, e:
                        print e
            self.__juzgado.setCampos(self.__campos)
        return True
    
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
                
                p.guardarJuzgado(juzgado)
                self.__juzgado = juzgado
            else:
                self.__juzgado.setNombre(self.txtNombre.text())
                self.__juzgado.setDireccion(self.txtDireccion.text())
                self.__juzgado.setCiudad(self.txtCiudad.text())
                self.__juzgado.setTelefono(self.txtTelefono.text())
                self.__juzgado.setTipo(self.txtTipo.text())
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
            message.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            message.setDefaultButton(QtGui.QMessageBox.No)
            message.setText(unicode("¿Desea guardar sin agregar un teléfono?"))
            ret = message.exec_()
            if ret == QtGui.QMessageBox.Yes:
                self.guardar()
            else:
                self.txtTelefono.setFocus()            
        elif self.organizarCampos():
            self.guardar()
    
    def borrarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QtGui.QFormLayout.LabelRole)
        item = self.formLayout.itemAt(index, QtGui.QFormLayout.FieldRole)
        label.widget().deleteLater()
        item.widget().deleteLater()
        self.__campos[index - 5] = None
        
    def editarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QtGui.QFormLayout.LabelRole).widget()
        txtBox = self.formLayout.itemAt(index, QtGui.QFormLayout.FieldRole).widget()
        campo = self.__campos[index - 5]
        dialogo = NuevoCampo(NuevoCampo.juzgado, campo, self)
        if dialogo.exec_():
            label.setText(unicode("%s:" % campo.getNombre()))
            if campo.getLongitudMax() is not 0:
                txtBox.setMaxLength(campo.getLongitudMax())
    
    def createAction(self, text, slot = None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action
    
    def addCampo(self, campo = None):
        if campo is not None:
            if campo in self.__campos:
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
                
                eliminar = self.createAction('Eliminar', self.borrarElemento)
                eliminar.setData(txtBox)
                editar = self.createAction("Editar", self.editarElemento)
                editar.setData(txtBox)
                
                txtBox.addActions([eliminar, editar])
                self.formLayout.addRow(label, txtBox)
                self.__campos.append(campo)
        else:
            dialogo = ListadoDialogo(ListadoDialogo.campoJuzgado, self)
            if dialogo.exec_():
                campo = dialogo.getSelected()
                self.addCampo(campo)
                
import sys

app = QtGui.QApplication(sys.argv)
form = NuevoJuzgado(None, None)
form.show()
app.exec_()