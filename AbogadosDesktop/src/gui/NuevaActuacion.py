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
        
        if actuacion is not None:
            self.__juzgado = actuacion.getJuzgado()
            self.txtDescripcion.setText(unicode(actuacion.getDescripcion()))
            self.lblJuzgado.setText(unicode(self.__juzgado.getNombre()))
            self.dteFecha.setDateTime(actuacion.getFecha())
            self.dteFechaProxima.setDateTime(actuacion.getFechaProxima())
        
        horizontal = self.horizontal  
        slf = self
        lblJuzgado = self.lblJuzgado
        dteFecha = self.dteFecha
        dteFechaProxima = self.dteFechaProxima   
            
        def mousePressEvent(self):
            if self.sender() is dteFecha:
                print "sender"
            if Qt.MouseButton.LeftButton is self.button():
                if horizontal.count() is 2:
                    horizontal.removeItem(horizontal.itemAt(1))
                juzgado = Juzgado("nombre", "ciudad", "direccion", "telefono", "tipo", None, [])
                vista = VerJuzgado(juzgado, slf)
                horizontal.addWidget(vista)
            else:
                return QLabel.mousePressEvent(lblJuzgado,self)
        self.lblJuzgado.mousePressEvent = mousePressEvent
                    
        def mousePressEvent1(self):
            print "Entro"
            if Qt.MouseButton.LeftButton is self.button():
                if horizontal.count() is 2:
                    horizontal.removeItem(horizontal.itemAt(1))
                calendar = QCalendarWidget()
                calendar.setMinimumDate(dteFecha.dateTime())
                horizontal.addWidget(calendar)
            else:
                return QCalendarWidget.mousePressEvent(dteFecha,self)
        self.dteFecha.mousePressEvent = mousePressEvent
        
                    
    def click(self):
        print "hola"

import sys 

fecha = datetime(2012, 1, 1, 14, 15, 16, 0, None)
fechaProxima = datetime(2011, 2, 2, 15, 16, 17, 0, None)

juzgado = Juzgado(nombre = "Juzgado", ciudad = "Pereira", direccion = "calle", telefono = "3333333",tipo = "De familia")
actuacion = Actuacion(juzgado = juzgado,fecha = fecha,fechaProxima = fechaProxima,descripcion = "Actuación")
           
app = QApplication(sys.argv)
form = NuevaActuacion(actuacion)
form.show()
app.exec_()
        