'''
Created on 26/01/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from gui.VerActuacionScreen import Ui_VerActuacion


class VerActuacion(QWidget, Ui_VerActuacion):
    def __init__(self, actuacion = None, parent = None):
        super(VerActuacion, self).__init__(parent)
        self.__actuacion = actuacion
        self.setupUi(self)
        self.setActuacion(self.__actuacion)
                
    def setActuacion(self, actuacion):
        if actuacion:
            self.lblJuzgado.setText(unicode(actuacion.getJuzgado()))
            self.lblDescripcion.setText(actuacion.getDescripcion())
            self.dteFecha.setDateTime(actuacion.getFecha())
            self.dteFechaProxima.setDateTime(actuacion.getFechaProxima())
            for campo in actuacion.getCampos():
                label = QLabel()
                label.setText('%s:' % campo.getNombre())
                lblBox = QLabel()
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label, lblBox)
        
