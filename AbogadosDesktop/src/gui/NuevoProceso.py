# -*- coding: utf-8 -*-
'''
Created on 7/02/2012

@author: harold
'''

from PySide import QtGui, QtCore
from core.Proceso import Proceso
from gui.NuevoProcesoScreen import Ui_NuevoProceso
from copy import deepcopy
from gui.ListadoDialogo import ListadoDialogo
from gui.NuevoCampo import NuevoCampo
from persistence.Persistence import Persistence

class NuevoProceso(QtGui.QDialog, Ui_NuevoProceso):
    '''
    classdocs
    '''


    def __init__(self, proceso = None, parent = None):
        '''
        Constructor
        '''
        super(NuevoProceso, self).__init__(parent)
        if proceso is not None and not isinstance(proceso, Proceso):
            raise TypeError("El objeto proceso debe pertenecer a la clase Proceso")
        if proceso is not None:
            self.groupBox.setTitle("Datos del proceso:")
            self.setWindowTitle("Editar proceso")
            
        self.setupUi(self)
        self.__proceso = proceso
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.addCampo)
        self.__campos = []
        self.__demandante = None
        self.__demandado = None
        self.__juzgado = None
        self.__categoria = None
        
        if self.__proceso is not None:
            self.__demandante = self.__proceso.getDemandante()
            self.__demandado = self.__proceso.getDemandado()
            self.__juzgado = self.__proceso.getJuzgado()
            self.__categoria = self.__proceso.getCategoria()
            self.__campos = deepcopy(self.__proceso.getCampos())
            
            self.lblDemandante.setText(self.__demandante.getNombre())
            self.lblDemandado.setText(self.__demandado.getNombre())
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            self.lblCategoria.setText(self.__categoria.getNombre())
            self.txtRadicado.setText(self.__proceso.getRadicado())
            self.txtRadicadoUnico.setText(self.__proceso.getRadicadoUnico())
            self.txtTipo.setText(self.__proceso.getTipo())
            self.txtEstado.setText(self.__proceso.getEstado())
            self.sbPrioridad.setRange(0,10)
            self.sbPrioridad.setValue(self.__proceso.getPrioridad())
            self.dteFecha.setDateTime(self.__proceso.getFecha())
            self.txtNotas.setText(self.__proceso.getNotas())
            
        if self.__campos is not None and self.__campos != []:
            for campo in self.__campos:
                self.addCampo(campo)
                
    def accept(self):
        if self.__demandante is None or self.__demandante.getId_persona() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El demandante se considera obligatorio")
            message.exec_()
        elif self.__demandado is None or self.__demandado.getId_persona() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El demandado se considera obligatorio")
            message.exec_()
        elif self.__juzgado is None or self.__juzgado.getId_juzgado() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El juzgado se considera obligatorio")
            message.exec_()
        elif len(self.txtRadicado.text()) is 0:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("El radicado se considera obligatorio")
            message.exec_()
            self.txtRadicado.setFocus()
        elif self.organizarCampos():
            self.guardar()
    
    def guardar(self):
        pass
                
    def getProceso(self):
        return self.__proceso
                
    def organizarCampos(self):
        count = 11
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
                    
        count = 11
        for campo in self.__campos:
            if campo is not None:
                item = self.formLayout.itemAt(count, QtGui.QFormLayout.FieldRole).widget()
                campo.setValor(item.text())
            count += 1
                        
        func = lambda x: x is not None and 1 or 0
        self.__campos = filter(func, self.__campos)
        
        if self.__proceso is not None:        
            camposObjeto = self.__persona.getCampos()
            
            for campoNuevo in self.__campos:
                if campoNuevo not in camposObjeto:
                    try:
                        p = Persistence()
                        p.guardarCampoPersonalizado(campoNuevo, self.__proceso.getId_proceso())
                    except Exception, e:
                        print e
            for campoViejo in camposObjeto:
                if campoViejo not in self.__campos:
                    try:
                        p = Persistence()
                        p.borrarCampoPersonalizado(campoViejo)
                    except Exception, e:
                        print e
            self.__persona.setCampos(self.__campos)
        return True
    
    def borrarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QtGui.QFormLayout.LabelRole)
        item = self.formLayout.itemAt(index, QtGui.QFormLayout.FieldRole)
        label.widget().deleteLater()
        item.widget().deleteLater()
        self.__campos[index - 11] = None
        
    def editarElemento(self):
        index = self.formLayout.getWidgetPosition(self.sender().data())[0]
        label = self.formLayout.itemAt(index, QtGui.QFormLayout.LabelRole).widget()
        txtBox = self.formLayout.itemAt(index, QtGui.QFormLayout.FieldRole).widget()
        campo = self.__campos[index - 11]
        dialogo = NuevoCampo(NuevoCampo.proceso, campo, self)
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
            dialogo = ListadoDialogo(ListadoDialogo.campoProcesoPlantilla, self)                
            if dialogo.exec_():
                campo = dialogo.getSelected()
                self.addCampo(campo)
                
import sys
app = QtGui.QApplication(sys.argv)
form = NuevoProceso(None, None)
form.show()
app.exec_()