# -*- coding: utf-8 -*-

'''
Created on 30/01/2012

@author: elfotografo007
'''
from PySide import QtCore, QtGui
from MainAppScreen import Ui_mainApp
from gui.Columna import ColumnaWidget
from gui.Columna import ColumnaDerecha
from persistence.Persistence import Persistence
from core.Proceso import Proceso
from gui.ver.VerProceso import VerProceso
from core.Plantilla import Plantilla
from gui.ver.VerPlantilla import VerPlantilla
from gui.ver.VerPersona import VerPersona
from core.Persona import Persona
from core.Juzgado import Juzgado
from gui.ver.VerJuzgado import VerJuzgado
from core.Categoria import Categoria
from gui.ver.VerCategoria import VerCategoria
from gui.ver.VerActuacion import VerActuacion
from gui.ver.VerCampoPersonalizado import VerCampoPersonalizado
from gui.nuevo.NuevaPersona import NuevaPersona
from gui.nuevo.NuevoJuzgado import NuevoJuzgado
from gui.nuevo.NuevaCategoria import NuevaCategoria
from gui.nuevo.NuevoCampo import NuevoCampo
from gui.nuevo.NuevaActuacion import NuevaActuacion
from gui.nuevo.NuevoProceso import NuevoProceso
from gui.nuevo.NuevaPlantilla import NuevaPlantilla
from gui.ListadoDialogo import ListadoDialogo
from gui.ListadoBusqueda import ListadoBusqueda
import resources
from gui.ColumnaSync import ColumnaSync
from core.ActuacionCritica import ActuacionCritica
from gui.ExportarCSVDialog import ExportarCSVDialog
import shutil
from persistence.ConnectionManager import ConnectionManager
from gui.GestorCitas import GestorCitas
from gui.Calendar import Calendar

