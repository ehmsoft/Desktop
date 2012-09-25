# -*- coding: utf-8 -*-
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


    def __init__(self, juzgado, fecha, fechaProxima, descripcion, id_actuacion=None, uid=None, campos=[]):
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
        return u'{0}\n  Creado: {1:%d/%m/%Y %I:%M %p}\n  Vence: {2:%d/%m/%Y %I:%M %p}\n  {3}'.format(self.getDescripcion(), self.getFecha(), self.getFechaProxima(), self.getJuzgado())
    
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Actuacion):
            if self.__juzgado != other.getJuzgado():
                return False
            if self.__fecha != other.getFecha():
                return False
            if self.__fechaProxima != other.getFechaProxima():
                return False
            if self.__descripcion != other.getDescripcion():
                return False
            if len(self.__campos) != len(other.getCampos()):
                return False
            else:
                camposOther = other.getCampos()
                campos = self.__campos
                for i in range(len(campos)):
                    if campos[i] != camposOther[i]:
                        return False
            return True
        else:
            return False

    def __ne__(self, other):
        if other is None:
            return True
        if isinstance(other, Actuacion):
            if self.__juzgado != other.getJuzgado():
                return True
            if self.__fecha != other.getFecha():
                return True
            if self.__fechaProxima != other.getFechaProxima():
                return True
            if self.__descripcion != other.getDescripcion():
                return True
            if len(self.__campos) != len(other.getCampos()):
                return True
            else:
                camposOther = other.getCampos()
                campos = self.__campos
                for i in range(len(campos)):
                    if campos[i] != camposOther[i]:
                        return True
            return False
        else:
            return True
        
    @classmethod
    def getHeaders(self):
        #Devuelve una lista de strings con los encabezados del CSV
        return [u'descripcion', u'fechaCreacion', u'fechaVencimiento', u'juzgado', u'campos']
    def toCSV(self):
        #Devuelve una lista con los valores de los atributos para CSV
        listaReturn = [self.__descripcion.encode('utf-8'), self.__fecha, self.__fechaProxima, self.__juzgado.getNombre().encode('utf-8') ]
        for campo in self.__campos:
            listaReturn.append([u'{0}:{1}'.format(campo.getNombre(), campo.getValor())])
        return listaReturn
