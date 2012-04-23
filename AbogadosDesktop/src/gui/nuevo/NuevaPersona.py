# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from NuevaPersonaScreen import Ui_NuevaPersona
from core.Persona import Persona
from persistence.Persistence import Persistence
from NuevoCampo import NuevoCampo
from gui.GestorCampos import GestorCampos
from gui.ListadoDialogo import ListadoDialogo
from gui import Util

class NuevaPersona(QtGui.QDialog, Ui_NuevaPersona):
    def __init__(self, persona=None, tipo=None, parent=None):
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
                
        self.__gestor = GestorCampos(campos=campos, formLayout=self.formLayout, parent=self, constante_de_edicion=NuevoCampo.PERSONA, constante_de_creacion=constante)
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.__gestor.addCampo)
        
        self.txtNombre.textEdited.connect(self.setDirty)
        self.txtCedula.textEdited.connect(self.setDirty)
        self.txtCorreo.textEdited.connect(self.setDirty)
        self.txtDireccion.textEdited.connect(self.setDirty)
        self.txtNotas.textChanged.connect(self.setDirty)
        self.txtTelefono.textEdited.connect(self.setDirty)
                        
    def getPersona(self):
        return self.__persona
    
    def __guardar(self):
        try:
            p = Persistence()
            tipo = self.__tipo
            nombre = self.txtNombre.text()
            cedula = self.txtCedula.text()
            telefono = self.txtTelefono.text()
            direccion = self.txtDireccion.text()
            correo = self.txtCorreo.text()
            notas = self.txtNotas.toPlainText()
            campos = self.__gestor.getCampos()
            if not self.__persona:
                self.__persona = Persona(tipo=tipo, id=cedula, nombre=nombre, telefono=telefono, direccion=direccion, correo=correo, notas=notas, campos=campos)                                
                p.guardarPersona(self.__persona)
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
                        p.guardarCampoDemandante(campoPersonalizado=campo, id_demandante=self.__persona.getId_persona())
                    else:
                        p.guardarCampoDemandado(campoPersonalizado=campo, id_demandado=self.__persona.getId_persona())
                self.__persona.setNombre(nombre)
                self.__persona.setId(cedula)
                self.__persona.setTelefono(telefono)
                self.__persona.setDireccion(direccion)
                self.__persona.setCorreo(correo)
                self.__persona.setNotas(notas)
                self.__persona.setCampos(campos)
                p.actualizarPersona(self.__persona)
        except Exception, e:
            print e
        finally:
            return QtGui.QDialog.accept(self)
            
    def accept(self):
        if not len(self.txtNombre.text()):
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
