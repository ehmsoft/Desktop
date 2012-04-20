# -*- coding: utf-8 -*-
'''
Created on 4/04/2012

@author: esteban
'''
from PreferenciasScreen import Ui_Form
from PySide import QtGui, QtCore
from core.Preferencias import Preferencias
import MainApp

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
        
        
    def borrarEventos(self):
        
        print 'borrado'
        
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
        lista = [MainApp.MainApp.TXTEVENTOS,MainApp.MainApp.TXTPROCESOS, MainApp.MainApp.TXTPLANTILLAS, MainApp.MainApp.TXTDEMANDANTES, MainApp.MainApp.TXTDEMANDADOS, MainApp.MainApp.TXTJUZGADOS, MainApp.MainApp.TXTACTUACIONES, MainApp.MainApp.TXTCATEGORIAS, MainApp.MainApp.TXTCAMPOS, MainApp.MainApp.TXTSINCRONIZAR, MainApp.MainApp.TXTAJUSTES]
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
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTEVENTOS)
                elemento.codigo = 20111
                self.listaMainApp.addItem(elemento)
            elif item == 20105:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTPROCESOS)
                elemento.codigo = 20105
                self.listaMainApp.addItem(elemento)
            elif item == 20115:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTPLANTILLAS)
                elemento.codigo = 20115
                self.listaMainApp.addItem(elemento)
            elif item == 20114:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTDEMANDANTES)
                elemento.codigo = 20114
                self.listaMainApp.addItem(elemento)
            elif item == 20124:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTDEMANDADOS)
                elemento.codigo = 20124
                self.listaMainApp.addItem(elemento)
            elif item == 20103:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTJUZGADOS)
                elemento.codigo = 20103
                self.listaMainApp.addItem(elemento)
            elif item == 20101:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTACTUACIONES)
                elemento.codigo = 20101
                self.listaMainApp.addItem(elemento)
            elif item == 20107:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTCATEGORIAS)
                elemento.codigo = 20107
                self.listaMainApp.addItem(elemento)
            elif item == 20102:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTCAMPOS)
                elemento.codigo = 20102
                self.listaMainApp.addItem(elemento)
            elif item == 20108:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTSINCRONIZAR)
                elemento.codigo = 20108
                self.listaMainApp.addItem(elemento)
            elif item == 20109:
                elemento = QtGui.QListWidgetItem(MainApp.MainApp.TXTAJUSTES)
                elemento.codigo = 20109
                self.listaMainApp.addItem(elemento)
