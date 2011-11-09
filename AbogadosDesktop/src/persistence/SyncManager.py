'''
Created on 08/11/2011

@author: elfotografo007
'''
from ConnectionManager import ConnectionManager
import sqlite3
from datetime import datetime

class SyncManager(object):
    '''
    Clase SyncManager
    '''
    

    def __init__(self):
        self.__conMgr = ConnectionManager()
        
    def sincronizar(self, archivo_movil):
        try:
            self.__conMgr.prepararBD()
            connLocal = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            connLocal.row_factory = sqlite3.Row
            connMovil = sqlite3.connect(archivo_movil, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            connMovil.row_factory = sqlite3.Row
            cLocal = connLocal.cursor()
            cMovil = connMovil.cursor()
            #Eliminar lo que sea +ne
            cMovil.execute('''DELETE FROM demandantes WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM demandados WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM juzgados WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM categorias WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM actuaciones WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM atributos WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM procesos WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM plantillas WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM atributos_proceso WHERE nuevo = 1 AND eliminado = 1''')
            cMovil.execute('''DELETE FROM atributos_plantilla WHERE nuevo = 1 AND eliminado = 1''')
            #Agregar +n y -me
            #Seccion demandantes
            cMovil.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_demandante = str(row['id_demandante'])
                cedula = str(row['cedula'])
                nombre = str(row['nombre'])
                telefono = str(row['telefono'])
                direccion = str(row['direccion'])
                correo = str(row['correo'])
                notas = str(row['notas'])
                cLocal.execute('''INSERT INTO demandantes(cedula, nombre, telefono, direccion, correo, notas) VALUES(?,?,?,?,?,?)''', (cedula, nombre, telefono, direccion, correo, notas,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_demandante = ? WHERE id_demandante = ? ''', (id, id_demandante,))
                cMovil.execute('''UPDATE plantillas SET id_demandante = ? WHERE id_demandante = ? ''', (id, id_demandante,))
            #Seccion demandados
            
            cMovil.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_demandado = str(row['id_demandado'])
                cedula = str(row['cedula'])
                nombre = str(row['nombre'])
                telefono = str(row['telefono'])
                direccion = str(row['direccion'])
                correo = str(row['correo'])
                notas = str(row['notas'])
                cLocal.execute('''INSERT INTO demandados(cedula, nombre, telefono, direccion, correo, notas) VALUES(?,?,?,?,?,?)''', (cedula, nombre, telefono, direccion, correo, notas,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_demandado = ? WHERE id_demandado = ? ''', (id, id_demandado,))
                cMovil.execute('''UPDATE plantillas SET id_demandado = ? WHERE id_demandado = ? ''', (id, id_demandado,))            
            
            #Seccion Juzgados
            cMovil.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_juzgado = str(row['id_juzgado'])
                nombre = str(row['nombre'])
                ciudad = str(row['ciudad'])
                telefono = str(row['telefono'])
                direccion = str(row['direccion']) 
                tipo = str(row['tipo'])
                cLocal.execute('''INSERT INTO juzgados(nombre, ciudad, telefono, direccion, tipo) VALUES(?,?,?,?,?)''', (nombre, ciudad, telefono, direccion, tipo,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_juzgado = ? WHERE id_juzgado = ? ''', (id, id_juzgado,))
                cMovil.execute('''UPDATE plantillas SET id_juzgado = ? WHERE id_juzgado = ? ''', (id, id_juzgado,))
                cMovil.execute('''UPDATE actuaciones SET id_juzgado = ? WHERE id_juzgado = ? ''', (id, id_juzgado,))
            
            #Seccion categorias
            cMovil.execute('''SELECT id_categoria, descripcion WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_categoria = str(row['id_categoria'])
                descripcion = str(row['descripcion'])
                cLocal.execute('''INSERT INTO categorias(descripcion) VALUES(?)''', (descripcion,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_categoria = ? WHERE id_categoria = ? ''', (id, id_categoria,))
                cMovil.execute('''UPDATE plantillas SET id_categoria = ? WHERE id_categoria = ? ''', (id, id_categoria,))
            
                
            connMovil.commit()
            connLocal.commit()            
        except Exception as e:
            raise e
        finally:
            connLocal.close()
            connMovil.close()
       
        
        