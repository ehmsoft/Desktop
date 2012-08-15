# -*- coding: utf-8 -*-
'''
Created on 22/03/2012

@author: elfotografo007
'''
from datetime import datetime
from types import NoneType, IntType, BooleanType

class CitaCalendario(object):
    '''
    Clase CitaCalendario
    '''


    def __init__(self, fecha, anticipacion , descripcion, alarma=False, id_cita=None, id_actuacion=None, uid=None, conFecha=True):
        
        if isinstance(conFecha, BooleanType):
            self.__conFecha = conFecha
        else:
            raise TypeError('Tipo de dato no admitido')
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
        
        if isinstance(descripcion, basestring):
            self.__descripcion = descripcion
        else:
            raise TypeError('Tipo de dato no admitido')    
        
        if isinstance(alarma, BooleanType):
            self.__alarma = alarma
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
    def getDescripcion(self):
        return unicode(self.__descripcion)
    def isAlarma(self):
        return self.__alarma
    
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
    def setDescripcion(self, descripcion):
        if isinstance(descripcion, basestring):
            self.__descripcion = descripcion
        else:
            raise TypeError('Tipo de dato no admitido')
    def setAlarma(self, alarma):
        if isinstance(alarma, BooleanType):
            self.__alarma = alarma
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def transAnticipacion(self, ant):
        if ant < 3600:
            if ant == 60:
                return '1 minuto'
            else:
                return '%i minutos' % (ant / 60)
        elif ant < 86400:
            if ant == 3600:
                return '1 hora'
            else:
                return '%i horas' % (ant / 3600)
        else:
            if ant == 86400:
                return u'1 día'
            else:
                return u'%i días' % (ant / 86400)
            
    def setConFecha(self, fecha):
        if isinstance(fecha, BooleanType):
            self.__conFecha = fecha
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def __str__(self):
        if self.__conFecha:
            return u'Descripción: %s\nFecha: %s\nAnticipación: %s' % (self.getDescripcion(), '{:%d/%m/%Y %I:%M %p}'.format(self.getFecha()), self.transAnticipacion(self.getAnticipacion()))
        else:
            return u'Descripción: %s\nHora: %s\nAnticipación: %s' % (self.getDescripcion(), '{:%I:%M %p}'.format(self.getFecha()), self.transAnticipacion(self.getAnticipacion()))
    
    def __repr__(self):
        if self.__conFecha:
            return u'Descripción: %s\nFecha: %s\nAnticipación: %s' % (self.getDescripcion(), '{:%d/%m/%Y %I:%M %p}'.format(self.getFecha()), self.transAnticipacion(self.getAnticipacion()))
        else:
            return u'Descripción: %s\nHora: %s\nAnticipación: %s' % (self.getDescripcion(), '{:%I:%M %p}'.format(self.getFecha()), self.transAnticipacion(self.getAnticipacion()))
    
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, CitaCalendario):
            if self.__id_actuacion != other.getId_actuacion():
                return False
            return True
        else:
            return False
        
        
    def __ne__(self, other):
        if other is None:
            return True
        if isinstance(other, CitaCalendario):
            if self.__id_actuacion != other.getId_actuacion():
                return True
            return False
        else:
            return True
    
    #>=
    def __gt__(self, other):
        if self.__fecha >= other.getFecha():
            return True
        else:
            return False
    
    #>
    def __ge__(self, other):
        if self.__fecha > other.getFecha():
            return True
        else:
            return False
    
    #<=
    def __lt__(self, other):
        if self.__fecha <= other.getFecha():
            return True
        else:
            return False
    
    #<
    def __le__(self, other):
        if self.__fecha < other.getFecha():
            return True
        else:
            return False