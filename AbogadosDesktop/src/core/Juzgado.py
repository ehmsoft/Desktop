'''
Created on 04/08/2011

@author: elfotografo007
'''

class Juzgado(object):
    '''
    Clase Juzgado
    '''


    def __init__(self, nombre = None, ciudad = None, direccion = None, telefono = None, tipo = None, id_juzgado = None):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__telefono = telefono
        self.__tipo = tipo
        self.__id_juzgado = id_juzgado

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
        self.__nombre = nombre
    def setCiudad(self, ciudad):
        self.__ciudad = ciudad
    def setDireccion(self, direccion):
        self.__direccion = direccion
    def setTelefono(self, telefono):
        self.__telefono = telefono
    def setTipo(self, tipo):
        self.__tipo = tipo
    def setId_juzgado(self, id_juzgado):
        self.__id_juzgado = id_juzgado
    
    def __str__(self):
        return self.getNombre()