class MainApp(QtGui.QMainWindow, Ui_mainApp):
    #Constantes para elementos  del menu listaIzquierda
    TXTPROCESOS = 'Procesos'
    TXTPLANTILLAS = 'Plantillas'
    TXTDEMANDANTES = 'Demandantes'
    TXTDEMANDADOS = 'Demandados'
    TXTJUZGADOS = 'Juzgados'
    TXTACTUACIONES = 'Actuaciones'
    TXTCATEGORIAS = unicode('Categorías')
    TXTCAMPOS = 'Campos Personalizados'
    TXTSINCRONIZAR = 'Sincronizar'
    TXTAJUSTES = 'Ajustes'
    TXTEVENTOS = unicode('Eventos Próximos')
    CANTEVENTOS = 10
    
    def __init__(self, parent = None):
        super(MainApp, self).__init__(parent)
        self.last = None
        self.setupUi(self)
        self.__gestor = GestorCitas(self)
        try:
            self.__persistence = Persistence()
        except Exception:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText("Ocurrió un error al cargar la base de datos")
            message.exec_()
            
        self.setTrayIcon()
        #Crear menu izquierdo
        self.lista = [MainApp.TXTEVENTOS,MainApp.TXTPROCESOS, MainApp.TXTPLANTILLAS, MainApp.TXTDEMANDANTES, MainApp.TXTDEMANDADOS, MainApp.TXTJUZGADOS, MainApp.TXTACTUACIONES, MainApp.TXTCATEGORIAS, MainApp.TXTCAMPOS, MainApp.TXTSINCRONIZAR, MainApp.TXTAJUSTES]
        self.centralSplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        #El elemento de la izquierda es un splitter para pantallas pequenas
        self.scrollArea.setWidget(self.centralSplitter)
        #self.centralwidget.setStyleSheet('background-image: url(./images/bolita_marcaAgua.png);')
        self.image = QtGui.QImage(':/images/bolita.png')
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.listaIzquierda = QtGui.QListWidget()
        self.listaIzquierda.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.listaIzquierda.setStyleSheet('background-color: transparent;')
        #self.connect(self.listaIzquierda, QtCore.SIGNAL('itemClicked(QListWidgetItem*)'), self.elementClicked)
        self.connect(self.listaIzquierda, QtCore.SIGNAL('itemSelectionChanged()'), self.elementChanged)
        self.connect(self.listaIzquierda, QtCore.SIGNAL('customContextMenuRequested(QPoint)'), self.listaIzquierdaContextMenu)        
        self.listaIzquierda.setMouseTracking(True)
        for row in self.lista:
            #Recorre cada elemento de la lista izquierda y le establece la fuente por defecto
            item = QtGui.QListWidgetItem(row)
            fuente = item.font()
            fuente.setPointSize(16)
            fm = QtGui.QFontMetrics(fuente)
            item.setFont(fuente)
            item.setSizeHint(QtCore.QSize(fm.width(row), fm.height() + 20))
            item.setToolTip('Ver %s' % row)
            item.setStatusTip('Ver %s' % row)
            self.listaIzquierda.addItem(item)
        self.centralSplitter.addWidget(self.listaIzquierda)
        self.setWindowIcon(QtGui.QIcon(':/images/icono.png'))
        self.connect(self.actionNuevoProceso, QtCore.SIGNAL('triggered()'), self.menuNuevoProcesoClicked)
        self.connect(self.actionNuevaPlantilla, QtCore.SIGNAL('triggered()'), self.menuNuevaPlantillaClicked)
        self.connect(self.actionNuevoDemandante, QtCore.SIGNAL('triggered()'), self.menuNuevoDemandanteClicked)
        self.connect(self.actionNuevoDemandado, QtCore.SIGNAL('triggered()'), self.menuNuevoDemandadoClicked)
        self.connect(self.actionNuevoJuzgado, QtCore.SIGNAL('triggered()'), self.menuNuevoJuzgadoClicked)
        self.connect(self.actionNuevaCategoria, QtCore.SIGNAL('triggered()'), self.menuNuevaCategoriaClicked)
        self.connect(self.actionNuevaActuacion, QtCore.SIGNAL('triggered()'), self.menuNuevaActuacionClicked)
        self.connect(self.actionNuevoCampo_Proceso, QtCore.SIGNAL('triggered()'), self.menuNuevoCampoProcesoClicked)
        self.connect(self.actionNuevoCampo_Plantilla, QtCore.SIGNAL('triggered()'), self.menuNuevoCampoProcesoClicked)
        self.connect(self.actionNuevoCampo_Demandante, QtCore.SIGNAL('triggered()'), self.menuNuevoCampoPersonaClicked)
        self.connect(self.actionNuevoCampo_Demandado, QtCore.SIGNAL('triggered()'), self.menuNuevoCampoPersonaClicked)
        self.connect(self.actionNuevoCampo_Juzgado, QtCore.SIGNAL('triggered()'), self.menuNuevoCampoJuzgadoClicked)
        self.connect(self.actionNuevoCampo_Actuacion, QtCore.SIGNAL('triggered()'), self.menuNuevoCampoActuacionClicked)
        self.connect(self.actionNuevoProceso_a_partir_de_Plantilla, QtCore.SIGNAL('triggered()'), self.menuNuevoProcesoPlantillaClicked)
        self.connect(self.actionArchivo_CSV, QtCore.SIGNAL('triggered()'), self.menuExportarCSVClicked)
        self.connect(self.actionArchivo_de_Copia_de_Seguridad, QtCore.SIGNAL('triggered()'), self.menuExportarArchivoClicked)
        self.connect(self.actionImportar, QtCore.SIGNAL('triggered()'), self.menuImportarArchivoClicked)
        self.connect(self.actionCerrar, QtCore.SIGNAL('triggered()'), self.cerrar)
        
    def elementChanged(self):
        self.elementClicked(self.listaIzquierda.currentItem())
        
    def setTrayIcon(self):
        self.tray = QtGui.QSystemTrayIcon(self)
        self.tray.setIcon(QtGui.QIcon(':/images/icono.png'))
        calendario = self.__createAction('Calendario', self.mostrarCalendario)
        cerrar = self.__createAction('Cerrar', self.cerrar)
        menu = QtGui.QMenu(self)
        #menu.addAction(QtGui.QIcon(':/images/bolita.png'),'Calendario',self.mostrarCalendario)
        menu.addAction(calendario)
        menu.addSeparator()
        menu.addAction(cerrar)
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.trayClicked)
        self.tray.show()
        
    def cerrar(self):
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Question)
        message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        message.setDefaultButton(QtGui.QMessageBox.No)
        message.setText(unicode("¿Desea cerrar la aplicación, no obtendrá notificaciones de sus citas?"))
        ret = message.exec_()
        if ret == QtGui.QMessageBox.Yes:
            import sys
            sys.exit(0)
        
    def mostrarCalendario(self):
        calendar = Calendar(self)
        if self.isHidden():
            self.show()
        calendar.exec_()
        
    def trayClicked(self, reason):
        import sys
        if reason == QtGui.QSystemTrayIcon.ActivationReason.Trigger and sys.platform.lower() != 'darwin':
            if self.isHidden():
                self.show()
            else:
                self.hide()
                
    def event(self, event):
        if self.last == QtCore.QEvent.Type.Close and event.type() == QtCore.QEvent.Type.MenubarUpdated and self.last != QtCore.QEvent.Type.MenubarUpdated:
            if self.isHidden():
                self.show()
            self.last = event
            return QtCore.QObject.event(self, event) 
        elif event.type() == QtCore.QEvent.Type.Close:
            self.closeEvent(event)
            self.last = event
            return True
        else:
            self.last = event
            return QtCore.QObject.event(self, event)      
                
    def closeEvent(self, event):
        self.hide()
        event.ignore()
        #return QtGui.QMainWindow.closeEvent(self, *args, **kwargs)
        
    def elementClicked(self, item):
        #Metodo que maneja el click en la lista izquierda
        if item.text() == MainApp.TXTEVENTOS:
            if not self.centralSplitter.count() == 1:
                self.columna1.setParent(None)
            p = Persistence()
            listado = ListadoBusqueda(p.consultarActuacionesCriticas(MainApp.CANTEVENTOS))
            self.columna1 = ColumnaWidget(listado, addbutton=False)
            self.centralSplitter.addWidget(self.columna1)
            self.__restablecerElementoDerecho()
        
        if item.text() == MainApp.TXTPROCESOS:
            if not self.centralSplitter.count() == 1:
                self.columna1.setParent(None)
            p = Persistence()
            listado = ListadoBusqueda(p.consultarProcesos())
            self.columna1 = ColumnaWidget(listado, listado.getSearchField())
            self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.centralSplitter.addWidget(self.columna1)
            self.__restablecerElementoDerecho()

        elif item.text() == MainApp.TXTPLANTILLAS:
            if not self.centralSplitter.count() == 1:
                self.columna1.setParent(None)
            p = Persistence()
            lista = p.consultarPlantillas()
            listado = ListadoBusqueda(lista)
            self.columna1 = ColumnaWidget(listado, listado.getSearchField())
            self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.centralSplitter.addWidget(self.columna1)
            self.__restablecerElementoDerecho()
          
        elif item.text() == MainApp.TXTDEMANDANTES:
            if not self.centralSplitter.count() == 1:
                self.columna1.setParent(None)
            p = Persistence()
            listado = ListadoBusqueda(p.consultarDemandantes())
            self.columna1 = ColumnaWidget(listado, listado.getSearchField())
            self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.centralSplitter.addWidget(self.columna1)
            self.__restablecerElementoDerecho()

        elif item.text() == MainApp.TXTDEMANDADOS:
            if not self.centralSplitter.count() == 1:
                self.columna1.setParent(None)
            p = Persistence()
            listado = ListadoBusqueda(p.consultarDemandados())
            self.columna1 = ColumnaWidget(listado, listado.getSearchField())
            self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.centralSplitter.addWidget(self.columna1)
            self.__restablecerElementoDerecho()

        elif item.text() == MainApp.TXTJUZGADOS:
            if not self.centralSplitter.count() == 1:
                self.columna1.setParent(None)
            p = Persistence()
            listado = ListadoBusqueda(p.consultarJuzgados())
            self.columna1 = ColumnaWidget(listado, listado.getSearchField())
            self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.centralSplitter.addWidget(self.columna1)
            self.__restablecerElementoDerecho()
            
        elif item.text() == MainApp.TXTCATEGORIAS:
            if not self.centralSplitter.count() == 1:
                self.columna1.setParent(None)
            p = Persistence()
            listado = ListadoBusqueda(p.consultarCategorias())
            self.columna1 = ColumnaWidget(listado, listado.getSearchField())
            self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.centralSplitter.addWidget(self.columna1)
            self.__restablecerElementoDerecho()
            
        elif item.text() == MainApp.TXTACTUACIONES:
            if not self.centralSplitter.count() == 1:
                self.columna1.setParent(None)
            p = Persistence()
            listado = ListadoBusqueda(p.consultarProcesos())
            self.columna1 = ColumnaWidget(listado, listado.getSearchField())
            self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.centralSplitter.addWidget(self.columna1)
            self.__restablecerElementoDerecho()
           
        elif item.text() == MainApp.TXTCAMPOS:
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                lista = [MainApp.TXTPROCESOS, MainApp.TXTPLANTILLAS, MainApp.TXTDEMANDANTES, MainApp.TXTDEMANDADOS, MainApp.TXTJUZGADOS, MainApp.TXTACTUACIONES]
                listado = QtGui.QListWidget()
                listado.setMouseTracking(True)
                listado.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                for row in lista:
                    #Recorrer la lista y cambiar la fuente de los elementos
                    itemTemp = QtGui.QListWidgetItem(row)
                    fuente = itemTemp.font()
                    fuente.setPointSize(15)
                    fm = QtGui.QFontMetrics(fuente)
                    itemTemp.setFont(fuente)
                    itemTemp.setSizeHint(QtCore.QSize(fm.width(row), fm.height() + 20))
                    itemTemp.setToolTip('Campos para %s' % row)
                    itemTemp.setStatusTip('Campos para %s' % row)
                    listado.addItem(itemTemp)
                #La columna central (columna1) se vuelve un splitter para poder tener una tercera columna
                splitter = QtGui.QSplitter()
                splitter.addWidget(listado)
                self.columna1 = splitter
                self.centralSplitter.addWidget(self.columna1)
                self.__restablecerElementoDerecho()
            else:
                #Borrar la segunda columna y poner una nueva
                lista = [MainApp.TXTPROCESOS, MainApp.TXTPLANTILLAS, MainApp.TXTDEMANDANTES, MainApp.TXTDEMANDADOS, MainApp.TXTJUZGADOS, MainApp.TXTACTUACIONES]
                listado = QtGui.QListWidget()
                listado.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                for row in lista:
                    #Recorrer la lista y cambiar la fuente de los elementos
                    itemTemp = QtGui.QListWidgetItem(row)
                    fuente = itemTemp.font()
                    fuente.setPointSize(15)
                    fm = QtGui.QFontMetrics(fuente)
                    itemTemp.setFont(fuente)
                    itemTemp.setSizeHint(QtCore.QSize(fm.width(row), fm.height() + 20))
                    itemTemp.setToolTip('Campos para %s' % row)
                    itemTemp.setStatusTip('Campos para %s' % row)
                    listado.addItem(itemTemp)
                self.columna1.hide()
                self.__restablecerElementoDerecho()
                #La columna central (columna1) se vuelve un splitter para permitir una tercera columna
                splitter = QtGui.QSplitter()
                splitter.addWidget(listado)
                self.columna1 = splitter
                self.centralSplitter.addWidget(self.columna1)
            self.connect(listado, QtCore.SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
            self.connect(listado, QtCore.SIGNAL('customContextMenuRequested(QPoint)'), self.listaCamposContextMenu)
                
        elif item.text() == MainApp.TXTSINCRONIZAR:   
            if self.centralSplitter.count() == 1:
                #Agregar la segunda columna si no existe
                self.columna1 =  ColumnaSync()
                #self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                self.centralSplitter.addWidget(self.columna1)
                self.__restablecerElementoDerecho()
            else:
                #Borrar la segunda columna y poner una nueva
                self.columna1.hide()
                self.columna1 = ColumnaSync()
                #self.columna1.getCentralWidget().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                self.centralSplitter.addWidget(self.columna1)
                self.__restablecerElementoDerecho()
            #self.__restablecerElementoDerecho()
        elif item.text() == MainApp.TXTAJUSTES:     
            #TODO: Acciones para el menu Ajustes
            self.__restablecerElementoDerecho()
        if item.text() in [MainApp.TXTEVENTOS,MainApp.TXTPROCESOS, MainApp.TXTPLANTILLAS, MainApp.TXTDEMANDANTES, MainApp.TXTDEMANDADOS, MainApp.TXTJUZGADOS, MainApp.TXTACTUACIONES, MainApp.TXTCATEGORIAS]:
            self.connect(self.columna1, QtCore.SIGNAL('clicked()'), self.columna1AgregarClicked)
            self.connect(self.columna1.getCentralWidget(), QtCore.SIGNAL('itemSelectionChanged()'), self.columna1ElementChanged)
            self.connect(self.columna1.getCentralWidget(), QtCore.SIGNAL('customContextMenuRequested(QPoint)'), self.columna1ContextMenu)
            
    def columna1AgregarClicked(self):
        #Manejar el evento de agregar un item en la columna1
        item = self.listaIzquierda.currentItem()
        if item.text() == MainApp.TXTPROCESOS:
            procesoVentana = NuevoProceso()
            if procesoVentana.exec_():
                proceso = procesoVentana.getProceso()
                self.columna1.getCentralWidget().add(proceso)
        elif item.text() == MainApp.TXTPLANTILLAS:
            plantillaVentana = NuevaPlantilla()
            if plantillaVentana.exec_():
                plantilla = plantillaVentana.getPlantilla()
                self.columna1.getCentralWidget().add(plantilla)
                
        elif item.text() == MainApp.TXTDEMANDANTES:
            personaVentana = NuevaPersona(tipo = 1)
            if personaVentana.exec_():
                persona = personaVentana.getPersona()
                self.columna1.getCentralWidget().add(persona)
            del personaVentana
        elif item.text() == MainApp.TXTDEMANDADOS:
            personaVentana = NuevaPersona(tipo = 2)
            if personaVentana.exec_():
                persona = personaVentana.getPersona()
                self.columna1.getCentralWidget().add(persona)
            del personaVentana
        elif item.text() == MainApp.TXTJUZGADOS:
            juzgadoVentana = NuevoJuzgado()
            if juzgadoVentana.exec_():
                juzgado = juzgadoVentana.getJuzgado()
                self.columna1.getCentralWidget().add(juzgado)
            del juzgadoVentana
        elif item.text() == MainApp.TXTCATEGORIAS:
            categoriaVentana = NuevaCategoria()
            if categoriaVentana.exec_():
                categoria = categoriaVentana.getCategoria()
                self.columna1.getCentralWidget().add(categoria)
            del categoriaVentana
        elif item.text() == MainApp.TXTACTUACIONES:
            if self.columna1.getCentralWidget().currentItem() is not None:
                proceso = self.columna1.getCentralWidget().getSelectedItem()
                actuacionVentana = NuevaActuacion()
                if actuacionVentana.exec_():
                    p = Persistence()
                    proceso = p.consultarProceso(proceso.getId_proceso())
                    proceso.addActuacion(actuacionVentana.getActuacion())
                    p.actualizarProceso(proceso)
                    self.columna1.getCentralWidget().replace(proceso)
                    self.columna1ElementChanged()
                del actuacionVentana
            else:
                QtGui.QMessageBox.warning(self, 'Advertencia', unicode('Debe seleccionar un proceso para poder agregar una actuación'))
                
    def columna1ElementChanged(self):
        if hasattr(self.columna1, 'getCentralWidget'):
            self.columna1ElementClicked(self.columna1.getCentralWidget().currentItem())
        else:
            self.columna1ElementClicked(None)
    
    def columna1ElementClicked(self, item):
        #Manejar cuando se da click a un elemento en la columna1
        if hasattr(item, 'getObjeto'):
            #Se va por aqui si columna1 tiene una lista
            if isinstance(item.getObjeto(), ActuacionCritica):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                actuacion =item.getObjeto()
                proc = Persistence().consultarProceso(actuacion.getId_proceso())
                proceso = VerProceso(proc)
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo = False, centralWidget = proceso)
                nuevoElemento.setMaximumWidth(340)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0, 1, 1, 1)
                self.connect(nuevoElemento.btnEditar, QtCore.SIGNAL('clicked()'), self.procesoEditarClicked)
                self.connect(nuevoElemento.btnEliminar, QtCore.SIGNAL('clicked()'), self.procesoEliminarClicked)
            if isinstance(item.getObjeto(), Proceso):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                proceso = VerProceso(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo = False, centralWidget = proceso)
                if self.listaIzquierda.currentItem().text() == MainApp.TXTACTUACIONES:
                    nuevoElemento.getCentralWidget().tabWidget.setCurrentIndex(1)
                nuevoElemento.setMaximumWidth(340)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0, 1, 1, 1)
                self.connect(nuevoElemento.btnEditar, QtCore.SIGNAL('clicked()'), self.procesoEditarClicked)
                self.connect(nuevoElemento.btnEliminar, QtCore.SIGNAL('clicked()'), self.procesoEliminarClicked)
            if isinstance(item.getObjeto(), Plantilla):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                plantilla = VerPlantilla(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo = True, centralWidget = plantilla, plantilla = True)
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0, 1, 1, 1)
                self.connect(nuevoElemento.btnCrearProceso, QtCore.SIGNAL('clicked()'), self.plantillaNuevoProcesoClicked)
                self.connect(nuevoElemento.btnEditar, QtCore.SIGNAL('clicked()'), self.plantillaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, QtCore.SIGNAL('clicked()'), self.plantillaEliminarClicked)
            if isinstance(item.getObjeto(), Persona):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                persona = VerPersona(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo = True, centralWidget = persona)
                nuevoElemento.setMaximumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0, 1, 1, 1)
                self.connect(nuevoElemento.btnEditar, QtCore.SIGNAL('clicked()'), self.personaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, QtCore.SIGNAL('clicked()'), self.personaEliminarClicked)
            if isinstance(item.getObjeto(), Juzgado):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                juzgado = VerJuzgado(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo = True, centralWidget = juzgado)
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0, 1, 1, 1)
                self.connect(nuevoElemento.btnEditar, QtCore.SIGNAL('clicked()'), self.juzgadoEditarClicked)
                self.connect(nuevoElemento.btnEliminar, QtCore.SIGNAL('clicked()'), self.juzgadoEliminarClicked)
            if isinstance(item.getObjeto(), Categoria):
                #Borrar el elemento derecho
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                categoria = VerCategoria(item.getObjeto())
                #Agregar elemento derecho y ponerle un tamano maximo
                nuevoElemento = ColumnaDerecha(titulo = True, centralWidget = categoria)
                nuevoElemento.setMaximumWidth(310)
                nuevoElemento.setMinimumWidth(310)
                self.gridLayout.addWidget(nuevoElemento, 0, 1, 1, 1)
                self.connect(nuevoElemento.btnEditar, QtCore.SIGNAL('clicked()'), self.categoriaEditarClicked)
                self.connect(nuevoElemento.btnEliminar, QtCore.SIGNAL('clicked()'), self.categoriaEliminarClicked)
        elif hasattr(self.columna1, 'widget'):
            #Se va por aqui si columna1 es un splitter
            self.__restablecerElementoDerecho()
            if self.columna1.widget(0).currentItem().text() == MainApp.TXTPROCESOS:
                p = Persistence()
                lista = p.consultarAtributos()
                listado = ListadoBusqueda(lista)
                listado.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                if self.columna1.count() > 1:
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                columna = ColumnaWidget(listado, listado.getSearchField())
                self.columna1.addWidget(columna)
            elif self.columna1.widget(0).currentItem().text() == MainApp.TXTPLANTILLAS:
                p = Persistence()
                lista = p.consultarAtributos()
                listado = ListadoBusqueda(lista)
                listado.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                if self.columna1.count() > 1:
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
                columna = ColumnaWidget(listado, listado.getSearchField())
                self.columna1.addWidget(columna)
            elif self.columna1.widget(0).currentItem().text() == MainApp.TXTDEMANDANTES:
                p = Persistence()
                lista = p.consultarAtributosPersona()
                listado = ListadoBusqueda(lista)
                listado.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                if self.columna1.count() > 1:
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
                columna = ColumnaWidget(listado, listado.getSearchField())
                self.columna1.addWidget(columna)
            elif self.columna1.widget(0).currentItem().text() == MainApp.TXTDEMANDADOS:
                p = Persistence()
                lista = p.consultarAtributosPersona()
                listado = ListadoBusqueda(lista)
                listado.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                if self.columna1.count() > 1:
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
                columna = ColumnaWidget(listado, listado.getSearchField())
                self.columna1.addWidget(columna)
            elif self.columna1.widget(0).currentItem().text() == MainApp.TXTJUZGADOS:
                p = Persistence()
                lista = p.consultarAtributosJuzgado()
                listado = ListadoBusqueda(lista)
                listado.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                if self.columna1.count() > 1:
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
                columna = ColumnaWidget(listado, listado.getSearchField())
                self.columna1.addWidget(columna)
            elif self.columna1.widget(0).currentItem().text() == MainApp.TXTACTUACIONES:
                p = Persistence()
                lista = p.consultarAtributosActuacion()
                listado = ListadoBusqueda(lista)
                listado.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                if self.columna1.count() > 1:
                    #Borrar la tercera columna si existe
                    self.columna1.widget(1).hide()
                    self.columna1.widget(1).deleteLater()
                #Agregar la tercera columna
                columna = ColumnaWidget(listado, listado.getSearchField())
                self.columna1.addWidget(columna)
            self.connect(listado, QtCore.SIGNAL('itemSelectionChanged()'), self.columnaCamposElementChanged)
            self.connect(listado, QtCore.SIGNAL('customContextMenuRequested(QPoint)'), self.camposContextMenu)
            self.connect(columna, QtCore.SIGNAL('clicked()'), self.columnaCamposAgregarClicked)    

    def columnaCamposElementChanged(self):
        if hasattr(self.columna1, 'count'):
            #Se maneja la seleccion de una campo personalizado en la tercera columna
            if self.columna1.count() > 1:
                item = self.columna1.widget(1).getCentralWidget().currentItem()
                if hasattr(item, 'getObjeto'):
                    # Se filtra que si se haya seleccionado algun campo
                    elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                    self.gridLayout.removeWidget(elementoGrid)
                    elementoGrid.setParent(None)
                    campo = VerCampoPersonalizado(item.getObjeto())
                    nuevoElemento = ColumnaDerecha(titulo = True, centralWidget = campo)
                    nuevoElemento.setMaximumWidth(310)
                    nuevoElemento.setMinimumWidth(310)
                    self.gridLayout.addWidget(nuevoElemento, 0, 1, 1, 1)
                    self.connect(nuevoElemento.btnEditar, QtCore.SIGNAL('clicked()'), self.campoEditarClicked)
                    self.connect(nuevoElemento.btnEliminar, QtCore.SIGNAL('clicked()'), self.campoEliminarClicked)
    
    def columnaCamposAgregarClicked(self):
        #Manejo del boton agregar en campos personalizados de la tercera columna
        if self.columna1.widget(0).currentItem().text() == MainApp.TXTPROCESOS:
            campoVentana = NuevoCampo(NuevoCampo.PROCESO)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTPLANTILLAS:
            campoVentana = NuevoCampo(NuevoCampo.PROCESO)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTDEMANDANTES:
            campoVentana = NuevoCampo(NuevoCampo.PERSONA)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTDEMANDADOS:
            campoVentana = NuevoCampo(NuevoCampo.PERSONA)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTJUZGADOS:
            campoVentana = NuevoCampo(NuevoCampo.JUZGADO)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTACTUACIONES:
            campoVentana = NuevoCampo(NuevoCampo.ACTUACION)
            if campoVentana.exec_():
                campo = campoVentana.getCampo()
                self.columna1.widget(1).getCentralWidget().add(campo)
            del campoVentana
    
    def procesoEditarClicked(self):
        elemento = self.columna1.getCentralWidget().currentItem().getObjeto()
        if isinstance(elemento, Proceso):
            proceso = elemento
            procesoVentana = NuevoProceso(proceso)
            if procesoVentana.exec_():
                self.columna1.getCentralWidget().replace(procesoVentana.getProceso())
            self.columna1ElementChanged()
            del procesoVentana
        else:
            #Se viene por aqui si es una ActuacionCritica
            proceso = Persistence().consultarProceso(elemento.getId_proceso())
            procesoVentana = NuevoProceso(proceso)
            if procesoVentana.exec_():
                self.elementChanged()
            del procesoVentana
        
            
        
    def procesoEliminarClicked(self):
        elemento = self.columna1.getCentralWidget().getSelectedItem()
        if self.columna1.getCentralWidget().remove():            
            if isinstance(elemento, Proceso):
                proceso = elemento
            else:   
                #Si es una actuacion critica, debe cargar el proceso desde la base de datos
                proceso = Persistence().consultarProceso(elemento.getId_proceso())
            p = Persistence()
            p.borrarProceso(proceso)           
            if not isinstance(elemento, Proceso):
                #Si es la seccion actuacion critica, debe recargar la lista
                self.elementChanged()
            elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                self.label = QtGui.QLabel() 
                self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
            
    
    def personaEditarClicked(self):
        persona = self.columna1.getCentralWidget().currentItem().getObjeto()
        personaVentana = NuevaPersona(persona)
        if personaVentana.exec_():
            self.columna1.getCentralWidget().replace(personaVentana.getPersona())
        self.columna1ElementChanged()
        del personaVentana
    
    def personaEliminarClicked(self):
        persona = self.columna1.getCentralWidget().getSelectedItem()
        if self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarPersona(persona)
            elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                self.label = QtGui.QLabel() 
                self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
    
    def juzgadoEditarClicked(self):
        juzgado = self.columna1.getCentralWidget().currentItem().getObjeto()
        juzgadoVentana = NuevoJuzgado(juzgado)
        if juzgadoVentana.exec_():
            self.columna1.getCentralWidget().replace(juzgadoVentana.getJuzgado())
        self.columna1ElementChanged()
        del juzgadoVentana
    
    def juzgadoEliminarClicked(self):
        juzgado = self.columna1.getCentralWidget().getSelectedItem()
        if self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarJuzgado(juzgado)
            elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                self.label = QtGui.QLabel() 
                self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
    
    def plantillaNuevoProcesoClicked(self):
        plantilla = self.columna1.getCentralWidget().currentItem().getObjeto()
        procesoVentana = NuevoProceso(plantilla = plantilla)
        procesoVentana.exec_()
        self.columna1ElementChanged()
        del procesoVentana
    
    def plantillaEditarClicked(self):
        plantilla = self.columna1.getCentralWidget().currentItem().getObjeto()
        plantillaVentana = NuevaPlantilla(plantilla)
        if plantillaVentana.exec_():
            self.columna1.getCentralWidget().replace(plantillaVentana.getPlantilla())
        self.columna1ElementChanged()
        del plantillaVentana
    
    def plantillaEliminarClicked(self):
        plantilla = self.columna1.getCentralWidget().getSelectedItem()
        if self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarPlantilla(plantilla)
            elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                self.label = QtGui.QLabel() 
                self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
    
    def categoriaEditarClicked(self):
        categoria = self.columna1.getCentralWidget().currentItem().getObjeto()
        categoriaVentana = NuevaCategoria(categoria)
        if categoriaVentana.exec_():
            self.columna1.getCentralWidget().replace(categoriaVentana.getCategoria())
        self.columna1ElementChanged()
        del categoriaVentana
    
    def categoriaEliminarClicked(self):
        categoria = self.columna1.getCentralWidget().getSelectedItem()
        if categoria.getId_categoria() == '1':
            QtGui.QMessageBox.warning(self, 'No se puede borrar', unicode('La categoría Ninguna es por defecto y no se puede eliminar'))
        elif self.columna1.getCentralWidget().remove():
            p = Persistence()
            p.borrarCategoria(categoria)
            elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
            if self.columna1.getCentralWidget().count() == 0:
                self.gridLayout.removeWidget(elementoGrid)
                elementoGrid.setParent(None)
                self.label = QtGui.QLabel() 
                self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
    
    def campoEditarClicked(self):
        if self.columna1.widget(0).currentItem().text() == MainApp.TXTPROCESOS:
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(), 'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo = NuevoCampo.PROCESO, campo = campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTPLANTILLAS:
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(), 'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo = NuevoCampo.PROCESO, campo = campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTDEMANDANTES:
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(), 'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo = NuevoCampo.PERSONA, campo = campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTDEMANDADOS:
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(), 'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo = NuevoCampo.PERSONA, campo = campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTJUZGADOS:
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(), 'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo = NuevoCampo.JUZGADO, campo = campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                del campoVentana
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTACTUACIONES:
            if hasattr(self.columna1.widget(1).getCentralWidget().currentItem(), 'getObjeto'):
                campo = self.columna1.widget(1).getCentralWidget().currentItem().getObjeto()
                campoVentana = NuevoCampo(tipo = NuevoCampo.ACTUACION, campo = campo)
                if campoVentana.exec_():
                    self.columna1.widget(1).getCentralWidget().replace(campoVentana.getCampo())
                    self.columnaCamposElementChanged()
                del campoVentana
    
    def campoEliminarClicked(self):
        campo = self.columna1.widget(1).getCentralWidget().getSelectedItem()
        if self.columna1.widget(0).currentItem().text() == MainApp.TXTPROCESOS:
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributo(campo)
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    self.gridLayout.removeWidget(elementoGrid)
                    elementoGrid.setParent(None)
                    self.label = QtGui.QLabel() 
                    self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTPLANTILLAS:
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributo(campo)
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    self.gridLayout.removeWidget(elementoGrid)
                    elementoGrid.setParent(None)
                    self.label = QtGui.QLabel() 
                    self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTDEMANDANTES:
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributoPersona(campo)
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    self.gridLayout.removeWidget(elementoGrid)
                    elementoGrid.setParent(None)
                    self.label = QtGui.QLabel() 
                    self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTDEMANDADOS:
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributoPersona(campo)
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    self.gridLayout.removeWidget(elementoGrid)
                    elementoGrid.setParent(None)
                    self.label = QtGui.QLabel() 
                    self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTJUZGADOS:
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributoJuzgado(campo)
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    self.gridLayout.removeWidget(elementoGrid)
                    elementoGrid.setParent(None)
                    self.label = QtGui.QLabel() 
                    self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        elif self.columna1.widget(0).currentItem().text() == MainApp.TXTACTUACIONES:
            if self.columna1.widget(1).getCentralWidget().remove():
                p = Persistence()
                p.borrarAtributoActuacion(campo)
                elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
                if self.columna1.widget(1).getCentralWidget().count() == 0:
                    self.gridLayout.removeWidget(elementoGrid)
                    elementoGrid.setParent(None)
                    self.label = QtGui.QLabel() 
                    self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
                    self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
                    
    def __restablecerElementoDerecho(self):
        #Reestablecer el logo de la bolita
        elementoGrid = self.gridLayout.itemAtPosition(0, 1).widget()
        if isinstance(elementoGrid, (VerProceso, VerPersona, VerPlantilla, VerJuzgado, VerActuacion, VerCategoria, VerCampoPersonalizado, ColumnaDerecha)):
            self.gridLayout.removeWidget(elementoGrid)
            elementoGrid.setParent(None)
            self.label = QtGui.QLabel() 
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
            self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
            
    def listaIzquierdaContextMenu(self, pos):
        item = self.listaIzquierda.currentItem()
        if item.text() not in (MainApp.TXTACTUACIONES, MainApp.TXTCAMPOS, MainApp.TXTSINCRONIZAR, MainApp.TXTAJUSTES):
            menu = QtGui.QMenu(self)
            menu.addAction(self.__createAction('Nuevo', self.columna1AgregarClicked))
            menu.exec_(self.mapToGlobal(pos))
        
    def listaCamposContextMenu(self, pos):
        menu = QtGui.QMenu(self)
        menu.addAction(self.__createAction('Nuevo', self.columnaCamposAgregarClicked))
        menu.exec_(self.columna1.mapToGlobal(pos))
        
    def camposContextMenu(self, pos):
        menu = QtGui.QMenu(self)
        menu.addAction(self.__createAction('Nuevo', self.columnaCamposAgregarClicked))
        menu.addAction(self.__createAction('Editar', self.campoEditarClicked))
        menu.addSeparator()
        menu.addAction(self.__createAction('Eliminar', self.campoEliminarClicked))
        menu.exec_(self.columna1.widget(1).getCentralWidget().mapToGlobal(pos))
        
    def columna1ContextMenu(self, pos):
        menu = QtGui.QMenu(self)
        menu.addAction(self.__createAction('Nuevo', self.columna1AgregarClicked))
        menu.addAction(self.__createAction('Editar', self.columna1ContextEditar))
        menu.addSeparator()
        menu.addAction(self.__createAction('Eliminar', self.columna1ContextEliminar))
        menu.exec_(self.columna1.mapToGlobal(pos))
    
    def columna1ContextEditar(self):
        objeto = self.columna1.getCentralWidget().currentItem().getObjeto()
        if isinstance(objeto, Proceso):
            self.procesoEditarClicked()
        elif isinstance(objeto, Plantilla):
            self.plantillaEditarClicked()
        elif isinstance(objeto, Persona):
            self.personaEditarClicked()
        elif isinstance(objeto, Juzgado):
            self.juzgadoEditarClicked()
        elif isinstance(objeto, Categoria):
            self.categoriaEditarClicked()
            
    def columna1ContextEliminar(self):
        objeto = self.columna1.getCentralWidget().currentItem().getObjeto()
        if isinstance(objeto, Proceso):
            self.procesoEliminarClicked()
        elif isinstance(objeto, Plantilla):
            self.plantillaEliminarClicked()
        elif isinstance(objeto, Persona):
            self.personaEliminarClicked()
        elif isinstance(objeto, Juzgado):
            self.juzgadoEliminarClicked()
        elif isinstance(objeto, Categoria):
            self.categoriaEliminarClicked()
            
    def menuNuevoProcesoClicked(self):
        procesoVentana = NuevoProceso()
        if procesoVentana.exec_():
            self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTPROCESOS))
            self.elementChanged()
        del procesoVentana
        
    def menuNuevaPlantillaClicked(self):
        plantillaVentana = NuevaPlantilla()
        if plantillaVentana.exec_():
            self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTPLANTILLAS))
            self.elementChanged()
        del plantillaVentana
    
    def menuNuevoDemandanteClicked(self):
        personaVentana = NuevaPersona(tipo = 1)
        if personaVentana.exec_():
            self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTDEMANDANTES))
            self.elementChanged()
        del personaVentana
    
    def menuNuevoDemandadoClicked(self):
        personaVentana = NuevaPersona(tipo = 2)
        if personaVentana.exec_():
            self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTDEMANDADOS))
            self.elementChanged()
        del personaVentana      
        
    def menuNuevoJuzgadoClicked(self):
        juzgadoVentana = NuevoJuzgado()
        if juzgadoVentana.exec_():
            self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTJUZGADOS))
            self.elementChanged()
        del juzgadoVentana
    
    def menuNuevaActuacionClicked(self):
        procesoSelect = ListadoDialogo(ListadoDialogo.PROCESO)
        if procesoSelect.exec_():
            nuevaActuacion = NuevaActuacion()
            if nuevaActuacion.exec_():
                p = Persistence()
                p.guardarActuacion(nuevaActuacion.getActuacion(), procesoSelect.getSelected().getId_proceso())
            del nuevaActuacion
            self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTACTUACIONES))
            self.elementChanged()
        del procesoSelect
    
    def menuNuevaCategoriaClicked(self):
        categoriaVentana = NuevaCategoria()
        if categoriaVentana.exec_():
            self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTCATEGORIAS))
            self.elementChanged()
        del categoriaVentana
        
    def menuNuevoCampoProcesoClicked(self):
            campoVentana = NuevoCampo(NuevoCampo.PROCESO)
            if campoVentana.exec_():
                self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTCAMPOS))
                self.elementChanged()
            del campoVentana

    def menuNuevoCampoPersonaClicked(self):
            campoVentana = NuevoCampo(NuevoCampo.PERSONA)
            if campoVentana.exec_():
                self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTCAMPOS))
                self.elementChanged()
            del campoVentana
            
    def menuNuevoCampoJuzgadoClicked(self):
            campoVentana = NuevoCampo(NuevoCampo.JUZGADO)
            if campoVentana.exec_():
                self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTCAMPOS))
                self.elementChanged()
            del campoVentana

    def menuNuevoCampoActuacionClicked(self):
            campoVentana = NuevoCampo(NuevoCampo.ACTUACION)
            if campoVentana.exec_():
                self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTCAMPOS))
                self.elementChanged()
            del campoVentana
            
    def menuNuevoProcesoPlantillaClicked(self):
        plantillaSelect = ListadoDialogo(ListadoDialogo.PLANTILLA)
        if plantillaSelect.exec_():
            procesoVentana = NuevoProceso(plantilla = plantillaSelect.getSelected())
            if procesoVentana.exec_():
                self.listaIzquierda.setCurrentRow(self.lista.index(MainApp.TXTPROCESOS))
                self.elementChanged()
            del procesoVentana
        del plantillaSelect
        
    def menuExportarCSVClicked(self):
        exportarDialog = ExportarCSVDialog()
        exportarDialog.exec_()
    
    def menuExportarArchivoClicked(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Exportar Archivo')[0]
        if fname != '':
            fname = fname + '.bk'
            shutil.copy(ConnectionManager().getDbLocation(), fname)
    
    def menuImportarArchivoClicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Importar Archivo')[0]
        if fname != '':
            shutil.copy(fname, ConnectionManager().getDbLocation())
    
    def __createAction(self, text, slot = None, shortcut = None, icon = None, tip = None, checkable = False, signal = "triggered()"):
        action = QtGui.QAction(text, self)
        if icon is not None:
            action.setIcon(QtGui.QIcon(":/images/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action
import sys
app = QtGui.QApplication(sys.argv)
app.setOrganizationName("ehmSoftware")
app.setOrganizationDomain("ehmsoft.com")
app.setApplicationName("Procesos Judiciales")
app.setWindowIcon(QtGui.QIcon(":/images/icono.png"))
theapp = MainApp()
theapp.listaIzquierda.setCurrentRow(0)
theapp.show()
sys.exit(app.exec_())
