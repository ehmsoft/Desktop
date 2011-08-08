'''
Created on 07/08/2011

@author: elfotografo007
'''
from ConnectionManager import ConnectionManager
import sqlite3
from datetime import datetime
from core.Persona import Persona
from core.Proceso import Proceso
from core.Actuacion import Actuacion
from core.CampoPersonalizado import CampoPersonalizado
from core.Categoria import Categoria
from core.Juzgado import Juzgado
from core.Plantilla import Plantilla

class Persistence(object):
    '''
    Clase Persistence
    '''


    def __init__(self):
        self.__conMgr = ConnectionManager()
    
    #Metodos de Guardado
    def actualizarPersona(self, persona):
        pass
    def guardarPersona(self, persona):
        pass
    def borrarPersona(self, persona):
        pass
    
    def actualizarJuzgado(self, juzgado):
        pass
    def guardarJuzgado(self, juzgado):
        pass
    def borrarJuzgado(self, juzgado):
        pass
    
    def actualizarActuacion(self, actuacion):
        pass
    def guardarActuacion(self, actuacion, id_proceso):
        pass
    def borrarActuacion(self, actuacion):
        pass
    
    def actualizarCampoPersonalizado(self, campoPersonalizado):
        pass
    def guardarCampoPersonalizado(self, campoPersonalizado, id_proceso):
        pass
    def borrarCampoPersonalizado(self, campoPersonalizado):
        pass
    
    def actualizarAtributo(self, campoPersonalizado):
        pass
    def guardarAtributo(self, campoPersonalizado):
        pass
    def borrarAtributo(self, campoPersonalizado):
        pass
    
    def actualizarProceso(self, proceso):
        pass
    def guardarProceso(self, proceso):
        pass
    def borrarProceso(self, proceso):
        pass
    
    def actualizarCategoria(self, categoria):
        pass
    def guardarCategoria(self, categoria):
        pass
    def borrarCategoria(self, categoria):
        pass
    
    def actualizarPlantilla(self, plantilla):
        pass
    def guardarPlantilla(self, plantilla):
        pass
    def borrarPlantilla(self, plantilla):
        pass
    
    def actualizarCampoPlantilla(self, campoPersonalizado):
        pass
    def guardarCampoPlantilla(self, campoPersonalizado, id_proceso):
        pass
    def borrarCampoPlantilla(self, campoPersonalizado):
        pass
    
    def actualizarPreferencia(self, id_preferencia, valor):
        pass
    def borrarPreferencia(self, id_preferencia):
        pass
    #Metodos de Cargado
    
    def consultarDemandantes(self):
        self.__conMgr.prepararBD()
        conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes order by nombre''')
        demandantes = []
        for row in c:
            id_demandante = str(row['id_demandante'])
            cedula = str(row['cedula'])
            nombre = str(row['nombre'])
            telefono = str(row['telefono'])
            direccion = str(row['direccion'])            
            correo = str(row['correo'])
            notas = str(row['notas'])
            demandante = Persona(1, cedula, nombre, telefono, direccion, correo, notas, id_demandante)
            demandantes.append(demandante)
        return demandantes
    
    def consultarDemandados(self):
        self.__conMgr.prepararBD()
        conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados order by nombre''')
        demandados = []
        for row in c:
            id_demandado = str(row['id_demandado'])
            cedula = str(row['cedula'])
            nombre = str(row['nombre'])
            telefono = str(row['telefono'])
            direccion = str(row['direccion'])            
            correo = str(row['correo'])
            notas = str(row['notas'])
            demandado = Persona(2, cedula, nombre, telefono, direccion, correo, notas, id_demandado)
            demandados.append(demandado)
        return demandados
    
    def consultarPersonas(self):
        pass
    def consultarPersona(self, id_persona, tipo):
        pass
    def consultarProcesos(self):
        pass
    def consultarProceso(self, id_proceso):
        pass
    def consultarActuaciones(self, proceso):
        pass
    def consultarActuacion(self, id_actuacion):
        pass
    def consultarActuacionesCriticas(self, cantidad):
        pass
    def consultarJuzgados(self):
        pass
    def consultarJuzgado(self, id_juzgado):
        pass
    def consultarCategoria(self, id_categoria):
        pass
    def consultarCategorias(self):
        pass
    def consultarCampos(self):
        pass
    def consultarCampo(self, id_campo):
        pass
    def consultarAtributos(self):
        pass
    def consultarPlantillas(self):
        pass
    def consultarPlantilla(self, id_plantilla):
        pass
    def consultarCamposPlantilla(self, plantilla):
        pass
    def consultarCampoPlantilla(self, id_plantilla):
        pass
    def consultarPreferencia(self, id_preferencia):
        pass