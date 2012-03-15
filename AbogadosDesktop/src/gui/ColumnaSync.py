# -*- coding: utf-8 -*-
'''
Created on 14/03/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from gui.ColumnaSyncScreen import Ui_ColumnaSync
from persistence.Sync import Sync

class ColumnaSync(QWidget, Ui_ColumnaSync):
    def __init__(self,parent = None):
        super(ColumnaSync, self).__init__(parent)
        self.syncObject = Sync()
        self.setupUi(self)
        self.connect(self.btnSincronizar, SIGNAL("clicked()"), self.sincronizar)
        
    def sincronizar(self):

        self.syncObject.syncViaUSB()
        dialogoOk = QMessageBox()
        dialogoOk.setText(unicode("Sincronización Finalizada con éxito!"))
        dialogoOk.exec_()
        #TODO: Capturar excepciones
        