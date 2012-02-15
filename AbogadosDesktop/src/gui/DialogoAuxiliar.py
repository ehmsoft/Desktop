'''
Created on 15/02/2012

@author: harold
'''
from PySide import QtGui, QtCore

class DialogoAuxiliar(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        super(DialogoAuxiliar, self).__init__(parent)
        self.__parent = parent
        self.__layout = QtGui.QVBoxLayout()
        self.setLayout(self.__layout)
        
    def setWidget(self, widget):
        if not isinstance(widget, QtGui.QWidget):
            raise TypeError("widget debe pertenecer a la clase QWidget")
        if self.__layout.count() > 0:
            item = self.__layout.takeAt(0)
            if item is not None:
                item.widget().deleteLater()
        self.__layout.addWidget(widget)
        
    def getWidget(self):
        if self.__layout.count() > 0:
            return self.__layout.itemAt(0).widget()
        else:
            return None