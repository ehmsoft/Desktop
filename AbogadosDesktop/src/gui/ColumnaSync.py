# -*- coding: utf-8 -*-
'''
Created on 14/03/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from gui.ColumnaSyncScreen import Ui_ColumnaSync
from persistence.Sync import Sync
from persistence.USBSync import NoDeviceError
import sqlite3
from persistence.SyncManager import SyncDupException

class ColumnaSync(QWidget, Ui_ColumnaSync):
    def __init__(self, parent=None, carpeta=None):
        super(ColumnaSync, self).__init__(parent)
        self.syncObject = Sync(carpeta=carpeta)
        self.setupUi(self)
        self.connect(self.btnSincronizar, SIGNAL("clicked()"), self.sincronizar)
        
    def sincronizar(self):
        try:
            self.syncObject.syncViaUSB()
            dialogoOk = QMessageBox()
            dialogoOk.setText(u'Sincronización Finalizada con éxito!')
            dialogoOk.exec_()
        except NoDeviceError:
            QMessageBox.warning(self, "Error", u'El dispositivo no fue encontrado, verifique que está conectado mediante USB y el modo Unidad USB está activado.\nSi el problema persiste solicite ayuda en soporte@ehmsoft.com')
        except SyncDupException as e:
            QMessageBox.warning(self, "Error", u'{0}\nSi el problema persiste solicite ayuda en soporte@ehmsoft.com'.format(e.message))

        #TODO: Capturar excepciones
        
