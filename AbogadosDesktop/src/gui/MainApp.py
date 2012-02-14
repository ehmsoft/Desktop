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
from gui.NuevoCampo import NuevoCampo
from gui.NuevaActuacion import NuevaActuacion
from gui.NuevoProceso import NuevoProceso
from gui.NuevaPlantilla import NuevaPlantilla

class MainApp(QMainWindow, Ui_mainApp):
    def __init__(self, parent = None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        #Crear menu izquierdo
        self.lista = ['Procesos', 'Plantillas', 'Demandantes', 'Demandados', 'Juzgados', 'Actuaciones', unicode('Categorías'), 'Campos Personalizados', 'Sincronizar', 'Ajustes']
        self.centralSplitter = QSplitter(Qt.Horizontal)
        #El elemento de la izquierda es un splitter para pantallas pequenas
        self.scrollArea.setWidget(self.centralSplitter)
        #self.centralwidget.setStyleSheet('background-image: url(./images/bolita_marcaAgua.png);')
        self.image = QImage('./images/bolita.png')
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.listaIzquierda = QListWidget()
        #self.listaIzquierda.setStyleSheet('background-color: transparent;')
        #self.connect(self.listaIzquierda, SIGNAL('itemClicked(QListWidgetItem*)'), self.elementClicked)
        self.connect(self.listaIzquierda, SIGNAL('itemSelectionChanged()'), self.elementChanged)
        for row in self.lista:
            #Recorre cada elemento de la lista izquierda y le establece la fuente por defecto
            item = QListWidgetItem(row)
            fuente = item.font()
            fuente.setPointSize(16)
            fm = QFontMetrics(fuente)
            item.setFont(fuente)
            item.setSizeHint(QSize(fm.width(row), fm.height() +20))
            self.listaIzquierda.addItem(item)
        self.centralSplitter.addWidget(self.listaIzquierda)
        self.setWindowIcon(QIcon('./images/icono.png'))
        
        
    def elementChanged(self):
        self.elementClicked(self.listaIzquierda.currentItem())
        
    def elementClicked(self, item):
        #Metodo que maneja el click en la lista izquierda
        if item.text() == 'Procesos':
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                #Borrar la segunda columna y poner una nueva
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1.hide()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Plantillas':
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                p = Persistence()
                lista = p.consultarPlantillas()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
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
                #Borrar la segunda columna y poner una nueva
                p = Persistence()
                lista = p.consultarPlantillas()
                self.columna1.hide()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
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
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
                
        elif item.text() == 'Demandantes':
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                p = Persistence()
                listado = Listado(p.consultarDemandantes())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                #Borrar la segunda columna y poner una nueva
                p = Persistence()
                listado = Listado(p.consultarDemandantes())
                self.columna1.hide()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Demandados':
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                p = Persistence()
                listado = Listado(p.consultarDemandados())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                #Borrar la segunda columna y poner una nueva
                p = Persistence()
                listado = Listado(p.consultarDemandados())
                self.columna1.hide()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Juzgados':
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                p = Persistence()
                listado = Listado(p.consultarJuzgados())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                #Borrar la segunda columna y poner una nueva
                p = Persistence()
                listado = Listado(p.consultarJuzgados())
                self.columna1.hide()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == unicode('Categorías'):
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                p = Persistence()
                listado = Listado(p.consultarCategorias())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                #Borrar la segunda columna y poner una nueva
                p = Persistence()
                listado = Listado(p.consultarCategorias())
                self.columna1.hide()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Actuaciones':
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                #Borrar la segunda columna y poner una nueva
                p = Persistence()
                listado = Listado(p.consultarProcesos())
                self.columna1.hide()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.columna1 = ColumnaWidget(listado)
                self.centralSplitter.addWidget(self.columna1)
                self.connect(self.columna1, SIGNAL('clicked()'), self.columna1AgregarClicked)
                self.connect(self.columna1.getCentralWidget(), SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Campos Personalizados':
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                lista = ['Procesos', 'Plantillas', 'Demandantes', 'Demandados', 'Juzgados', 'Actuaciones']
                listado = QListWidget()
                for row in lista:
                    #Recorrer la lista y cambiar la fuente de los elementos
                    item = QListWidgetItem(row)
                    fuente = item.font()
                    fuente.setPointSize(15)
                    fm = QFontMetrics(fuente)
                    item.setFont(fuente)
                    item.setSizeHint(QSize(fm.width(row), fm.height() +20))
                    listado.addItem(item)
                #La columna central (columna1) se vuelve un splitter para poder tener una tercera columna
                splitter = QSplitter()
                splitter.addWidget(listado)
                self.columna1 = splitter
                self.centralSplitter.addWidget(self.columna1)
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
            else:
                #Borrar la segunda columna y poner una nueva
                lista = ['Procesos', 'Plantillas', 'Demandantes', 'Demandados', 'Juzgados', 'Actuaciones']
                listado = QListWidget()
                for row in lista:
                    #Recorrer la lista y cambiar la fuente de los elementos
                    item = QListWidgetItem(row)
                    fuente = item.font()
                    fuente.setPointSize(16)
                    fm = QFontMetrics(fuente)
                    item.setFont(fuente)
                    item.setSizeHint(QSize(fm.width(row), fm.height() +20))
                    listado.addItem(item)
                self.columna1.hide()
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                #Reestablecer el logo de la bolita
                if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion,VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                    elementoGrid.hide()
                    elementoGrid.deleteLater()
                    self.label = QLabel() 
                    self.label.setPixmap(QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0,1,1,1)
                #La columna central (columna1) se vuelve un splitter para permitir una tercera columna
                splitter = QSplitter()
                splitter.addWidget(listado)
                self.columna1 = splitter
                self.centralSplitter.addWidget(self.columna1)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
                p = None
        elif item.text() == 'Sincronizar':   
            #TODO: Acciones para el menu sincronizar
            pass
        elif item.text() == 'Ajustes':     
            #TODO: Acciones para el menu Ajustes
            pass
    def columna1AgregarClicked(self):
        #Manejar el evento de agregar un item en la columna1
        item = self.listaIzquierda.currentItem()
        if item.text() == 'Procesos':
            procesoVentana = NuevoProceso()
            if procesoVentana.exec_():
                proceso = procesoVentana.getProceso()
                self.columna1.getCentralWidget().add(proceso)
        elif item.text() == 'Plantillas':
            plantillaVentana = NuevaPlantilla()
            if plantillaVentana.exec_():
                plantilla = plantillaVentana.getPlantilla()
                self.columna1.getCentralWidget().add(plantilla)
                
        elif item.text() == 'Demandantes':
            personaVentana = NuevaPersona(tipo = 1)
            if personaVentana.exec_():
                persona = personaVentana.getPersona()
                self.columna1.getCentralWidget().add(persona)
            personaVentana = None
        elif item.text() == 'Demandados':
            personaVentana = NuevaPersona(tipo = 2)
            if personaVentana.exec_():
                persona = personaVentana.getPersona()
                self.columna1.getCentralWidget().add(persona)
            personaVentana = None
        elif item.text() == 'Juzgados':
            juzgadoVentana = NuevoJuzgado()
            if juzgadoVentana.exec_():
                juzgado = juzgadoVentana.getJuzgado()
                self.columna1.getCentralWidget().add(juzgado)
            juzgadoVentana = None
        elif item.text() == 'Categorias':
            categoriaVentana = NuevaCategoria()
            if categoriaVentana.exec_():
                categoria = categoriaVentana.getCategoria()
                self.columna1.getCentralWidget().add(categoria)
            categoriaVentana = None
        elif item.text() == 'Actuaciones':
            if self.columna1.getCentralWidget().currentItem() is not None:
                proceso = self.columna1.getCentralWidget().getSelectedItem()
                actuacionVentana = NuevaActuacion(id_proceso=proceso.getId_proceso())
                if actuacionVentana.exec_():
                    p = Persistence()
                    proceso = p.consultarProceso(proceso.getId_proceso())
                    self.columna1.getCentralWidget().replace(proceso)
                    p = None
                    self.columna1ElementChanged()
                actuacionVentana = None
            else:
                QMessageBox.warning(self, 'Advertencia', unicode('Debe seleccionar un proceso para poder agregar una actuación'))
                
    def columna1ElementChanged(self):
        if hasattr(self.columna1, 'getCentralWidget'):
            self.columna1ElementClicked(self.columna1.getCentralWidget().currentItem())
        else:
            self.columna1ElementClicked(None)
    
    def columna1ElementClicked(self, item):
        #Manejar cuando se da click a un elemento en la columna1
        if hasattr(item, 'getObjeto'):
            #Se va por aqui si columna1 tiene una lista
            if isinstance(item.getObjeto(), Proceso):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                proceso = VerProceso(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo=False, centralWidget=proceso)
                if self.listaIzquierda.currentItem().text() == 'Actuaciones':
                    nuevoElemento.getCentralWidget().tabWidget.setCurrentIndex(1)
                nuevoElemento.setMaximumWidth(340)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.procesoEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.procesoEliminarClicked)
            if isinstance(item.getObjeto(), Plantilla):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                plantilla = VerPlantilla(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=plantilla )
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.plantillaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.plantillaEliminarClicked)
            if isinstance(item.getObjeto(), Persona):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                persona = VerPersona(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=persona)
                nuevoElemento.setMaximumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.personaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.personaEliminarClicked)
            if isinstance(item.getObjeto(), Juzgado):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                juzgado = VerJuzgado(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=juzgado)
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.juzgadoEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.juzgadoEliminarClicked)
            if isinstance(item.getObjeto(), Categoria):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
                elementoGrid.hide()
                elementoGrid.deleteLater()
                categoria = VerCategoria(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo=True, centralWidget=categoria)
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0,1,1,1)
                self.connect(nuevoElemento.btnEditar, SIGNAL('clicked()'), self.categoriaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, SIGNAL('clicked()'), self.categoriaEliminarClicked)
        elif hasattr(self.columna1, 'widget'):
            #Se va por aqui si columna1 es un splitter
            elementoGrid = self.gridLayout.itemAtPosition(0,1).widget()
            #Reestablecer el logo de la bolita
            if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion, VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
                elementoGrid.hide()
                elementoGrid.deleteLater()
                self.label = QLabel() 
                self.label.setPixmap(QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
            if self.columna1.widget(0).currentItem().text() == 'Procesos':
                p = Persistence()
                lista = p.consultarAtributos()
                listado = Listado(lista)
                if self.columna1.count() > 1:
                    #Borrar la tercera columna si existe
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
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
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
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
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
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
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
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
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
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
                columna = ColumnaWidget(listado)
                self.columna1.addWidget(columna)
                self.connect(listado, SIGNAL('itemSelectionChanged()'), self.columnaCamposElementChanged)
                self.connect(columna, SIGNAL('clicked()'), self.columnaCamposAgregarClicked)
                p = None       

    def columnaCamposElementChanged(self):
        if hasattr(self.columna1, 'count'):
            #Se maneja la seleccion de una campo personalizado en la tercera columna
            if self.columna1.count() > 1:
                item = self.columna1.widget(1).getCentralWidget().currentItem()
                if hasattr(item, 'getObjeto'):
                    # Se filtra que si se haya seleccionado algun campo
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
        #Manejo del boton agregar en campos personalizados de la tercera columna
        if self.columna1.widget(0).currentItem().text() == 'Procesos':
            campoVentana = NuevoCampo(NuevoCampo.PROCESO)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Plantillas':
            campoVentana = NuevoCampo(NuevoCampo.PROCESO)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Demandantes':
            campoVentana = NuevoCampo(NuevoCampo.PERSONA)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Demandados':
            campoVentana = NuevoCampo(NuevoCampo.PERSONA)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Juzgados':
            campoVentana = NuevoCampo(NuevoCampo.JUZGADO)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Actuaciones':
            campoVentana = NuevoCampo(NuevoCampo.ACTUACION)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            campoVentana = None
    
    def procesoEditarClicked(self):
        proceso = self.columna1.getCentralWidget().currentItem().getObjeto()
        procesoVentana = NuevoProceso(proceso)
        if procesoVentana.exec_():
            self.columna1.getCentralWidget().replace(procesoVentana.getProceso())
        self.columna1ElementChanged()
        procesoVentana = None
        
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
        persona = self.columna1.getCentralWidget().currentItem().getObjeto()
        personaVentana = NuevaPersona(persona)
        if personaVentana.exec_():
            self.columna1.getCentralWidget().replace(personaVentana.getPersona())
        self.columna1ElementChanged()
        personaVentana = None
    
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
        juzgado = self.columna1.getCentralWidget().currentItem().getObjeto()
        juzgadoVentana = NuevoJuzgado(juzgado)
        if juzgadoVentana.exec_():
            self.columna1.getCentralWidget().replace(juzgadoVentana.getJuzgado())
        self.columna1ElementChanged()
        juzgadoVentana = None
    
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
        plantilla = self.columna1.getCentralWidget().currentItem().getObjeto()
        plantillaVentana = NuevaPlantilla(plantilla)
        if plantillaVentana.exec_():
            self.columna1.getCentralWidget().replace(plantillaVentana.getPlantilla())
        self.columna1ElementChanged()
        plantillaVentana = None
    
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
        categoria = self.columna1.getCentralWidget().currentItem().getObjeto()
        categoriaVentana = NuevaCategoria(categoria)
        if categoriaVentana.exec_():
            self.columna1.getCentralWidget().replace(categoriaVentana.getCategoria())
        self.columna1ElementChanged()
        categoriaVentana = None
    
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
        if self.columna1.widget(0).currentItem().text() == 'Procesos':
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(),'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo=NuevoCampo.PROCESO, campo=campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Plantillas':
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(),'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo=NuevoCampo.PROCESO, campo=campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Demandantes':
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(),'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo=NuevoCampo.PERSONA, campo=campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Demandados':
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(),'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo=NuevoCampo.PERSONA, campo=campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Juzgados':
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(),'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo=NuevoCampo.JUZGADO, campo=campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                campoVentana = None
        elif self.columna1.widget(0).currentItem().text() == 'Actuaciones':
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(),'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo=NuevoCampo.ACTUACION, campo=campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                campoVentana = None
    
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