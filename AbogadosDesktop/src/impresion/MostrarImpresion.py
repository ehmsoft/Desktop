'''
Created on 22/03/2012

@author: esteban
'''

import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MostrarImpresion(QDialog):
    def __init__(self,html,landscape = False, parent = None):
        super(MostrarImpresion, self).__init__(parent)
        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPageSize(QPrinter.Letter)
        if landscape:
            self.printer.setOrientation(QPrinter.Landscape)
        layout = QVBoxLayout()
        self.browser = QTextBrowser()
        self.browser.setHtml(html)
        self.document= QTextDocument()
        self.document.setHtml(html)
        HLayout = QHBoxLayout()
        HLayout.addStretch()
        printBtn = QPushButton('Imprimir')
        printPdfBtn = QPushButton('Imprimir PDF')
        HLayout.addWidget(printBtn)
        HLayout.addWidget(printPdfBtn)
        layout.addWidget(self.browser)
        layout.addLayout(HLayout)
        self.connect(printBtn, SIGNAL("clicked()"), self.imprimir)
        self.connect(printPdfBtn, SIGNAL("clicked()"), self.imprimirPdf)
        self.setLayout(layout)
        self.showMaximized()
    
    def imprimir(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            self.browser.print_(self.printer)
            self.accept()
    
    def imprimirPdf(self):
        self.printer.setOutputFormat(QPrinter.PdfFormat)
        name = QFileDialog.getSaveFileName(self,'Guardar PDF')[0]
        if name != '' :
            fname = unicode( name + '.pdf')
            self.printer.setOutputFileName(fname)
            self.document.print_(self.printer)
            self.accept()
        
    
    
    