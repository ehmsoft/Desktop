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
        self.connect(parent, QtCore.SIGNAL("accepted()"), self.cerrar)
        self.connect(parent, QtCore.SIGNAL("rejected()"), self.cerrar)
        
    def setWidget(self, widget):
        if not isinstance(widget, QtGui.QWidget):
            raise TypeError("widget debe pertenecer a la clase QWidget")
        if self.isHidden():
            self.move(self.__parent.x() + self.__parent.frameSize().width(), self.__parent.y())
            self.show()
        if self.__layout.count() > 0:
            item = self.__layout.takeAt(0)
            if item is not None:
                del(item)
        self.__layout.addWidget(widget)
        
    def getWidget(self):
        if self.__layout.count() > 0:
            return self.__layout.itemAt(0).widget()
        else:
            return None
        
    def cerrar(self):
        self.hide()
