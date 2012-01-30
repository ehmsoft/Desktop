'''
Created on 26/01/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from gui.VerCampoPersonalizadoScreen import Ui_VerCampoPersonalizado


class VerCampoPersonalizado(QWidget, Ui_VerCampoPersonalizado):
    def __init__(self, campo = None, parent = None):
        super(VerCampoPersonalizado, self).__init__(parent)
        self.__campo = campo
        self.setupUi(self)
        if self.__campo:
            self.lblNombre.setText(self.__campo.getNombre())
            self.lblValor.setText(self.__campo.getValor())
            self.lblLongitudMax.setNum(self.__campo.getLongitudMax())
            self.lblLongitudMin.setNum(self.__campo.getLongitudMin())
            self.chkObligatorio.setChecked(self.__campo.isObligatorio())