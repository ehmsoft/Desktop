'''
Created on 03/08/2011

@author: elfotografo007
'''
from types import NoneType
class Categoria(object):
    '''
    Clase Categoria
    '''


    def __init__(self, descripcion = None, id_categoria = None):
        if isinstance(id_categoria, basestring) or isinstance(id_categoria, NoneType):
            self.__id_categoria = id_categoria
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(descripcion, basestring):
            self.__descripcion = descripcion
        else:
            raise TypeError('Tipo de dato no admitido')
    
    #Getters
    def getId_categoria(self):
        return self.__id_categoria
    def getDescripcion(self):
        return self.__descripcion
    
    #Setters
    def setId_categoria(self, id_categoria):
        if isinstance(id_categoria, basestring) or isinstance(id_categoria, NoneType):
            self.__id_categoria = id_categoria
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setDescripcion(self, descripcion):
        if isinstance(descripcion, basestring) or isinstance(descripcion, NoneType):
            self.__descripcion = descripcion
        else:
            raise TypeError('Tipo de dato no admitido')
        
        
    def __str__(self):
        return self.getDescripcion()
