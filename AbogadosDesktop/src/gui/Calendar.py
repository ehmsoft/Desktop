# -*- coding: utf-8 -*-
'''
Created on 22/03/2012

@author: harold
'''

from PySide import QtGui, QtCore
from persistence.Persistence import Persistence
from ItemListas import ItemListas
from datetime import datetime
from datetime import date as DATE
from CalendarScreen import Ui_Calendar
from gui.nuevo.NuevaCita import NuevaCita
from gui.ListadoDialogo import ListadoDialogo
from copy import deepcopy
from gui.GestorCitas import GestorCitas
from datetime import timedelta

class QCalendar(QtGui.QCalendarWidget):
    def __init__(self, citas=[], *args, **kwargs):
        self.__citas = citas
        QtGui.QCalendarWidget.__init__(self, *args, **kwargs)
    
    def paintCell(self, painter, rect, date):
        #painter.background().setColor(QtGui.QColor('red'))
        QtGui.QCalendarWidget.paintCell(self, painter, rect, date)
        pen = self.__en(date.toPython())
        if pen != None:
            painter.setPen(pen)
            painter.setBrush(QtGui.QBrush(QtCore.Qt.transparent))
            painter.drawRect(rect.adjusted(1, 1 , -1, -1))
            
    def __en(self, date):
        cuantas = 0
        for cita in self.__citas:
            dateCita = cita.getFecha().date()
            if dateCita == date:
                cuantas += 1
        if cuantas >= 1:
            if date < datetime.today().date():
                return QtGui.QPen(QtCore.Qt.gray)
            elif cuantas == 1:
                return QtGui.QPen(QtCore.Qt.red)
            elif cuantas > 1:
                return QtGui.QPen(QtCore.Qt.blue)
            else:
                return None  
    
    def setCitas(self, citas):
        self.__citas = citas
        self.repaint()
            
