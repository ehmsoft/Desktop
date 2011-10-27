'''
Created on 27/10/2011

@author: elfotografo007
'''
from types import NoneType

class Archivo(object):
    '''
    Clase Archivo
    '''


    def __init__(self, ruta, id_archivo = None, archivo=None):
        self.__archivo = archivo
        if isinstance(ruta, basestring):
            self.__ruta = ruta
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id_archivo, basestring) or isinstance(id_archivo, NoneType):
            self.__id_archivo = id_archivo
        else:
            raise TypeError('Tipo de dato no admitido')         
    
    #Getters    
    def getRuta(self):
        return self.__ruta
    def getId_archivo(self):
        return self.__id_archivo
    def getArchivo(self):
        return self.__archivo
    
    #Setters
    def setRuta(self, ruta):
        if isinstance(ruta, basestring):
            self.__ruta = ruta
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId_archivo(self, id_archivo):
        if isinstance(id_archivo, basestring) or isinstance(id_archivo, NoneType):
            self.__id_archivo = id_archivo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setArchivo(self, archivo):
        self.__archivo = archivo