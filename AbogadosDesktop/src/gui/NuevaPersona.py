# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide.QtCore import *
from NuevaPersonaScreen import Ui_NuevaPersona
from core.Persona import Persona
from persistence.Persistence import Persistence
from copy import deepcopy

class NuevaPersona(QDialog, Ui_NuevaPersona):
    def __init__(self,persona=None,tipo = None,parent=None):
        super(NuevaPersona, self).__init__(parent)
        self.__persona = persona
        self.__campos = deepcopy(persona.getCampos())
        self.setupUi(self)
        self.connect(self.btnAdd,SIGNAL("clicked()"),self.addCampo)
        
        if self.__persona is not None:
            self.__tipo = persona.getTipo()
            self.txtNombre.setText(self.__persona.getNombre())
            self.txtCedula.setText(self.__persona.getId())
            self.txtTelefono.setText(self.__persona.getTelefono())
            self.txtDireccion.setText(self.__persona.getDireccion())
            self.txtCorreo.setText(self.__persona.getCorreo())
            self.txtNotas.setText(self.__persona.getNotas())
        else:
            self.__tipo = tipo
            
        if self.__campos is not None and self.__campos != []:
            for campo in self.__campos:
                self.addCampo(campo)
  
            
            
    def getPersona(self):
        return self.__persona
    
    def guardar(self):
        try:
            p = Persistence()
            if self.__persona is None:
                persona = Persona(self.__tipo)
                persona.setNombre(self.txtNombre.text())
                persona.setId(self.txtCedula.text())
                persona.setTelefono(self.txtTelefono.text())
                persona.setDireccion(self.txtDireccion.text())
                persona.setCorreo(self.txtCorreo.text())
                persona.setNotas(self.txtNotas.text())
                
                p.guardarPersona(persona)
                self.__persona = persona
            else:
                self.__persona = Persona(self.__tipo)
                self.__persona.setNombre(self.txtNombre.text())
                self.__persona.setId(self.txtCedula.text())
                self.__persona.setTelefono(self.txtTelefono.text())
                self.__persona.setDireccion(self.txtDireccion.text())
                self.__persona.setCorreo(self.txtCorreo.text())
                self.__persona.setNotas(self.txtNotas.text())
                p.actualizarPersona(self.__persona)
                    
        except Exception, e:
            print e
        finally:
            return QDialog.accept(self)
            
    def accept(self):
        if self.__campos != self.__persona.getCampos():
            func = lambda x: x is not None and 1 or 0
            self.__campos = filter(func,self.__campos)
            self.__persona.setCampos(self.__campos)
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
        self.__campos[index - 6] = None
    
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
    
    def addCampo(self,campo):
        label = QLabel()
        label.setText(campo.getNombre())
        txtBox = QLineEdit()
        txtBox.setText(campo.getValor())
        txtBox.setContextMenuPolicy(Qt.ActionsContextMenu)
        action = self.createAction('Eliminar', self.borrarElemento)
        action.setData(txtBox)
        txtBox.addAction(action)
        self.formLayout.addRow(label,txtBox)     
    

import sys
from PySide.QtGui import QApplication
from core.CampoPersonalizado import CampoPersonalizado
from core.Persona import Persona

persona = None
try:
    p = Persistence()
    persona = p.consultarPersona("2", 1)

    app = QApplication(sys.argv)
    dialog = NuevaPersona(persona)
    dialog.show()
    app.exec_()
except Exception, e:
    print e