# -*- coding: utf-8 -*-
'''
Created on 19/01/2012

@author: esteban

'''
from PySide.QtGui import QListWidgetItem

class ItemListas(QListWidgetItem):
    def __init__(self, objeto, parent = None):
        super(ItemListas, self).__init__(unicode(objeto), parent)
        self.__objeto = objeto
        

    def getObjeto(self):
        return self.__objeto
    

    def setObjeto(self, objeto):
        self.__objeto = objeto
        self.setText(unicode(self.__objeto))
