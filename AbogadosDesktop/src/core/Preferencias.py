# -*- coding: utf-8 -*-
'''
Created on 29/03/2012

@author: esteban
'''
from types import  ListType
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
    
    def __init__(self):
        self.p = Persistence()
        preferencias = self.p.consultarPreferencias()
        for llaveD, valor in preferencias.iteritems():
            if llaveD == 10101:
                self.__listaMainApp = valor
            #consultar Preferencias:  correo 
            elif llaveD == 10402:
                self.__correo = valor
            #consultar Preferencias: Cantidad Eventos Proximos 
            elif llaveD == 10501:
                self.__cantidadEventos = valor
            #consultar Preferencias: Tipo Alarma 0 ninguni, 1 correo y alerta, 2 solo correo, 3 solo alerta
            elif llaveD == 10601:
                self.__tipoAlarma = valor    
            #consultar Preferencias: Cantidad Maxima Copias de Seguridad 
            elif llaveD == 10701:
                self.__cantCopiaSeg = valor
            #consultar Preferencias: llave 
            elif llaveD == 998:
                self.__llave = valor
            #consultar Preferencias: Version 
            elif llaveD == 999:
                self.__version = valor
            #consultar Preferencias: Ultima sincronizacion 
            elif llaveD == 997:
                self.__ultimaSinc = valor
    
    #Getters    
    def getId_preferencia(self):
        return self.__id_preferencia
    def getListaMainApp(self):
        return self.__listaMainApp
    def getCantidadEventos(self):
        return self.__cantidadEventos
    def getCorreo(self):
        return self.__correo
    def getTipoAlarma(self):
        return self.__tipoAlarma
    def getCantCopiaSeg(self):
        return self.__cantCopiaSeg
    def getLlave(self):
        return self.__llave
    def getVersion(self):
        return self.__version
    def getUltimaSinc(self):
        return self.__ultimaSinc
    
    #Setters
    def setListaMainApp(self, listaMainApp):
        if isinstance(listaMainApp, ListType):
            self.__listaMainApp = listaMainApp
            self.p.actualizarPreferencia(id=10101 , valor=listaMainApp)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setCantidadEventos(self, cantidadEventos):
        if isinstance(cantidadEventos, IntType):
            self.__cantidadEventos = cantidadEventos
            self.p.actualizarPreferencia(id=10501, valor=cantidadEventos)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setCorreo(self, correo):
        if isinstance(correo, basestring):
            self.__correo = correo
            self.p.actualizarPreferencia(id=10402, valor=correo)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setTipoAlarma(self, tipoAlarma):
        if isinstance(tipoAlarma, IntType):
            self.__tipoAlarma = tipoAlarma
            self.p.actualizarPreferencia(id=10601, valor=tipoAlarma)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setCantCopiaSeg(self, cantCopiaSeg):
        if isinstance(cantCopiaSeg, IntType):
            self.__cantCopiaSeg = cantCopiaSeg
            self.p.actualizarPreferencia(id=10701, valor=cantCopiaSeg)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setLlave(self, llave):
        if isinstance(llave, IntType):
            self.__llave = llave
            self.p.actualizarPreferencia(id=998, valor=llave)
            
        else:
            raise TypeError('Tipo de dato no admitido')
    def setVersion(self, version):
        if isinstance(id, IntType):
            self.__version = version
            self.p.actualizarPreferencia(id=999, valor=version)
        else:
            raise TypeError('Tipo de dato no admitido')
    def setUltimaSinc(self, ultimaSinc):
        if isinstance(ultimaSinc, IntType):
            self.__ultimaSinc = ultimaSinc
            self.p.actualizarPreferencia(id=997, valor=ultimaSinc)
        else:
            raise TypeError('Tipo de dato no admitido')                   
                             
    def borrarPreferencia(self, id_preferencia):
        p = Persistence()
        if id_preferencia == 10101:
            self.__listaMainApp = '20111,20105,20115,20114,20124,20123,20101,20107,20102,20108,20109'
            p.borrarPreferencia(id_preferencia=10101) 
        #consultar Preferencias:  correo 
        elif id_preferencia == 10402:
            self.__correo = ' '
            p.borrarPreferencia(id_preferencia=10402)               
        #consultar Preferencias: Cantidad Eventos Proximos 
        elif id_preferencia == 10501:
            self.__cantidadEventos = 10
            p.borrarPreferencia(id_preferencia=10501) 
        #consultar Preferencias: Tipo Alarma 0 ninguni, 1 correo y alerta, 2 solo correo, 3 solo alerta
        elif id_preferencia == 10601:
            self.__tipoAlarma = 1
            p.borrarPreferencia(id_preferencia=10601)     
        #consultar Preferencias: Cantidad Maxima Copias de Seguridad 
        elif id_preferencia == 10701:
            self.__cantCopiaSeg = 5
            p.borrarPreferencia(id_preferencia=10701) 
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
        self.__listaMainApp = '20111,20105,20115,20114,20124,20123,20101,20107,20102,20108,20109'
        self.__correo = ' '
        self.__cantidadEventos = 10
        self.__tipoAlarma = 1
        self.__cantCopiaSeg = 5
        self.__llave = 0000
        self.__version = 1
        self.__ultimaSinc = 0000
        
def actualizarPrefrencia(self, id_preferencia, valor):
        p = Persistence()
        if id_preferencia == 10101:
            p.actualizarPreferencia(id=id_preferencia, valor=valor)
            self.__listaMainApp = valor
        #consultar Preferencias:  correo 
        elif id_preferencia == 10402:
            p.actualizarPreferencia(id=id_preferencia, valor=valor)
            self.__correo = valor              
        #consultar Preferencias: Cantidad Eventos Proximos 
        elif id_preferencia == 10501:
            p.actualizarPreferencia(id=id_preferencia, valor=valor)
            self.__cantidadEventos = valor
        #consultar Preferencias: Tipo Alarma 0 ninguni, 1 correo y alerta, 2 solo correo, 3 solo alerta
        elif id_preferencia == 10601:
            p.actualizarPreferencia(id=id_preferencia, valor=valor)
            self.__tipoAlarma = valor
        #consultar Preferencias: Cantidad Maxima Copias de Seguridad 
        elif id_preferencia == 10701:
            p.actualizarPreferencia(id=id_preferencia, valor=valor)
            self.__cantCopiaSeg = valor
        #consultar Preferencias: llave 
        elif id_preferencia == 998:
            p.actualizarPreferencia(id=id_preferencia, valor=valor)
            self.__llave = valor
        #consultar Preferencias: Version 
        elif id_preferencia == 999:
            p.actualizarPreferencia(id=id_preferencia, valor=valor)
            self.__version = valor
        #consultar Preferencias: Ultima sincronizacion 
        elif id_preferencia == 997:
            p.actualizarPreferencia(id=id_preferencia, valor=valor)
            self.__ultimaSinc = 0000
