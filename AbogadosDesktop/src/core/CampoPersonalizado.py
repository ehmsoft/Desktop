'''
Created on 04/08/2011

@author: elfotografo007
'''

class CampoPersonalizado(object):
    '''
    Clase CampoPersonalizado
    '''


    def __init__(self, nombre, valor, obligatorio, longitudMax, longitudMin, id_campo = None, id_atributo = None):
        self.__nombre = nombre
        self.__valor = valor
        self.__obligatorio = obligatorio
        self.__longitudMax = longitudMax
        self.__longitudMin = longitudMin
        self.__id_campo = id_campo
        self.__id_atributo = id_atributo
    
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
        self.__nombre = nombre
    def setValor(self, valor):
        self.__valor = valor
    def setObligatorio(self, obligatorio):
        self.__obligatorio = obligatorio
    def setLongitudMax(self, longitudMax):
        self.__longitudMax = longitudMax
    def setLongitudMin(self, longitudMin):
        self.__longitudMin = longitudMin
    def setId_campo(self, id_campo):
        self.__id_campo = id_campo
    def setId_atributo(self, id_atributo):
        self.__id_atributo = id_atributo
