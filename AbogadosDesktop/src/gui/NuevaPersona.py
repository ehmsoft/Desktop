# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from NuevaPersonaScreen import Ui_NuevaPersona
from core.Persona import Persona
from persistence.Persistence import Persistence
from gui.NuevoCampo import NuevoCampo
from gui.GestorCampos import GestorCampos
from gui.ListadoDialogo import ListadoDialogo
import Util

class NuevaPersona(QtGui.QDialog, Ui_NuevaPersona):
    def __init__(self, persona = None, tipo = None, parent = None):
        super(NuevaPersona, self).__init__(parent)
        
        self.__dirty = False
        
        if(persona is None and tipo is None):
            raise TypeError("Para crear una nueva persona debe pasar el argumento tipo")
        if persona is not None and not isinstance(persona, Persona):
            raise TypeError("El objeto persona debe ser de la clase Persona")
        self.__persona = persona
        self.setupUi(self)
        
        if self.__persona is not None:
            campos = persona.getCampos()
            self.__tipo = persona.getTipo()
            self.txtNombre.setText(self.__persona.getNombre())
            self.txtCedula.setText(self.__persona.getId())
            self.txtTelefono.setText(self.__persona.getTelefono())
            self.txtDireccion.setText(self.__persona.getDireccion())
            self.txtCorreo.setText(self.__persona.getCorreo())
            self.txtNotas.setText(self.__persona.getNotas())
        else:
            campos = []
            self.__tipo = tipo
                        
        if self.__tipo is 1:
            constante = ListadoDialogo.CAMPODEMANDADO
            if persona is None:
                self.setWindowTitle("Nuevo demandante")
                self.groupBox.setTitle("Ingrese los datos del nuevo demandante:")
            else:
                self.setWindowTitle("Editar demandante")
                self.groupBox.setTitle("Ingrese los datos del demandante:")
        elif self.__tipo is 2:
            constante = ListadoDialogo.CAMPODEMANDADO
            if persona is None:
                self.setWindowTitle("Nuevo demandado")
                self.groupBox.setTitle("Ingrese los datos del nuevo demandado:")
            else:
                self.setWindowTitle("Editar demandado")
                self.groupBox.setTitle("Ingrese los datos del demandado:")
                
        self.__gestor = GestorCampos(campos = campos, formLayout = self.formLayout, parent = self, constante_de_edicion = NuevoCampo.PERSONA, constante_de_creacion = constante)
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.__gestor.addCampo)
        
        self.txtNombre.textEdited.connect(self.setDirty)
        self.txtCedula.textEdited.connect(self.setDirty)
        self.txtCorreo.textEdited.connect(self.setDirty)
        self.txtDireccion.textEdited.connect(self.setDirty)
        self.txtNotas.textEdited.connect(self.setDirty)
        self.txtTelefono.textEdited.connect(self.setDirty)
                        
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
                persona.setCampos(self.__gestor.getCampos())
                                
                p.guardarPersona(persona)
                self.__persona = persona
            else:
                camposNuevos = self.__gestor.getCamposNuevos()
                camposEliminados = self.__gestor.getCamposEliminados()
                for campo in camposEliminados:
                    if self.__tipo is 1:
                        p.borrarCampoDemandante(campo)
                    else:
                        p.borrarCampoDemandado(campo)
                for campo in camposNuevos:
                    if self.__tipo is 1:
                        p.guardarCampoDemandante(campoPersonalizado = campo, id_demandante = self.__persona.getId_persona())
                    else:
                        p.guardarCampoDemandado(campoPersonalizado = campo, id_demandante = self.__persona.getId_persona())
                self.__persona.setNombre(self.txtNombre.text())
                self.__persona.setId(self.txtCedula.text())
                self.__persona.setTelefono(self.txtTelefono.text())
                self.__persona.setDireccion(self.txtDireccion.text())
                self.__persona.setCorreo(self.txtCorreo.text())
                self.__persona.setNotas(self.txtNotas.text())
                self.__persona.setCampos(self.__gestor.getCampos())
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
            
    def reject(self):
        Util.reject(self, self.__dirty)
                    
    def setDirty(self):
        self.__dirty = True
        print "Signal"
        self.disconnect(self.sender(), QtCore.SIGNAL("textEdited()"), self.setDirty)
