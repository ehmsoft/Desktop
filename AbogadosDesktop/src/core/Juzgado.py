# -*- coding: utf-8 -*-
'''
Created on 04/08/2011

@author: elfotografo007
'''
from types import NoneType, ListType
from CampoPersonalizado import CampoPersonalizado

class Juzgado(object):
    '''
    Clase Juzgado
    '''


    def __init__(self, nombre = None, ciudad = None, direccion = None, 
                telefono = None, tipo = None, id_juzgado = None, campos= []):
        if isinstance(nombre, basestring) or isinstance(nombre, NoneType):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(ciudad, basestring) or isinstance(ciudad, NoneType):
            self.__ciudad = ciudad
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(direccion, basestring) or isinstance(direccion, NoneType):
            self.__direccion = direccion
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(telefono, basestring) or isinstance(telefono, NoneType):
            self.__telefono = telefono
        else:
            raise TypeError('Tipo de dato no admitido')  
        
        if isinstance(tipo, basestring) or isinstance(tipo, NoneType):
            self.__tipo = tipo
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id_juzgado, basestring) or isinstance(id_juzgado, NoneType):
            self.__id_juzgado = id_juzgado
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
    def getNombre(self):
        return self.__nombre
    def getCiudad(self):
        return self.__ciudad
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getTipo(self):
        return self.__tipo
    def getId_juzgado(self):
        return self.__id_juzgado
    def getCampos(self):
        return self.__campos
    #Setters
    def setNombre(self, nombre):
        if isinstance(nombre, basestring) or isinstance(nombre, NoneType):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setCiudad(self, ciudad):
        if isinstance(ciudad, basestring) or isinstance(ciudad, NoneType):
            self.__ciudad = ciudad
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setDireccion(self, direccion):
        if isinstance(direccion, basestring) or isinstance(direccion, NoneType):
            self.__direccion = direccion
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setTelefono(self, telefono):
        if isinstance(telefono, basestring) or isinstance(telefono, NoneType):
            self.__telefono = telefono
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setTipo(self, tipo):
        if isinstance(tipo, basestring) or isinstance(tipo, NoneType):
            self.__tipo = tipo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId_juzgado(self, id_juzgado):
        if isinstance(id_juzgado, basestring) or isinstance(id_juzgado, NoneType):
            self.__id_juzgado = id_juzgado
        else:
            raise TypeError('Tipo de dato no admitido')
    def setCampos(self, campos):
        if isinstance(campos, ListType):
            self.__campos = campos
        else:
            raise TypeError('Tipo de dato no admitido')
    
    def __str__(self):
        return self.getNombre()
    
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Juzgado):
            if self.__nombre  is None:
                if other.getNombre() != None:
                    return False
            elif self.__nombre != other.getNombre():
                return False
            if self.__direccion is None:
                if other.getDireccion() != None:
                    return False
            elif self.__direccion != other.getDireccion():
                return False
            if self.__telefono is None:
                if other.getTelefono() != None:
                    return False
            elif self.__telefono != other.getTelefono():
                return False
            if self.__ciudad is None:
                if other.getCiudad() != None:
                    return False
            elif self.__ciudad != other.getCiudad():
                return False
            if self.__tipo is None:
                if other.getTipo() != None:
                    return False
            elif self.__tipo != other.getTipo():
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
        if isinstance(other, Juzgado):
            if self.__nombre  is None:
                if other.getNombre() != None:
                    return True
            elif self.__nombre != other.getNombre():
                return True
            if self.__direccion is None:
                if other.getDireccion() != None:
                    return True
            elif self.__direccion != other.getDireccion():
                return True
            if self.__telefono is None:
                if other.getTelefono() != None:
                    return True
            elif self.__telefono != other.getTelefono():
                return True
            if self.__ciudad is None:
                if other.getCiudad() != None:
                    return True
            elif self.__ciudad != other.getCiudad():
                return True
            if self.__tipo is None:
                if other.getTipo() != None:
                    return True
            elif self.__tipo != other.getTipo():
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
        return [u'nombre',u'telefono', u'direccion',u'ciudad',u'tipo',u'campos']
    
    def toCSV(self):
        #Devuelve una lista con los valores de los atributos para CSV
        listaReturn = [self.__nombre.encode('utf-8'),self.__telefono.encode('utf-8'),self.__direccion.encode('utf-8'),self.__ciudad.encode('utf-8'), self.__tipo.encode('utf-8')]
        for campo in self.__campos:
            listaReturn.append([u'{0}:{1}'.format(campo.getNombre(), campo.getValor())])
        return listaReturn