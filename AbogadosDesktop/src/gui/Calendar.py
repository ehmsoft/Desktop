# -*- coding: utf-8 -*-
'''
Created on 22/03/2012

@author: harold
'''

from PySide import QtGui, QtCore
from persistence.Persistence import Persistence
from ItemListas import ItemListas
from core.CitaCalendario import CitaCalendario
from datetime import datetime
from CalendarScreen import Ui_Calendar
from CitaScreen import Ui_Cita
from gui.ListadoDialogo import ListadoDialogo
from gui.Listado import Listado
from types import NoneType

class QCalendar(QtGui.QCalendarWidget):
    def __init__(self, citas,*args, **kwargs):
        self.__citas = citas
        QtGui.QCalendarWidget.__init__(self, *args, **kwargs)
    
    def paintCell(self, painter, rect, date):
        #painter.background().setColor(QtGui.QColor('red'))
        QtGui.QCalendarWidget.paintCell(self, painter, rect, date)
        if self.en(date.toPython(), self.__citas):
            painter.setPen(QtGui.QPen(QtCore.Qt.red))
            painter.setBrush(QtGui.QBrush(QtCore.Qt.transparent))
            painter.drawRect(rect.adjusted(0,0,-1,-1))
            
    def en(self, date, citas):
        for cita in citas:
            dateCita = cita.getObjeto().getFecha().date()
            if dateCita == date:
                return True
        return False
            
