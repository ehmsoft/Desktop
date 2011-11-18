'''
Created on 08/11/2011

@author: elfotografo007
'''
from ConnectionManager import ConnectionManager
import sqlite3

class SyncManager(object):
    '''
    Clase SyncManager
    '''
    

    def __init__(self):
        self.__conMgr = ConnectionManager()
        
    def sincronizarLocal(self, archivo_movil):
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
            
            #Agregar +n y -e
            #Seccion demandantes
            cMovil.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_demandante = row['id_demandante']
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']
                correo = row['correo']
                notas = row['notas']
                cLocal.execute('''INSERT INTO demandantes(cedula, nombre, telefono, direccion, correo, notas) VALUES(?,?,?,?,?,?)''', (cedula, nombre, telefono, direccion, correo, notas,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_demandante = ? WHERE id_demandante = ? ''', (id, id_demandante,))
                cMovil.execute('''UPDATE plantillas SET id_demandante = ? WHERE id_demandante = ? ''', (id, id_demandante,))
            
            #Seccion demandados
            cMovil.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_demandado = row['id_demandado']
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']
                correo = row['correo']
                notas = row['notas']
                cLocal.execute('''INSERT INTO demandados(cedula, nombre, telefono, direccion, correo, notas) VALUES(?,?,?,?,?,?)''', (cedula, nombre, telefono, direccion, correo, notas,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_demandado = ? WHERE id_demandado = ? ''', (id, id_demandado,))
                cMovil.execute('''UPDATE plantillas SET id_demandado = ? WHERE id_demandado = ? ''', (id, id_demandado,))            
            
            #Seccion Juzgados
            cMovil.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_juzgado = row['id_juzgado']
                nombre = row['nombre']
                ciudad = row['ciudad']
                telefono = row['telefono']
                direccion = row['direccion'] 
                tipo = row['tipo']
                cLocal.execute('''INSERT INTO juzgados(nombre, ciudad, telefono, direccion, tipo) VALUES(?,?,?,?,?)''', (nombre, ciudad, telefono, direccion, tipo,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_juzgado = ? WHERE id_juzgado = ? ''', (id, id_juzgado,))
                cMovil.execute('''UPDATE plantillas SET id_juzgado = ? WHERE id_juzgado = ? ''', (id, id_juzgado,))
                cMovil.execute('''UPDATE actuaciones SET id_juzgado = ? WHERE id_juzgado = ? ''', (id, id_juzgado,))
            
            #Seccion categorias
            cMovil.execute('''SELECT id_categoria, descripcion FROM categorias WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_categoria = row['id_categoria']
                descripcion = row['descripcion']
                cLocal.execute('''INSERT INTO categorias(descripcion) VALUES(?)''', (descripcion,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_categoria = ? WHERE id_categoria = ? ''', (id, id_categoria,))
                cMovil.execute('''UPDATE plantillas SET id_categoria = ? WHERE id_categoria = ? ''', (id, id_categoria,))
            
            #Seccion Atributos
            cMovil.execute('''SELECT id_atributo, nombre, obligatorio, longitud_max, longitud_min FROM atributos WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_atributo = row['id_atributo']
                nombre = row['nombre']
                obligatorio = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                cLocal.execute('''INSERT INTO atributos(nombre, obligatorio, longitud_max, longitud_min) VALUES(?,?,?,?)''', (nombre, obligatorio, longitud_max, longitud_min,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_proceso SET id_atributo = ? WHERE id_atributo = ? ''', (id, id_atributo,))
                cMovil.execute('''UPDATE atributos_plantilla SET id_atributo = ? WHERE id_atributo = ? ''', (id, id_atributo,))
            
            #Seccion Procesos
            cMovil.execute('''SELECT id_proceso, id_demandante, id_demandado, fecha_creacion as "fecha_creacion [timestamp]", radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM procesos WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_proceso = row['id_proceso']
                id_demandante = row['id_demandante']
                id_demandado = row['id_demandado']
                fecha_creacion = row['fecha_creacion']
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = row['prioridad']
                id_juzgado = row['id_juzgado']
                id_categoria = row['id_categoria']
                cLocal.execute('''INSERT INTO procesos(id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_proceso SET id_proceso = ? WHERE id_proceso = ? ''', (id, id_proceso,))
                cMovil.execute('''UPDATE actuaciones SET id_proceso = ? WHERE id_proceso = ? ''', (id, id_proceso,))
            
            #Seccion Plantillas
            cMovil.execute('''SELECT id_plantilla, nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM plantillas WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_plantilla = row['id_plantilla']
                nombre = row['nombre']
                id_demandante = row['id_demandante']
                id_demandado = row['id_demandado']
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = row['prioridad']
                id_juzgado = row['id_juzgado']
                id_categoria = row['id_categoria']
                cLocal.execute('''INSERT INTO plantillas(nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_plantilla SET id_plantilla = ? WHERE id_plantilla = ? ''', (id, id_plantilla,))
            
            #Seccion Actuaciones
            cMovil.execute('''SELECT id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE nuevo = 1 AND eliminado = 0''')
            for row in cMovil:
                id_proceso = row['id_proceso']
                id_juzgado = row['id_juzgado']
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = row['descripcion']
                uid = row['uid']
                cLocal.execute('''INSERT INTO actuaciones(id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid) VALUES(?,?,?,?,?,?)''', (id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid,))

            #Seccion Atributos por Proceso
            cMovil.execute('''SELECT id_atributo, id_proceso, valor FROM atributos_proceso WHERE nuevo = 1 AND eliminado = 0''')
            for row in cMovil:
                id_atributo = row['id_atributo']
                id_proceso = row['id_proceso']
                valor = row['valor']
                cLocal.execute('''INSERT INTO atributos_proceso(id_atributo, id_proceso, valor) VALUES (?,?,?)''', (id_atributo, id_proceso, valor,))
                
            #Seccion Atributos por plantilla
            cMovil.execute('''SELECT id_atributo, id_plantilla, valor FROM atributos_plantilla WHERE nuevo = 1 AND eliminado = 0''')
            for row in cMovil:
                id_atributo = row['id_atributo']
                id_plantilla = row['id_plantilla']
                valor = row['valor']
                cLocal.execute('''INSERT INTO atributos_plantilla(id_atributo, id_plantilla, valor) VALUES (?,?,?)''', (id_atributo, id_plantilla, valor,))
            
            #Bajar Flag +n -me
            cMovil.execute('''UPDATE demandantes SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')     
            cMovil.execute('''UPDATE demandados SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')   
            cMovil.execute('''UPDATE juzgados SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')   
            cMovil.execute('''UPDATE categorias SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            cMovil.execute('''UPDATE atributos SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
            cMovil.execute('''UPDATE procesos SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''') 
            cMovil.execute('''UPDATE plantillas SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')           
            cMovil.execute('''UPDATE actuaciones SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')   
            cMovil.execute('''UPDATE atributos_proceso SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')   
            cMovil.execute('''UPDATE atributos_plantilla SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')
              
            #Bajar Flag +nm -e
            cMovil.execute('''UPDATE demandantes SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')     
            cMovil.execute('''UPDATE demandados SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')   
            cMovil.execute('''UPDATE juzgados SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')   
            cMovil.execute('''UPDATE categorias SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')
            cMovil.execute('''UPDATE atributos SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')
            cMovil.execute('''UPDATE procesos SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''') 
            cMovil.execute('''UPDATE plantillas SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')           
            cMovil.execute('''UPDATE actuaciones SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')   
            cMovil.execute('''UPDATE atributos_proceso SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')   
            cMovil.execute('''UPDATE atributos_plantilla SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')
            
            #Eliminar +e
            #Demandantes
            cMovil.execute('''SELECT id_demandante FROM demandantes WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_demandante = row['id_demandante']
                cLocal.execute('''DELETE FROM demandantes WHERE id_demandante = ?''', (id_demandante,))
            cMovil.execute('''DELETE FROM demandantes WHERE eliminado = 1''')
            
            #Demandados
            cMovil.execute('''SELECT id_demandado FROM demandados WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_demandado = row['id_demandado']
                cLocal.execute('''DELETE FROM demandados WHERE id_demandado = ?''', (id_demandado,))
            cMovil.execute('''DELETE FROM demandados WHERE eliminado = 1''')
            
            #Juzgados
            cMovil.execute('''SELECT id_juzgado FROM juzgados WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_juzgado = row['id_juzgado']
                cLocal.execute('''DELETE FROM juzgados WHERE id_juzgado = ?''', (id_juzgado,))
            cMovil.execute('''DELETE FROM juzgados WHERE eliminado = 1''')
            
            #Categorias
            cMovil.execute('''SELECT id_categoria FROM categorias WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_categoria = row['id_categoria']
                cLocal.execute('''DELETE FROM categorias WHERE id_categoria = ?''', (id_categoria,))
            cMovil.execute('''DELETE FROM categorias WHERE eliminado = 1''')
            
            #Atributos
            cMovil.execute('''SELECT id_atributo FROM atributos WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_atributo = row['id_atributo']
                cLocal.execute('''DELETE FROM atributos WHERE id_atributo = ?''', (id_atributo,))
            cMovil.execute('''DELETE FROM atributos WHERE eliminado = 1''')
            
            #Procesos
            cMovil.execute('''SELECT id_proceso FROM procesos WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_proceso = row['id_proceso']
                cLocal.execute('''DELETE FROM procesos WHERE id_proceso = ?''', (id_proceso,))
            cMovil.execute('''DELETE FROM procesos WHERE eliminado = 1''')
            
            #Actuaciones
            cMovil.execute('''SELECT id_actuacion FROM actuaciones WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_actuacion = row['id_actuacion']
                cLocal.execute('''DELETE FROM actuaciones WHERE id_actuacion = ?''', (id_actuacion,))
            cMovil.execute('''DELETE FROM actuaciones WHERE eliminado = 1''')
            
            #Plantillas
            cMovil.execute('''SELECT id_plantilla FROM plantillas WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_plantilla = row['id_plantilla']
                cLocal.execute('''DELETE FROM plantillas WHERE id_plantilla = ?''', (id_plantilla,))
            cMovil.execute('''DELETE FROM plantillas WHERE eliminado = 1''')
            
            #Atributos por Proceso
            cMovil.execute('''SELECT id_atributo_proceso FROM atributos_proceso WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_atributo_proceso = row['id_atributo_proceso']
                cLocal.execute('''DELETE FROM atributos_proceso WHERE id_atributo_proceso = ?''', (id_atributo_proceso,))
            cMovil.execute('''DELETE FROM atributos_proceso WHERE eliminado = 1''')
            
            #Atributos por plantilla
            cMovil.execute('''SELECT id_atributo_plantilla FROM atributos_plantilla WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_atributo_plantilla = row['id_atributo_plantilla']
                cLocal.execute('''DELETE FROM atributos_plantilla WHERE id_atributo_plantilla = ?''', (id_atributo_plantilla,))
            cMovil.execute('''DELETE FROM atributos_plantilla WHERE eliminado = 1''')
            
            #Actualizar +m 
            #Seccion demandantes
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE modificado = 1''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                fecha_mod = row['fecha_mod']
                id_demandante = row['id_demandante']
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']
                correo = row['correo']
                notas = row['notas']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM demandantes WHERE id_demandante = ? ''', (id_demandante,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE demandantes SET cedula = ?, nombre = ?, telefono = ?, direccion = ?, correo = ?, notas = ? WHERE id_demandante = ?''', (cedula, nombre, telefono, direccion, correo, notas, id_demandante,))
                else:
                    raise Exception('registro No encontrado')
            
            #Seccion demandados
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE modificado = 1''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                fecha_mod = row['fecha_mod']
                id_demandado = row['id_demandado']
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']
                correo = row['correo']
                notas = row['notas']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM demandados WHERE id_demandado = ? ''', (id_demandado,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE demandados SET cedula = ?, nombre = ?, telefono = ?, direccion = ?, correo = ?, notas = ? WHERE id_demandado = ?''', (cedula, nombre, telefono, direccion, correo, notas, id_demandado,))
                else:
                    raise Exception('registro No encontrado')  
            
            #Seccion Juzgados
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE modificado = 1''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                fecha_mod = row['fecha_mod']
                id_juzgado = row['id_juzgado']
                nombre = row['nombre']
                ciudad = row['ciudad']
                telefono = row['telefono']
                direccion = row['direccion'] 
                tipo = row['tipo']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM juzgados WHERE id_juzgado = ? ''', (id_juzgado,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE juzgados SET nombre = ?, ciudad = ?, telefono = ?, direccion = ?, tipo = ? WHERE id_juzgado = ?''', (nombre, ciudad, telefono, direccion, tipo, id_juzgado,))
                else:
                    raise Exception('registro No encontrado')  
            
            #Seccion categorias
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_categoria, descripcion FROM categorias WHERE modificado = 1''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                fecha_mod = row['fecha_mod']
                id_categoria = row['id_categoria']
                descripcion = row['descripcion']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM categorias WHERE id_categoria = ? ''', (id_categoria,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE categorias SET descripcion = ? WHERE id_categoria = ?''', (descripcion, id_categoria,))
                else:
                    raise Exception('registro No encontrado')  
            
            #Seccion Atributos
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_atributo, nombre, obligatorio, longitud_max, longitud_min FROM atributos WHERE modificado = 1''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                fecha_mod = row['fecha_mod']
                id_atributo = row['id_atributo']
                nombre = row['nombre']
                obligatorio = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM atributos WHERE id_atributo = ? ''', (id_atributo,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE atributos SET nombre = ?, obligatorio = ?, longitud_max = ?, longitud_min = ? WHERE id_atributo = ?''', (nombre, obligatorio, longitud_max, longitud_min, id_atributo,))
                else:
                    raise Exception('registro No encontrado')
            
            #Seccion Procesos
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_proceso, id_demandante, id_demandado, fecha_creacion as "fecha_creacion [timestamp]", radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM procesos WHERE modificado = 1''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                fecha_mod = row['fecha_mod']
                id_proceso = row['id_proceso']
                id_demandante = row['id_demandante']
                id_demandado = row['id_demandado']
                fecha_creacion = row['fecha_creacion']
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = row['prioridad']
                id_juzgado = row['id_juzgado']
                id_categoria = row['id_categoria']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM procesos WHERE id_proceso = ? ''', (id_proceso,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE procesos SET id_demandante = ?, id_demandado = ?, fecha_creacion = ?, radicado = ?, radicado_unico = ?, estado = ?, tipo = ?, notas = ?, prioridad = ?, id_juzgado = ?, id_categoria = ?  WHERE id_proceso = ?''', (id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, id_proceso,))
                else:
                    raise Exception('registro No encontrado')  
            
            #Seccion Plantillas
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_plantilla, nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM plantillas WHERE modificado = 1''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                fecha_mod = row['fecha_mod']
                id_plantilla = row['id_plantilla']
                nombre = row['nombre']
                id_demandante = row['id_demandante']
                id_demandado = row['id_demandado']
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = row['prioridad']
                id_juzgado = row['id_juzgado']
                id_categoria = row['id_categoria']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM plantillas WHERE id_plantilla = ? ''', (id_plantilla,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE plantillas SET nombre = ? id_demandante = ?, id_demandado = ?, radicado = ?, radicado_unico = ?, estado = ?, tipo = ?, notas = ?, prioridad = ?, id_juzgado = ?, id_categoria = ?  WHERE id_plantilla = ?''', (nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, id_plantilla,))
                else:
                    raise Exception('registro No encontrado')

            #Seccion Actuaciones
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE modificado = 1''')
            for row in cMovil:
                fecha_mod = row['fecha_mod']
                id_actuacion = row['id_actuacion']
                id_proceso = row['id_proceso']
                id_juzgado = row['id_juzgado']
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = row['descripcion']
                uid = row['uid']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM actuaciones WHERE id_actuacion = ? ''', (id_actuacion,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE actuaciones SET id_proceso = ?, id_juzgado = ?, fecha_creacion = ?, fecha_proxima = ?, descripcion = ?, uid = ? WHERE id_actuacion = ?''', (id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid, id_actuacion,))
                else:
                    raise Exception('registro No encontrado')
                
            #Seccion Atributos por Proceso
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_atributo_proceso, id_atributo, id_proceso, valor FROM atributos_proceso WHERE modificado = 1''')
            for row in cMovil:
                fecha_mod = row['fecha_mod']
                id_atributo_proceso = row['id_atributo_proceso']
                id_atributo = row['id_atributo']
                id_proceso = row['id_proceso']
                valor = row['valor']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM atributos_proceso WHERE id_atributo_proceso = ? ''', (id_atributo_proceso,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE atributos_proceso SET id_atributo = ?, id_proceso = ?, valor = ? WHERE id_atributo_proceso = ?''', (id_atributo, id_proceso, valor, id_atributo_proceso,))
                else:
                    raise Exception('registro No encontrado')
                
            #Seccion Atributos por plantilla
            cMovil.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", id_atributo_plantilla, id_atributo, id_plantilla, valor FROM atributos_plantilla WHERE modificado = 1''')
            for row in cMovil:
                fecha_mod = row['fecha_mod']
                id_atributo_plantilla = row['id_atributo_plantilla']
                id_atributo = row['id_atributo']
                id_plantilla = row['id_plantilla']
                valor = row['valor']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM atributos_plantilla WHERE id_atributo_plantilla = ? ''', (id_atributo_plantilla,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            raise Exception('Conflicto de sincronizacion, el local es mas antiguo que el movil')
                        else:
                            raise Exception('Conflicto de sincronizacion, el movil es mas antiguo que el local')
                    else:
                        cLocal.execute('''UPDATE atributos_plantilla SET id_atributo = ?, id_plantilla = ?, valor = ? WHERE id_atributo_plantilla = ?''', (id_atributo, id_plantilla, valor, id_atributo_plantilla,))
                else:
                    raise Exception('registro No encontrado')
            #Bajar Flags +m
            cMovil.execute('''UPDATE demandantes SET modificado = 0 WHERE modificado = 1''')     
            cMovil.execute('''UPDATE demandados SET modificado = 0 WHERE modificado = 1''')   
            cMovil.execute('''UPDATE juzgados SET modificado = 0 WHERE modificado = 1''')   
            cMovil.execute('''UPDATE categorias SET modificado = 0 WHERE modificado = 1''')
            cMovil.execute('''UPDATE atributos SET modificado = 0 WHERE modificado = 1''')
            cMovil.execute('''UPDATE procesos SET modificado = 0 WHERE modificado = 1''') 
            cMovil.execute('''UPDATE plantillas SET modificado = 0 WHERE modificado = 1''')           
            cMovil.execute('''UPDATE actuaciones SET modificado = 0 WHERE modificado = 1''')   
            cMovil.execute('''UPDATE atributos_proceso SET modificado = 0 WHERE modificado = 1''')   
            cMovil.execute('''UPDATE atributos_plantilla SET modificado = 0 WHERE modificado = 1''')
            print 'sincronizacion terminada'         
        except Exception as e:
            raise e
        finally:
            connMovil.commit()
            connLocal.commit()
            connLocal.close()
            connMovil.close()
        
    def restaurarArchivo(self, archivo_movil):
        try:
            self.__conMgr.prepararBD()
            connLocal = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            connLocal.row_factory = sqlite3.Row
            connMovil = sqlite3.connect(archivo_movil, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            connMovil.row_factory = sqlite3.Row
            cLocal = connLocal.cursor()
            cMovil = connMovil.cursor()
            
            #Vaciar tablas
            cMovil.execute('''DELETE FROM demandantes WHERE id_demandante <> 1''')
            cMovil.execute('''DELETE FROM demandados WHERE id_demandados <> 1''')
            cMovil.execute('''DELETE FROM juzgados WHERE id_juzgado <> 1''')
            cMovil.execute('''DELETE FROM categorias WHERE id_categoria <> 1''')
            cMovil.execute('''DELETE FROM atributos WHERE id_atributo <> 0''')
            cMovil.execute('''DELETE FROM procesos WHERE id_proceso <> 0''')
            cMovil.execute('''DELETE FROM plantillas WHERE id_plantilla <> 0''')
            cMovil.execute('''DELETE FROM actuaciones WHERE id_actuacion <> 0''')
            cMovil.execute('''DELETE FROM atributos_proceso WHERE id_atributo_proceso <> 0''')
            cMovil.execute('''DELETE FROM atributos_plantilla WHERE id_atributo_plantilla <> 0''')
            
            #Copiar demandantes
            cLocal.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE id_demandante <> 1''')
            for row in cLocal:
                id_demandante = row['id_demandante']
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']
                correo = row['correo']
                notas = row['notas']
                cMovil.execute('''INSERT INTO demandantes(id_demandante, cedula, nombre, telefono, direccion, correo, notas, nuevo) VALUES(?,?,?,?,?,?,?,0)''', (id_demandante, cedula, nombre, telefono, direccion, correo, notas,))
            
            #Copiar demandados
            cLocal.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE id_demandado <> 1''')
            for row in cLocal:
                id_demandado = row['id_demandado']
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']
                correo = row['correo']
                notas = row['notas']
                cMovil.execute('''INSERT INTO demandados(id_demandado, cedula, nombre, telefono, direccion, correo, notas, nuevo) VALUES(?,?,?,?,?,?,?,0)''', (id_demandado, cedula, nombre, telefono, direccion, correo, notas,))
                    
            #Copiar Juzgados
            cLocal.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE id_juzgado <> 1''')
            for row in cLocal:
                id_juzgado = row['id_juzgado']
                nombre = row['nombre']
                ciudad = row['ciudad']
                telefono = row['telefono']
                direccion = row['direccion'] 
                tipo = row['tipo']
                cMovil.execute('''INSERT INTO juzgados(id_juzgado, nombre, ciudad, telefono, direccion, tipo, nuevo) VALUES(?,?,?,?,?,?,0)''', (id_juzgado, nombre, ciudad, telefono, direccion, tipo,))

            #Copiar categorias
            cLocal.execute('''SELECT id_categoria, descripcion FROM categorias WHERE id_categoria <> 1''')
            for row in cLocal:
                id_categoria = row['id_categoria']
                descripcion = row['descripcion']
                cMovil.execute('''INSERT INTO categorias(id_categoria, descripcion, nuevo) VALUES(?,?,0)''', (id_categoria, descripcion,))
                
            #Copiar atributos
            cLocal.execute('''SELECT id_atributo, nombre, obligatorio, longitud_max, longitud_min FROM atributos WHERE id_atributo <> 0''')
            for row in cLocal:
                id_atributo = row['id_atributo']
                nombre = row['nombre']
                obligatorio = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                cMovil.execute('''INSERT INTO atributos(id_atributo, nombre, obligatorio, longitud_max, longitud_min, nuevo) VALUES(?,?,?,?,?,0)''', (id_atributo, nombre, obligatorio, longitud_max, longitud_min,))
            
            #Copiar procesos
            cLocal.execute('''SELECT id_proceso, id_demandante, id_demandado, fecha_creacion as "fecha_creacion [timestamp]", radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM procesos WHERE id_proceso <> 0''')
            for row in cLocal:
                id_proceso = row['id_proceso']
                id_demandante = row['id_demandante']
                id_demandado = row['id_demandado']
                fecha_creacion = row['fecha_creacion']
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = row['prioridad']
                id_juzgado = row['id_juzgado']
                id_categoria = row['id_categoria']
                cLocal.execute('''INSERT INTO procesos(id_proceso, id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, nuevo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0)''', (id_proceso, id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                
            
            
            print 'Archivo Movil actualizado'         
        except Exception as e:
            raise e
        finally:
            connMovil.commit()
            connLocal.commit()
            connLocal.close()
            connMovil.close()