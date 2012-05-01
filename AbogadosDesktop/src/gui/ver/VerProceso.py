# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: elfotografo007
'''
from PySide import QtGui
from VerProcesoScreen import Ui_VerProceso
from VerActuacion import VerActuacion

class VerProceso(QtGui.QWidget, Ui_VerProceso):
    def __init__(self, proceso=None, parent=None):
        super(VerProceso, self).__init__(parent)
        self.__proceso = proceso
        self.setupUi(self)
    
        if self.__proceso:
            self.lblDemandante.setText(unicode(self.__proceso.getDemandante()))
            self.lblDemandado.setText(unicode(self.__proceso.getDemandado()))
            self.dteFecha.setDateTime(self.__proceso.getFecha())
            self.lblJuzgado.setText(unicode(self.__proceso.getJuzgado()))
            self.lblRadicado.setText(self.__proceso.getRadicado())
            self.lblRadicadoUnico.setText(self.__proceso.getRadicadoUnico())
            self.lblEstado.setText(self.__proceso.getEstado())
            self.lblCategoria.setText(unicode(self.__proceso.getCategoria()))
            self.lblTipo.setText(unicode(self.__proceso.getTipo()))
            self.lblPrioridad.setNum(self.__proceso.getPrioridad())
            self.lblNotas.setText(self.__proceso.getNotas())
            
            for campo in self.__proceso.getCampos():
                label = QtGui.QLabel()
                label.setText(u'{0}:'.format(campo.getNombre()))
                lblBox = QtGui.QLabel()
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label, lblBox)
            actuaciones = self.__proceso.getActuaciones()
            if len(actuaciones) is not 0:
                vbox = QtGui.QVBoxLayout()
                for actuacion in actuaciones:
                    vbox.addWidget(VerActuacion(actuacion))
                
                vbox.setContentsMargins(1, 1, 1, 1)
                vbox.setSpacing(1)
                scroll = QtGui.QScrollArea()
                widgetActuaciones = QtGui.QWidget()
                widgetActuaciones.setLayout(vbox)
                widgetActuaciones.setContentsMargins(0, 0, 0, 0)
                scroll.setWidget(widgetActuaciones)
                self.tabWidget.addTab(scroll, "Actuaciones")
