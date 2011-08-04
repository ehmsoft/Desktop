'''
Created on 04/08/2011

@author: elfotografo007
'''
from Juzgado import Juzgado
class Actuacion(object):
    '''
    Clase Actuacion
    '''


    def __init__(self, juzgado, fecha, fechaProxima, descripcion, id_actuacion = None, uid = None):
        self.__juzgado = juzgado
        self.__fecha = fecha
        self.__fechaProxima = fechaProxima
        self.__descripcion = descripcion
        self.__id_actuacion = id_actuacion
        self.__uid = uid
    
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
    #Setters
    def setJuzgado(self, juzgado):
        self.__juzgado = juzgado
    def setFecha(self, fecha):
        self.__fecha = fecha
    def setFechaProxima(self, fechaProxima):
        self.__fechaProxima = fechaProxima
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
    def setId_actuacion(self, id_actuacion):
        self.__id_actuacion = id_actuacion
    def setUid(self, uid):
        self.__uid = uid
    def __str__(self):
        return self.getDescripcion()