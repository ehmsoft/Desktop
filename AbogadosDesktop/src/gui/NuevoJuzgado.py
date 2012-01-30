# -*- coding: utf-8 -*-

'''
Created on 25/01/2012

@author: harold
'''

from PySide.QtGui import *
from PySide.QtCore import *
from NuevoJuzgadoScreen import Ui_NuevoJuzgado
from core.Juzgado import Juzgado
from persistence.Persistence import Persistence
from copy import deepcopy
from core.CampoPersonalizado import CampoPersonalizado

class NuevoJuzgado(QDialog, Ui_NuevoJuzgado):
    '''
    classdocs
    '''
    
    def __init__(self, juzgado = None, parent = None):
        '''
        Constructor
        '''
        super(NuevoJuzgado, self).__init__(parent)
        self.__juzgado = juzgado
        self.setupUi(self)
        self.connect(self.btnAdd,SIGNAL("clicked()"),self.addCampo)
        
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
        func = lambda x: x is not None and 1 or 0
        self.__campos = filter(func,self.__campos)
        self.__juzgado.setCampos(self.__campos)
        
        camposJuzgado = self.__juzgado.getCampos()
        
        for campoNuevo in self.__campos:
            if campoNuevo not in camposJuzgado:
                try:
                    p = Persistence()
                    p.guardarCampoJuzgado(campoNuevo, self.__juzgado.getId())
                except Exception, e:
                    print e
        for campoViejo in camposJuzgado:
            if campoViejo not in self.__campos:
                try:
                    p = Persistence()
                    p.borrarCampoJuzgado(campoViejo)
                except Exception, e:
                    print e
        self.__juzgado.setCampos(self.__campos)
    
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
            return QDialog.accept(self)
            
    def accept(self):
        if self.__campos != self.__juzgado.getCampos():
            self.organizarCampos()
        if self.txtNombre.text().__len__() == 0 or self.txtNombre.text() == " ":
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText("El nombre se considera obligatorio")
            message.exec_()
            self.txtNombre.setFocus()
        elif self.txtTelefono.text().__len__() == 0 or self.txtTelefono.text() == " ":
            message = QMessageBox()
            message.setIcon(QMessageBox.Question)
            message.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            message.setDefaultButton(QMessageBox.No)
            message.setText(unicode("¿Desea guardar sin agregar un teléfono?"))
            ret = message.exec_()
            if ret == QMessageBox.Yes:
                self.guardar()
            else:
                self.txtTelefono.setFocus()            
        else:
            self.guardar()
    
    def borrarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QFormLayout.LabelRole)
        item = self.formLayout.itemAt(index, QFormLayout.FieldRole)
        label.widget().deleteLater()
        item.widget().deleteLater()
        self.__campos[index - 5] = None
    
    def createAction(self, text, slot= None, shortcut = None, icon = None, tip = None, checkable = False, signal = "triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon("./images/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action
    
    def addCampo(self,campo = None):
        if campo is not None:
            label = QLabel()
            label.setText("%s:" % campo.getNombre())
            txtBox = QLineEdit()
            txtBox.setText(campo.getValor())
            txtBox.setContextMenuPolicy(Qt.ActionsContextMenu)
            action = self.createAction('Eliminar', self.borrarElemento)
            action.setData(txtBox)
            txtBox.addAction(action)
            self.formLayout.addRow(label,txtBox)
        else:
            pass     