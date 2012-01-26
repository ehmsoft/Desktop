# -*- coding: utf-8 -*-

'''
Created on 26/01/2012

@author: harold
'''
from PySide.QtGui import *
from PySide.QtCore import *
from core.CampoPersonalizado import CampoPersonalizado
from persistence.Persistence import Persistence
from NuevoCampoScreen import Ui_NuevoCampo

class NuevoCampo(QDialog, Ui_NuevoCampo):
    '''
    classdocs
    '''
    persona = 1
    juzgado = 2
    actuacion = 3
    proceso = 4
    
    def __init__(self,tipo,campo=None,parent=None):
        super(NuevoCampo, self).__init__(parent)
        self.__campo = campo
        self.__tipo = tipo
        self.setupUi(self)
        
        
        if self.__campo is not None:
            self.txtNombre.setText(self.__campo.getNombre())
            self.txtLongMax.setText(self.__campo.getLongitudMax())
            self.txtLongMin.setText(self.__campo.getLongitudMin())
            self.cbObligatorio.setChecked(self.__campo.isObligatorio())
        self.sbLongMax.valueChanged[int].connect(self.validarLongitudMax)
        self.sbLongMin.valueChanged[int].connect(self.validarLongitudMin)       
        
    def validarLongitudMax(self,lmax):
        lmin = self.sbLongMin.value()
        if lmin is not 0 and lmax < lmin:
            self.sbLongMax.setValue(lmax+1)
            
    def validarLongitudMin(self,lmin):
        lmax = self.sbLongMax.value()
        if lmax is not 0 and lmin > lmax:
            self.sbLongMin.setValue(lmin-1)          
            
    def getCampo(self):
        return self.__campo
    
    def guardar(self):
        try:
            p = Persistence()
            if self.__campo is None:
                campo = CampoPersonalizado(self.txtNombre.text())
                campo.setLongitudMax(self.txtLongMax.text())
                campo.setLongitudMin(self.txtLongMin.text())
                campo.setObligatorio(self.cbObligatorio.isChecked())
                
                if self.__tipo is self.__class__.persona:
                    p.guardarAtributoPersona(campo)
                elif self.__tipo is self.__class__.juzgado:
                    p.guardarAtributoJuzgado(campo)
                elif self.__tipo is self.__class__.actuacion:
                    p.guardarAtributoActuacion(campo)
                elif self.__tipo is self.__class__.proceso:
                    p.guardarAtributo(campo)
                self.__campo = campo
            else:
                self.__campo = CampoPersonalizado(self.txtNombre.text())
                self.__campo.setLongitudMax(self.txtLongMax.text())
                self.__campo.setLongitudMin(self.txtLongMin.text())
                self.__campo.setObligatorio(self.cbObligatorio.isChecked())
                if self.__tipo is self.__class__.persona:
                    p.actualizarAtributoPersona(campo)
                elif self.__tipo is self.__class__.juzgado:
                    p.actualizarAtributoJuzgado(campo)
                elif self.__tipo is self.__class__.actuacion:
                    p.actualizarAtributoActuacion(campo)
                elif self.__tipo is self.__class__.proceso:
                    p.actualizarAtributo(campo)
                    
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
        else:
            self.guardar()     