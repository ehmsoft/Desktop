'''
Created on 25/01/2012

@author: elfotografo007
'''
from PySide import QtGui
from gui.ver.VerJuzgadoScreen import Ui_VerJuzgado


class VerJuzgado(QtGui.QWidget, Ui_VerJuzgado):
    def __init__(self, juzgado=None, parent=None):
        super(VerJuzgado, self).__init__(parent)
        self.__juzgado = juzgado
        self.setupUi(self)
        if self.__juzgado:
            self.__tipo = self.__juzgado.getTipo()
            self.lblNombre.setWordWrap(True)
            self.lblCiudad.setWordWrap(True)
            self.lblTelefono.setWordWrap(True)
            self.lblDireccion.setWordWrap(True)
            self.lblTipo.setWordWrap(True)
            self.lblNombre.setToolTip(self.__juzgado.getNombre())
            self.lblCiudad.setToolTip(self.__juzgado.getCiudad())
            self.lblTelefono.setToolTip(self.__juzgado.getTelefono())
            self.lblDireccion.setToolTip(self.__juzgado.getDireccion())
            self.lblTipo.setToolTip(self.__juzgado.getTipo())
            self.lblNombre.setText(self.__juzgado.getNombre())
            self.lblCiudad.setText(self.__juzgado.getCiudad())
            self.lblTelefono.setText(self.__juzgado.getTelefono())
            self.lblDireccion.setText(self.__juzgado.getDireccion())
            self.lblTipo.setText(self.__juzgado.getTipo())
            for campo in self.__juzgado.getCampos():
                label = QtGui.QLabel()
                label.setWordWrap(True)
                label.setText(u'{0}:'.format(campo.getNombre()))
                lblBox = QtGui.QLabel()
                lblBox.setWordWrap(True)
                lblBox.setToolTip(campo.getValor())
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label, lblBox)

