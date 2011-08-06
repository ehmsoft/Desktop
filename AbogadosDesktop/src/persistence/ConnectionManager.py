'''
Created on 06/08/2011

@author: elfotografo007
'''
import sqlite3
from os.path import exists

class ConnectionManager(object):
    '''
    Clase ConnectionManager
    '''

    
    def __init__(self):
        self.__DBNAME = './database.ehm'
        
    def prepararBD(self):
        if not exists(self.__DBNAME):
            self.__crearBD()
    
    def __crearBD(self):
        try:
            conn = sqlite3.connect(self.__DBNAME)
            c = conn.cursor()
            #Crear Tablas
            
            #Crear tabla Demandantes
            c.execute('''CREATE TABLE 'demandantes'('id_demandante' INTEGER PRIMARY KEY,'cedula' TEXT,'nombre' TEXT,'telefono' TEXT,'direccion' TEXT,'correo' TEXT,'notas' TEXT, UNIQUE('cedula','nombre'))''')
            #Crear tabla Demandados
            c.execute('''CREATE TABLE 'demandados'('id_demandado' INTEGER PRIMARY KEY,'cedula' TEXT,'nombre' TEXT,'telefono' TEXT,'direccion' TEXT,'correo' TEXT,'notas' TEXT, UNIQUE('cedula','nombre'))''')
            #Crear tabla Juzgados
            c.execute('''CREATE TABLE 'juzgados'('id_juzgado' INTEGER PRIMARY KEY,'nombre' TEXT,'ciudad' TEXT,'telefono' TEXT,'direccion' TEXT,'tipo' TEXT, UNIQUE('nombre','ciudad','tipo'))''')
            #Crear tabla Actuaciones
            c.execute('''CREATE TABLE 'actuaciones'('id_actuacion' INTEGER PRIMARY KEY,'id_proceso' INTEGER,'id_juzgado' INTEGER,'fecha_creacion' DATE,'fecha_proxima' DATE,'descripcion' TEXT,'uid' TEXT,FOREIGN KEY(id_proceso) REFERENCES procesos(id_proceso),FOREIGN KEY(id_juzgado) REFERENCES juzgados(id_juzgado), UNIQUE('id_proceso','id_juzgado','fecha_creacion','fecha_proxima','descripcion'))''')
            #Crear tabla Categorias
            c.execute('''CREATE TABLE 'categorias'('id_categoria' INTEGER PRIMARY KEY,'descripcion' TEXT)''')
            #Crear tabla Atributos
            c.execute('''CREATE TABLE 'atributos'('id_atributo' INTEGER PRIMARY KEY,'nombre' TEXT,'obligatorio' BOOLEAN,'longitud_max' INTEGER,'longitud_min' INTEGER, UNIQUE('nombre','obligatorio'))''')
            #Crear tabla Atritutos por Proceso
            c.execute('''CREATE TABLE 'atributos_proceso'('id_atributo_proceso' INTEGER PRIMARY KEY,'id_atributo' INTEGER,'id_proceso' INTEGER,'valor' TEXT,FOREIGN KEY(id_atributo) REFERENCES atributos(id_atributo),FOREIGN KEY(id_proceso) REFERENCES procesos(id_proceso),UNIQUE('id_atributo','id_proceso','valor'))''')
            #Crear tabla Procesos
            c.execute('''CREATE TABLE 'procesos'('id_proceso' INTEGER PRIMARY KEY,'id_demandante' INTEGER,'id_demandado' INTEGER,'fecha_creacion' DATE,'radicado' TEXT,'radicado_unico' TEXT,'estado' TEXT,'tipo' TEXT,'notas' TEXT,'prioridad' TEXT,'id_juzgado' INTEGER,'id_categoria' INTEGER,FOREIGN KEY(id_demandante) REFERENCES demandantes(id_demandante),FOREIGN KEY(id_demandado) REFERENCES demandados(id_demandado),FOREIGN KEY(id_juzgado) REFERENCES juzgados(id_juzgado),FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria), UNIQUE('id_demandante','id_demandado','radicado','radicado_unico','id_juzgado'))''')
            #Crear tabla Filtros 
            c.execute('''CREATE TABLE 'filtros'('id_filtro' INTEGER PRIMARY KEY,'nombre' TEXT,'sentencia' TEXT)''')
            #Crear tabla Plantillas
            c.execute('''CREATE TABLE 'plantillas'('id_plantilla' INTEGER PRIMARY KEY,'nombre' TEXT,'id_demandante' INTEGER,'id_demandado' INTEGER,'radicado' TEXT,'radicado_unico' TEXT,'estado' TEXT,'tipo' TEXT,'notas' TEXT,'prioridad' TEXT,'id_juzgado' INTEGER,'id_categoria' INTEGER,FOREIGN KEY(id_demandante) REFERENCES demandantes(id_demandante),FOREIGN KEY(id_demandado) REFERENCES demandados(id_demandado),FOREIGN KEY(id_juzgado) REFERENCES juzgados(id_juzgado),FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria), UNIQUE('id_demandante','id_demandado','radicado','radicado_unico','id_juzgado'))''')
            #Crear tabla Atributos por Plantilla
            c.execute('''CREATE TABLE 'atributos_plantilla'('id_atributo_plantilla' INTEGER PRIMARY KEY,'id_atributo' INTEGER,'id_plantilla' INTEGER,'valor' TEXT,FOREIGN KEY(id_atributo) REFERENCES atributos(id_atributo),FOREIGN KEY(id_plantilla) REFERENCES plantillas(id_plantilla),UNIQUE('id_atributo','id_plantilla','valor'))''')
            #Crear tabla Preferencias
            c.execute('''CREATE TABLE 'preferencias'('id_preferencia' INTEGER PRIMARY KEY,'valor' INTEGER)''')
            #Crear Categorias
            c.execute('''INSERT INTO 'categorias' VALUES(1,'Ninguna')''')
            #Insertar Valores por defecto
            c.execute('''INSERT INTO demandantes VALUES(1, 'No id', 'vacio', 'vacio', 'vacio', 'vacio', 'vacio')''')
            c.execute('''INSERT INTO demandados VALUES(1, 'No id', 'vacio', 'vacio', 'vacio', 'vacio', 'vacio')''')
            c.execute('''INSERT INTO juzgados VALUES(1,'vacio','vacio', 'vacio','vacio', 'vacio')''')
            #Insertar la version de la base de datos
            c.execute('''INSERT INTO 'preferencias' VALUES(999,2)''')
            conn.commit()
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def getDbLocation(self):
        return self.__DBNAME                        
