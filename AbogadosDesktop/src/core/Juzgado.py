'''
Created on 04/08/2011

@author: elfotografo007
'''
from types import NoneType

class Juzgado(object):
    '''
    Clase Juzgado
    '''


    def __init__(self, nombre = None, ciudad = None, direccion = None, 
                telefono = None, tipo = None, id_juzgado = None):
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
    
    def __str__(self):
        return self.getNombre()