# -*- coding: utf-8 -*-
'''
Created on 10/08/2012

@author: elfotografo007
'''
from PySide import QtGui


class DialogoEspera(QtGui.QDialog):
    def __init__(self, parent = None):
        super(DialogoEspera, self).__init__(parent)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(QtGui.QLabel(u'Por Favor espere mientras se comunica con el servidor de activación'))
        self.setLayout(layout)
    
    
