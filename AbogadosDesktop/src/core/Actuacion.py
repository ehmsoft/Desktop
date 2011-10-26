'''
Created on 04/08/2011

@author: elfotografo007
'''
from Juzgado import Juzgado
from datetime import datetime
from types import NoneType, ListType
from CampoPersonalizado import CampoPersonalizado

class Actuacion(object):
    '''
    Clase Actuacion
    '''


    def __init__(self, juzgado, fecha, fechaProxima, descripcion, id_actuacion = None, uid = None, campos=[]):
        if isinstance(juzgado, Juzgado):
            self.__juzgado = juzgado
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(fecha, datetime):
            self.__fecha = fecha
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(fechaProxima, datetime):
            self.__fechaProxima = fechaProxima
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(descripcion, basestring):
            self.__descripcion = descripcion
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id_actuacion, basestring) or isinstance(id_actuacion, NoneType):
            self.__id_actuacion = id_actuacion
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(uid, basestring) or isinstance(uid, NoneType):
            self.__uid = uid
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(campos, ListType):
            self.__campos = campos
        else:
            raise TypeError('Tipo de dato no admitido')
    
    
    def addCampo(self, campo):
        if isinstance(campo, CampoPersonalizado):
            self.__campos.append(campo)
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def delCampo(self, campo):
        self.__campos.remove(campo)
    
    #Getters
    def getJuzgado(self):
        return self.__juzgado
    def getFecha(self):
        return self.__fecha
    def getFechaProxima(self):
        return self.__fechaProxima
    def getDescripcion(self):
        return self.__descripcion
    def getId_actuacion(self):
        return self.__id_actuacion
    def getUid(self):
        return self.__uid
    def getCampos(self):
        return self.__campos
    #Setters
    def setJuzgado(self, juzgado):
        if isinstance(juzgado, Juzgado):
            self.__juzgado = juzgado
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setFecha(self, fecha):
        if isinstance(fecha, datetime):
            self.__fecha = fecha
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setFechaProxima(self, fechaProxima):
        if isinstance(fechaProxima, datetime):
            self.__fechaProxima = fechaProxima
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setDescripcion(self, descripcion):
        if isinstance(descripcion, basestring):
            self.__descripcion = descripcion
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId_actuacion(self, id_actuacion):
        if isinstance(id_actuacion, basestring) or isinstance(id_actuacion, NoneType):
            self.__id_actuacion = id_actuacion
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setUid(self, uid):
        if isinstance(uid, basestring) or isinstance(uid, NoneType):
            self.__uid = uid
        else:
            raise TypeError('Tipo de dato no admitido')
    def setCampos(self, campos):
        if isinstance(campos, ListType):
            self.__campos = campos
        else:
            raise TypeError('Tipo de dato no admitido')
    
    def __str__(self):
        return self.getDescripcion()
