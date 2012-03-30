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
from Listado import Listado
from copy import deepcopy
from gui.GestorCitas import GestorCitas

class QCalendar(QtGui.QCalendarWidget):
    def __init__(self, citas = [],*args, **kwargs):
        self.__citas = citas
        QtGui.QCalendarWidget.__init__(self, *args, **kwargs)
    
    def paintCell(self, painter, rect, date):
        #painter.background().setColor(QtGui.QColor('red'))
        QtGui.QCalendarWidget.paintCell(self, painter, rect, date)
        pen = self.__en(date.toPython())
        if pen != None:
            painter.setPen(pen)
            painter.setBrush(QtGui.QBrush(QtCore.Qt.transparent))
            painter.drawRect(rect.adjusted(1,1 ,-1,-1))
            
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
    def __init__(self, parent = None):
        super(Calendar, self).__init__(parent)
        self.setupUi(self)
        self.__dia = datetime.today()
        self.__calendar = QCalendar()
        self.horizontalLayout_2.addWidget(self.__calendar)
        self.__citas = self.__cargarCitas()
        for cita in self.__citas:
            if cita.getFecha() > datetime.today():
                self.__calendar.setSelectedDate(cita.getFecha().date())
        else:
            self.__calendar.setSelectedDate(datetime.today().date())
        self.__montarTodas()
        self.__montarDia()
        self.__calendar.setCitas(self.__citas)
        
        self.__calendar.clicked.connect(self.__clickCalendar)
        self.btnAgregar.clicked.connect(self.__clickBtn)
        self.btnAgregar2.clicked.connect(self.__clickBtn)
        self.tabWidget.currentChanged.connect(self.__tabClicked)
        self.lista.currentItemChanged.connect(self.__clickLista)
        
        actionEliminar = QtGui.QAction('Eliminar',self)
        actionEliminar.setToolTip('Elimina definitivamente la cita')
        self.connect(actionEliminar, QtCore.SIGNAL('triggered()'), self.__eliminar)
        actionEditar = QtGui.QAction('Editar', self)
        actionEditar.setToolTip('Lanza la ventana de edición de la cita seleccionada')
        self.connect(actionEditar, QtCore.SIGNAL('triggered()'), self.__editar)
        
        self.lista.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lista.addActions([actionEliminar, actionEditar])
        
        self.lista2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lista2.addActions([actionEliminar, actionEditar])
        
    def __clickLista(self,current, previous):
        if current is not None:
            fecha = current.getObjeto().getFecha().date()
            self.__calendar.setSelectedDate(fecha)
        
    def __eliminar(self):
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Question)
        message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        message.setDefaultButton(QtGui.QMessageBox.No)
        message.setText(unicode("¿Desea eliminar la cita?"))
        ret = message.exec_()
        if ret == QtGui.QMessageBox.Yes:
            if self.tabWidget.currentIndex() == 0:
                cita = self.lista.currentItem().getObjeto()
            else:
                cita = self.lista2.currentItem().getObjeto()
            try:
                p = Persistence()
                p.borrarCitaCalendario(cita)
                self.__citas.remove(cita)
                self.__montarTodas()
                self.__montarDia(self.__dia)
                self.__redibujar()          
            except Exception as e:
                print e
    
    def __editar(self):
        if self.tabWidget.currentIndex() == 0:
            cita = self.lista.currentItem().getObjeto()
        else:
            cita = self.lista2.currentItem().getObjeto()
        editar = NuevaCita(cita = cita, parent = self)
        if editar.exec_():
            self.__montarTodas()
            self.__montarDia(self.__dia)
            self.__redibujar()
        
    def __tabClicked(self, index):
        if index == 1:
            self.__calendar.setSelectedDate(self.__dia)
        
    def __clickBtn(self):
        procesos = ListadoDialogo(ListadoDialogo.PROCESO, self)
        if procesos.exec_():
            proceso = procesos.getSelected()
            actuaciones = DialogoActuaciones(proceso, self)
            if actuaciones.exec_():
                actuacion = actuaciones.getSelected()
                dialogo = NuevaCita(actuacion = actuacion, parent = self)
                if dialogo.exec_():
                    cita = dialogo.getCita()
                    self.__ubicarCita(cita)
                    self.__redibujar()
                dialogo.setParent(None)
            actuaciones.setParent(None)
        procesos.setParent(None)
                    
    def __ubicarCita(self, cita):
        for c in self.__citas:
            if cita <= c:
                index = self.__citas.index(c)
                self.__citas.insert(index, cita)
                break
        else:
            self.__citas.append(cita) 
    
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
        
    def __cargarCitas(self):
        try:
            p = Persistence()
            citas = p.consultarCitasCalendario()
            return citas
        except Exception as e:
            print e
            
    def __montarTodas(self):
        self.__citas = self.__cargarCitas()
        while self.lista.count() > 0:
            self.lista.takeItem(0)
        for cita in self.__citas:
            self.lista.addItem(ItemListas(cita, self.lista))
    
    def __montarDia(self, date = None):
        self.__citas = self.__cargarCitas()
        while self.lista2.count() > 0:
            self.lista2.takeItem(0)
        if date == None:
            for cita in self.__citas:
                if cita.getFecha() > datetime.today():
                    self.__dia = date = cita.getFecha().date()
            else:
                date = datetime.today().date()
        else:
            if not isinstance(date, DATE):
                self.__dia = date.date()
            else:
                self.__dia = date
        self.tabWidget.setTabText(1,'{:%d/%m/%Y}'.format(date))
        for cita in self.__citas:
            dateCita = cita.getFecha().date()
            if date == dateCita:
                c = deepcopy(cita)
                c.setConFecha(False)
                self.lista2.addItem(ItemListas(c,self.lista2))
            
class DialogoActuaciones(QtGui.QDialog):
    def __init__(self, proceso,parent = None):
        super(DialogoActuaciones, self).__init__(parent)
        listado = Listado(proceso.getActuaciones())
        layout = QtGui.QVBoxLayout()
        layout.addWidget(listado)
        self.setLayout(layout)
        self.selected = None
        
        #self.connect(listado, QtCore.SIGNAL('itemClicked(QtGui.QListWidgetItem)'), self.click)
        listado.itemClicked.connect(self.click)
        
    def click(self, item):
        self.selected = item.getObjeto()
        self.accept()
        
    def getSelected(self):
        return self.selected
    
import sys
        
app = QtGui.QApplication(sys.argv)
form = Calendar()
form.show()
app.exec_()
