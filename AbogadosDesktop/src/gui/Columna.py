'''
Created on 01/02/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *


class ColumnaWidget(QWidget):
    def __init__(self, centralWidget,parent=None):
        super(ColumnaWidget, self).__init__(parent)
        self.centralWidget = centralWidget
        layout = QVBoxLayout()
        btnLayout = QHBoxLayout()
        btnLayout.addStretch()
        self.btnAgregar = QPushButton('+')
        btnLayout.addWidget(self.btnAgregar)
        layout.addWidget(self.centralWidget)
        layout.addStretch()
        layout.addLayout(btnLayout)
        self.setLayout(layout)
        self.connect(self.btnAgregar, SIGNAL('clicked()'), self.click)
        
    def click(self):
        self.emit(SIGNAL('clicked()')) 