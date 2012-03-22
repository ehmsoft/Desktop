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
        self.lista.addItems(self.__citas)
        self.calendario = QCalendar(self.__citas)
        self.horizontalLayout_4.addWidget(self.calendario)
        
        self.connect(self.calendario, QtCore.SIGNAL('selectionChanged()'), self.calendarSelection)
        self.connect(self.lista, QtCore.SIGNAL('itemSelectionChanged()'), self.listSelection)
        self.connect(self.btnAgregar, QtCore.SIGNAL('clicked()'), self.click)
        
    def click(self):
        procesos = ListadoDialogo(ListadoDialogo.PROCESO, self)
        if procesos.exec_():
            proceso = procesos.getSelected()
            actuaciones = Listado(proceso.getActuaciones())
            actuaciones.show()
        dialogo = CitaScreen()
        print dialogo.exec_()
        
    def calendarSelection(self):
        selectedDate = self.calendario.selectedDate().toPython()
        for cita in self.__citas:
            date = cita.getObjeto().getFecha().date()
            if selectedDate == date:
                self.lista.setCurrentItem(cita)
                break
            
    def listSelection(self):
        selectedDate = self.lista.currentItem().getObjeto().getFecha().date()
        if selectedDate != self.calendario.selectedDate().toPython():
            self.calendario.setSelectedDate(selectedDate)        
        
    def crearCitas(self):
        try:
            p = Persistence()
            cita1 = CitaCalendario(fecha = datetime(2012,03,13), anticipacion = 5, id_cita = '', id_actuacion = '1', uid = '')
            cita2 = CitaCalendario(fecha = datetime(2012,03,24), anticipacion = 3600, id_cita = '', id_actuacion = '1', uid = '')
            cita3 = CitaCalendario(fecha = datetime(2012,03,26), anticipacion = 86400, id_cita = '', id_actuacion = '1', uid = '')
            citas = [cita1,cita2,cita3]
            r = []
            for cita in citas:
                c = Cita(cita)
                item = ItemListas(c, self.lista)
                r.append(item)
            return r
        except Exception, e:
            print e
        
        
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
    def __init__(self,id_actuacion, cita = None,parent = None):
        super(CitaScreen, self).__init__(parent)
        self.setupUi(self)
        self.fecha.setDateTime(datetime.today())
        
        self.connect(self.calendar, QtCore.SIGNAL('selectionChanged()'), self.calendarSelection)
        self.connect(self.fecha, QtCore.SIGNAL('dateChanged(QDate)'), self.fechaSelection)
        
    def calendarSelection(self):
        self.fecha.setDate(self.calendar.selectedDate())
        
    def fechaSelection(self, selected):
        if self.calendar.selectedDate() != self.fecha.date():
            self.calendar.setSelectedDate(selected)
        
        
import sys        
app = QtGui.QApplication(sys.argv)
form = Calendar()
form.show()
app.exec_()