class Calendar(QtGui.QDialog, Ui_Calendar):
    def __init__(self, parent = None):
        super(Calendar, self).__init__(parent)
        self.setupUi(self)
        self.__citas = self.crearCitas()
        for cita in self.__citas:
            self.lista.addItem(cita)
        self.calendario = QCalendar(self.__citas)
        self.horizontalLayout_4.addWidget(self.calendario)
        
        self.connect(self.calendario, QtCore.SIGNAL('selectionChanged()'), self.calendarSelection)
        self.connect(self.lista, QtCore.SIGNAL('itemSelectionChanged()'), self.listSelection)
        self.connect(self.btnAgregar, QtCore.SIGNAL('clicked()'), self.click)
        
        eliminar = self.createAction('Eliminar', self.eliminar)
        editar = self.createAction('Editar', self.editar)
        
        self.lista.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.lista.addActions([editar,eliminar])
    
    def eliminar(self):
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Question)
        message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        message.setDefaultButton(QtGui.QMessageBox.No)
        message.setText(unicode("¿Desea eliminar la cita?"))
        ret = message.exec_()
        if ret == QtGui.QMessageBox.Yes:
            index = self.lista.currentRow()
            item = self.lista.takeItem(index)
            del self.__citas[index]
            try:
                p = Persistence()
                p.borrarCitaCalendario(item.getObjeto().getCita())
            except Exception, e:
                print e
    
    def editar(self):
        item = self.lista.currentItem()
        index = self.lista.currentRow()
        dialog = CitaScreen(cita = item.getObjeto().getCita(), parent = self)
        if dialog.exec_():
            cita = dialog.getCita()
            self.lista.takeItem(index)
            del self.__citas[index]
            self.ubicarCita(cita)            
        
    def createAction(self, text, slot = None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action
        
    def click(self):
        procesos = ListadoDialogo(ListadoDialogo.PROCESO, self)
        if procesos.exec_():
            proceso = procesos.getSelected()
            actuaciones = DialogoActuaciones(proceso, self)
            if actuaciones.exec_():
                actuacion = actuaciones.getSelected()
                dialogo = CitaScreen(actuacion = actuacion, parent = self)
                if dialogo.exec_():
                    cita = dialogo.getCita()
                    self.ubicarCita(cita)
                dialogo.setParent(None)
                actuaciones.setParent(None)
                procesos.setParent(None)
                
    def ubicarCita(self, cita):
        dateCita = cita.getFecha()
        index = len(self.__citas)
        for c in self.__citas:
            dateCitas = c.getObjeto().getFecha()
            if dateCita < dateCitas:
                index = self.__citas.index(c)
                break
        if index == len(self.__citas):
            item = ItemListas(Cita(cita),self.lista)
            self.__citas.append(item)
            self.lista.addItem(item)
        else:
            item = ItemListas(Cita(cita),self.lista)
            self.__citas.insert(index, item)
            while self.lista.count() != 0:
                self.lista.takeItem(0)
            for cita in self.__citas:
                self.lista.addItem(cita)
            
        
    def calendarSelection(self):
        selectedDate = self.calendario.selectedDate().toPython()
        for cita in self.__citas:
            date = cita.getObjeto().getFecha().date()
            if selectedDate == date:
                self.lista.setCurrentItem(cita)
                break
            
    def listSelection(self):
        item = self.lista.currentItem()
        if not isinstance(item, NoneType):
            selectedDate = item.getObjeto().getFecha().date()
            if selectedDate != self.calendario.selectedDate().toPython():
                self.calendario.setSelectedDate(selectedDate)        
        
    def crearCitas(self):
        try:
            p = Persistence()
            citas = p.consultarCitasCalendario()
            r = []
            for cita in citas:
                c = Cita(cita)
                item = ItemListas(c, self.lista)
                r.append(item)
            return r
        except Exception, e:
            print e
            
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
        
        
class Cita(object):
    def __init__(self, cita):
        actuacion = None
        try:
            p = Persistence()
            actuacion = p.consultarActuacion(cita.getId_actuacion())
        except Exception, e:
            print e, e.args, e.message
            
        self.__descripcion = actuacion.getDescripcion()
        self.__fecha = cita.getFecha()
        self.__anticipacion = cita.getAnticipacion()
        self.__cita = cita
        
    def getCita(self):
        return self.__cita
        
    def getDescripcion(self):
        return self.__descripcion
    
    def getFecha(self):
        return self.__fecha
    
    def getAnticipacion(self):
        return self.__anticipacion
    
    def transAnticipacion(self, ant):
        if ant < 3600:
            if ant == 60:
                return '1 minuto'
            else:
                return '%i minutos' % (ant / 60)
        elif ant < 86400:
            if ant == 3600:
                return '1 hora'
            else:
                return '%i horas' % (ant / 3600)
        else:
            if ant == 86400:
                return '1 día'
            else:
                return '%i días' % (ant / 86400)
    
    def __str__(self):
        return 'Descripción: %s\nFecha: %s\nAnticipación: %s' % (self.__descripcion, '{:%d/%m/%Y %I:%M %p}'.format(self.__fecha), self.transAnticipacion(self.__anticipacion))

class CitaScreen(QtGui.QDialog, Ui_Cita):
    def __init__(self,actuacion = None, cita = None,parent = None):
        super(CitaScreen, self).__init__(parent)
        self.setupUi(self)
        self.cita = cita
        self.fecha.setDateTime(datetime.today())
        self.actuacion = actuacion
        
        if cita == None:        
            self.fecha.setDateTime(self.actuacion.getFechaProxima())
        else:
            try:
                p = Persistence()
                self.actuacion = p.consultarActuacion(self.cita.getId_actuacion())
            except Exception, e:
                print e
            self.fecha.setDateTime(self.cita.getFecha())
            ant = self.transAnticipacion(self.cita.getAnticipacion())
            self.comboAnticipacion.setCurrentIndex(self.comboAnticipacion.findText(ant[1]))
            self.spinAnticipacion.setValue(ant[0])
        self.calendar.setSelectedDate(self.fecha.date())
        self.descripcion.setText(self.actuacion.getDescripcion())        
        
        self.connect(self.calendar, QtCore.SIGNAL('selectionChanged()'), self.calendarSelection)
        self.connect(self.fecha, QtCore.SIGNAL('dateChanged(QDate)'), self.fechaSelection)
        
    def calendarSelection(self):
        self.fecha.setDate(self.calendar.selectedDate())
        
    def fechaSelection(self, selected):
        if self.calendar.selectedDate() != self.fecha.date():
            self.calendar.setSelectedDate(selected)
            
    def getAnticipacion(self):
        escala = self.comboAnticipacion.currentText()
        ant = self.spinAnticipacion.value()
        if escala == 'minutos':
            return ant * 60
        elif escala == 'horas':
            return ant * 3600
        elif escala == 'días':
            return ant * 86400
        else:
            raise TypeError('Error en valores')
        
    def transAnticipacion(self, ant):
        if ant < 3600:
            return (ant / 60, 'minutos')
        elif ant < 86400:
            return (ant / 3600, 'horas')
        else:
            return (ant / 86400, 'días')
        
    def guardar(self):
        fecha = self.fecha.dateTime().toPython()
        anticipacion = self.getAnticipacion()
        if self.cita == None:
            self.cita = CitaCalendario(fecha = fecha, anticipacion = anticipacion, id_cita = None, 
                              id_actuacion = self.actuacion.getId_actuacion(),uid = '')
        else:
            self.cita.setFecha(fecha)
            self.cita.setAnticipacion(anticipacion)
        try:
            p = Persistence()
            if self.cita.getId_cita() == None:
                p.guardarCitaCalendario(self.cita)
            else:
                p.actualizarCitaCalendario(self.cita)
            return QtGui.QDialog.accept(self)
        except Exception, e:
            print e
            return QtGui.QDialog.reject(self)

            
    def accept(self):
        self.guardar()
            
    def getCita(self):
        return self.cita
    
import sys
        
app = QtGui.QApplication(sys.argv)
form = Calendar()
form.show()
app.exec_()
