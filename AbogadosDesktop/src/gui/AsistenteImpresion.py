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
import qrcode

class AsistenteImpresion(QDialog, Ui_AsistenteImpresionDialog):
    def __init__(self, parent=None):
        super(AsistenteImpresion, self).__init__(parent)
        self.setupUi(self)
        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPageSize(QPrinter.Letter)
    
    def accept(self):
        QDialog.accept(self)
        if self.rdProceso.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.PROCESO)
            if dialogo.exec_():
                proceso = dialogo.getSelected()
                MostrarImpresion(html=Impresion().imprimirProceso(proceso=proceso)).exec_()
                del proceso
            del dialogo
            
        elif self.rdJuzgado.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.JUZGADO)
            if dialogo.exec_():
                juzgado = dialogo.getSelected()
                MostrarImpresion(html=Impresion().imprimirJuzgado(juzgado=juzgado)).exec_()
                del juzgado
            del dialogo
            
        elif self.rdDemandante.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.DEMANDANTE)
            if dialogo.exec_():
                demandante = dialogo.getSelected()
                MostrarImpresion(html=Impresion().imprimirPersona(persona=demandante)).exec_()
                del demandante
            del dialogo
            
        elif self.rdDemandado.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.DEMANDADO)
            if dialogo.exec_():
                demandado = dialogo.getSelected()
                MostrarImpresion(html=Impresion().imprimirPersona(persona=demandado)).exec_()
                del demandado
            del dialogo
            
        elif self.rdQR.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.PROCESO)
            if dialogo.exec_():
                proceso = dialogo.getSelected()
                self.printer = QPrinter(QPrinter.HighResolution)
                self.printer.setPageSize(QPrinter.Letter)
                dialog = QPrintDialog(self.printer, self)
                if proceso:
                    if dialog.exec_():
                        qr = qrcode.make('id_proceso:'+proceso.getId_proceso())
                        image = QImage()
                        if hasattr(qr, 'tobitmap'):
                            image.loadFromData(QByteArray(qr.tobitmap()), "XBM")
                        else:
                            image.loadFromData(QByteArray(qr._img.tobitmap()), "XBM")
                        image.invertPixels()
                        painter = QPainter(self.printer)
                        width = image.width() *6
                        height = image.height() *6
                        painter.drawImage(0, 0, image.scaled(width, height))
                del proceso
                del dialog
            del dialogo
            
        elif self.rdListadoProcesos.isChecked():
            dialogo = ListadoDialogoMultipleSeleccion(ListadoDialogoMultipleSeleccion.PROCESO)
            if dialogo.exec_():
                procesos = dialogo.getSelected()
                if len(procesos) > 0:
                    MostrarImpresion(html=Impresion().imprimirProcesos(procesos=procesos), landscape=True).exec_()
                del procesos
            del dialogo
            
        elif self.rdListadoJuzgados.isChecked():
            dialogo = ListadoDialogoMultipleSeleccion(ListadoDialogoMultipleSeleccion.JUZGADO)
            if dialogo.exec_():
                juzgados = dialogo.getSelected()
                if len(juzgados) > 0:
                    MostrarImpresion(html=Impresion().imprimirJuzgados(juzgados=juzgados), landscape=True).exec_()
                del juzgados
            del dialogo
            
        elif self.rdListadoDemandantes.isChecked():
            dialogo = ListadoDialogoMultipleSeleccion(ListadoDialogoMultipleSeleccion.DEMANDANTE)
            if dialogo.exec_():
                demandantes = dialogo.getSelected()
                if len(demandantes) > 0:
                    MostrarImpresion(html=Impresion().imprimirPersonas(tipo=1, personas=demandantes), landscape=True).exec_()
                del demandantes
            del dialogo
            
        elif self.rdListadoDemandados.isChecked():
            dialogo = ListadoDialogoMultipleSeleccion(ListadoDialogoMultipleSeleccion.DEMANDADO)
            if dialogo.exec_():
                demandados = dialogo.getSelected()
                if len(demandados) > 0:
                    MostrarImpresion(html=Impresion().imprimirPersonas(tipo=2, personas=demandados), landscape=True).exec_()
                del demandados
            del dialogo
            
        elif self.rdListadoActuaciones.isChecked():
            dialogo = ListadoDialogo(ListadoDialogo.PROCESO)
            if dialogo.exec_():
                proceso = dialogo.getSelected()
                MostrarImpresion(html=Impresion().imprimirActuaciones(proceso=proceso), landscape=True).exec_()
                del proceso
            del dialogo
            
        elif self.rdEventosProximos.isChecked():
            MostrarImpresion(html=Impresion().imprimirEventosProximos(), landscape=True).exec_()