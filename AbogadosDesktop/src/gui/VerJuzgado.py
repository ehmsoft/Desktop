'''
Created on 25/01/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from gui.VerJuzgadoScreen import Ui_VerJuzgado


class VerJuzgado(QWidget, Ui_VerJuzgado):
    def __init__(self, juzgado = None, parent = None):
        super(VerJuzgado, self).__init__(parent)
        self.__juzgado = juzgado
        self.setupUi(self)
        if self.__juzgado:
            self.__tipo = self.__juzgado.getTipo()
            self.lblNombre.setText(self.__juzgado.getNombre())
            self.lblCiudad.setText(self.__juzgado.getCiudad())
            self.lblTelefono.setText(self.__juzgado.getTelefono())
            self.lblDireccion.setText(self.__juzgado.getDireccion())
            self.lblTipo.setText(self.__juzgado.getTipo())
            for campo in self.__juzgado.getCampos():
                label = QLabel()
                label.setText('%s:' % campo.getNombre())
                lblBox = QLabel()
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label,lblBox)

