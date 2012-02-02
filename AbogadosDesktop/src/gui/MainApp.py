'''
Created on 30/01/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from MainAppScreen import Ui_mainApp
from gui.Listado import Listado
from gui.Columna import ColumnaWidget
from persistence.Persistence import Persistence
from core.Proceso import Proceso
from gui.VerProceso import VerProceso
from core.Plantilla import Plantilla
from gui.VerPlantilla import VerPlantilla
from gui.VerPersona import VerPersona
from core.Persona import Persona
from core.Juzgado import Juzgado
from gui.VerJuzgado import VerJuzgado
from core.Categoria import Categoria
from gui.VerCategoria import VerCategoria

class MainApp(QMainWindow, Ui_mainApp):
    def __init__(self, parent = None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.lista = ['Procesos', 'Plantillas', 'Demandantes', 'Demandados', 'Juzgados', 'Actuaciones', 'Categorias', 'Campos Personalizados', 'Sincronizar', 'Ajustes']
        self.centralSplitter = QSplitter(Qt.Horizontal)
        self.scrollArea.setWidget(self.centralSplitter)
        #self.centralwidget.setStyleSheet('background-image: url(./images/bolita_marcaAgua.png);')
        self.image = QImage('./images/bolita.png')
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.listaIzquierda = QListWidget()
        #self.listaIzquierda.setStyleSheet('background-color: transparent;')
        self.connect(self.listaIzquierda, SIGNAL('itemClicked(QListWidgetItem*)'), self.elementClicked)
        
        for row in self.lista:
            item = QListWidgetItem(row)
            fuente = item.font()
            fuente.setPointSize(18)
            fm = QFontMetrics(fuente)
            item.setFont(fuente)
            item.setSizeHint(QSize(fm.width(row), fm.height() +20))
            self.listaIzquierda.addItem(item)
        self.centralSplitter.addWidget(self.listaIzquierda)
        
    def elementClicked(self, item):
        if item.text() == 'Procesos':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
            else:
                p = Persistence()
                lista = p.consultarProcesos()
                self.columna1.hide()
                self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                if len(lista) != 0:
                    listado = Listado(lista)
                    self.columna1 = ColumnaWidget(listado)
                    self.centralSplitter.addWidget(self.columna1)
                    self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
        elif item.text() == 'Plantillas':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarPlantillas())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
            else:
                p = Persistence()
                lista = p.consultarPlantillas()
                self.columna1.hide()
                self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                if len(lista) != 0:
                    listado = Listado(lista)
                    self.columna1 = ColumnaWidget(listado)
                    self.centralSplitter.addWidget(self.columna1)
                    self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                    self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
                
        elif item.text() == 'Demandantes':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarDemandantes())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
            else:
                p = Persistence()
                lista = p.consultarDemandantes()
                self.columna1.hide()
                self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                if len(lista) != 0:
                    listado = Listado(lista)
                    self.columna1 = ColumnaWidget(listado)
                    self.centralSplitter.addWidget(self.columna1)
                    self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                    self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
        elif item.text() == 'Demandados':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarDemandados())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
            else:
                p = Persistence()
                lista = p.consultarDemandados()
                self.columna1.hide()
                self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                if len(lista) != 0:
                    listado = Listado(lista)
                    self.columna1 = ColumnaWidget(listado)
                    self.centralSplitter.addWidget(self.columna1)
                    self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                    self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
        elif item.text() == 'Juzgados':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarJuzgados())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
            else:
                p = Persistence()
                lista = p.consultarJuzgados()
                self.columna1.hide()
                self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                if len(lista) != 0:
                    listado = Listado(lista)
                    self.columna1 = ColumnaWidget(listado)
                    self.centralSplitter.addWidget(self.columna1)
                    self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                    self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
        elif item.text() == 'Categorias':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarCategorias())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
            else:
                p = Persistence()
                lista = p.consultarCategorias()
                self.columna1.hide()
                self.columna1.deleteLater()
                if len(lista) != 0:
                    listado = Listado(lista)
                    self.columna1 = ColumnaWidget(listado)
                    self.centralSplitter.addWidget(self.columna1)
                    self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                    self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                p = None
        
    def columna1AgregarClicked(self):
        pass
    
    def columna1ElementClicked(self, item):
        if isinstance(item.getObjeto(), Proceso):
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            elementoGrid.hide()
            elementoGrid.deleteLater()
            nuevoElemento = VerProceso(item.getObjeto())
            nuevoElemento.setMaximumWidth(310)
            nuevoElemento.setMinimumWidth(310)
            self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
        if isinstance(item.getObjeto(), Plantilla):
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            elementoGrid.hide()
            elementoGrid.deleteLater()
            nuevoElemento = VerPlantilla(item.getObjeto())
            nuevoElemento.setMaximumWidth(310)
            nuevoElemento.setMinimumWidth(310)
            self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
        if isinstance(item.getObjeto(), Persona):
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            elementoGrid.hide()
            elementoGrid.deleteLater()
            nuevoElemento = VerPersona(item.getObjeto())
            nuevoElemento.setMaximumWidth(310)
            self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
        if isinstance(item.getObjeto(), Juzgado):
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            elementoGrid.hide()
            elementoGrid.deleteLater()
            nuevoElemento = VerJuzgado(item.getObjeto())
            nuevoElemento.setMaximumWidth(310)
            nuevoElemento.setMinimumWidth(310)
            self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)    
        if isinstance(item.getObjeto(), Categoria):
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            elementoGrid.hide()
            elementoGrid.deleteLater()
            nuevoElemento = VerCategoria(item.getObjeto())
            nuevoElemento.setMaximumWidth(310)
            nuevoElemento.setMinimumWidth(310)
            self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
        
import sys
app = QApplication(sys.argv)
theapp = MainApp()
theapp.show()
app.exec_()