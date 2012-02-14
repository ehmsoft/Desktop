'''
Created on 28/01/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from gui.VerPlantillaScreen import Ui_VerPlantilla

class VerPlantilla(QWidget, Ui_VerPlantilla):
    def __init__(self, plantilla = None, parent = None):
        super(VerPlantilla, self).__init__(parent)
        self.__plantilla = plantilla
        self.setupUi(self)
    
        if self.__plantilla:
            self.lblNombre.setText(unicode(self.__plantilla))
            self.lblDemandante.setText(unicode(self.__plantilla.getDemandante()))
            self.lblDemandado.setText(unicode(self.__plantilla.getDemandado()))
            self.lblJuzgado.setText(unicode(self.__plantilla.getJuzgado()))
            self.lblRadicado.setText(self.__plantilla.getRadicado())
            self.lblRadicadoUnico.setText(self.__plantilla.getRadicadoUnico())
            self.lblEstado.setText(self.__plantilla.getEstado())
            self.lblCategoria.setText(unicode(self.__plantilla.getCategoria()))
            self.lblTipo.setText(unicode(self.__plantilla.getTipo()))
            self.lblPrioridad.setNum(self.__plantilla.getPrioridad())
            self.lblNotas.setText(self.__plantilla.getNotas())
            
            for campo in self.__plantilla.getCampos():
                label = QLabel()
                label.setText('%s:' % campo.getNombre())
                lblBox = QLabel()
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label,lblBox)