'''
Created on 03/08/2011

@author: elfotografo007
'''

class Categoria(object):
    '''
    Clase Categoria
    '''


    def __init__(self, descripcion, id_categoria = None):
        self.__id_categoria = id_categoria
        self.__descripcion = descripcion
    def getId_categoria(self):
        return self.__id_categoria
    def getDescripcion(self):
        return self.__descripcion
    def setId_categoria(self, id_categoria):
        self.__id_categoria = id_categoria
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
    def __str__(self):
        return self.getDescripcion()
