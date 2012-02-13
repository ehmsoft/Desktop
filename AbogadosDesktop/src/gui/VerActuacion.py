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
        if self.__actuacion:
            self.lblJuzgado.setText(self.__actuacion.getJuzgado().getNombre())
            self.lblDescripcion.setText(self.__actuacion.getDescripcion())
            self.dteFecha.setDateTime(self.__actuacion.getFecha())
            self.dteFechaProxima.setDateTime(self.__actuacion.getFechaProxima())
            for campo in self.__actuacion.getCampos():
                label = QLabel()
                label.setText('%s:' % campo.getNombre())
                lblBox = QLabel()
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label,lblBox)