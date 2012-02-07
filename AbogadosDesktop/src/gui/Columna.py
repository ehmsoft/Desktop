'''
Created on 01/02/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *


class ColumnaWidget(QWidget):
    def __init__(self, centralWidget,parent=None):
        super(ColumnaWidget, self).__init__(parent)
        self.__centralWidget = centralWidget
        layout = QVBoxLayout()
        btnLayout = QHBoxLayout()
        btnLayout.addStretch()
        self.btnAgregar = QPushButton('+')
        btnLayout.addWidget(self.btnAgregar)
        layout.addWidget(self.__centralWidget)
        layout.addStretch()
        layout.addLayout(btnLayout)
        self.setLayout(layout)
        self.connect(self.btnAgregar, SIGNAL('clicked()'), self.click)
        
    def setCentralWidget(self, widget):
        self.__centralWidget = widget
                
    def getCentralWidget(self):
        return self.__centralWidget
        
    def click(self):
        self.emit(SIGNAL('clicked()')) 
        
class ColumnaDerecha(QWidget):
    def __init__(self, titulo,centralWidget,parent=None):
        super(ColumnaDerecha, self).__init__(parent)
        self.__centralWidget = centralWidget
        self.__titulo = titulo
        layout = QVBoxLayout()
        btnLayout = QHBoxLayout()
        btnLayout.addStretch()
        self.btnEditar = QPushButton('Editar')
        self.btnEliminar = QPushButton('Eliminar')
        btnLayout.addWidget(self.btnEditar)
        btnLayout.addWidget(self.btnEliminar)
        if self.__titulo:
            label = QLabel(self.__centralWidget.windowTitle())
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)
        layout.addWidget(self.__centralWidget)
        layout.addStretch()
        layout.addLayout(btnLayout)
        self.setLayout(layout)
    
    def setCentralWidget(self, widget):
        self.__centralWidget = widget
                
    def getCentralWidget(self):
        return self.__centralWidget
