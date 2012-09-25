# -*- coding: utf-8 -*-
'''
Created on 22/03/2012

@author: elfotografo007
'''
from Juzgado import Juzgado
from datetime import datetime
from types import NoneType, ListType
from CampoPersonalizado import CampoPersonalizado
from core.Actuacion import Actuacion

class ActuacionCritica(Actuacion):
    '''
    Clase Actuacion Critica, que contiene un id_proceso para poder cargar el proceso
    '''


    def __init__(self, juzgado, fecha, fechaProxima, descripcion, id_proceso, id_actuacion = None, uid = None, campos=[]):
        super(ActuacionCritica, self).__init__(juzgado=juzgado, fecha=fecha, fechaProxima=fechaProxima, descripcion=descripcion, id_actuacion = id_actuacion, uid = uid, campos=campos)
        if isinstance(id_proceso, basestring):
            self.__id_proceso = id_proceso
        else:
            raise TypeError('Tipo de dato no admitido')
        
    #Getters
    def getId_proceso(self):
        return self.__id_proceso

    #Setters
    def setId_proceso(self, id_proceso):
        if isinstance(id_proceso, basestring) or isinstance(id_proceso, NoneType):
            self.__id_proceso = id_proceso
        else:
            raise TypeError('Tipo de dato no admitido')