'''
Created on 04/08/2011

@author: elfotografo007
'''
from Categoria import Categoria
from Actuacion import Actuacion
from Juzgado import Juzgado
from Persona import Persona
from CampoPersonalizado import CampoPersonalizado
from types import IntType, NoneType, ListType
from datetime import datetime

class Proceso(object):
    '''
    Clase Proceso
    '''


    def __init__(self, demandante, demandado, fecha, juzgado, radicado, 
                 radicadoUnico, actuaciones, estado, categoria, tipo, notas, prioridad, campos=[], id_proceso = None):
        if isinstance(demandante, Persona):
            self.__demandante = demandante
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(demandado, Persona):
            self.__demandado = demandado
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(fecha, datetime):
            self.__fecha = fecha
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(juzgado, Juzgado):
            self.__juzgado = juzgado
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(radicado, basestring):
            self.__radicado = radicado
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(radicadoUnico, basestring):
            self.__radicadoUnico = radicadoUnico
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(actuaciones, ListType):
            self.__actuaciones = actuaciones
        else:
            raise TypeError('Tipo de dato no admitido')
           
        if isinstance(estado, basestring):
            self.__estado = estado
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(categoria, Categoria):
            self.__categoria = categoria
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(tipo, basestring):
            self.__tipo = tipo
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(notas, basestring):
            self.__notas  = notas
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(campos, ListType):
            self.__campos = campos
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(prioridad, IntType):
            self.__prioridad = prioridad
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id_proceso, basestring) or isinstance(id_proceso, NoneType):
            self.__id_proceso = id_proceso
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def addActuacion(self, actuacion):
        if isinstance(actuacion, Actuacion):
            self.__actuaciones.append(actuacion)
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def delActuacion(self, actuacion):
        self.__actuaciones.remove(actuacion)
    def addCampo(self, campo):
        if isinstance(campo, CampoPersonalizado):
            self.__campos.append(campo)
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def delCampo(self, campo):
        self.__campos.remove(campo)
        
    #Getters
    def getDemandante(self):
        return self.__demandante
    def getDemandado(self):
        return self.__demandado
    def getFecha(self):
        return self.__fecha
    def getJuzgado(self):
        return self.__juzgado
    def getRadicado(self):
        return self.__radicado
    def getRadicadoUnico(self):
        return self.__radicadoUnico
    def getActuaciones(self):
        return self.__actuaciones
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
    def getId_proceso(self):
        return self.__id_proceso
    #Setters
    def setDemandante(self, demandante):
        if isinstance(demandante, Persona):
            self.__demandante = demandante
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setDemandado(self,demandado):
        if isinstance(demandado, Persona):
            self.__demandado = demandado
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setFecha(self, fecha):
        if isinstance(fecha, datetime):
            self.__fecha = fecha
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setJuzgado(self, juzgado):
        if isinstance(juzgado, Juzgado):
            self.__juzgado = juzgado
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setRadicado(self, radicado):
        if isinstance(radicado, basestring):
            self.__radicado = radicado
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setRadicadoUnico(self, radicadoUnico):
        if isinstance(radicadoUnico, basestring):
            self.__radicadoUnico = radicadoUnico
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setActuaciones(self, actuaciones):
        if isinstance(actuaciones, ListType):
            self.__actuaciones = actuaciones
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setEstado(self, estado):
        if isinstance(estado, basestring):
            self.__estado = estado
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setCategoria(self, categoria):
        if isinstance(categoria, Categoria):
            self.__categoria = categoria
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setTipo(self, tipo):
        if isinstance(tipo, basestring):
            self.__tipo = tipo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setNotas(self, notas):
        if isinstance(notas, basestring):
            self.__notas  = notas
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setCampos(self, campos):
        if isinstance(campos, ListType):
            self.__campos = campos
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setPrioridad(self, prioridad):
        if isinstance(prioridad, IntType):
            self.__prioridad = prioridad
        else:
            raise TypeError('Tipo de dato no admitido')
    def setId_proceso(self, id_proceso):
        if isinstance(id_proceso, basestring) or isinstance(id_proceso, NoneType):
            self.__id_proceso = id_proceso
        else:
            raise TypeError('Tipo de dato no admitido')