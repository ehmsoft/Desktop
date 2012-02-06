# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: harold
'''

from PySide.QtGui import *
from PySide.QtCore import *
from gui.NuevaActuacionScreen import Ui_NuevaActuacion
from persistence.Persistence import Persistence
from core.Juzgado import Juzgado
from core.Actuacion import Actuacion
from datetime import datetime
from gui.VerJuzgado import VerJuzgado

class NuevaActuacion(QDialog, Ui_NuevaActuacion):
    '''
    classdocs
    '''


    def __init__(self, actuacion = None, id_proceso = None, parent = None):
        super(NuevaActuacion, self).__init__(parent)
        self.setupUi(self)
        self.__actuacion = actuacion
        self.__idProceso = id_proceso
        self.__juzgado = None
        self.lblJuzgado.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
                
        if actuacion is not None:
            self.__juzgado = actuacion.getJuzgado()
            self.txtDescripcion.setText(unicode(actuacion.getDescripcion()))
            self.lblJuzgado.setText(unicode(self.__juzgado.getNombre()))
            self.dteFecha.setDateTime(actuacion.getFecha())
            self.dteFechaProxima.setDateTime(actuacion.getFechaProxima())
        
        self.clickJuzgado()
        self.clickFecha()
        self.clickFechaProxima()
        
    def clickJuzgado(self):
        container = self.horizontal  
        widget = self
        lblJuzgado = self.lblJuzgado
                    
        def mousePressEvent(self):
            if Qt.MouseButton.LeftButton is self.button():
                if container.itemAt(1) is None:
                    if widget.__juzgado.getId_juzgado is not "1":
                        vista = VerJuzgado(widget.__juzgado, widget)
                        container.addWidget(vista)
                #elif isinstance(container.itemAt(1).widget(), VerJuzgado):
                    #pass
                else:
                    container.itemAt(1).widget().deleteLater()
                    if widget.__juzgado.getId_juzgado is not "1":
                        vista = VerJuzgado(widget.__juzgado, widget)
                        container.addWidget(vista)
            else:
                return QLabel.mousePressEvent(lblJuzgado,self)
            
        self.lblJuzgado.mousePressEvent = mousePressEvent
    
    def clickFecha(self):
        container = self.horizontal  
        dteFecha = self.dteFecha
        
        def focusInEvent(self):
            if container.itemAt(1) is None:
                calendar = QCalendarWidget()
                calendar.setSelectedDate(dteFecha.dateTime().date())
                container.addWidget(calendar)
            elif isinstance(container.itemAt(1).widget(), QCalendarWidget):
                calendar = container.itemAt(1).widget()
                calendar.setSelectedDate(dteFecha.dateTime().date())
            else:
                container.itemAt(1).widget().deleteLater()
                calendar = QCalendarWidget()
                calendar.setSelectedDate(dteFecha.dateTime().date())
                container.addWidget(calendar)                
            return QDateTimeEdit.focusInEvent(dteFecha,self)
        
        def dateChanged():
            calendar = container.itemAt(1).widget()
            calendar.setSelectedDate(dteFecha.dateTime().date())        
            
        dteFecha.focusInEvent = focusInEvent
        dteFecha.dateChanged.connect(dateChanged)
        
    
    def clickFechaProxima(self):
        container = self.horizontal  
        dteFecha = self.dteFechaProxima
        
        def focusInEvent(self):
            if container.itemAt(1) is None:
                calendar = QCalendarWidget()
                calendar.setSelectedDate(dteFecha.dateTime().date())
                container.addWidget(calendar)
            elif isinstance(container.itemAt(1).widget(), QCalendarWidget):
                calendar = container.itemAt(1).widget()
                calendar.setSelectedDate(dteFecha.dateTime().date())
            else:
                container.itemAt(1).widget().deleteLater()
                calendar = QCalendarWidget()
                calendar.setSelectedDate(dteFecha.dateTime().date())
                container.addWidget(calendar)                
            return QDateTimeEdit.focusInEvent(dteFecha,self)
        
        def dateChanged():
            calendar = container.itemAt(1).widget()
            calendar.setSelectedDate(dteFecha.dateTime().date())    
            
        dteFecha.focusInEvent = focusInEvent
        dteFecha.dateChanged.connect(dateChanged)

import sys 

fecha = datetime(2012, 1, 1, 14, 15, 16, 0, None)
fechaProxima = datetime(2011, 2, 2, 15, 16, 17, 0, None)

juzgado = Juzgado(nombre = "Juzgado", ciudad = "Pereira", direccion = "calle", telefono = "3333333",tipo = "De familia")
actuacion = Actuacion(juzgado = juzgado,fecha = fecha,fechaProxima = fechaProxima,descripcion = "Actuación")
           
app = QApplication(sys.argv)
form = NuevaActuacion(actuacion)
form.show()
app.exec_()
        