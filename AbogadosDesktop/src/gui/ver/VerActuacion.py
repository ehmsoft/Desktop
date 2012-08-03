'''
Created on 26/01/2012

@author: elfotografo007
'''
from PySide import QtGui
from VerActuacionScreen import Ui_VerActuacion


class VerActuacion(QtGui.QWidget, Ui_VerActuacion):
    def __init__(self, actuacion=None, parent=None):
        super(VerActuacion, self).__init__(parent)
        self.__actuacion = actuacion
        self.setupUi(self)
        if self.__actuacion:
            self.lblJuzgado.setText(self.__actuacion.getJuzgado().getNombre())
            self.lblDescripcion.setText(self.__actuacion.getDescripcion())
            self.lblJuzgado.setToolTip(self.__actuacion.getJuzgado().getNombre())
            self.lblDescripcion.setToolTip(self.__actuacion.getDescripcion())
            self.lblJuzgado.setWordWrap(True)
            self.lblDescripcion.setWordWrap(True)
            self.dteFecha.setDateTime(self.__actuacion.getFecha())
            self.dteFechaProxima.setDateTime(self.__actuacion.getFechaProxima())
            for campo in self.__actuacion.getCampos():
                label = QtGui.QLabel()
                label.setWordWrap(True)
                label.setText(u'{0}:'.format(campo.getNombre()))
                lblBox = QtGui.QLabel()
                lblBox.setWordWrap(True)
                lblBox.setToolTip(campo.getValor())          
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label, lblBox)
