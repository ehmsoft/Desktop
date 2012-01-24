# -*- coding: utf-8 -*-

from PySide.QtGui import QDialog, QMessageBox
from NuevaPersonaScreen import Ui_NuevaPersona
from core.Persona import Persona
from persistence.Persistence import Persistence

class NuevaPersona(QDialog, Ui_NuevaPersona):
    def __init__(self,persona=None,tipo = None,parent=None):
        super(NuevaPersona, self).__init__(parent)
        self.__persona = persona
        self.setupUi(self)
        
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