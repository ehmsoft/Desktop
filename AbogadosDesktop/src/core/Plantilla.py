'''
Created on 05/08/2011

@author: elfotografo007
'''
from Categoria import Categoria
from Actuacion import Actuacion
from Juzgado import Juzgado
from Persona import Persona
from CampoPersonalizado import CampoPersonalizado


class Plantilla(object):
    '''
    Clase Plantilla
    '''


    def __init__(self, nombre, demandante, demandado, juzgado, radicado, radicadoUnico, estado, categoria, tipo, notas, campos, prioridad, id_plantilla = None):
        self.__nombre = nombre
        self.__demandante = demandante
        self.__demandado = demandado
        self.__juzgado = juzgado
        self.__radicado = radicado
        self.__radicadoUnico = radicadoUnico
        self.__estado = estado
        self.__categoria = categoria
        self.__tipo = tipo
        self.__notas  = notas
        self.__campos = campos
        self.__prioridad = prioridad
        self.__id_plantilla = id_plantilla
     
    def addCampo(self, campo):
        self.__campos.append(campo)
    def delCampo(self, campo):
        self.__campos.remove(campo)
    #Getters
    def getNombre(self):
        return self.__nombre
    def getDemandante(self):
        return self.__demandante
    def getDemandado(self):
        return self.__demandado
    def getJuzgado(self):
        return self.__juzgado
    def getRadicado(self):
        return self.__radicado
    def getRadicadoUnico(self):
        return self.__radicadoUnico
    def getEstado(self):
        return self.__estado
    def getCategoria(self):
        return self.__categoria
    def getTipo(self):
        return self.__tipo
    def getNotas(self):
        return self.__notas
    def getCampos(self):
        return self.__campos
    def getPrioridad(self):
        return self.__prioridad
    def getId_plantilla(self):
        return self.__id_plantilla
    
    #Setters
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setDemandante(self, demandante):
        self.__demandante = demandante
    def setDemandado(self,demandado):
        self.__demandado = demandado
    def setJuzgado(self, juzgado):
        self.__juzgado = juzgado
    def setRadicado(self, radicado):
        self.__radicado = radicado
    def setRadicadoUnico(self, radicadoUnico):
        self.__radicadoUnico = radicadoUnico
    def setEstado(self, estado):
        self.__estado = estado
    def setCategoria(self, categoria):
        self.__categoria = categoria
    def setTipo(self, tipo):
        self.__tipo = tipo
    def setNotas(self, notas):
        self.__notas = notas
    def setCampos(self, campos):
        self.__campos = campos
    def setPrioridad(self, prioridad):
        self.__prioridad = prioridad
    def setId_plantilla(self, id_plantilla):
        self.__id_plantilla = id_plantilla