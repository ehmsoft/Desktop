# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from NuevaPersonaScreen import Ui_NuevaPersona
from core.Persona import Persona
from persistence.Persistence import Persistence
from copy import deepcopy

class NuevaPersona(QtGui.QDialog, Ui_NuevaPersona):
    def __init__(self,persona=None,tipo = None,parent=None):
        super(NuevaPersona, self).__init__(parent)
        
        if(persona is None and tipo is None):
            raise TypeError("Para crear una nueva persona debe pasar el argumento tipo")
        if persona is not None and not isinstance(persona, Persona):
            raise TypeError("El objeto persona debe ser de la clase Persona")
        self.__persona = persona
        self.setupUi(self)
        self.connect(self.btnAdd,QtCore.SIGNAL("clicked()"),self.addCampo)
        
        self.__campos = []
        
        if self.__persona is not None:
            self.__campos = deepcopy(persona.getCampos())
            self.__tipo = persona.getTipo()
            self.txtNombre.setText(self.__persona.getNombre())
            self.txtCedula.setText(self.__persona.getId())
            self.txtTelefono.setText(self.__persona.getTelefono())
            self.txtDireccion.setText(self.__persona.getDireccion())
            self.txtCorreo.setText(self.__persona.getCorreo())
            self.txtNotas.setText(self.__persona.getNotas())
        else:
            self.__tipo = tipo
            
        if self.__tipo is 1:
            if persona is None:
                self.setWindowTitle("Nuevo demandante")
                self.groupBox.setTitle("Ingrese los datos del nuevo demandante:")
            else:
                self.setWindowTitle("Editar demandante")
                self.groupBox.setTitle("Ingrese los datos del demandante:")
        elif self.__tipo is 2:
            if persona is None:
                self.setWindowTitle("Nuevo demandado")
                self.groupBox.setTitle("Ingrese los datos del nuevo demandado:")
            else:
                self.setWindowTitle("Editar demandado")
                self.groupBox.setTitle("Ingrese los datos del demandado:")
            
            
        if self.__campos is not None and self.__campos != []:
            for campo in self.__campos:
                self.addCampo(campo)
  
            
            
    def getPersona(self):
        return self.__persona
    
    def organizarCampos(self):
        count = 6
        for campo in self.__campos:
            if campo is not None:
                label = self.formLayout.itemAt(count, QtGui.QFormLayout.LabelRole).widget()
                item = self.formLayout.itemAt(count, QtGui.QFormLayout.FieldRole).widget()
                
                message = QtGui.QMessageBox()
                message.setIcon(QtGui.QMessageBox.Warning)
                
                if campo.isObligatorio() and len(item.text()) is 0:
                    message.setText("%s es obligatorio" % label.text())
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
                    
        count = 6
        for campo in self.__campos:
            if campo is not None:
                item = self.formLayout.itemAt(count, QtGui.QFormLayout.FieldRole).widget()
                campo.setValor(item.text())
                        
        func = lambda x: x is not None and 1 or 0
        self.__campos = filter(func,self.__campos)
        
        if self.__persona is not None:        
            camposObjeto = self.__persona.getCampos()
            
            for campoNuevo in self.__campos:
                if campoNuevo not in camposObjeto:
                    try:
                        p = Persistence()
                        if self.__tipo is 1:
                            p.guardarCampoDemandante(campoNuevo, self.__persona.getId_persona())
                        else:
                            p.guardarCampoDemandado(campoNuevo, self.__persona.getId_persona())
                    except Exception, e:
                        print e
            for campoViejo in camposObjeto:
                if campoViejo not in self.__campos:
                    try:
                        p = Persistence()
                        if self.__tipo is 1:
                            p.borrarCampoDemandante(campoViejo)
                        else:
                            p.borrarCampoDemandado(campoViejo)
                    except Exception, e:
                        print e
            self.__persona.setCampos(self.__campos)
        return True
    
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
                persona.setCampos(self.__campos)
                
                p.guardarPersona(persona)
                self.__persona = persona
            else:
                self.__persona.setNombre(self.txtNombre.text())
                self.__persona.setId(self.txtCedula.text())
                self.__persona.setTelefono(self.txtTelefono.text())
                self.__persona.setDireccion(self.txtDireccion.text())
                self.__persona.setCorreo(self.txtCorreo.text())
                self.__persona.setNotas(self.txtNotas.text())
                self.__persona.setCampos(self.__campos)
                p.actualizarPersona(self.__persona)
                    
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
        self.__campos[index - 6] = None
    
    def createAction(self, text, slot= None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action
    
    def addCampo(self,campo = None):
        if campo is not None:
            label = QtGui.QLabel()
            label.setText("%s:" % campo.getNombre())
            txtBox = QtGui.QLineEdit()
            txtBox.setText(campo.getValor())
            txtBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
            action = self.createAction('Eliminar', self.borrarElemento)
            action.setData(txtBox)
            txtBox.addAction(action)
            self.formLayout.addRow(label,txtBox)
        else:
            pass