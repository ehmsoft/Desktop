# -*- coding: utf-8 -*-
'''
Created on 29/03/2012

@author: esteban
'''
from types import IntType
from persistence.Persistence import Persistence

class Preferencias(object):
    '''
        Clase Preferencias
        tipo alarma mensaje emerjento, correo electronico,icono notificacion, eliminar citas
    '''
    TXTPROCESOS = u'Procesos'
    TXTPLANTILLAS = u'Plantillas'
    TXTDEMANDANTES = u'Demandantes'
    TXTDEMANDADOS = u'Demandados'
    TXTJUZGADOS = u'Juzgados'
    TXTACTUACIONES = u'Actuaciones'
    TXTCATEGORIAS = u'Categorías'
    TXTCAMPOS = 'Campos Personalizados'
    TXTSINCRONIZAR = 'Sincronizar'
    TXTAJUSTES = 'Ajustes'
    TXTEVENTOS = u'Eventos Próximos'
    CANTEVENTOS = 10
    
    CORREO = 10402
    CORREO_NOTIFICACION = 10602
    CANTIDAD_EVENTOS = 10501
    TIPO_ALARMA = 10601
    LLAVE = 998
    VERSION = 999
    ULTIMA_SINC = 997
    
    def __init__(self):
        self.p = Persistence()
        preferencias = self.p.consultarPreferencias()
        for llaveD, valor in preferencias.iteritems():
            #consultar Preferencias:  correo 
            if llaveD == self.CORREO:
                self.__correo = valor
            #consultar Preferencias: Cantidad Eventos Proximos 
            elif llaveD == self.CANTIDAD_EVENTOS:
                self.__cantidadEventos = valor
            #consultar Preferencias: Tipo Alarma es un valor binario, primer bit mensaje emergente, segundo bit ,emsaje en icono de notificación, tercer bit correo electrónico
            elif llaveD == self.TIPO_ALARMA:
                self.__tipoAlarma = valor    
            #consultar Preferencias: llave 
            elif llaveD == self.LLAVE:
                self.__llave = valor
            #consultar Preferencias: Version 
            elif llaveD == self.VERSION:
                self.__version = valor
            #consultar Preferencias: Ultima sincronizacion 
            elif llaveD == self.ULTIMA_SINC:
                self.__ultimaSinc = valor
            elif llaveD == self.CORREO_NOTIFICACION:
                self.__correoNotificacion = valor
    
    #Getters    
    def getId_preferencia(self):
        return self.__id_preferencia
    def getCantidadEventos(self):
        return self.__cantidadEventos
    def getCorreo(self):
        return self.__correo
    def getCorreoNotificacion(self):
        return self.__correoNotificacion
    def getTipoAlarma(self):
        return self.__tipoAlarma
    def getLlave(self):
        return self.__llave
    def getVersion(self):
        return self.__version
    def getUltimaSinc(self):
        return self.__ultimaSinc
    
    #Setters
    def setCantidadEventos(self, cantidadEventos):
        if isinstance(cantidadEventos, IntType):
            self.__cantidadEventos = cantidadEventos
            self.p.actualizarPreferencia(id_preferencia=10501, valor=cantidadEventos)
            Preferencias.CANTEVENTOS = cantidadEventos
        else:
            raise TypeError('Tipo de dato no admitido')
    def setCorreo(self, correo):
        if isinstance(correo, basestring):
            self.__correo = correo
            self.p.actualizarPreferencia(id_preferencia=10402, valor=correo)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setCorreoNotificacion(self, correo):
        if isinstance(correo, basestring):
            self.__correoNotificacion = correo
            self.p.actualizarPreferencia(id_preferencia=self.CORREO_NOTIFICACION, valor=correo)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setTipoAlarma(self, tipoAlarma):
        if isinstance(tipoAlarma, IntType):
            self.__tipoAlarma = tipoAlarma
            self.p.actualizarPreferencia(id_preferencia=10601, valor=tipoAlarma)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setLlave(self, llave):
        if isinstance(llave, IntType):
            self.__llave = llave
            self.p.actualizarPreferencia(id_preferencia=998, valor=llave)
            
        else:
            raise TypeError('Tipo de dato no admitido')
    def setVersion(self, version):
        if isinstance(version, IntType):
            self.__version = version
            self.p.actualizarPreferencia(id_preferencia=999, valor=version)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setUltimaSinc(self, ultimaSinc):
        if isinstance(ultimaSinc, IntType):
            self.__ultimaSinc = ultimaSinc
            self.p.actualizarPreferencia(id_preferencia=997, valor=ultimaSinc)
        else:
            raise TypeError('Tipo de dato no admitido')                   
                             
    def borrarPreferencia(self, id_preferencia):
        p = Persistence()
        #consultar Preferencias:  correo 
        if id_preferencia == 10402:
            self.__correo = ''
            p.borrarPreferencia(id_preferencia=10402)
        elif id_preferencia == self.CORREO_NOTIFICACION:
            self.__correoNotificacion = ''
            p.borrarPreferencia(self.CORREO_NOTIFICACION)               
        #consultar Preferencias: Cantidad Eventos Proximos 
        elif id_preferencia == 10501:
            self.__cantidadEventos = 10
            p.borrarPreferencia(id_preferencia=10501) 
        #consultar Preferencias: Tipo Alarma 0 ninguni, 1 correo y alerta, 2 solo correo, 3 solo alerta
        elif id_preferencia == 10601:
            self.__tipoAlarma = 0
            p.borrarPreferencia(id_preferencia=10601)     
        #consultar Preferencias: llave 
        elif id_preferencia == 998:
            self.__llave = 0000
            p.borrarPreferencia(id_preferencia=998) 
        #consultar Preferencias: Version 
        elif id_preferencia == 999:
            self.__version = 1
            p.borrarPreferencia(id_preferencia=999) 
        #consultar Preferencias: Ultima sincronizacion 
        elif id_preferencia == 997:
            self.__ultimaSinc = 0000
            p.borrarPreferencia(id_preferencia=997) 
            
    def borrarPreferencias(self):
            p = Persistence()
            p.borrarPreferencias()
            self.__correo = ''
            self.__correoNotificacion = ''
            self.__cantidadEventos = 10
            self.__tipoAlarma = 1
            self.__llave = 0
            self.__version = 1
            self.__ultimaSinc = 0
            
    def actualizarPrefrencia(self, id_preferencia, valor):
            p = Persistence()
            #consultar Preferencias:  correo 
            if id_preferencia == 10402:
                p.actualizarPreferencia(id_preferencia=id_preferencia, valor=valor)
                self.__correo = valor
            elif id_preferencia == self.CORREO_NOTIFICACION:
                p.actualizarPreferencia(id_preferencia=id_preferencia, valor = valor)   
                self.__correoNotificacion = valor           
            #consultar Preferencias: Cantidad Eventos Proximos 
            elif id_preferencia == 10501:
                p.actualizarPreferencia(id_preferencia=id_preferencia, valor=valor)
                self.__cantidadEventos = valor
            #consultar Preferencias: Tipo Alarma 0 ninguni, 1 correo y alerta, 2 solo correo, 3 solo alerta
            elif id_preferencia == 10601:
                p.actualizarPreferencia(id_preferencia=id_preferencia, valor=valor)
                self.__tipoAlarma = valor
            #consultar Preferencias: llave 
            elif id_preferencia == 998:
                p.actualizarPreferencia(id_preferencia=id_preferencia, valor=valor)
                self.__llave = valor
            #consultar Preferencias: Version 
            elif id_preferencia == 999:
                p.actualizarPreferencia(id_preferencia=id_preferencia, valor=valor)
                self.__version = valor
            #consultar Preferencias: Ultima sincronizacion 
            elif id_preferencia == 997:
                p.actualizarPreferencia(id_preferencia=id_preferencia, valor=valor)
                self.__ultimaSinc = 0
