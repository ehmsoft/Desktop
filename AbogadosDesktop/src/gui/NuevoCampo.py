# -*- coding: utf-8 -*-

'''
Created on 26/01/2012

@author: harold
'''
from PySide.QtGui import *
from PySide.QtCore import *
from core.CampoPersonalizado import CampoPersonalizado
from persistence.Persistence import Persistence
from copy import deepcopy
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
        self.sbLongMax.valueChanged[int].connect(self.validarLongitudes)
        self.sbLongMin.valueChanged[int].connect(self.validarLongitudes)       
        
    def validarLongitudes(self):
        lmax = self.sbLongMax.value()
        lmin = self.sbLongMin.value()
        if lmin is not 0 and lmax < lmin:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText("La longitud máxima no puede ser menor a la mínima")
            message.exec_()
            self.sbLongMin.setValue(lmin-1)
        elif lmax is not 0 and lmin > lmax:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText("La longitud mínima no puede superar la máima")
            message.exec_()
            self.sbLongMax.setValue(lmax+1)
            
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
            
import sys

app = QApplication(sys.argv)
form = NuevoCampo(NuevoCampo.proceso)
form.show()
app.exec_()        