class Calendar(QtGui.QDialog, Ui_Calendar):
    def __init__(self, parent=None):
        super(Calendar, self).__init__(parent)
        self.setupUi(self)
        self.__dia = datetime.today()
        self.__calendar = QCalendar()
        self.horizontalLayout_2.addWidget(self.__calendar)
        self.__citas = self.__cargarCitas()
        for cita in self.__citas:
            fechamas = cita.getFecha() + timedelta(0, cita.getAnticipacion())
            toda = datetime.today()
            if fechamas > toda:
                self.__calendar.setSelectedDate(cita.getFecha().date())
                break
        else:
            self.__calendar.setSelectedDate(datetime.today().date())
        self.__montarTodas()
        self.__montarDia()
        
        self.__calendar.clicked.connect(self.__clickCalendar)
        self.btnAgregar.clicked.connect(self.__clickBtn)
        self.btnAgregar2.clicked.connect(self.__clickBtn)
        self.tabWidget.currentChanged.connect(self.__tabClicked)
        self.lista.currentItemChanged.connect(self.__clickLista)
        
        actionEliminar = QtGui.QAction('Eliminar', self)
        actionEliminar.setToolTip('Elimina definitivamente la cita')
        self.connect(actionEliminar, QtCore.SIGNAL('triggered()'), self.__eliminar)
        actionEditar = QtGui.QAction('Editar', self)
        actionEditar.setToolTip(u'Lanza la ventana de edición de la cita seleccionada')
        self.connect(actionEditar, QtCore.SIGNAL('triggered()'), self.__editar)
        self.btnEliminar.clicked.connect(self.__clickEliminar)
        
        self.lista.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lista.addActions([actionEliminar, actionEditar])
        
        self.lista2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lista2.addActions([actionEliminar, actionEditar])
        
        self.lista3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lista3.addActions([actionEliminar, actionEditar])
        
        gestor = GestorCitas()
        gestor.registrarCallBack(self.callBack)
        
    def callBack(self):
        self.__redibujar()
        
    def __clickEliminar(self):
        items = self.lista3.selectedItems()
        if len(items) != 0:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Question)
            message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            message.setDefaultButton(QtGui.QMessageBox.No)
            message.setText(u'¿Desea eliminar las citas seleccionadas?')
            ret = message.exec_()
            if ret == QtGui.QMessageBox.Yes:
                p = Persistence()
                for item in items:
                    p.borrarCitaCalendario(item.getObjeto())
                    self.__citas.remove(item.getObjeto())
                self.__redibujar()
        else:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Question)
            message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            message.setDefaultButton(QtGui.QMessageBox.No)
            message.setText(u"¿Desea eliminar todas las citas vencidas?")
            ret = message.exec_()
            if ret == QtGui.QMessageBox.Yes:
                p = Persistence()
                while self.lista3.count() > 0:
                    item = self.lista3.takeItem(0)
                    p.borrarCitaCalendario(item.getObjeto())
                    self.__citas.remove(item.getObjeto())
                self.__redibujar()          
                    
        
    def __clickLista(self, current, previous):
        if current is not None:
            fecha = current.getObjeto().getFecha().date()
            self.__calendar.setSelectedDate(fecha)
        
    def __eliminar(self):
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Question)
        message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        message.setDefaultButton(QtGui.QMessageBox.No)
        message.setText(u"¿Desea eliminar la cita?")
        ret = message.exec_()
        if ret == QtGui.QMessageBox.Yes:
            if self.tabWidget.currentIndex() == 0:
                cita = self.lista.currentItem().getObjeto()
            elif self.tabWidget.currentIndex() == 1:
                cita = self.lista2.currentItem().getObjeto()
            else:
                cita = self.lista3.currentItem().getObjeto()
            try:
                p = Persistence()
                p.borrarCitaCalendario(cita)
                self.__citas.remove(cita)
                self.__redibujar()          
            except Exception as e:
                print e
    
    def __editar(self):
        if self.tabWidget.currentIndex() == 0:
            cita = self.lista.currentItem().getObjeto()
        elif self.tabWidget.currentIndex() == 1:
            cita = self.lista2.currentItem().getObjeto()
        else:
            cita = self.lista3.currentItem().getObjeto()
        editar = NuevaCita(cita=cita, parent=self, isGuardar=True)
        if editar.exec_():
            self.__redibujar()
        
    def __tabClicked(self, index):
        if index == 1:
            self.__calendar.setSelectedDate(self.__dia)
        
    def __clickBtn(self):
        procesos = ListadoDialogo(ListadoDialogo.PROCESO, self)
        if procesos.exec_():
            proceso = procesos.getSelected()
            actuaciones = ListadoDialogo(tipo = ListadoDialogo.ACTUACION, parent = self, proceso = proceso)
            if actuaciones.exec_():
                actuacion = actuaciones.getSelected()
                if not self.hasCita(actuacion.getId_actuacion()):
                    if hasattr(actuacion, 'cita'):
                        cita1 = actuacion.cita
                    else:
                        cita1 = None
                    dialogo = NuevaCita(actuacion=actuacion, cita=cita1, parent=self)
                    if dialogo.exec_():
                        #cita = dialogo.getCita()
                        #self.__ubicarCita(cita)
                        self.__redibujar()
                    dialogo.setParent(None)
                else:
                    QtGui.QMessageBox.information(self,'Error', u'La actuación ya tiene una cita asignada')
            actuaciones.setParent(None)
        procesos.setParent(None)
        
    def hasCita(self, id_actuacion):
        for cita in self.__citas:
            if cita.getId_actuacion() == id_actuacion:
                return True
        else:
            return False
                    
    def __ubicarCita(self, cita):
        if cita not in self.__citas:
            for c in self.__citas:
                if cita <= c:
                    index = self.__citas.index(c)
                    self.__citas.insert(index, cita)
                    break
            else:
                self.__citas.append(cita)
        else:
            QtGui.QMessageBox.information(self, 'Error', u'La actuación seleccionada ya tiene cita asociada')
    
    def __redibujar(self):
        gestor = GestorCitas(self)
        gestor.actualizarCitas() 
        self.__montarTodas()
        self.__montarDia(self.__dia)
        
    def __clickCalendar(self):
        date = self.__calendar.selectedDate().toPython()
        for cita in self.__citas:
            if date == cita.getFecha().date():
                self.__montarDia(date)
                self.tabWidget.setCurrentIndex(1)
                break
    def __compararCitas(self, a, b):
        return int((a.getFecha() - b.getFecha()).total_seconds())
    
        
    def __cargarCitas(self):
        try:
            p = Persistence()
            citas = sorted(p.consultarCitasCalendario(), self.__compararCitas)
            self.__calendar.setCitas(citas)
            return citas
        except Exception as e:
            print e
            
    def reject(self, *args, **kwargs):
        gestor = GestorCitas()
        gestor.retirarCallBack()
        return QtGui.QDialog.reject(self, *args, **kwargs)
            
    def __montarTodas(self):
        self.__citas = self.__cargarCitas()
        while self.lista.count() > 0:
            self.lista.takeItem(0)
        while self.lista3.count() > 0:
            self.lista3.takeItem(0)
        for cita in self.__citas:
            if cita.getFecha() > datetime.today():
                item = ItemListas(cita, self.lista)
                self.lista.addItem(item)
                self.lista.setCurrentItem(item)
            else:
                item = ItemListas(cita, self.lista3)
                self.lista3.addItem(item)
    
    def __montarDia(self, date=None):
        self.__citas = self.__cargarCitas()
        while self.lista2.count() > 0:
            self.lista2.takeItem(0)
        if not date:
            for cita in self.__citas:
                if cita.getFecha() - timedelta(0, cita.getAnticipacion()) > datetime.today():
                    self.__dia = date = cita.getFecha().date()
                    break
            else:
                date = DATE.today()
        else:
            if isinstance(date, datetime):
                self.__dia = date = date.date()
            else:
                self.__dia = date
        self.tabWidget.setTabText(1, '{:%d/%m/%Y}'.format(date))
        for cita in self.__citas:
            dateCita = cita.getFecha().date()
            if date == dateCita:
                c = deepcopy(cita)
                c.setConFecha(False)
                self.lista2.addItem(ItemListas(c, self.lista2))