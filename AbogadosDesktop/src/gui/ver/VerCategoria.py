'''
Created on 26/01/2012

@author: elfotografo007
'''
from PySide import QtGui
from gui.ver.VerCategoriaScreen import Ui_VerCategoria


class VerCategoria(QtGui.QWidget, Ui_VerCategoria):
    def __init__(self, categoria = None, parent = None):
        super(VerCategoria, self).__init__(parent)
        self.__categoria = categoria
        self.setupUi(self)
        if self.__categoria:
            self.lblDescripcion.setWordWrap(True)
            self.lblDescripcion.setToolTip(self.__categoria.getDescripcion())
            self.lblDescripcion.setText(self.__categoria.getDescripcion())
            
