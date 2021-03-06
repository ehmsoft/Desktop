# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: harold
'''

from PySide import QtGui, QtCore
from NuevaActuacionScreen import Ui_NuevaActuacion
from core.Actuacion import Actuacion
from gui.ver.VerJuzgado import VerJuzgado
from gui.ListadoDialogo import ListadoDialogo
from NuevoCampo import NuevoCampo
from datetime import datetime
from NuevoJuzgado import NuevoJuzgado
from gui.GestorCampos import GestorCampos
from persistence.Persistence import Persistence
from gui.DialogoAuxiliar import DialogoAuxiliar
from gui import Util
from gui.nuevo.NuevaCita import NuevaCita
from gui.GestorCitas import GestorCitas

class NuevaActuacion(QtGui.QDialog, Ui_NuevaActuacion):
    '''
    classdocs
    '''
    def __init__(self, actuacion=None, parent=None):
        super(NuevaActuacion, self).__init__(parent)
        self.__dirty = False
        
        if actuacion is not None and not isinstance(actuacion, Actuacion):
            raise TypeError("El objeto actuacion debe ser de la clase Actuacion")
 
        self.setupUi(self)
        self.__actuacion = actuacion
        self.__juzgado = None
        campos = []
                
        if actuacion is not None:
            self.setWindowTitle(u'Editar actuación')
            self.groupBox.setTitle(u'Datos de la actuación:')
            self.__juzgado = actuacion.getJuzgado()
            campos = actuacion.getCampos()
            self.txtDescripcion.setText(unicode(actuacion.getDescripcion()))
            self.lblJuzgado.setText(unicode(self.__juzgado.getNombre()))
            self.dteFecha.setDateTime(actuacion.getFecha())
            self.dteFechaProxima.setDateTime(actuacion.getFechaProxima())
            p = Persistence()
            citas = p.consultarCitasCalendario()
            for cita in citas:
                if cita.getId_actuacion() == actuacion.getId_actuacion():
                    self.__cita = cita
                    self.checkCita.setChecked(True)
                    break
            else:
                self.__cita = None
                self.checkCita.setChecked(False)
        else:
            self.dteFecha.setDateTime(datetime.today())
            self.dteFechaProxima.setDateTime(datetime.today())
            self.lblJuzgado.setText(u'vacío')
            self.__cita = None
            
        self.__dialogo = DialogoAuxiliar(self)
        
        self.__clickJuzgado()
        
        cambiar = self.__createAction("Cambiar", self.__cambiarJuzgado)
        cambiar.setData(self.lblJuzgado)
        editar = self.__createAction("Editar", self.__editarJuzgado)
        editar.setData(self.lblJuzgado)
        
        self.lblJuzgado.addActions([cambiar, editar])
        
        self.__gestor = GestorCampos(campos=campos, formLayout=self.formLayout, parent=self,
                                     constante_de_edicion=NuevoCampo.ACTUACION, constante_de_creacion=ListadoDialogo.CAMPOACTUACION)
        self.btnAdd.clicked.connect(self.__gestor.addCampo)
        
        self.txtDescripcion.textChanged.connect(self.setDirty)
        self.dteFecha.dateTimeChanged.connect(self.setDirty)
        self.dteFechaProxima.dateTimeChanged.connect(self.setDirty)
        self.dteFechaProxima.dateTimeChanged.connect(lambda : self.verificarFechas(interna = False))
        self.dteFecha.dateTimeChanged.connect(lambda : self.verificarFechas(interna = False))
        self.checkCita.clicked.connect(self.setCita)
        
        self.actionEditarCita = self.__createAction('Editar cita', self.editarCita)
        self.checkCita.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.setActionCita()
        
    def verificarFechas(self, fecha = None, interna = True):
        if self.dteFechaProxima.dateTime() < self.dteFecha.dateTime() and not interna:
            from datetime import timedelta
            self.dteFechaProxima.setDateTime(self.dteFecha.dateTime().toPython() + timedelta(0, 60))
            #QtGui.QMessageBox.information(self, 'Error', u'La fecha próxima no puede ser menor a la fecha de creación')
        
    def setActionCita(self):
        if self.__cita == None:
            self.checkCita.removeAction(self.actionEditarCita)
        else:
            self.checkCita.addAction(self.actionEditarCita)
        
    def editarCita(self):
        editar = NuevaCita(cita=self.__cita, parent=self)
        if editar.exec_():
            gestor = GestorCitas()
            gestor.actualizarCitas()
        
    def setCita(self):
        boolean = self.checkCita.checkState()
        if boolean:
            if self.__actuacion:
                guardar = True
            else:
                guardar = False
            nueva = NuevaCita(actuacion=self.__actuacion, cita=None, fecha=self.dteFechaProxima.dateTime(), parent=self, isGuardar=guardar)
            if nueva.exec_():
                self.__cita = nueva.getCita()
            else:
                self.checkCita.setChecked(False)
            nueva.setParent(None)
        else:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Question)
            message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            message.setDefaultButton(QtGui.QMessageBox.No)
            message.setText(u'¿Desea eliminar la cita?')
            if message.exec_() == QtGui.QMessageBox.Yes:
                if self.__actuacion:
                    p = Persistence()
                    p.borrarCitaCalendario(self.__cita)
                    gestor = GestorCitas()
                    gestor.actualizarCitas()
                self.__cita = None
            else:
                self.checkCita.setChecked(True)
        self.setActionCita()
        
    def getActuacion(self):
        return self.__actuacion
    
    def __createAction(self, text, slot=None):
        action = QtGui.QAction(text, self)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL("triggered()"), slot)
        return action 
    
    def __cambiarJuzgado(self):
        listado = ListadoDialogo(ListadoDialogo.JUZGADO, self)
        if listado.exec_():
            self.__juzgado = listado.getSelected()
            self.lblJuzgado.setText(self.__juzgado.getNombre())
            self.__dirty = True
            del(listado)
    
    def __editarJuzgado(self):
        if self.__juzgado is not None and self.__juzgado.getId_juzgado() is not "1":
            dialogo = NuevoJuzgado(self.__juzgado, self)
            if dialogo.exec_():
                self.lblJuzgado.setText(self.__juzgado.getNombre())
                if isinstance(self.horizontal.itemAt(1).widget(), VerJuzgado):
                    self.horizontal.itemAt(1).widget().deleteLater()
                    vista = VerJuzgado(self.__juzgado, self)
                    self.horizontal.addWidget(vista)
            del(dialogo)
        
    def accept(self):
        if len(self.txtDescripcion.text()) is 0:
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText(u"La descripción se considera obligatoria")
            message.exec_()
            self.txtDescripcion.setFocus()
        elif self.__juzgado is None or self.__juzgado.getId_juzgado() is "1":
            message = QtGui.QMessageBox()
            message.setIcon(QtGui.QMessageBox.Warning)
            message.setText(u"El juzgado no se permite vacío")
            message.exec_()
            self.txtDescripcion.setFocus()
        elif self.__gestor.organizarCampos():
            self.__guardar()
            
    def __guardar(self):
        del(self.__dialogo)
        fecha = self.dteFecha.dateTime().toPython()
        fechaProxima = self.dteFechaProxima.dateTime().toPython()
        descripcion = self.txtDescripcion.text()
        if self.checkCita.isChecked():
            cita = self.__cita
        else:
            cita = None
        if not self.__actuacion:
            self.__actuacion = Actuacion(juzgado=self.__juzgado, fecha=fecha,
                                         fechaProxima=fechaProxima, descripcion=descripcion,
                                         campos=self.__gestor.getCampos())
        else:
            if self.__actuacion.getId_actuacion() is not None:
                camposNuevos = self.__gestor.getCamposNuevos()
                camposEliminados = self.__gestor.getCamposEliminados()
                try:
                    p = Persistence()
                    for campo in camposEliminados:
                        p.borrarCampoActuacion(campo)
                    for campo in camposNuevos:
                        p.guardarCampoActuacion(campo, self.__actuacion.getId_actuacion())
                except Exception, e:
                    print "guardar actuación -> " % e.args
            self.__actuacion.setDescripcion(descripcion)
            self.__actuacion.setFecha(fecha)
            self.__actuacion.setFechaProxima(fechaProxima)
            self.__actuacion.setCampos(self.__gestor.getCampos())
            self.__actuacion.setJuzgado(self.__juzgado)
        self.__actuacion.cita = cita
        return QtGui.QDialog.accept(self)
        
    def __clickJuzgado(self):
        dialogo = self.__dialogo
        widget = self
        lblJuzgado = self.lblJuzgado
                    
        def mousePressEvent(self):
            if QtCore.Qt.MouseButton.LeftButton is self.button():
                if widget.__juzgado is not None and widget.__juzgado.getId_juzgado() is not "1":
                    vista = VerJuzgado(widget.__juzgado, widget)
                    dialogo.setWidget(vista)
                else:
                    widget.__cambiarJuzgado()
            return QtGui.QLabel.mousePressEvent(lblJuzgado, self)
            
        self.lblJuzgado.mousePressEvent = mousePressEvent
        
    def reject(self):
        #del(self.__dialogo)
        Util.reject(self, self.__dirty)
        
    def setDirty(self):
        sender = self.sender()
        if isinstance(sender, QtGui.QLineEdit):
            self.__dirty = True
            self.disconnect(sender, QtCore.SIGNAL("textEdited()"), self.setDirty)
        elif isinstance(sender, QtGui.QDateTimeEdit):
            self.__dirty = True
            self.disconnect(sender, QtCore.SIGNAL("dateTimeChanged()"), self.setDirty)
