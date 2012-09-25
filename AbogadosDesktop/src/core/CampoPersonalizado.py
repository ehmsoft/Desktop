# -*- coding: utf-8 -*-
'''
Created on 04/08/2011

@author: elfotografo007
'''
from types import IntType, NoneType, BooleanType

class CampoPersonalizado(object):
    '''
    Clase CampoPersonalizado
    '''


    def __init__(self, nombre, valor = None, obligatorio = False, longitudMax = 0,
                longitudMin = 0, id_campo = None, id_atributo = None):
        if isinstance(nombre, basestring):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(valor, basestring) or isinstance(valor, NoneType):
            self.__valor = valor
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(obligatorio, BooleanType):
            self.__obligatorio = obligatorio
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(longitudMax, IntType):
            self.__longitudMax = longitudMax
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(longitudMin, IntType):
            self.__longitudMin = longitudMin
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id_campo, basestring) or isinstance(id_campo, NoneType):
            self.__id_campo = id_campo
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id_atributo, basestring) or isinstance(id_atributo, NoneType):
            self.__id_atributo = id_atributo
        else:
            raise TypeError('Tipo de dato no admitido')
    
    #Getters
    def getNombre(self):
        return self.__nombre
    def getValor(self):
        return self.__valor
    def isObligatorio(self):
        return self.__obligatorio
    def getLongitudMax(self):
        return self.__longitudMax
    def getLongitudMin(self):
        return self.__longitudMin
    def getId_campo(self):
        return self.__id_campo
    def getId_atributo(self):
        return self.__id_atributo
    #Setters
    def setNombre(self, nombre):
        if isinstance(nombre, basestring):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setValor(self, valor):
        if isinstance(valor, basestring) or isinstance(valor, NoneType):
            self.__valor = valor
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setObligatorio(self, obligatorio):
        if isinstance(obligatorio, BooleanType):
            self.__obligatorio = obligatorio
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setLongitudMax(self, longitudMax):
        if isinstance(longitudMax, IntType):
            self.__longitudMax = longitudMax
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setLongitudMin(self, longitudMin):
        if isinstance(longitudMin, IntType):
            self.__longitudMin = longitudMin
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId_campo(self, id_campo):
        if isinstance(id_campo, basestring) or isinstance(id_campo, NoneType):
            self.__id_campo = id_campo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId_atributo(self, id_atributo):
        if isinstance(id_atributo, basestring) or isinstance(id_atributo, NoneType):
            self.__id_atributo = id_atributo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def __str__(self):
        return self.getNombre()
    
    def __repr__(self):
        return self.getNombre()
    
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, CampoPersonalizado):
            if self.__longitudMax != other.getLongitudMax():
                return False
            if self.__longitudMin != other.getLongitudMin():
                return False
            if self.__obligatorio != other.isObligatorio():
                return False
            if self.__nombre != other.getNombre():
                return False
            if self.__valor is None:
                if other.getValor() is not None:
                    return False
            elif self.__valor != other.getValor():
                return False
            return True
        else:
            return False

    def __ne__(self, other):
        if other is None:
            return True
        if isinstance(other, CampoPersonalizado):
            if self.__longitudMax != other.getLongitudMax():
                return True
            if self.__longitudMin != other.getLongitudMin():
                return True
            if self.__obligatorio != other.isObligatorio():
                return True
            if self.__nombre != other.getNombre():
                return True
            if self.__valor is None:
                if other.getValor() is not None:
                    return True
            elif self.__valor != other.getValor():
                return True
            return False
        else:
            return True