'''
Created on 04/08/2011

@author: elfotografo007
'''

class Persona(object):
    '''
    Clase Persona
    '''


    def __init__(self, tipo, id = None, nombre = None, telefono = None, direccion = None, correo = None, notas = None, id_persona = None):
        self.__tipo = tipo
        self.__id = id
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = direccion
        self.__correo = correo
        self.__notas = notas
        self.__id_persona = id_persona
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
    #Setters
    def setTipo(self, tipo):
        self.__tipo = tipo
    def setId(self, id):
        self.__id = id
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setTelefono(self, telefono):
        self.__telefono = telefono
    def setDireccion(self, direccion):
        self.__direccion = direccion
    def setCorreo(self, correo):
        self.__correo = correo
    def setNotas(self, notas):
        self.__notas = notas
    def setId_persona(self, id_persona):
        self.__id_persona = id_persona
        
    def __str__(self):
        return self.getNombre()
