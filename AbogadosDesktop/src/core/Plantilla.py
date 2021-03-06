# -*- coding: utf-8 -*-
'''
Created on 05/08/2011

@author: elfotografo007
'''
from Categoria import Categoria
from Juzgado import Juzgado
from Persona import Persona
from CampoPersonalizado import CampoPersonalizado
from types import IntType, NoneType, ListType

class Plantilla(object):
    '''
    Clase Plantilla
    '''


    def __init__(self, nombre, demandante, demandado, juzgado, radicado, 
                radicadoUnico, estado, categoria, tipo, notas, campos, prioridad, id_plantilla = None):
        if isinstance(nombre, basestring):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(demandante, Persona) or isinstance(demandante, NoneType):
            self.__demandante = demandante
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(demandado, Persona) or isinstance(demandado, NoneType):
            self.__demandado = demandado
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(juzgado, Juzgado) or isinstance(juzgado, NoneType):
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
        
        if isinstance(id_plantilla, basestring) or isinstance(id_plantilla, NoneType):
            self.__id_plantilla = id_plantilla
        else:
            raise TypeError('Tipo de dato no admitido')
     
    def addCampo(self, campo):
        if isinstance(campo, CampoPersonalizado):
            self.__campos.append(campo)
        else:
            raise TypeError('Tipo de dato no admitido')
        
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
        if isinstance(nombre, basestring):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
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
        
    def setId_plantilla(self, id_plantilla):
        if isinstance(id_plantilla, basestring) or isinstance(id_plantilla, NoneType):
            self.__id_plantilla = id_plantilla
        else:
            raise TypeError('Tipo de dato no admitido')    
    def __str__(self):
        return self.getNombre()
    
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Plantilla):
            if self.__demandado != other.getDemandado():
                return False
            if self.__demandante != other.getDemandante():
                return False
            if self.__juzgado != other.getJuzgado():
                return False
            if self.__nombre != other.getNombre():
                return False
            if self.__radicado != other.getRadicado():
                return False
            if self.__radicadoUnico != other.getRadicadoUnico():
                return False
            if self.__tipo != other.getTipo():
                return False
            if self.__estado != other.getEstado():
                return False
            if self.__categoria != other.getCategoria():
                return False
            if self.__notas != other.getNotas():
                return False
            if self.__prioridad != other.getPrioridad():
                return False
            if len(self.__campos) != len(other.getCampos()):
                return False
            else:
                camposOther = other.getCampos()
                campos = self.__campos
                for i in range(len(campos)):
                    if campos[i] != camposOther[i]:
                        return False
            return True         
        else:
            return False
        
    def __ne__(self, other):
        if other is None:
            return True
        if isinstance(other, Plantilla):
            if self.__demandado != other.getDemandado():
                return True
            if self.__demandante != other.getDemandante():
                return True
            if self.__juzgado != other.getJuzgado():
                return True
            if self.__nombre != other.getNombre():
                return True
            if self.__radicado != other.getRadicado():
                return True
            if self.__radicadoUnico != other.getRadicadoUnico():
                return True
            if self.__tipo != other.getTipo():
                return True
            if self.__estado != other.getEstado():
                return True
            if self.__categoria != other.getCategoria():
                return True
            if self.__notas != other.getNotas():
                return True
            if self.__prioridad != other.getPrioridad():
                return True
            if len(self.__campos) != len(other.getCampos()):
                return True
            else:
                camposOther = other.getCampos()
                campos = self.__campos
                for i in range(len(campos)):
                    if campos[i] != camposOther[i]:
                        return True
            return False         
        else:
            return True
        
    @classmethod    
    def getHeaders(self):
        #Devuelve una lista de strings con los encabezados del CSV
        return [u'nombre',u'radicado',u'cliente',u'contraparte',u'juzgado',u'radicadoUnico',u'estado',u'categoria',u'tipo',u'notas',u'prioridad',u'campos']
    
    def toCSV(self):
        #Devuelve una lista con los valores de los atributos para CSV
        listaReturn = [self.__nombre.encode('utf-8'),self.__radicado.encode('utf-8'), self.__demandante.getNombre().encode('utf-8'), self.__demandado.getNombre().encode('utf-8'), self.__juzgado.getNombre().encode('utf-8'), self.__radicadoUnico.encode('utf-8'), self.__estado.encode('utf-8'), self.__categoria.getDescripcion().encode('utf-8'), self.__tipo.encode('utf-8'),self.__notas.encode('utf-8')]
        for campo in self.__campos:
            listaReturn.append([u'{0}:{1}'.format(campo.getNombre(), campo.getValor())])
        return listaReturn