# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainApp.ui'
#
# Created: Fri Oct 19 09:59:51 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainApp(object):
    def setupUi(self, mainApp):
        mainApp.setObjectName("mainApp")
        mainApp.resize(800, 573)
        self.centralwidget = QtGui.QWidget(mainApp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 664, 504))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        mainApp.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_Archivo = QtGui.QMenu(self.menubar)
        self.menu_Archivo.setObjectName("menu_Archivo")
        self.menu_Nuevo = QtGui.QMenu(self.menu_Archivo)
        self.menu_Nuevo.setObjectName("menu_Nuevo")
        self.menuCampo_Personalizado = QtGui.QMenu(self.menu_Nuevo)
        self.menuCampo_Personalizado.setObjectName("menuCampo_Personalizado")
        self.menuExportar = QtGui.QMenu(self.menu_Archivo)
        self.menuExportar.setObjectName("menuExportar")
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuCalendario = QtGui.QMenu(self.menubar)
        self.menuCalendario.setObjectName("menuCalendario")
        mainApp.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainApp)
        self.statusbar.setObjectName("statusbar")
        mainApp.setStatusBar(self.statusbar)
        self.actionNuevoProceso = QtGui.QAction(mainApp)
        self.actionNuevoProceso.setObjectName("actionNuevoProceso")
        self.actionNuevaPlantilla = QtGui.QAction(mainApp)
        self.actionNuevaPlantilla.setObjectName("actionNuevaPlantilla")
        self.actionNuevoDemandante = QtGui.QAction(mainApp)
        self.actionNuevoDemandante.setObjectName("actionNuevoDemandante")
        self.actionNuevoDemandado = QtGui.QAction(mainApp)
        self.actionNuevoDemandado.setObjectName("actionNuevoDemandado")
        self.actionNuevoJuzgado = QtGui.QAction(mainApp)
        self.actionNuevoJuzgado.setObjectName("actionNuevoJuzgado")
        self.actionNuevaActuacion = QtGui.QAction(mainApp)
        self.actionNuevaActuacion.setObjectName("actionNuevaActuacion")
        self.actionNuevaCategoria = QtGui.QAction(mainApp)
        self.actionNuevaCategoria.setObjectName("actionNuevaCategoria")
        self.actionNuevoCampo_Proceso = QtGui.QAction(mainApp)
        self.actionNuevoCampo_Proceso.setObjectName("actionNuevoCampo_Proceso")
        self.actionNuevoCampo_Plantilla = QtGui.QAction(mainApp)
        self.actionNuevoCampo_Plantilla.setObjectName("actionNuevoCampo_Plantilla")
        self.actionNuevoCampo_Demandante = QtGui.QAction(mainApp)
        self.actionNuevoCampo_Demandante.setObjectName("actionNuevoCampo_Demandante")
        self.actionNuevoCampo_Demandado = QtGui.QAction(mainApp)
        self.actionNuevoCampo_Demandado.setObjectName("actionNuevoCampo_Demandado")
        self.actionNuevoCampo_Juzgado = QtGui.QAction(mainApp)
        self.actionNuevoCampo_Juzgado.setObjectName("actionNuevoCampo_Juzgado")
        self.actionNuevoCampo_Actuacion = QtGui.QAction(mainApp)
        self.actionNuevoCampo_Actuacion.setObjectName("actionNuevoCampo_Actuacion")
        self.actionImprimir = QtGui.QAction(mainApp)
        self.actionImprimir.setObjectName("actionImprimir")
        self.actionImportar = QtGui.QAction(mainApp)
        self.actionImportar.setObjectName("actionImportar")
        self.actionNuevoProceso_a_partir_de_Plantilla = QtGui.QAction(mainApp)
        self.actionNuevoProceso_a_partir_de_Plantilla.setObjectName("actionNuevoProceso_a_partir_de_Plantilla")
        self.actionArchivo_CSV = QtGui.QAction(mainApp)
        self.actionArchivo_CSV.setObjectName("actionArchivo_CSV")
        self.actionArchivo_de_Copia_de_Seguridad = QtGui.QAction(mainApp)
        self.actionArchivo_de_Copia_de_Seguridad.setObjectName("actionArchivo_de_Copia_de_Seguridad")
        self.actionAcerca_de_Procesos_Judiciales = QtGui.QAction(mainApp)
        self.actionAcerca_de_Procesos_Judiciales.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAcerca_de_Procesos_Judiciales.setObjectName("actionAcerca_de_Procesos_Judiciales")
        self.actionAcerca_de_Qt = QtGui.QAction(mainApp)
        self.actionAcerca_de_Qt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.actionAcerca_de_Qt.setObjectName("actionAcerca_de_Qt")
        self.actionMostrarCalendario = QtGui.QAction(mainApp)
        self.actionMostrarCalendario.setObjectName("actionMostrarCalendario")
        self.actionSalir_de_Procesos_Judiciales = QtGui.QAction(mainApp)
        self.actionSalir_de_Procesos_Judiciales.setMenuRole(QtGui.QAction.QuitRole)
        self.actionSalir_de_Procesos_Judiciales.setObjectName("actionSalir_de_Procesos_Judiciales")
        self.actionNuevaCitaCalendario = QtGui.QAction(mainApp)
        self.actionNuevaCitaCalendario.setObjectName("actionNuevaCitaCalendario")
        self.actionNuevaCita = QtGui.QAction(mainApp)
        self.actionNuevaCita.setObjectName("actionNuevaCita")
        self.actionDesactivar = QtGui.QAction(mainApp)
        self.actionDesactivar.setObjectName("actionDesactivar")
        self.menuCampo_Personalizado.addAction(self.actionNuevoCampo_Proceso)
        self.menuCampo_Personalizado.addAction(self.actionNuevoCampo_Plantilla)
        self.menuCampo_Personalizado.addAction(self.actionNuevoCampo_Demandante)
        self.menuCampo_Personalizado.addAction(self.actionNuevoCampo_Demandado)
        self.menuCampo_Personalizado.addAction(self.actionNuevoCampo_Juzgado)
        self.menuCampo_Personalizado.addAction(self.actionNuevoCampo_Actuacion)
        self.menu_Nuevo.addAction(self.actionNuevoProceso)
        self.menu_Nuevo.addAction(self.actionNuevaPlantilla)
        self.menu_Nuevo.addAction(self.actionNuevoDemandante)
        self.menu_Nuevo.addAction(self.actionNuevoDemandado)
        self.menu_Nuevo.addAction(self.actionNuevoJuzgado)
        self.menu_Nuevo.addAction(self.actionNuevaActuacion)
        self.menu_Nuevo.addAction(self.actionNuevaCategoria)
        self.menu_Nuevo.addAction(self.menuCampo_Personalizado.menuAction())
        self.menu_Nuevo.addAction(self.actionNuevoProceso_a_partir_de_Plantilla)
        self.menuExportar.addAction(self.actionArchivo_CSV)
        self.menuExportar.addAction(self.actionArchivo_de_Copia_de_Seguridad)
        self.menu_Archivo.addAction(self.menu_Nuevo.menuAction())
        self.menu_Archivo.addAction(self.actionImprimir)
        self.menu_Archivo.addAction(self.menuExportar.menuAction())
        self.menu_Archivo.addAction(self.actionImportar)
        self.menu_Archivo.addAction(self.actionSalir_de_Procesos_Judiciales)
        self.menuAyuda.addAction(self.actionAcerca_de_Procesos_Judiciales)
        self.menuAyuda.addAction(self.actionAcerca_de_Qt)
        self.menuAyuda.addAction(self.actionDesactivar)
        self.menuCalendario.addAction(self.actionMostrarCalendario)
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.menubar.addAction(self.menuCalendario.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(mainApp)
        QtCore.QMetaObject.connectSlotsByName(mainApp)

    def retranslateUi(self, mainApp):
        mainApp.setWindowTitle(QtGui.QApplication.translate("mainApp", "Procesos Judiciales", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Archivo.setTitle(QtGui.QApplication.translate("mainApp", "&Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Nuevo.setTitle(QtGui.QApplication.translate("mainApp", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCampo_Personalizado.setTitle(QtGui.QApplication.translate("mainApp", "Campo Personalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExportar.setTitle(QtGui.QApplication.translate("mainApp", "Exportar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setTitle(QtGui.QApplication.translate("mainApp", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCalendario.setTitle(QtGui.QApplication.translate("mainApp", "Calendario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoProceso.setText(QtGui.QApplication.translate("mainApp", "Proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevaPlantilla.setText(QtGui.QApplication.translate("mainApp", "Plantilla", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoDemandante.setText(QtGui.QApplication.translate("mainApp", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoDemandado.setText(QtGui.QApplication.translate("mainApp", "Contraparte", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoJuzgado.setText(QtGui.QApplication.translate("mainApp", "Juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevaActuacion.setText(QtGui.QApplication.translate("mainApp", "Actuación", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevaCategoria.setText(QtGui.QApplication.translate("mainApp", "Categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Proceso.setText(QtGui.QApplication.translate("mainApp", "Campo Proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Plantilla.setText(QtGui.QApplication.translate("mainApp", "Campo Plantilla", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Plantilla.setToolTip(QtGui.QApplication.translate("mainApp", "Nuevo Campo Plantilla", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Demandante.setText(QtGui.QApplication.translate("mainApp", "Campo Demandante", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Demandante.setToolTip(QtGui.QApplication.translate("mainApp", "Nuevo Campo Demandante", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Demandado.setText(QtGui.QApplication.translate("mainApp", "Campo Demandado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Demandado.setToolTip(QtGui.QApplication.translate("mainApp", "Nuevo Campo Demandado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Juzgado.setText(QtGui.QApplication.translate("mainApp", "Campo Juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Juzgado.setToolTip(QtGui.QApplication.translate("mainApp", "Nuevo Campo Juzgado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Actuacion.setText(QtGui.QApplication.translate("mainApp", "Campo Actuacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoCampo_Actuacion.setToolTip(QtGui.QApplication.translate("mainApp", "Nuevo Campo Actuacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImprimir.setText(QtGui.QApplication.translate("mainApp", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImprimir.setShortcut(QtGui.QApplication.translate("mainApp", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportar.setText(QtGui.QApplication.translate("mainApp", "Importar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportar.setShortcut(QtGui.QApplication.translate("mainApp", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevoProceso_a_partir_de_Plantilla.setText(QtGui.QApplication.translate("mainApp", "Proceso a partir de Plantilla", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArchivo_CSV.setText(QtGui.QApplication.translate("mainApp", "Archivo CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArchivo_de_Copia_de_Seguridad.setText(QtGui.QApplication.translate("mainApp", "Archivo de Copia de Seguridad", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de_Procesos_Judiciales.setText(QtGui.QApplication.translate("mainApp", "Acerca de Procesos Judiciales", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de_Qt.setText(QtGui.QApplication.translate("mainApp", "Acerca de Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMostrarCalendario.setText(QtGui.QApplication.translate("mainApp", "Mostrar Calendario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir_de_Procesos_Judiciales.setText(QtGui.QApplication.translate("mainApp", "Salir de Procesos Judiciales", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir_de_Procesos_Judiciales.setShortcut(QtGui.QApplication.translate("mainApp", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevaCitaCalendario.setText(QtGui.QApplication.translate("mainApp", "Cita", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNuevaCita.setText(QtGui.QApplication.translate("mainApp", "Nueva Cita", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesactivar.setText(QtGui.QApplication.translate("mainApp", "Desactivar", None, QtGui.QApplication.UnicodeUTF8))

