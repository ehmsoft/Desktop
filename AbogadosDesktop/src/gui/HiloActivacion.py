# -*- coding: utf-8 -*-
'''
Created on 21/08/2012

@author: elfotografo007
'''
from PySide import QtCore
from httplib import HTTPSConnection
from urllib import urlencode
from xml.dom.minidom import parseString
from ssl import SSLError
class HiloActivacion(QtCore.QThread):
    def run(self):
        self.peticion(correo=self.correo, peticion=self.pet)
        self.exec_()
        
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
        conn= HTTPSConnection('activacionehm.herokuapp.com', timeout=10)
        params = urlencode({'correo':'%s' % correo, 'aplicacion_id':1})
        conn.request(method="POST", url="/%s.xml" % peticion, body=params)
        try:
            response = conn.getresponse()
            data = response.read()
            self.flag, self.respuesta = self.procesar(data, peticion)
        except SSLError:
            self.flag = False
            self.respuesta = u"El servidor ha tardado demasiado en responder. Por favor verifique su conexión a internet e intente de nuevo. Si el problema persiste por favor comuníquese con nuestro personal de soporte técnico: soporte@ehmsoft.com"
        finally:
            conn.close()
            self.exit()