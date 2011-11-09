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
            cMovil.execute('''SELECT id_categoria, descripcion FROM categorias WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_categoria = str(row['id_categoria'])
                descripcion = str(row['descripcion'])
                cLocal.execute('''INSERT INTO categorias(descripcion) VALUES(?)''', (descripcion,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_categoria = ? WHERE id_categoria = ? ''', (id, id_categoria,))
                cMovil.execute('''UPDATE plantillas SET id_categoria = ? WHERE id_categoria = ? ''', (id, id_categoria,))
            
            #Seccion Atributos
            cMovil.execute('''SELECT id_atributo, nombre, obligatorio, longitud_max, longitud_min FROM atributos WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_atributo = str(row['id_atributo'])
                nombre = str(row['nombre'])
                obligatorio = str(row['obligatorio'])
                longitud_max = str(row['longitud_max'])
                longitud_min = str(row['longitud_min'])
                cLocal.execute('''INSERT INTO atributos(nombre, obligatorio, longitud_max, longitud_min) VALUES(?,?,?,?)''', (nombre, obligatorio, longitud_max, longitud_min,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_proceso SET id_atributo = ? WHERE id_atributo = ? ''', (id, id_atributo,))
                cMovil.execute('''UPDATE atributos_plantilla SET id_atributo = ? WHERE id_atributo = ? ''', (id, id_atributo,))
            
            #Seccion Procesos
            cMovil.execute('''SELECT id_proceso, id_demandante, id_demandado, fecha_creacion as "fecha_creacion [timestamp]", radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM procesos WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_proceso = str(row['id_proceso'])
                id_demandante = str(row['id_demandante'])
                id_demandado = str(row['id_demandado'])
                fecha_creacion = row['fecha_creacion']
                radicado = str(row['radicado'])
                radicado_unico = str(row['radicado_unico'])
                estado = str(row['estado'])
                tipo = str(row['tipo'])
                notas = str(row['notas'])
                prioridad = int(row['prioridad'])
                id_juzgado = str(row['id_juzgado'])
                id_categoria = str(row['id_categoria'])
                cLocal.execute('''INSERT INTO procesos(id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_proceso SET id_proceso = ? WHERE id_proceso = ? ''', (id, id_proceso,))
                cMovil.execute('''UPDATE actuaciones SET id_proceso = ? WHERE id_proceso = ? ''', (id, id_proceso,))
            
            #Seccion Plantillas
            cMovil.execute('''SELECT id_plantilla, nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM plantillas WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_plantilla = str(row['id_plantilla'])
                nombre = str(row['nombre'])
                id_demandante = str(row['id_demandante'])
                id_demandado = str(row['id_demandado'])
                radicado = str(row['radicado'])
                radicado_unico = str(row['radicado_unico'])
                estado = str(row['estado'])
                tipo = str(row['tipo'])
                notas = str(row['notas'])
                prioridad = int(row['prioridad'])
                id_juzgado = str(row['id_juzgado'])
                id_categoria = str(row['id_categoria'])
                cLocal.execute('''INSERT INTO plantillas(nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_plantilla SET id_plantilla = ? WHERE id_plantilla = ? ''', (id, id_plantilla,))
            
            #Seccion Actuaciones
            cMovil.execute('''SELECT id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            for row in cMovil:
                id_proceso = str(row['id_proceso'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = str(row['descripcion'])
                uid = str(row['uid'])
                cLocal.execute('''INSERT INTO actuaciones(id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid) VALUES(?,?,?,?,?,?)''', (id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid,))

            #Seccion Atributos por Proceso
            cMovil.execute('''SELECT id_atributo, id_proceso, valor FROM atributos_proceso WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            for row in cMovil:
                id_atributo = str(row['id_atributo'])
                id_proceso = str(row['id_proceso'])
                valor = str(row['valor'])
                cLocal.execute('''INSERT INTO atributos_proceso(id_atributo, id_proceso, valor) VALUES (?,?,?)''', (id_atributo, id_proceso, valor,))
                
            #Seccion Atributos por plantilla
            cMovil.execute('''SELECT id_atributo, id_plantilla, valor FROM atributos_plantilla WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            for row in cMovil:
                id_atributo = str(row['id_atributo'])
                id_plantilla = str(row['id_plantilla'])
                valor = str(row['valor'])
                cLocal.execute('''INSERT INTO atributos_plantilla(id_atributo, id_plantilla, valor) VALUES (?,?,?)''', (id_atributo, id_plantilla, valor,))
                            
            connMovil.commit()
            connLocal.commit()            
        except Exception as e:
            raise e
        finally:
            connLocal.close()
            connMovil.close()
       
        
        