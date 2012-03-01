# -*- coding: utf-8 -*-

'''
Created on 26/01/2012

@author: harold
'''
from PySide import QtGui, QtCore
from core.CampoPersonalizado import CampoPersonalizado
from persistence.Persistence import Persistence
from NuevoCampoScreen import Ui_NuevoCampo
import Util

class NuevoCampo(QtGui.QDialog, Ui_NuevoCampo):
    '''
    classdocs
    '''
    PERSONA = 1
    JUZGADO = 2
    ACTUACION = 3
    PROCESO = 4
    
    def __init__(self, tipo, campo = None, parent = None):
        super(NuevoCampo, self).__init__(parent)
        self.__dirty = False
        self.__campo = campo
        self.__tipo = tipo
        self.setupUi(self)
        
        if tipo is None:
            raise TypeError("El tipo es necesario para identificar el tipo de CampoPersonalizado")        
        if tipo in range(1, 5):
            pass
        else:
            raise TypeError("El tipo %s no está soportado" % tipo)
        if campo is not None and not isinstance(campo, CampoPersonalizado):
            raise TypeError("El objeto campo debe ser de la clase CampoPersonalizado")
        
        
        if self.__campo is not None:
            self.setWindowTitle(unicode("Editar campo personalizado"))
            self.groupBox.setTitle(unicode("Datos del campo personalizado:"))
            self.txtNombre.setText(self.__campo.getNombre())
            self.sbLongMax.setValue(self.__campo.getLongitudMax())
            self.sbLongMin.setValue(self.__campo.getLongitudMin())
            self.cbObligatorio.setChecked(self.__campo.isObligatorio())
        self.sbLongMax.valueChanged[int].connect(self.validarLongitudMax)
        self.sbLongMin.valueChanged[int].connect(self.validarLongitudMin)
        
        self.txtNombre.textChanged.connect(self.setDirty)
        self.cbObligatorio.stateChanged.connect(self.setDirty)       
        
    def validarLongitudMax(self, lmax):
        if lmax is not 0:
            lmin = self.sbLongMin.value()
            if lmin is not 0 and lmax < lmin:
                self.sbLongMax.setValue(lmax + 1)
        self.__dirty = True
            
    def validarLongitudMin(self, lmin):
        lmax = self.sbLongMax.value()
        if lmax is not 0 and lmin > lmax:
            self.sbLongMin.setValue(lmin - 1) 
        self.__dirty = True         
            
    def getCampo(self):
        return self.__campo
    
    def guardar(self):
        try:
            p = Persistence()
            if self.__campo is None:
                campo = CampoPersonalizado(self.txtNombre.text())
                campo.setLongitudMax(self.sbLongMax.value())
                campo.setLongitudMin(self.sbLongMin.value())
                campo.setObligatorio(self.cbObligatorio.isChecked())
                
                if self.__tipo is self.__class__.PERSONA:
                    p.guardarAtributoPersona(campo)
                elif self.__tipo is self.__class__.JUZGADO:
                    p.guardarAtributoJuzgado(campo)
                elif self.__tipo is self.__class__.ACTUACION:
                    p.guardarAtributoActuacion(campo)
                elif self.__tipo is self.__class__.PROCESO:
                    p.guardarAtributo(campo)
                self.__campo = campo
            else:
                self.__campo.setNombre(self.txtNombre.text())
                self.__campo.setLongitudMax(self.sbLongMax.value())
                self.__campo.setLongitudMin(self.sbLongMin.value())
                self.__campo.setObligatorio(self.cbObligatorio.isChecked())
                if self.__tipo is self.__class__.PERSONA:
                    p.actualizarAtributoPersona(self.__campo)
                elif self.__tipo is self.__class__.JUZGADO:
                    p.actualizarAtributoJuzgado(self.__campo)
                elif self.__tipo is self.__class__.ACTUACION:
                    p.actualizarAtributoActuacion(self.__campo)
                elif self.__tipo is self.__class__.PROCESO:
                    p.actualizarAtributo(self.__campo)
                    
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
        else:
            self.guardar()
            
    def reject(self):
        Util.reject(self, self.__dirty)
            
    def setDirty(self):
        sender = self.sender()
        if isinstance(sender, QtGui.QLineEdit):
            self.disconnect(sender, QtCore.SIGNAL("textChanged()"), self.setDirty)
        elif isinstance(sender, QtGui.QCheckBox):
            self.disconnect(sender, QtCore.SIGNAL("stateChanged()"), self.setDirty)
