# -*- coding: utf-8 -*-
'''
Created on 4/04/2012

@author: esteban
'''
from PreferenciasScreen import Ui_Form
from PySide import QtGui, QtCore
from core.Preferencias import Preferencias
from persistence.Persistence import Persistence
class Preferencias_GUI(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        self.preferencia = Preferencias()
        super(Preferencias_GUI, self).__init__(parent)
        self.setupUi(self)
        self.BorrarEventosBtn.clicked.connect(self.borrarEventos)
        self.OrdenArribaBtn.clicked.connect(self.listaArriba)
        self.OrdenAbajoBtn.clicked.connect(self.listaAbajo)       
        self.OrdenRestablecerBtn.clicked.connect(self.restablecerLista)
        self.GuardarBtn.clicked.connect(self.guardar)
        alarma = self.preferencia.getTipoAlarma()
        self.cantidadEventosSpin.setValue(self.preferencia.getCantidadEventos())
        if alarma == 0:
            self.alarmaMenEmergente.setChecked(False)
            self.alarmaIcono.setChecked(False)
        elif alarma == 1:
            self.alarmaMenEmergente.setChecked(True)
            self.alarmaIcono.setChecked(True)
        
        elif alarma == 2:
            self.alarmaMenEmergente.setChecked(True)
            self.alarmaIcono.setChecked(False)
        elif alarma == 3:
            self.alarmaMenEmergente.setChecked(False)
            self.alarmaIcono.setChecked(True)
        self.cantCopiaSegSpin.setValue(self.preferencia.getCantCopiaSeg())
        self.OrdenarListaMainApp()
        
    def borrarEventos(self):
        p = Persistence()
        p.borrarEventosVencidos()
        
    def listaArriba(self):
        flag = False
        row = self.listaMainApp.currentRow()
        if row == 0:
            return
        current = self.listaMainApp.currentItem()
        currentText = current.text()
        if hasattr(current, 'codigo'):
            currentCode = current.codigo
            flag= True
        next = self.listaMainApp.item(row - 1)
        current.setText(next.text())
        if hasattr(next, 'codigo'):
            current.codigo = next.codigo
        next.setText(currentText)
        if flag:
            next.codigo = currentCode
        self.listaMainApp.setCurrentRow(row - 1)
        
        
    def listaAbajo(self):
        row = self.listaMainApp.currentRow()
        if row == self.listaMainApp.count()-1:
            return
        current = self.listaMainApp.currentItem()
        currentText = current.text()
        if hasattr(current, 'codigo'):
            currentCode = current.codigo
            flag= True
        next = self.listaMainApp.item(row + 1)
        current.setText(next.text())
        if hasattr(next, 'codigo'):
            current.codigo = next.codigo
        
        next.setText(currentText)
        if flag:
            next.codigo = currentCode
        self.listaMainApp.setCurrentRow(row + 1)
        
        
        
    def restablecerLista(self):
        eventos = QtGui.QListWidgetItem(Preferencias.TXTEVENTOS)
        eventos.codigo = 20111
        procesos = QtGui.QListWidgetItem(Preferencias.TXTPROCESOS)
        procesos.codigo = 20105
        plantillas = QtGui.QListWidgetItem(Preferencias.TXTPLANTILLAS)
        plantillas.codigo = 20115
        demandantes = QtGui.QListWidgetItem(Preferencias.TXTDEMANDANTES)
        demandantes.codigo = 20114
        demandados = QtGui.QListWidgetItem(Preferencias.TXTDEMANDADOS)
        demandados.codigo = 20124
        juzgados = QtGui.QListWidgetItem(Preferencias.TXTJUZGADOS)
        juzgados.codigo = 20103
        actuaciones = QtGui.QListWidgetItem(Preferencias.TXTACTUACIONES)
        actuaciones.codigo = 20101
        categorias = QtGui.QListWidgetItem(Preferencias.TXTCATEGORIAS)
        categorias.codigo = 20107
        campos = QtGui.QListWidgetItem(Preferencias.TXTCAMPOS)
        campos.codigo = 20102
        sincronizar = QtGui.QListWidgetItem(Preferencias.TXTSINCRONIZAR)
        sincronizar.codigo = 20108
        ajustes = QtGui.QListWidgetItem(Preferencias.TXTAJUSTES)
        ajustes.codigo = 20109
        
        lista = [eventos, procesos, plantillas, demandantes, demandados,juzgados, actuaciones,categorias,campos, sincronizar, ajustes]
        for i in range(len(lista)):
            self.listaMainApp.takeItem(0)
        for i in lista:
            self.listaMainApp.addItem(i)
            
    def guardar(self):
        cantEventos = self.cantidadEventosSpin.value()
        mensajeEmergente = self.alarmaMenEmergente.isChecked()
        alarmaIcono = self.alarmaIcono.isChecked()
        cantCopias = self.cantCopiaSegSpin.value()
        listaMainApp = []
        for i in range(self.listaMainApp.count()):
            item = self.listaMainApp.item(i)
            if hasattr(item, 'codigo'):
                listaMainApp.append(item.codigo)
        if mensajeEmergente is True:
            if alarmaIcono is True:
                self.preferencia.setTipoAlarma(tipoAlarma=1)
            else:
                self.preferencia.setTipoAlarma(tipoAlarma=2)
        else:
            if alarmaIcono is True:
                self.preferencia.setTipoAlarma(tipoAlarma=3)
            else:
                self.preferencia.setTipoAlarma(tipoAlarma=0)
        self.preferencia.setCantidadEventos(cantidadEventos = cantEventos)
        self.preferencia.setCantCopiaSeg(cantCopiaSeg = cantCopias)
        self.preferencia.setListaMainApp(listaMainApp = listaMainApp)
        
    def OrdenarListaMainApp(self):
        for item in self.preferencia.getListaMainApp():
            if item == 20111:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTEVENTOS)
                elemento.codigo = 20111
                self.listaMainApp.addItem(elemento)
            elif item == 20105:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTPROCESOS)
                elemento.codigo = 20105
                self.listaMainApp.addItem(elemento)
            elif item == 20115:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTPLANTILLAS)
                elemento.codigo = 20115
                self.listaMainApp.addItem(elemento)
            elif item == 20114:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTDEMANDANTES)
                elemento.codigo = 20114
                self.listaMainApp.addItem(elemento)
            elif item == 20124:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTDEMANDADOS)
                elemento.codigo = 20124
                self.listaMainApp.addItem(elemento)
            elif item == 20103:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTJUZGADOS)
                elemento.codigo = 20103
                self.listaMainApp.addItem(elemento)
            elif item == 20101:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTACTUACIONES)
                elemento.codigo = 20101
                self.listaMainApp.addItem(elemento)
            elif item == 20107:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTCATEGORIAS)
                elemento.codigo = 20107
                self.listaMainApp.addItem(elemento)
            elif item == 20102:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTCAMPOS)
                elemento.codigo = 20102
                self.listaMainApp.addItem(elemento)
            elif item == 20108:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTSINCRONIZAR)
                elemento.codigo = 20108
                self.listaMainApp.addItem(elemento)
            elif item == 20109:
                elemento = QtGui.QListWidgetItem(Preferencias.TXTAJUSTES)
                elemento.codigo = 20109
                self.listaMainApp.addItem(elemento)
