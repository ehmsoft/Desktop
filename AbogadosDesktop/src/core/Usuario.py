'''
Created on 26/10/2011

@author: elfotografo007
'''
from types import IntType, NoneType

class Usuario(object):
    '''
    Clase Usuario
    '''


    def __init__(self, nombre, permisos, telefono=None, direccion=None, correo=None, id_usuario=None):
        '''
        Constructor
        '''
        if isinstance(nombre, basestring):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')  
        
        if isinstance(permisos, IntType):
            self.__permisos = permisos
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
        
        if isinstance(id_usuario, basestring) or isinstance(id_usuario, NoneType):
            self.__id_usuario = id_usuario
        else:
            raise TypeError('Tipo de dato no admitido')   
      
    #Getters
    def getNombre(self):
        return self.__nombre
    def getPermisos(self):
        return self.__permisos
    def getTelefono(self):
        return self.__telefono
    def getDireccion(self):
        return self.__direccion
    def getCorreo(self):
        return self.__correo
    def getId_Usuario(self):
        return self.__id_usuario
    #Setters
    def setNombre(self, nombre):
        if isinstance(nombre, basestring) or isinstance(nombre, NoneType):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
    
    def setPermisos(self, permisos):
        if isinstance(permisos, IntType):
            self.__permisos = permisos
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
        
    def setId_Usuario(self, id_usuario):
        if isinstance(id_usuario, basestring) or isinstance(id_usuario, NoneType):
            self.__id_usuario = id_usuario
        else:
            raise TypeError('Tipo de dato no admitido')   
