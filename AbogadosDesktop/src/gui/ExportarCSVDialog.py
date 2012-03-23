# -*- coding: utf-8 -*-
'''
Created on 22/03/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from gui.ExportarCSVDialogScreen import Ui_ExportarCSVDialog
from ehmsoft import Exportar
from gui.ListadoDialogo import ListadoDialogo

class ExportarCSVDialog(QDialog, Ui_ExportarCSVDialog):
    def __init__(self, parent = None):
        super(ExportarCSVDialog, self).__init__(parent)
        self.setupUi(self)
        self.canteventos = 10
    def accept(self):
        fname = QFileDialog.getSaveFileName(self, 'Exportar CSV')[0]
        tab = self.rdTab.isChecked()
        if fname != '':
            fname = fname + '.csv'
            if self.rdProcesos.isChecked():
                Exportar.exportarProcesosCSV(fname, tab)
            elif self.rdDemandantes.isChecked():
                Exportar.exportarDemandantesCSV(fname, tab)
            elif self.rdDemandados.isChecked():
                Exportar.exportarDemandadosCSV(fname, tab)
            elif self.rdJuzgados.isChecked():
                Exportar.exportarJuzgadosCSV(fname, tab)
            elif self.rdActuaciones.isChecked():
                dialogProceso = ListadoDialogo(ListadoDialogo.PROCESO)
                if dialogProceso.exec_():
                    proceso = dialogProceso.getSelected()
                    Exportar.exportarActuacionesCSV(fname, proceso, tab)
            elif self.rdActuacionesCriticas.isChecked():
                Exportar.exportarActuacionesCriticasCSV(fname, self.canteventos, tab)
        QDialog.accept(self)