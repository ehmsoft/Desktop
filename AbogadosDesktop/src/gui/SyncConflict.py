# -*- coding: utf-8 -*-
'''
Created on 16/03/2012

@author: elfotografo007
'''
from PySide import QtCore, QtGui
from core.CampoPersonalizado import CampoPersonalizado
from core.Categoria import Categoria
from core.Juzgado import Juzgado
from core.Persona import Persona
from core.Plantilla import Plantilla
from core.Proceso import Proceso
from core.Actuacion import Actuacion
from gui.ver.VerProceso import VerProceso
from gui.ver.VerPlantilla import VerPlantilla
from gui.ver.VerPersona import VerPersona
from gui.ver.VerJuzgado import VerJuzgado
from gui.ver.VerCategoria import VerCategoria
from gui.ver.VerCampoPersonalizado import VerCampoPersonalizado
from gui.ver.VerActuacion import VerActuacion
from gui.SyncConflictScreen import Ui_SyncConflictDialog

class SyncConflict(QtGui.QDialog, Ui_SyncConflictDialog):
    def __init__(self, local, movil, fechaLocal=None, fechaMovil=None,parent = None):
        super(SyncConflict, self).__init__(parent)
        self.setupUi(self)
        if isinstance(local, Proceso):
            self.verLocal = VerProceso(local)
            self.verMovil = VerProceso(movil)
        elif isinstance(local, Plantilla):
            self.verLocal = VerPlantilla(local)
            self.verMovil = VerPlantilla(movil)
        elif isinstance(local, Persona):
            self.verLocal = VerPersona(local)
            self.verMovil = VerPersona(movil)
        elif isinstance(local, Juzgado):
            self.verLocal = VerJuzgado(local)
            self.verMovil = VerJuzgado(movil)
        elif isinstance(local, Categoria):
            self.verLocal = VerCategoria(local)
            self.verMovil = VerCategoria(movil)
        elif isinstance(local, CampoPersonalizado):
            self.verLocal = VerCampoPersonalizado(local)
            self.verMovil = VerCampoPersonalizado(movil)
        elif isinstance(local, Actuacion):
            self.verLocal = VerActuacion(local)
            self.verMovil = VerActuacion(movil)
        if fechaLocal:
            self.lblFechaLocal.setText(unicode(fechaLocal))
        if fechaMovil:
            self.lblFechaMovil.setText(unicode(fechaMovil))
        self.localLayout.addWidget(self.verLocal)
        self.mobileLayout.addWidget(self.verMovil)
        self.__seleccionado = True
        self.connect(self.btnSeleccionLocal, QtCore.SIGNAL("clicked()"), self.btnSeleccionLocalClicked)
        self.connect(self.btnSeleccionMovil, QtCore.SIGNAL("clicked()"), self.btnSeleccionMovilClicked)
        self.updateGeometry()
        
    def btnSeleccionLocalClicked(self):
        self.__seleccionado = True
        self.accept()
        
    def btnSeleccionMovilClicked(self):
        self.__seleccionado = False
        self.accept()
        
    def getSeleccionado(self):
        #True para Local, False para Movil
        self.exec_()
        return self.__seleccionado

#import sys
#from persistence.Persistence import Persistence   
#app = QApplication(sys.argv)
#p = Persistence()
##local = p.consultarPersona(2, 1)
##movil = p.consultarPersona(3, 1)
##local = p.consultarProceso(2)
##movil = p.consultarProceso(3)
##local = p.consultarJuzgado(2)
##movil = p.consultarJuzgado(3)
#local = p.consultarPlantilla(1)
#movil = p.consultarPlantilla(1)
#ventana = SyncConflict(local, movil)
#print ventana.getSeleccionado()
#sys.exit(app.exec_())