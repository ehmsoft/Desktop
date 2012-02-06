'''
Created on 19/01/2012

@author: esteban

'''
from PySide.QtCore import *
from PySide.QtGui import *
import sys

class ItemListas(QListWidgetItem):
    def __init__(self, objeto, parent = None):
        super(ItemListas, self).__init__(str(objeto), parent)
        self.__objeto = objeto
        

    def getObjeto(self):
        return self.__objeto
    

    def setObjeto(self, objeto):
        self.__objeto = objeto
        self.setText(str(self.__objeto))
