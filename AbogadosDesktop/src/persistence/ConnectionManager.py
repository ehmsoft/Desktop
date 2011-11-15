'''
Created on 06/08/2011

@author: elfotografo007
'''
import hashlib
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
            c.execute('''CREATE TABLE 'demandantes'('id_demandante' INTEGER PRIMARY KEY,'cedula' TEXT,'nombre' TEXT,'telefono' TEXT,'direccion' TEXT,'correo' TEXT,'notas' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), UNIQUE('cedula','nombre'))''')
            #Crear tabla Demandados
            c.execute('''CREATE TABLE 'demandados'('id_demandado' INTEGER PRIMARY KEY,'cedula' TEXT,'nombre' TEXT,'telefono' TEXT,'direccion' TEXT,'correo' TEXT,'notas' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), UNIQUE('cedula','nombre'))''')
            #Crear tabla de AtributosPersona que almacena los campos Personalizados para demandantes y demandados
            c.execute('''CREATE TABLE 'atributosPersona'('id_atributo' INTEGER PRIMARY KEY,'nombre' TEXT,'obligatorio' BOOLEAN,'longitud_max' INTEGER,'longitud_min' INTEGER, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), UNIQUE('nombre','obligatorio'))''')
            #Crear tabla Atributos por demandante, para relacionar los campos personalizados con los demandantes
            c.execute('''CREATE TABLE 'atributos_demandante'('id_atributo_demandante' INTEGER PRIMARY KEY,'id_atributo' INTEGER,'id_demandante' INTEGER,'valor' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_atributo) REFERENCES atributosPersona(id_atributo),FOREIGN KEY(id_demandante) REFERENCES demandantes(id_demandante),UNIQUE('id_atributo','id_demandante','valor'))''')
            #Crear tabla Atributos por demandado, para relacionar los campos personalizados con los demandados
            c.execute('''CREATE TABLE 'atributos_demandado'('id_atributo_demandado' INTEGER PRIMARY KEY,'id_atributo' INTEGER,'id_demandado' INTEGER,'valor' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_atributo) REFERENCES atributosPersona(id_atributo),FOREIGN KEY(id_demandado) REFERENCES demandados(id_demandado),UNIQUE('id_atributo','id_demandado','valor'))''')
            #Crear tabla Juzgados
            c.execute('''CREATE TABLE 'juzgados'('id_juzgado' INTEGER PRIMARY KEY,'nombre' TEXT,'ciudad' TEXT,'telefono' TEXT,'direccion' TEXT,'tipo' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), UNIQUE('nombre','ciudad','tipo'))''')
            #Crear tabla de atributosJuzgado que almacena los campos Personalizados para los juzgados
            c.execute('''CREATE TABLE 'atributosJuzgado'('id_atributo' INTEGER PRIMARY KEY,'nombre' TEXT,'obligatorio' BOOLEAN,'longitud_max' INTEGER,'longitud_min' INTEGER, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), UNIQUE('nombre','obligatorio'))''')
            #Crear tabla Atributos por juzgado, para relacionar los campos personalizados con los juzgados
            c.execute('''CREATE TABLE 'atributos_juzgado'('id_atributo_juzgado' INTEGER PRIMARY KEY,'id_atributo' INTEGER,'id_juzgado' INTEGER,'valor' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_atributo) REFERENCES atributosJuzgado(id_atributo),FOREIGN KEY(id_juzgado) REFERENCES juzgados(id_juzgado),UNIQUE('id_atributo','id_juzgado','valor'))''')
            #Crear tabla Actuaciones
            c.execute('''CREATE TABLE 'actuaciones'('id_actuacion' INTEGER PRIMARY KEY,'id_proceso' INTEGER,'id_juzgado' INTEGER,'fecha_creacion' DATE,'fecha_proxima' DATE,'descripcion' TEXT,'uid' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_proceso) REFERENCES procesos(id_proceso),FOREIGN KEY(id_juzgado) REFERENCES juzgados(id_juzgado), UNIQUE('id_proceso','id_juzgado','fecha_creacion','fecha_proxima','descripcion'))''')
            #Crear tabla de atributosActuacion que almacena los campos Personalizados para actuaciones
            c.execute('''CREATE TABLE 'atributosActuacion'('id_atributo' INTEGER PRIMARY KEY,'nombre' TEXT,'obligatorio' BOOLEAN,'longitud_max' INTEGER,'longitud_min' INTEGER, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), UNIQUE('nombre','obligatorio'))''')
            #Crear tabla Atributos por actuacion, para relacionar los campos personalizados con los actuaciones
            c.execute('''CREATE TABLE 'atributos_actuacion'('id_atributo_actuacion' INTEGER PRIMARY KEY,'id_atributo' INTEGER,'id_actuacion' INTEGER,'valor' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_atributo) REFERENCES atributosActuacion(id_atributo),FOREIGN KEY(id_actuacion) REFERENCES actuaciones(id_actuacion),UNIQUE('id_atributo','id_actuacion','valor'))''')
            #Crear tabla Categorias
            c.execute('''CREATE TABLE 'categorias'('id_categoria' INTEGER PRIMARY KEY,'descripcion' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')))''')
            #Crear tabla Atributos
            c.execute('''CREATE TABLE 'atributos'('id_atributo' INTEGER PRIMARY KEY,'nombre' TEXT,'obligatorio' BOOLEAN,'longitud_max' INTEGER,'longitud_min' INTEGER, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), UNIQUE('nombre','obligatorio'))''')
            #Crear tabla Atributos por Proceso
            c.execute('''CREATE TABLE 'atributos_proceso'('id_atributo_proceso' INTEGER PRIMARY KEY,'id_atributo' INTEGER,'id_proceso' INTEGER,'valor' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_atributo) REFERENCES atributos(id_atributo),FOREIGN KEY(id_proceso) REFERENCES procesos(id_proceso),UNIQUE('id_atributo','id_proceso','valor'))''')
            #Crear tabla Procesos
            c.execute('''CREATE TABLE 'procesos'('id_proceso' INTEGER PRIMARY KEY,'id_demandante' INTEGER,'id_demandado' INTEGER,'fecha_creacion' DATE,'radicado' TEXT,'radicado_unico' TEXT,'estado' TEXT,'tipo' TEXT,'notas' TEXT,'prioridad' TEXT,'id_juzgado' INTEGER,'id_categoria' INTEGER, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_demandante) REFERENCES demandantes(id_demandante),FOREIGN KEY(id_demandado) REFERENCES demandados(id_demandado),FOREIGN KEY(id_juzgado) REFERENCES juzgados(id_juzgado),FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria), UNIQUE('id_demandante','id_demandado','radicado','radicado_unico','id_juzgado'))''')
            #Crear tabla Arvhivos por proceso
            c.execute('''CREATE TABLE 'archivos_proceso'('id_archivo_proceso' INTEGER PRIMARY KEY, 'id_proceso' INTEGER, 'ruta' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')))''')
            #Crear tabla Plantillas
            c.execute('''CREATE TABLE 'plantillas'('id_plantilla' INTEGER PRIMARY KEY,'nombre' TEXT,'id_demandante' INTEGER,'id_demandado' INTEGER,'radicado' TEXT,'radicado_unico' TEXT,'estado' TEXT,'tipo' TEXT,'notas' TEXT,'prioridad' TEXT,'id_juzgado' INTEGER,'id_categoria' INTEGER, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_demandante) REFERENCES demandantes(id_demandante),FOREIGN KEY(id_demandado) REFERENCES demandados(id_demandado),FOREIGN KEY(id_juzgado) REFERENCES juzgados(id_juzgado),FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria), UNIQUE('id_demandante','id_demandado','radicado','radicado_unico','id_juzgado'))''')
            #Crear tabla Atributos por Plantilla
            c.execute('''CREATE TABLE 'atributos_plantilla'('id_atributo_plantilla' INTEGER PRIMARY KEY,'id_atributo' INTEGER,'id_plantilla' INTEGER,'valor' TEXT, 'nuevo' BOOLEAN DEFAULT 1, 'modificado' BOOLEAN DEFAULT 0, 'eliminado' BOOLEAN DEFAULT 0, 'fecha_mod' DATE DEFAULT (datetime('now', 'localtime')), FOREIGN KEY(id_atributo) REFERENCES atributos(id_atributo),FOREIGN KEY(id_plantilla) REFERENCES plantillas(id_plantilla),UNIQUE('id_atributo','id_plantilla','valor'))''')
            #Crear tabla Usuarios
            c.execute('''CREATE TABLE 'usuarios'('id_usuario' INTEGER PRIMARY KEY, 'nombre_usuario' TEXT, 'permisos' INTEGER, 'password' TEXT, 'telefono' TEXT, 'direccion' TEXT, 'correo' TEXT)''')
            #Crear tabla Preferencias
            c.execute('''CREATE TABLE 'preferencias'('id_preferencia' INTEGER PRIMARY KEY,'valor' INTEGER)''')
            #Crear Categorias
            c.execute('''INSERT INTO 'categorias'(id_categoria, descripcion) VALUES(1,'Ninguna')''')
            #Insertar Valores por defecto
            c.execute('''INSERT INTO demandantes(id_demandante, cedula, nombre, telefono, direccion, correo, notas) VALUES(1, 'No id', 'vacio', 'vacio', 'vacio', 'vacio', 'vacio')''')
            c.execute('''INSERT INTO demandados(id_demandado, cedula, nombre, telefono, direccion, correo, notas) VALUES(1, 'No id', 'vacio', 'vacio', 'vacio', 'vacio', 'vacio')''')
            c.execute('''INSERT INTO juzgados(id_juzgado, nombre, ciudad, telefono, direccion, tipo) VALUES(1,'vacio','vacio', 'vacio','vacio', 'vacio')''')
            c.execute('''INSERT INTO usuarios(id_usuario, nombre_usuario, permisos, password, telefono, direccion, correo) VALUES(1, 'Administrador', 1,?, 'vacio', 'vacio', 'vacio')''', (hashlib.sha1('admin').hexdigest(),))
            #Insertar la version de la base de datos
            c.execute('''INSERT INTO 'preferencias' VALUES(999,1)''')
            conn.commit()
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def getDbLocation(self):
        return self.__DBNAME                        

