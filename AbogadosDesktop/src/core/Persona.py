# -*- coding: utf-8 -*-
'''
Created on 04/08/2011

@author: elfotografo007
'''
from types import IntType, NoneType, ListType
from CampoPersonalizado import CampoPersonalizado

class Persona(object):
    '''
    Clase Persona
    Tipo 1 Demandante
    Tipo 2 Demandado
    '''


    def __init__(self, tipo, id = None, nombre = None, telefono = None,
                direccion = None, correo = None, notas = None, id_persona = None, campos=[]):
        if isinstance(tipo, IntType):
            self.__tipo = tipo
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(id, basestring) or isinstance(id, NoneType):
            self.__id = id
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(nombre, basestring) or isinstance(nombre, NoneType):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
        if isinstance(telefono, basestring) or isinstance(telefono, NoneType):
            self.__telefono = telefono
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(direccion, basestring) or isinstance(direccion, NoneType):
            self.__direccion = direccion
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(correo, basestring) or isinstance(correo, NoneType):
            self.__correo = correo
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(notas, basestring) or isinstance(notas, NoneType):
            self.__notas = notas
        else:
            raise TypeError('Tipo de dato no admitido')   
        
        if isinstance(id_persona, basestring) or isinstance(id_persona, NoneType):
            self.__id_persona = id_persona
        else:
            raise TypeError('Tipo de dato no admitido') 
        if isinstance(campos, ListType):
            self.__campos = campos
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
    def getTipo(self):
        return self.__tipo
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getDireccion(self):
        return self.__direccion
    def getCorreo(self):
        return self.__correo
    def getNotas(self):
        return self.__notas
    def getId_persona(self):
        return self.__id_persona
    def getCampos(self):
        return self.__campos
    #Setters
    def setTipo(self, tipo):
        if isinstance(tipo, IntType):
            self.__tipo = tipo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId(self, id):
        if isinstance(id, basestring) or isinstance(id, NoneType):
            self.__id = id
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setNombre(self, nombre):
        if isinstance(nombre, basestring) or isinstance(nombre, NoneType):
            self.__nombre = nombre
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setTelefono(self, telefono):
        if isinstance(telefono, basestring) or isinstance(telefono, NoneType):
            self.__telefono = telefono
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setDireccion(self, direccion):
        if isinstance(direccion, basestring) or isinstance(direccion, NoneType):
            self.__direccion = direccion
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setCorreo(self, correo):
        if isinstance(correo, basestring) or isinstance(correo, NoneType):
            self.__correo = correo
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setNotas(self, notas):
        if isinstance(notas, basestring) or isinstance(notas, NoneType):
            self.__notas = notas
        else:
            raise TypeError('Tipo de dato no admitido')
        
    def setId_persona(self, id_persona):
        if isinstance(id_persona, basestring) or isinstance(id_persona, NoneType):
            self.__id_persona = id_persona
        else:
            raise TypeError('Tipo de dato no admitido')
    def setCampos(self, campos):
        if isinstance(campos, ListType):
            self.__campos = campos
        else:
            raise TypeError('Tipo de dato no admitido')
    
    def __str__(self):
        return self.getNombre()
    
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Persona):
            if self.__tipo != other.getTipo():
                return False
            if self.__correo is None:
                if other.getCorreo() != None:
                    return False
            elif self.__correo != other.getCorreo():
                return False
            if self.__direccion is None:
                if other.getDireccion() != None:
                    return False
            elif self.__direccion != other.getDireccion():
                return False
            if self.__id is None:
                if other.getId() != None:
                    return False
            elif self.__id != other.getId():
                return False
            if self.__nombre  is None:
                if other.getNombre() != None:
                    return False
            elif self.__nombre != other.getNombre():
                return False
            if self.__notas is None:
                if other.getNotas() != None:
                    return False
            elif self.__notas != other.getNotas():
                return False
            if self.__telefono is None:
                if other.getTelefono() != None:
                    return False
            elif self.__telefono != other.getTelefono():
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
        if isinstance(other, Persona):
            if self.__tipo != other.getTipo():
                return True
            if self.__correo is None:
                if other.getCorreo() != None:
                    return True
            elif self.__correo != other.getCorreo():
                return True
            if self.__direccion is None:
                if other.getDireccion() != None:
                    return True
            elif self.__direccion != other.getDireccion():
                return True
            if self.__id is None:
                if other.getId() != None:
                    return True
            elif self.__id != other.getId():
                return True
            if self.__nombre  is None:
                if other.getNombre() != None:
                    return True
            elif self.__nombre != other.getNombre():
                return True
            if self.__notas is None:
                if other.getNotas() != None:
                    return True
            elif self.__notas != other.getNotas():
                return True
            if self.__telefono is None:
                if other.getTelefono() != None:
                    return True
            elif self.__telefono != other.getTelefono():
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
        return [u'nombre',u'telefono', u'direccion',u'correo',u'notas',u'campos']
    
    def toCSV(self):
        #Devuelve una lista con los valores de los atributos para CSV
        listaReturn = [self.__nombre.encode('utf-8'),self.__telefono.encode('utf-8'),self.__direccion.encode('utf-8'),self.__correo.encode('utf-8'), self.__notas.encode('utf-8')]
        for campo in self.__campos:
            listaReturn.append([u'{0}:{1}'.format(campo.getNombre(), campo.getValor())])
        return listaReturn
        
