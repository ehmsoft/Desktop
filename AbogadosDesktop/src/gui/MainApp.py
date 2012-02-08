# -*- coding: utf-8 -*-

'''
Created on 30/01/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from MainAppScreen import Ui_mainApp
from gui.Listado import Listado
from gui.Columna import ColumnaWidget
from gui.Columna import ColumnaDerecha
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
from gui.VerActuacion import VerActuacion
from gui.VerCampoPersonalizado import VerCampoPersonalizado
from gui.NuevaPersona import NuevaPersona
from gui.NuevoJuzgado import NuevoJuzgado
from gui.NuevaCategoria import NuevaCategoria

class MainApp(QMainWindow, Ui_mainApp):
    def __init__(self, parent = None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.lista = ['Procesos', 'Plantillas', 'Demandantes', 'Demandados', 'Juzgados', 'Actuaciones', unicode('Categorías'), 'Campos Personalizados', 'Sincronizar', 'Ajustes']
        self.centralSplitter = QSplitter(Qt.Horizontal)
        self.scrollArea.setWidget(self.centralSplitter)
        #self.centralwidget.setStyleSheet('background-image: url(./images/bolita_marcaAgua.png);')
        self.image = QImage('./images/bolita.png')
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.listaIzquierda = QListWidget()
        #self.listaIzquierda.setStyleSheet('background-color: transparent;')
        #self.connect(self.listaIzquierda, SIGNAL('itemClicked(QListWidgetItem*)'), self.elementClicked)
        self.connect(self.listaIzquierda, SIGNAL('itemSelectionChanged()'), self.elementChanged)
        for row in self.lista:
            item = QListWidgetItem(row)
            fuente = item.font()
            fuente.setPointSize(18)
            fm = QFontMetrics(fuente)
            item.setFont(fuente)
            item.setSizeHint(QSize(fm.width(row), fm.height() +20))
            self.listaIzquierda.addItem(item)
        self.centralSplitter.addWidget(self.listaIzquierda)
        self.setWindowIcon(QIcon('./images/icono.png'))
        
        
    def elementChanged(self):
        self.elementClicked(self.listaIzquierda.currentItem())
        
    def elementClicked(self, item):
        if item.text() == 'Procesos':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1.hide()
                #self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                    
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Plantillas':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                lista = p.consultarPlantillas()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                listado = Listado(lista)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                p = Persistence()
                lista = p.consultarPlantillas()
                self.columna1.hide()
                #self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)

                listado = Listado(lista)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
                
        elif item.text() == 'Demandantes':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarDemandantes())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                p = Persistence()
                listado = Listado(p.consultarDemandantes())
                self.columna1.hide()
                #self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Demandados':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarDemandados())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                p = Persistence()
                listado = Listado(p.consultarDemandados())
                self.columna1.hide()
                #self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Juzgados':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarJuzgados())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                p = Persistence()
                listado = Listado(p.consultarJuzgados())
                self.columna1.hide()
                #self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Categorias':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarCategorias())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                p = Persistence()
                listado = Listado(p.consultarCategorias())
                self.columna1.hide()
                #self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Actuaciones':
            if self.centralSplitter.count() == 1:
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1.hide()
                #self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                    
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                #self.connect(self.columna1.getCentralWidget(), SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Campos Personalizados':
            if self.centralSplitter.count() == 1:
                lista = ['Procesos', 'Plantillas', 'Demandantes', 'Demandados', 'Juzgados', 'Actuaciones']
                listado = QListWidget()
                for row in lista:
                    item = QListWidgetItem(row)
                    fuente = item.font()
                    fuente.setPointSize(16)
                    fm = QFontMetrics(fuente)
                    item.setFont(fuente)
                    item.setSizeHint(QSize(fm.width(row), fm.height() +20))
                    listado.addItem(item)
                splitter = QSplitter()
                splitter.addWidget(listado)
                self.columna1 = splitter
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                #self.connect(listado, SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                lista = ['Procesos', 'Plantillas', 'Demandantes', 'Demandados', 'Juzgados', 'Actuaciones']
                listado = QListWidget()
                for row in lista:
                    item = QListWidgetItem(row)
                    fuente = item.font()
                    fuente.setPointSize(16)
                    fm = QFontMetrics(fuente)
                    item.setFont(fuente)
                    item.setSizeHint(QSize(fm.width(row), fm.height() +20))
                    listado.addItem(item)
                self.columna1.hide()
                #self.columna1.deleteLater()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                splitter = QSplitter()
                splitter.addWidget(listado)
                self.columna1 = splitter
                self.centralSplitter.addWidget(self.columna1)
                #self.connect(listado, SIGNAL('itemClicked(QListWidgetItem*)'), self.columna1ElementClicked)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
    def columna1AgregarClicked(self):
        item = self.listaIzquierda.currentItem()
        if item.text() == 'Procesos':
            pass
        elif item.text() == 'Plantillas':
            pass
                
        elif item.text() == 'Demandantes':
            personaVentana = NuevaPersona(tipo = 1)
            if personaVentana.exec_():
                persona = personaVentana.getPersona()
                self.columna1.getCentralWidget().add(persona)
        elif item.text() == 'Demandados':
            personaVentana = NuevaPersona(tipo = 2)
            if personaVentana.exec_():
                persona = personaVentana.getPersona()
                self.columna1.getCentralWidget().add(persona)
        elif item.text() == 'Juzgados':
            juzgadoVentana = NuevoJuzgado()
            if juzgadoVentana.exec_():
                juzgado = juzgadoVentana.getJuzgado()
                self.columna1.getCentralWidget().add(juzgado)
        elif item.text() == 'Categorias':
            categoriaVentana = NuevaCategoria()
            if categoriaVentana.exec_():
                categoria = categoriaVentana.getCategoria()
                self.columna1.getCentralWidget().add(categoria)
        elif item.text() == 'Actuaciones':
            pass
    
    def columna1ElementChanged(self):
        if hasattr(self.columna1, 'getCentralWidget'):
            self.columna1ElementClicked(self.columna1.getCentralWidget().currentItem())
        else:
            self.columna1ElementClicked(None)
    
    def columna1ElementClicked(self, item):
        if hasattr(item, 'getObjeto'):
            if isinstance(item.getObjeto(), Proceso):
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                proceso = VerProceso(item.getObjeto())
                nuevoElemento = ColumnaDerecha(titulo=False, centralWidget=proceso)
                if self.listaIzquierda.currentItem().text() == 'Actuaciones':
                    nuevoElemento.getCentralWidget().tabWidget.setCurrentIndex(1)
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.procesoEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.procesoEliminarClicked)
            if isinstance(item.getObjeto(), Plantilla):
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                plantilla = VerPlantilla(item.getObjeto())
                nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=plantilla )
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.plantillaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.plantillaEliminarClicked)
            if isinstance(item.getObjeto(), Persona):
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                persona = VerPersona(item.getObjeto())
                nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=persona)
                nuevoElemento.setMaximumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.personaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.personaEliminarClicked)
            if isinstance(item.getObjeto(), Juzgado):
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                juzgado = VerJuzgado(item.getObjeto())
                nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=juzgado)
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.juzgadoEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.juzgadoEliminarClicked)
            if isinstance(item.getObjeto(), Categoria):
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                categoria = VerCategoria(item.getObjeto())
                nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=categoria)
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.categoriaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.categoriaEliminarClicked)
        elif hasattr(self.columna1, 'widget'):
            if self.columna1.widget(0).currentItem().text() == 'Procesos':
                p = Persistence()
                lista = p.consultarAtributos()
                listado = Listado(lista)
                if self.columna1.count() > 1:
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                columna = ColumnaWidget(listado)
                self.columna1.addWidget(columna)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columnaCamposElementChanged)
                self.connect(columna, SIGNAL('clicked()'), self.columnaCamposAgregarClicked)
                p = None
            elif self.columna1.widget(0).currentItem().text() == 'Plantillas':
                p = Persistence()
                lista = p.consultarAtributos()
                listado = Listado(lista)
                if self.columna1.count() > 1:
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                columna = ColumnaWidget(listado)
                self.columna1.addWidget(columna)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columnaCamposElementChanged)
                self.connect(columna, SIGNAL('clicked()'), self.columnaCamposAgregarClicked)
                p = None
            elif self.columna1.widget(0).currentItem().text() == 'Demandantes':
                p = Persistence()
                lista = p.consultarAtributosPersona()
                listado = Listado(lista)
                if self.columna1.count() > 1:
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                columna = ColumnaWidget(listado)
                self.columna1.addWidget(columna)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columnaCamposElementChanged)
                self.connect(columna, SIGNAL('clicked()'), self.columnaCamposAgregarClicked)
                p = None
            elif self.columna1.widget(0).currentItem().text() == 'Demandados':
                p = Persistence()
                lista = p.consultarAtributosPersona()
                listado = Listado(lista)
                if self.columna1.count() > 1:
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                columna = ColumnaWidget(listado)
                self.columna1.addWidget(columna)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columnaCamposElementChanged)
                self.connect(columna, SIGNAL('clicked()'), self.columnaCamposAgregarClicked)
                p = None
            elif self.columna1.widget(0).currentItem().text() == 'Juzgados':
                p = Persistence()
                lista = p.consultarAtributosJuzgado()
                listado = Listado(lista)
                if self.columna1.count() > 1:
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                columna = ColumnaWidget(listado)
                self.columna1.addWidget(columna)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columnaCamposElementChanged)
                self.connect(columna, SIGNAL('clicked()'), self.columnaCamposAgregarClicked)
                p = None
            elif self.columna1.widget(0).currentItem().text() == 'Actuaciones':
                p = Persistence()
                lista = p.consultarAtributosActuacion()
                listado = Listado(lista)
                if self.columna1.count() > 1:
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                columna = ColumnaWidget(listado)
                self.columna1.addWidget(columna)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columnaCamposElementChanged)
                self.connect(columna, SIGNAL('clicked()'), self.columnaCamposAgregarClicked)
                p = None       

    def columnaCamposElementChanged(self):
        if hasattr(self.columna1, 'count'):
            if self.columna1.count() > 1:
                item = self.columna1.widget(1).getCentralWidget().currentItem()
                if hasattr(item, 'getObjeto'):
                    elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    campo = VerCampoPersonalizado(item.getObjeto())
                    nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=campo)
                    nuevoElemento.setMaximumWidth(310)
                    nuevoElemento.setMinimumWidth(310)
                    self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                    self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.campoEditarClicked)
                    self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.campoEliminarClicked)
    
    def columnaCamposAgregarClicked(self):
        print '+'
    
    def procesoEditarClicked(self):
        print 'clicked'
        
    def procesoEliminarClicked(self):
        proceso = self.columna1.getCentralWidget().getSelectedItem()
        if self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarProceso(proceso)
            p=None
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
            
    
    def personaEditarClicked(self):
        pass
    
    def personaEliminarClicked(self):
        persona = self.columna1.getCentralWidget().getSelectedItem()
        if self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarPersona(persona)
            p=None
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
    
    def juzgadoEditarClicked(self):
        pass
    
    def juzgadoEliminarClicked(self):
        juzgado = self.columna1.getCentralWidget().getSelectedItem()
        if self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarJuzgado(juzgado)
            p=None
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
    
    def plantillaEditarClicked(self):
        pass
    
    def plantillaEliminarClicked(self):
        plantilla = self.columna1.getCentralWidget().getSelectedItem()
        if self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarPlantilla(plantilla)
            p=None
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
    
    def categoriaEditarClicked(self):
        pass
    
    def categoriaEliminarClicked(self):
        categoria = self.columna1.getCentralWidget().getSelectedItem()
        if categoria.getId_categoria() == '1':
            QMessageBox.warning(self, 'No se puede borrar',unicode('La categoría Ninguna es por defecto y no se puede eliminar'))
        elif self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarCategoria(categoria)
            p=None
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0,1,1,1)
    
    def campoEditarClicked(self):
        pass
    
    def campoEliminarClicked(self):
        campo = self.columna1.widget(1).getCentralWidget().getSelectedItem()
        if self.columna1.widget(0).currentItem().text() == 'Procesos':
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributo(campo)
                p = None
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
        elif self.columna1.widget(0).currentItem().text() == 'Plantillas':
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributo(campo)
                p = None
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
        elif self.columna1.widget(0).currentItem().text() == 'Demandantes':
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributoPersona(campo)
                p = None
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
        elif self.columna1.widget(0).currentItem().text() == 'Demandados':
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributoPersona(campo)
                p = None
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
        elif self.columna1.widget(0).currentItem().text() == 'Juzgados':
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributoJuzgado(campo)
                p = None
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
            p = None
        elif self.columna1.widget(0).currentItem().text() == 'Actuaciones':
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributoActuacion(campo)
                p = None
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
import sys
app = QApplication(sys.argv)
app.setOrganizationName("ehmSoftware")
app.setOrganizationDomain("ehmsoft.com")
app.setApplicationName("Procesos Judiciales")
app.setWindowIcon(QIcon("./images/icono.png"))
theapp = MainApp()
theapp.show()
app.exec_()