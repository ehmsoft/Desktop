# -*- coding: utf-8 -*-
'''
Created on 26/03/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from AsistenteImpresionScreen import Ui_AsistenteImpresionDialog
from gui.ListadoDialogoMultipleSeleccion import ListadoDialogoMultipleSeleccion
from gui.ListadoDialogo import ListadoDialogo
from impresion.MostrarImpresion import MostrarImpresion
from impresion.Impresion import Impresion

class AsistenteImpresion(QDialog, Ui_AsistenteImpresionDialog):
    def __init__(self, parent=None):
        super(AsistenteImpresion, self).__init__(parent)
        self.setupUi(self)
        
    
    def accept(self):
        QDialog.accept(self)
        if self.rdProceso.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.PROCESO)
            if dialogo.exec_():
                proceso = dialogo.getSelected()
                Impresion().imprimirProceso(proceso=proceso)
                del proceso
            del dialogo
            
        elif self.rdJuzgado.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.JUZGADO)
            if dialogo.exec_():
                juzgado = dialogo.getSelected()
                Impresion().imprimirJuzgado(juzgado=juzgado)
                del juzgado
            del dialogo
            
        elif self.rdDemandante.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.DEMANDANTE)
            if dialogo.exec_():
                demandante = dialogo.getSelected()
                Impresion().imprimirPersona(persona=demandante)
                del demandante
            del dialogo
            
        elif self.rdDemandado.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.DEMANDADO)
            if dialogo.exec_():
                demandado = dialogo.getSelected()
                Impresion().imprimirPersona(persona=demandado)
                del demandado
            del dialogo
            
        elif self.rdQR.isChecked():
            pass
        
        elif self.rdListadoProcesos.isChecked():
            dialogo = ListadoDialogoMultipleSeleccion(ListadoDialogoMultipleSeleccion.PROCESO)
            if dialogo.exec_():
                procesos = dialogo.getSelected()
                if len(procesos) > 0:
                    Impresion().imprimirProcesos(procesos=procesos)
                del procesos
            del dialogo
            
        elif self.rdListadoJuzgados.isChecked():
            dialogo = ListadoDialogoMultipleSeleccion(ListadoDialogoMultipleSeleccion.JUZGADO)
            if dialogo.exec_():
                juzgados = dialogo.getSelected()
                if len(juzgados) > 0:
                    Impresion().imprimirJuzgados(juzgados=juzgados)
                del juzgados
            del dialogo
            
        elif self.rdListadoDemandantes.isChecked():
            dialogo = ListadoDialogoMultipleSeleccion(ListadoDialogoMultipleSeleccion.DEMANDANTE)
            if dialogo.exec_():
                demandantes = dialogo.getSelected()
                if len(demandantes) > 0:
                    Impresion().imprimirPersonas(tipo=1, personas=demandantes)
                del demandantes
            del dialogo
            
        elif self.rdListadoDemandados.isChecked():
            dialogo = ListadoDialogoMultipleSeleccion(ListadoDialogoMultipleSeleccion.DEMANDADO)
            if dialogo.exec_():
                demandados = dialogo.getSelected()
                if len(demandados) > 0:
                    Impresion().imprimirPersonas(tipo=2, personas=demandados)
                del demandados
            del dialogo
            
        elif self.rdListadoActuaciones.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.PROCESO)
            if dialogo.exec_():
                proceso = dialogo.getSelected()
                print proceso
                Impresion().imprimirActuaciones(proceso=proceso)
                del proceso
            del dialogo
            
        elif self.rdEventosProximos.isChecked():
            Impresion().imprimirEventosProximos()