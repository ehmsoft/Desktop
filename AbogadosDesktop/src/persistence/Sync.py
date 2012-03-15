'''
Created on 14/03/2012

@author: elfotografo007
'''
from persistence.SyncManager import SyncManager
from persistence.USBSync import USBSync

class Sync(object):
    '''
    Clase para sincronizar
    '''


    def __init__(self):
        self.syncMgr = SyncManager()
        self.usbSync = USBSync()
        
    def syncViaUSB(self):
        mobilePath = self.usbSync.getLocalMobilePath()
        self.syncMgr.sincronizarLocal(mobilePath)
        self.syncMgr.restaurarArchivo(mobilePath)
        self.usbSync.llevar()