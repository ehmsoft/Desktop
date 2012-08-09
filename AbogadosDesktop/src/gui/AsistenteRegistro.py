# -*- coding: utf-8 -*-
'''
Created on 09/08/2012

@author: elfotografo007
'''
from PySide import QtGui, QtCore
from gui.AsistenteRegistroScreen import Ui_WizardRegistro
from httplib import HTTPConnection
from urllib import urlencode
from xml.dom.minidom import parseString
from PyQt4.pyqtconfig import QtGuiModuleMakefile

class AsistenteRegistro(QtGui.QWizard, Ui_WizardRegistro):
    def __init__(self, parent=None):
        super(AsistenteRegistro, self).__init__(parent)
        self.setupUi(self)
        self.registro.validatePage = self.validatePage
        self.__valid = False
        
    def validatePage(self):
        correo = self.txtCorreo.text()
        if correo == "":
            QtGui.QMessageBox.warning(self, "Advertencia", u"El campo correo no puede estar vacío")
            return False
        else:
            dialogo = DialogoEspera()
            flag, respuesta = dialogo.iniciarActivacion(correo)
            QtGui.QMessageBox.warning(self,"Info", respuesta)
            self.__valid = flag
            return flag
    
    def isValid(self):
        return self.__valid
    
class DialogoEspera(QtGui.QDialog):
    def __init__(self, parent = None):
        super(DialogoEspera, self).__init__(parent)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(QtGui.QLabel(u'Por Favor espere mientras se comunica con el servidor de activación'))
        self.setLayout(layout)
        
    def iniciarActivacion(self, correo):
        self.show()
        self.raise_()
        flag, respuesta = self.peticion(correo)
        self.hide()
        return flag,respuesta
        
    def procesar(self,texto):
        documento = parseString(texto)
        result =  documento.getElementsByTagName("result")[0].childNodes[0].nodeValue
        if result == 'true':
            nodoCorreo=documento.getElementsByTagName("correo")[0]
            correo = nodoCorreo.childNodes[0].nodeValue
            pendiente=documento.getElementsByTagName("pendiente")[0].childNodes[0].nodeValue
            total = documento.getElementsByTagName("total")[0].childNodes[0].nodeValue
            return True, u"Activación Correcta\nCorreo: {0}\nActivaciones restantes: {1}\nTotal: {2}".format(correo, pendiente, total)
        else:
            return False, u"Lo sentimos pero no se han encontrado licencias disponibles. Por favor comuníquese con nuestro personal de soporte técnico: soporte@ehmsoft.com"
        
    def peticion(self, correo):
        conn= HTTPConnection('localhost', 3000, timeout=10)
        params = urlencode({'correo':'%s' % correo, 'aplicacion_id':1})
        conn.request(method="POST", url="/activar.xml", body=params)
        response = conn.getresponse()
        data = response.read()
        flag, respuesta = self.procesar(data)
        conn.close()
        return flag, respuesta