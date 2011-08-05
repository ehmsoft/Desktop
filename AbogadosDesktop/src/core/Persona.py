'''
Created on 04/08/2011

@author: elfotografo007
'''
from types import IntType, NoneType

class Persona(object):
    '''
    Clase Persona
    Tipo 1 Demandante
    Tipo 2 Demandado
    '''


    def __init__(self, tipo, id = None, nombre = None, telefono = None,
                direccion = None, correo = None, notas = None, id_persona = None):
        if isinstance(tipo, IntType):
            self.__tipo = tipo
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id, basestring) or isinstance(id, NoneType):
            self.__id = id
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(nombre, basestring) or isinstance(nombre, NoneType):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(telefono, basestring) or isinstance(telefono, NoneType):
            self.__telefono = telefono
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(direccion, basestring) or isinstance(direccion, NoneType):
            self.__direccion = direccion
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(correo, basestring) or isinstance(correo, NoneType):
            self.__correo = correo
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(notas, basestring) or isinstance(notas, NoneType):
            self.__notas = notas
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(id_persona, basestring) or isinstance(id_persona, NoneType):
            self.__id_persona = id_persona
        else:
            raise TypeError('Tipo de dato no admitido')   
    #Getters
    def getTipo(self):
        return self.__tipo
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getDireccion(self):
        return self.__direccion
    def getCorreo(self):
        return self.__correo
    def getNotas(self):
        return self.__notas
    def getId_persona(self):
        return self.__id_persona
    #Setters
    def setTipo(self, tipo):
        if isinstance(tipo, IntType):
            self.__tipo = tipo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId(self, id):
        if isinstance(id, basestring) or isinstance(id, NoneType):
            self.__id = id
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setNombre(self, nombre):
        if isinstance(nombre, basestring) or isinstance(nombre, NoneType):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setTelefono(self, telefono):
        if isinstance(telefono, basestring) or isinstance(telefono, NoneType):
            self.__telefono = telefono
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setDireccion(self, direccion):
        if isinstance(direccion, basestring) or isinstance(direccion, NoneType):
            self.__direccion = direccion
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setCorreo(self, correo):
        if isinstance(correo, basestring) or isinstance(correo, NoneType):
            self.__correo = correo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setNotas(self, notas):
        if isinstance(notas, basestring) or isinstance(notas, NoneType):
            self.__notas = notas
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId_persona(self, id_persona):
        if isinstance(id_persona, basestring) or isinstance(id_persona, NoneType):
            self.__id_persona = id_persona
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def __str__(self):
        return self.getNombre()