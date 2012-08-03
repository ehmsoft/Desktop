'''
Created on 28/01/2012

@author: elfotografo007
'''
from PySide import QtGui
from VerPlantillaScreen import Ui_VerPlantilla

class VerPlantilla(QtGui.QWidget, Ui_VerPlantilla):
    def __init__(self, plantilla=None, parent=None):
        super(VerPlantilla, self).__init__(parent)
        self.__plantilla = plantilla
        self.setupUi(self)
    
        if self.__plantilla:
            self.lblNombre.setWordWrap(True)
            self.lblDemandante.setWordWrap(True)
            self.lblDemandado.setWordWrap(True)
            self.lblJuzgado.setWordWrap(True)
            self.lblRadicado.setWordWrap(True)
            self.lblRadicadoUnico.setWordWrap(True)
            self.lblEstado.setWordWrap(True)
            self.lblCategoria.setWordWrap(True)
            self.lblTipo.setWordWrap(True)
            
            self.lblNombre.setToolTip(unicode(self.__plantilla))
            self.lblDemandante.setToolTip(unicode(self.__plantilla.getDemandante()))
            self.lblDemandado.setToolTip(unicode(self.__plantilla.getDemandado()))
            self.lblJuzgado.setToolTip(unicode(self.__plantilla.getJuzgado()))
            self.lblRadicado.setToolTip(self.__plantilla.getRadicado())
            self.lblRadicadoUnico.setToolTip(self.__plantilla.getRadicadoUnico())
            self.lblEstado.setToolTip(self.__plantilla.getEstado())
            self.lblCategoria.setToolTip(unicode(self.__plantilla.getCategoria()))
            self.lblTipo.setToolTip(unicode(self.__plantilla.getTipo()))
            
            
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
                label = QtGui.QLabel()
                label.setWordWrap(True)
                label.setText(u'{0}:'.format(campo.getNombre()))
                lblBox = QtGui.QLabel()
                lblBox.setWordWrap(True)
                lblBox.setToolTip(campo.getValor())
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label, lblBox)
