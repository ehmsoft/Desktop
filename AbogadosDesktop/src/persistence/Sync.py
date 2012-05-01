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


    def __init__(self, carpeta=None):
        self.syncMgr = SyncManager(carpeta=carpeta)
        self.usbSync = USBSync(local=carpeta)
        
    def syncViaUSB(self):
        mobilePath = self.usbSync.getLocalMobilePath()
        if self.syncMgr.verificarSyncLocal(mobilePath):
            self.syncMgr.sincronizarLocal(mobilePath)
        self.syncMgr.restaurarArchivo(mobilePath)
        self.usbSync.llevar()