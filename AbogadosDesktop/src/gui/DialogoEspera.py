# -*- coding: utf-8 -*-
'''
Created on 10/08/2012

@author: elfotografo007
'''
from PySide import QtGui
from httplib import HTTPConnection
from urllib import urlencode
from xml.dom.minidom import parseString

class DialogoEspera(QtGui.QDialog):
    def __init__(self, parent = None):
        super(DialogoEspera, self).__init__(parent)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(QtGui.QLabel(u'Por Favor espere mientras se comunica con el servidor de activación'))
        self.setLayout(layout)
        
    def iniciarDesactivacion(self, correo):
        self.show()
        self.raise_()
        try:
            flag, respuesta = self.peticion(correo, 'desactivar')
        except Exception as e:
            raise e
        finally:   
            self.hide()
        return flag,respuesta
        
    def iniciarActivacion(self, correo):
        self.show()
        self.raise_()
        try:
            flag, respuesta = self.peticion(correo, 'activar')
        except Exception as e:
            raise e
        finally:   
            self.hide()
        return flag,respuesta
        
    def procesar(self,texto,peticion):
        documento = parseString(texto)
        result =  documento.getElementsByTagName("result")[0].childNodes[0].nodeValue
        if result == 'true':
            nodoCorreo=documento.getElementsByTagName("correo")[0]
            correo = nodoCorreo.childNodes[0].nodeValue
            pendiente=documento.getElementsByTagName("pendiente")[0].childNodes[0].nodeValue
            total = documento.getElementsByTagName("total")[0].childNodes[0].nodeValue
            if peticion == 'activar':
                return True, u"Activación Correcta\nCorreo: {0}\nActivaciones restantes: {1}\nTotal: {2}".format(correo, pendiente, total)
            else:
                return True, u"Desactivación Correcta\nCorreo: {0}\nActivaciones restantes: {1}\nTotal: {2}".format(correo, pendiente, total)
        else:
            if peticion == 'activar':
                return False, u"Lo sentimos pero no se han encontrado licencias disponibles. Por favor comuníquese con nuestro personal de soporte técnico: soporte@ehmsoft.com"
            else:
                return False, u"Lo sentimos pero no se ha encontrado la cuenta. Por favor comuníquese con nuestro personal de soporte técnico: soporte@ehmsoft.com"

    def peticion(self, correo, peticion):
        conn= HTTPConnection('localhost', 3000, timeout=10)
        params = urlencode({'correo':'%s' % correo, 'aplicacion_id':1})
        conn.request(method="POST", url="/%s.xml" % peticion, body=params)
        response = conn.getresponse()
        data = response.read()
        flag, respuesta = self.procesar(data, peticion)
        conn.close()
        return flag, respuesta