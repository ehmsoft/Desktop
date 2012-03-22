'''
Created on 22/03/2012

@author: elfotografo007
'''
from datetime import datetime
from types import NoneType, IntType

class CitaCalendario(object):
    '''
    Clase CitaCalendario
    '''


    def __init__(self, fecha, anticipacion, id_cita=None, id_actuacion = None, uid = None):
        
        if isinstance(fecha, datetime):
            self.__fecha = fecha
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(anticipacion, IntType):
            self.__anticipacion = anticipacion
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id_cita, basestring) or isinstance(id_cita, NoneType):
            self.__id_cita = id_cita
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
    
    #Getters
    def getFecha(self):
        return self.__fecha
    def getId_actuacion(self):
        return self.__id_actuacion
    def getUid(self):
        return self.__uid
    def getId_cita(self):
        return self.__id_cita
    def getAnticipacion(self):
        return self.__anticipacion
    #Setters      
    def setFecha(self, fecha):
        if isinstance(fecha, datetime):
            self.__fecha = fecha
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId_actuacion(self, id_actuacion):
        if isinstance(id_actuacion, basestring) or isinstance(id_actuacion, NoneType):
            self.__id_actuacion = id_actuacion
        else:
            raise TypeError('Tipo de dato no admitido')
    
    def setId_cita(self, id_cita):
        if isinstance(id_cita, basestring) or isinstance(id_cita, NoneType):
            self.__id_cita = id_cita
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setUid(self, uid):
        if isinstance(uid, basestring) or isinstance(uid, NoneType):
            self.__uid = uid
        else:
            raise TypeError('Tipo de dato no admitido')
    
    def setAnticipacion(self, anticipacion):
        if isinstance(anticipacion, IntType):
            self.__anticipacion = anticipacion
        else:
            raise TypeError('Tipo de dato no admitido')
    
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, CitaCalendario):
            if self.__fecha != other.getFecha():
                return False
            if self.__anticipacion != other.getAnticipacion():
                return False
            if self.__id_actuacion != other.getId_actuacion():
                return False
            if self.__id_cita != other.getId_cita():
                return False
            if self.__uid != other.getUid():
                return False
            return True
        else:
            return False

    def __ne__(self, other):
        if other is None:
            return True
        if isinstance(other, CitaCalendario):
            if self.__fecha != other.getFecha():
                return True
            if self.__anticipacion != other.getAnticipacion():
                return True
            if self.__id_actuacion != other.getId_actuacion():
                return True
            if self.__id_cita != other.getId_cita():
                return True
            if self.__uid != other.getUid():
                return True
            return False
        else:
            return True