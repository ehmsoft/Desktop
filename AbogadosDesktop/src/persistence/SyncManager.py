'''
Created on 08/11/2011

@author: elfotografo007
'''
from ConnectionManager import ConnectionManager
import sqlite3
from persistence.Persistence import Persistence
from core.Persona import Persona
from gui.SyncConflict import SyncConflict
from core.Juzgado import Juzgado
from core.Categoria import Categoria
from core.CampoPersonalizado import CampoPersonalizado
from core.Proceso import Proceso
from core.Plantilla import Plantilla
from core.Actuacion import Actuacion

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
            cMovil.execute('''DELETE FROM citas WHERE nuevo = 1 AND eliminado = 1''')
            
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
                cLocal.execute('''INSERT INTO demandantes(cedula, nombre, telefono, direccion, correo, notas, nuevo) VALUES(?,?,?,?,?,?,0)''', (cedula, nombre, telefono, direccion, correo, notas,))
                _id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_demandante = ? WHERE id_demandante = ? ''', (_id, id_demandante,))
                cMovil.execute('''UPDATE plantillas SET id_demandante = ? WHERE id_demandante = ? ''', (_id, id_demandante,))
            
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
                cLocal.execute('''INSERT INTO demandados(cedula, nombre, telefono, direccion, correo, notas, nuevo) VALUES(?,?,?,?,?,?,0)''', (cedula, nombre, telefono, direccion, correo, notas,))
                _id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_demandado = ? WHERE id_demandado = ? ''', (_id, id_demandado,))
                cMovil.execute('''UPDATE plantillas SET id_demandado = ? WHERE id_demandado = ? ''', (_id, id_demandado,))            
            
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
                cLocal.execute('''INSERT INTO juzgados(nombre, ciudad, telefono, direccion, tipo, nuevo) VALUES(?,?,?,?,?,0)''', (nombre, ciudad, telefono, direccion, tipo,))
                _id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_juzgado = ? WHERE id_juzgado = ? ''', (_id, id_juzgado,))
                cMovil.execute('''UPDATE plantillas SET id_juzgado = ? WHERE id_juzgado = ? ''', (_id, id_juzgado,))
                cMovil.execute('''UPDATE actuaciones SET id_juzgado = ? WHERE id_juzgado = ? ''', (_id, id_juzgado,))
            
            #Seccion categorias
            cMovil.execute('''SELECT id_categoria, descripcion FROM categorias WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_categoria = row['id_categoria']
                descripcion = row['descripcion']
                cLocal.execute('''INSERT INTO categorias(descripcion, nuevo) VALUES(?,0)''', (descripcion,))
                _id = cLocal.lastrowid
                cMovil.execute('''UPDATE procesos SET id_categoria = ? WHERE id_categoria = ? ''', (_id, id_categoria,))
                cMovil.execute('''UPDATE plantillas SET id_categoria = ? WHERE id_categoria = ? ''', (_id, id_categoria,))
            
            #Seccion Atributos
            cMovil.execute('''SELECT id_atributo, nombre, obligatorio, longitud_max, longitud_min FROM atributos WHERE nuevo = 1 AND eliminado = 0''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                id_atributo = row['id_atributo']
                nombre = row['nombre']
                obligatorio = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                cLocal.execute('''INSERT INTO atributos(nombre, obligatorio, longitud_max, longitud_min, nuevo) VALUES(?,?,?,?,0)''', (nombre, obligatorio, longitud_max, longitud_min,))
                _id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_proceso SET id_atributo = ? WHERE id_atributo = ? ''', (_id, id_atributo,))
                cMovil.execute('''UPDATE atributos_plantilla SET id_atributo = ? WHERE id_atributo = ? ''', (_id, id_atributo,))
            
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
                cLocal.execute('''INSERT INTO procesos(id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, nuevo) VALUES (?,?,?,?,?,?,?,?,?,?,?,0)''', (id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                _id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_proceso SET id_proceso = ? WHERE id_proceso = ? ''', (_id, id_proceso,))
                cMovil.execute('''UPDATE actuaciones SET id_proceso = ? WHERE id_proceso = ? ''', (_id, id_proceso,))
            
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
                cLocal.execute('''INSERT INTO plantillas(nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, nuevo) VALUES (?,?,?,?,?,?,?,?,?,?,?,0)''', (nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                _id = cLocal.lastrowid
                cMovil.execute('''UPDATE atributos_plantilla SET id_plantilla = ? WHERE id_plantilla = ? ''', (_id, id_plantilla,))
            
            #Seccion Actuaciones
            cMovil.execute('''SELECT id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE nuevo = 1 AND eliminado = 0''')
            for row in cMovil:
                id_proceso = row['id_proceso']
                id_juzgado = row['id_juzgado']
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = row['descripcion']
                uid = row['uid']
                cLocal.execute('''INSERT INTO actuaciones(id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid, nuevo) VALUES(?,?,?,?,?,?,0)''', (id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid,))

            #Seccion Atributos por Proceso
            cMovil.execute('''SELECT id_atributo, id_proceso, valor FROM atributos_proceso WHERE nuevo = 1 AND eliminado = 0''')
            for row in cMovil:
                id_atributo = row['id_atributo']
                id_proceso = row['id_proceso']
                valor = row['valor']
                cLocal.execute('''INSERT INTO atributos_proceso(id_atributo, id_proceso, valor, nuevo) VALUES (?,?,?,0)''', (id_atributo, id_proceso, valor,))
                
            #Seccion Atributos por plantilla
            cMovil.execute('''SELECT id_atributo, id_plantilla, valor FROM atributos_plantilla WHERE nuevo = 1 AND eliminado = 0''')
            for row in cMovil:
                id_atributo = row['id_atributo']
                id_plantilla = row['id_plantilla']
                valor = row['valor']
                cLocal.execute('''INSERT INTO atributos_plantilla(id_atributo, id_plantilla, valor, nuevo) VALUES (?,?,?,0)''', (id_atributo, id_plantilla, valor,))
            
            #Seccion Citas
            cMovil.execute('''SELECT  id_cita, uid,fecha as "fecha [timestamp]", anticipacion,id_actuacion FROM citas WHERE nuevo = 1 AND eliminado = 0''')
            for row in cMovil:
                id_actuacion = str(row['id_actuacion'])
                fecha = row['fecha']
                anticipacion = row['anticipacion']
                uid = row['uid']
                cLocal.execute('''INSERT INTO citas (id_cita,uid, fecha,anticipacion,id_actuacion, nuevo) VALUES( NULL,?,?,?,?,0)''', (uid,fecha,anticipacion,id_actuacion))
                               
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
            cMovil.execute('''UPDATE citas SET nuevo = 0 WHERE nuevo = 1 AND modificado = 0 AND eliminado = 0''')  
              
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
            cMovil.execute('''UPDATE citas SET nuevo = 0, modificado = 0 WHERE nuevo = 1 AND modificado = 1 AND eliminado = 0''')
            
            #Eliminar +e
            #Demandantes
            cMovil.execute('''SELECT id_demandante FROM demandantes WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_demandante = row['id_demandante']
                cLocal.execute('''DELETE FROM demandantes WHERE id_demandante = ?''', (id_demandante,))
                cLocal.execute('''DELETE FROM atributos_demandante WHERE id_demandante = ?''', (id_demandante,))
                cLocal.execute('''UPDATE procesos SET id_demandante = 1 WHERE id_demandante = ?''', (id_demandante,))
                cLocal.execute('''UPDATE plantillas SET id_demandante = 1 WHERE id_demandante = ?''', (id_demandante,))
            cMovil.execute('''DELETE FROM demandantes WHERE eliminado = 1''')
            
            #Demandados
            cMovil.execute('''SELECT id_demandado FROM demandados WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_demandado = row['id_demandado']
                cLocal.execute('''DELETE FROM demandados WHERE id_demandado = ?''', (id_demandado,))
                cLocal.execute('''DELETE FROM atributos_demandado WHERE id_demandado = ?''', (id_demandado,))
                cLocal.execute('''UPDATE procesos SET id_demandado = 1 WHERE id_demandado = ?''', (id_demandado,))
                cLocal.execute('''UPDATE plantillas SET id_demandado = 1 WHERE id_demandado = ?''', (id_demandado,))
            cMovil.execute('''DELETE FROM demandados WHERE eliminado = 1''')
            
            #Juzgados
            cMovil.execute('''SELECT id_juzgado FROM juzgados WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_juzgado = row['id_juzgado']
                cLocal.execute('''DELETE FROM juzgados WHERE id_juzgado = ?''', (id_juzgado,))
                cLocal.execute('''DELETE FROM atributos_juzgado WHERE id_juzgado = ?''', (id_juzgado,))
                cLocal.execute('''UPDATE procesos SET id_juzgado = 1 WHERE id_juzgado = ?''', (id_juzgado,))
                cLocal.execute('''UPDATE actuaciones SET id_juzgado = 1 WHERE id_juzgado = ?''', (id_juzgado,))
                cLocal.execute('''UPDATE plantillas SET id_juzgado = 1 WHERE id_juzgado = ?''', (id_juzgado,))
            cMovil.execute('''DELETE FROM juzgados WHERE eliminado = 1''')
            
            #Categorias
            cMovil.execute('''SELECT id_categoria FROM categorias WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_categoria = row['id_categoria']
                cLocal.execute('''DELETE FROM categorias WHERE id_categoria = ?''', (id_categoria,))
                cLocal.execute('''UPDATE procesos SET id_categoria = 1 WHERE id_categoria = ?''', (id_categoria,))        
                cLocal.execute('''UPDATE plantillas SET id_categoria = 1 WHERE id_categoria = ?''', (id_categoria,))  
            cMovil.execute('''DELETE FROM categorias WHERE eliminado = 1''')
            
            #Atributos
            cMovil.execute('''SELECT id_atributo FROM atributos WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_atributo = row['id_atributo']
                cLocal.execute('''DELETE FROM atributos WHERE id_atributo = ?''', (id_atributo,))
                cLocal.execute('''UPDATE atributos_proceso SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (id_atributo,))
                cLocal.execute('''UPDATE atributos_plantilla SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (id_atributo,))
            cMovil.execute('''DELETE FROM atributos WHERE eliminado = 1''')
            
            #Procesos
            cMovil.execute('''SELECT id_proceso FROM procesos WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_proceso = row['id_proceso']
                cLocal.execute('''DELETE FROM procesos WHERE id_proceso = ?''', (id_proceso,))
                cLocal.execute('''UPDATE actuaciones SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_proceso = ?''', (id_proceso,))
                cLocal.execute('''UPDATE atributos_proceso SET eliminado = 1,fecha_mod = datetime('now','localtime') WHERE id_proceso = ?''', (id_proceso,))
            cMovil.execute('''DELETE FROM procesos WHERE eliminado = 1''')
            
            #Actuaciones
            cMovil.execute('''SELECT id_actuacion FROM actuaciones WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_actuacion = row['id_actuacion']
                cLocal.execute('''DELETE FROM actuaciones WHERE id_actuacion = ?''', (id_actuacion,))
                cLocal.execute('''DELETE FROM atributos_actuacion WHERE id_actuacion = ?''', (id_actuacion,))
            cMovil.execute('''DELETE FROM actuaciones WHERE eliminado = 1''')
            
            #Plantillas
            cMovil.execute('''SELECT id_plantilla FROM plantillas WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_plantilla = row['id_plantilla']
                cLocal.execute('''DELETE FROM plantillas WHERE id_plantilla = ?''', (id_plantilla,))
                cLocal.execute('''UPDATE atributos_plantilla SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_plantilla = ?''', (id_plantilla,))
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
            
            #Citas
            cMovil.execute('''SELECT id_cita FROM citas WHERE eliminado = 1''')
            listaMovil = cMovil.fetchall()
            for row in listaMovil:
                id_cita = row['id_cita']
                cLocal.execute('''DELETE FROM citas WHERE id_cita = ?''', (id_cita,))  
            cMovil.execute('''DELETE FROM citas WHERE eliminado = 1''')
            
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
                        demandante_local = Persistence().consultarPersona(id_demandante, 1)
                        demandante_movil = Persona(tipo=1, id=cedula, nombre=nombre, telefono=telefono, direccion=direccion, correo=correo, notas=notas, id_persona=unicode(id_demandante))
                        if not SyncConflict(local=demandante_local, movil=demandante_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                            cLocal.execute('''UPDATE demandantes SET cedula = ?, nombre = ?, telefono = ?, direccion = ?, correo = ?, notas = ? WHERE id_demandante = ?''', (cedula, nombre, telefono, direccion, correo, notas, id_demandante,))
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
                        demandado_local = Persistence().consultarPersona(id_demandado, 2)
                        demandado_movil = Persona(tipo=2, id=cedula, nombre=nombre, telefono=telefono, direccion=direccion, correo=correo, notas=notas, id_persona=unicode(id_demandado))
                        if not SyncConflict(local=demandado_local, movil=demandado_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                            cLocal.execute('''UPDATE demandados SET cedula = ?, nombre = ?, telefono = ?, direccion = ?, correo = ?, notas = ? WHERE id_demandado = ?''', (cedula, nombre, telefono, direccion, correo, notas, id_demandado,))
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
                        juzgado_local = Persistence().consultarJuzgado(id_juzgado)
                        juzgado_movil = Juzgado(nombre=nombre, ciudad=ciudad, direccion=direccion, telefono=telefono, tipo=tipo, id_juzgado=unicode(id_juzgado))
                        if not SyncConflict(local=juzgado_local, movil=juzgado_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                            cLocal.execute('''UPDATE juzgados SET nombre = ?, ciudad = ?, telefono = ?, direccion = ?, tipo = ? WHERE id_juzgado = ?''', (nombre, ciudad, telefono, direccion, tipo, id_juzgado,))
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
                        categoria_local = Persistence().consultarCategoria(id_categoria)
                        categoria_movil = Categoria(descripcion=descripcion, id_categoria=unicode(id_categoria))
                        if not SyncConflict(local=categoria_local, movil=categoria_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                            cLocal.execute('''UPDATE categorias SET descripcion = ? WHERE id_categoria = ?''', (descripcion, id_categoria,))
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
                        atributo_local = Persistence().consultarAtributo(id_atributo)
                        if obligatorio == 1:
                            ob = True
                        else:
                            ob = False
                        atributo_movil = CampoPersonalizado(nombre=nombre, obligatorio=ob, longitudMax= longitud_max, longitudMin= longitud_min, id_atributo=unicode(id_atributo))
                        if not SyncConflict(local=atributo_local, movil=atributo_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                            cLocal.execute('''UPDATE atributos SET nombre = ?, obligatorio = ?, longitud_max = ?, longitud_min = ? WHERE id_atributo = ?''', (nombre, obligatorio, longitud_max, longitud_min, id_atributo,))
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
                        p = Persistence()
                        proceso_local = p.consultarProceso(id_proceso)
                        demandante = p.consultarPersona(id_demandante, 1)
                        demandado = p.consultarPersona(id_demandado, 2)
                        juzgado = p.consultarJuzgado(id_juzgado)
                        categoria = p.consultarCategoria(id_categoria)
                        proceso_movil = Proceso(demandante=demandante, demandado=demandado, fecha=fecha_creacion, juzgado=juzgado, radicado=radicado, radicadoUnico=radicado_unico, actuaciones=[],estado=estado, categoria=categoria, tipo=tipo, notas=notas, prioridad=int(prioridad), id_proceso=unicode(id_proceso))
                        if not SyncConflict(local=proceso_local, movil=proceso_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                            cLocal.execute('''UPDATE procesos SET id_demandante = ?, id_demandado = ?, fecha_creacion = ?, radicado = ?, radicado_unico = ?, estado = ?, tipo = ?, notas = ?, prioridad = ?, id_juzgado = ?, id_categoria = ?  WHERE id_proceso = ?''', (id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, id_proceso,))
                        del p
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
                        p = Persistence()
                        plantilla_local = p.consultarPlantilla(id_plantilla)
                        demandante = p.consultarPersona(id_demandante, 1)
                        demandado = p.consultarPersona(id_demandado, 2)
                        juzgado = p.consultarJuzgado(id_juzgado)
                        categoria = p.consultarCategoria(id_categoria)
                        plantilla_movil = Plantilla(nombre=nombre,demandante=demandante, demandado=demandado, juzgado=juzgado, radicado=radicado, radicadoUnico=radicado_unico, estado=estado, categoria=categoria, tipo=tipo, notas=notas, campos = [],prioridad=int(prioridad), id_plantilla=unicode(id_plantilla))
                        if not SyncConflict(local=plantilla_local, movil=plantilla_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                            cLocal.execute('''UPDATE plantillas SET nombre = ?, id_demandante = ?, id_demandado = ?, radicado = ?, radicado_unico = ?, estado = ?, tipo = ?, notas = ?, prioridad = ?, id_juzgado = ?, id_categoria = ?  WHERE id_plantilla = ?''', (nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, id_plantilla,))
                        del p
                    else:
                        cLocal.execute('''UPDATE plantillas SET nombre = ?, id_demandante = ?, id_demandado = ?, radicado = ?, radicado_unico = ?, estado = ?, tipo = ?, notas = ?, prioridad = ?, id_juzgado = ?, id_categoria = ?  WHERE id_plantilla = ?''', (nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, id_plantilla,))
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
                        p = Persistence()
                        actuacion_local = p.consultarActuacion(id_actuacion)
                        juzgado = p.consultarJuzgado(id_juzgado)
                        actuacion_movil = Actuacion(juzgado=juzgado, fecha=fecha_creacion, fechaProxima=fecha_proxima, descripcion=descripcion, id_actuacion=unicode(id_actuacion))
                        if not SyncConflict(local=actuacion_local, movil=actuacion_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                            cLocal.execute('''UPDATE actuaciones SET id_proceso = ?, id_juzgado = ?, fecha_creacion = ?, fecha_proxima = ?, descripcion = ?, uid = ? WHERE id_actuacion = ?''', (id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid, id_actuacion,))
                        del p
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
                        p = Persistence()
                        atributo_local = p.consultarCampo(id_atributo_proceso)
                        if valor != atributo_local.getValor():
                            atributo_movil = p.consultarCampo(id_atributo_proceso)
                            atributo_movil.setValor(valor)
                            if not SyncConflict(local=atributo_local, movil=atributo_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                                cLocal.execute('''UPDATE atributos_proceso SET id_atributo = ?, id_proceso = ?, valor = ? WHERE id_atributo_proceso = ?''', (id_atributo, id_proceso, valor, id_atributo_proceso,))
                        del p
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
                        p = Persistence()
                        atributo_local = p.consultarCampoPlantilla(id_atributo_plantilla)
                        if valor != atributo_local.getValor():
                            atributo_movil = p.consultarCampoPlantilla(id_atributo_plantilla)
                            atributo_movil.setValor(valor)
                            if not SyncConflict(local=atributo_local, movil=atributo_movil, fechaLocal=fecha_modLocal, fechaMovil=fecha_mod).getSeleccionado():
                                cLocal.execute('''UPDATE atributos_plantilla SET id_atributo = ?, id_plantilla = ?, valor = ? WHERE id_atributo_plantilla = ?''', (id_atributo, id_plantilla, valor, id_atributo_plantilla,))
                        del p
                    else:
                        cLocal.execute('''UPDATE atributos_plantilla SET id_atributo = ?, id_plantilla = ?, valor = ? WHERE id_atributo_plantilla = ?''', (id_atributo, id_plantilla, valor, id_atributo_plantilla,))
                else:
                    raise Exception('registro No encontrado')
                
            #Seccion Citas
            cMovil.execute('''SELECT  fecha_mod as "fecha_mod [timestamp]",id_cita, uid,fecha as "fecha [timestamp]", anticipacion,id_actuacion FROM citas WHERE modificado = 1''')
            listaCMovil = cMovil.fetchall()
            for row in listaCMovil:
                fecha_mod = row['fecha_mod']
                id_actuacion = str(row['id_actuacion'])
                id_cita = str(row['id_cita'])
                fecha = row['fecha']
                anticipacion = row['anticipacion']
                uid = row['uid']
                cLocal.execute('''SELECT fecha_mod as "fecha_mod [timestamp]", modificado FROM citas WHERE id_cita = ? ''', (id_cita,))
                row = cLocal.fetchone()
                if row:
                    modificado = row['modificado']
                    fecha_modLocal = row['fecha_mod']
                    if modificado:
                        if fecha_mod > fecha_modLocal:
                            cLocal.execute('''UPDATE citas SET uid=?, fecha=?,anticipacion=?,id_actuacion=?,WHERE id_cita=?''', (uid,fecha,anticipacion,id_actuacion,id_cita,))
                    else:
                        cLocal.execute('''UPDATE citas SET uid=?, fecha=?,anticipacion=?,id_actuacion=?,WHERE id_cita=?''', (uid,fecha,anticipacion,id_actuacion,id_cita,))
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
            cMovil.execute('''UPDATE citas SET modificado = 0 WHERE modificado = 1''')
            connMovil.commit()
            connLocal.commit()
            print 'sincronizacion terminada'         
        except Exception as e:
            connLocal.rollback()
            connMovil.rollback()
            print "Operations rolled back"
            raise e
        finally:
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
            #Borrar eliminados en la base de datos de escritorio
            cLocal.execute('''DELETE FROM demandantes WHERE eliminado = 1''')
            cLocal.execute('''DELETE FROM demandados WHERE eliminado = 1''')
            cLocal.execute('''DELETE FROM juzgados WHERE eliminado = 1''')
            cLocal.execute('''DELETE FROM categorias WHERE eliminado = 1''')
            cLocal.execute('''DELETE FROM actuaciones WHERE eliminado = 1''')
            cLocal.execute('''DELETE FROM atributos WHERE eliminado = 1''')
            cLocal.execute('''DELETE FROM procesos WHERE eliminado = 1''')
            cLocal.execute('''DELETE FROM plantillas WHERE eliminado = 1''')
            cLocal.execute('''DELETE FROM atributos_proceso WHERE  eliminado = 1''')
            cLocal.execute('''DELETE FROM atributos_plantilla WHERE  eliminado = 1''')
            cLocal.execute('''DELETE FROM citas WHERE  eliminado = 1''')
            
            #Vaciar tablas
            cMovil.execute('''DELETE FROM demandantes WHERE id_demandante <> 1''')
            cMovil.execute('''DELETE FROM demandados WHERE id_demandado <> 1''')
            cMovil.execute('''DELETE FROM juzgados WHERE id_juzgado <> 1''')
            cMovil.execute('''DELETE FROM categorias WHERE id_categoria <> 1''')
            cMovil.execute('''DELETE FROM atributos WHERE id_atributo <> 0''')
            cMovil.execute('''DELETE FROM procesos WHERE id_proceso <> 0''')
            cMovil.execute('''DELETE FROM plantillas WHERE id_plantilla <> 0''')
            cMovil.execute('''DELETE FROM actuaciones WHERE id_actuacion <> 0''')
            cMovil.execute('''DELETE FROM atributos_proceso WHERE id_atributo_proceso <> 0''')
            cMovil.execute('''DELETE FROM atributos_plantilla WHERE id_atributo_plantilla <> 0''')
            cMovil.execute('''DELETE FROM citas WHERE id_cita <> 0''')
            
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
                cMovil.execute('''INSERT INTO procesos(id_proceso, id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, nuevo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0)''', (id_proceso, id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
            
            #Copiar plantillas
            cLocal.execute('''SELECT id_plantilla, nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM plantillas WHERE id_plantilla <> 0''')
            for row in cLocal:
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
                cMovil.execute('''INSERT INTO plantillas(id_plantilla, nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, nuevo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,0)''', (id_plantilla, nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
            
            #Copiar actuaciones
            cLocal.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE id_actuacion <> 0''')
            for row in cLocal:
                id_actuacion = row['id_actuacion']
                id_proceso = row['id_proceso']
                id_juzgado = row['id_juzgado']
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = row['descripcion']
                uid = row['uid']
                cMovil.execute('''INSERT INTO actuaciones(id_actuacion, id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid, nuevo) VALUES(?,?,?,?,?,?,?,0)''', (id_actuacion, id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid,))
                
            #Copiar atributos por proceso
            cLocal.execute('''SELECT id_atributo_proceso, id_atributo, id_proceso, valor FROM atributos_proceso WHERE id_atributo_proceso <> 0''')
            for row in cLocal:
                id_atributo_proceso = row['id_atributo_proceso']
                id_atributo = row['id_atributo']
                id_proceso = row['id_proceso']
                valor = row['valor']
                cMovil.execute('''INSERT INTO atributos_proceso(id_atributo_proceso, id_atributo, id_proceso, valor, nuevo) VALUES (?,?,?,?,0)''', (id_atributo_proceso, id_atributo, id_proceso, valor,))
            
            #Copiar atributos por plantilla
            cLocal.execute('''SELECT id_atributo_plantilla, id_atributo, id_plantilla, valor FROM atributos_plantilla WHERE id_atributo_plantilla <> 0''')
            for row in cLocal:
                id_atributo_plantilla = row['id_atributo_plantilla']
                id_atributo = row['id_atributo']
                id_plantilla = row['id_plantilla']
                valor = row['valor']
                cMovil.execute('''INSERT INTO atributos_plantilla(id_atributo_plantilla, id_atributo, id_plantilla, valor, nuevo) VALUES (?,?,?,?,0)''', (id_atributo_plantilla, id_atributo, id_plantilla, valor,))
            
            #Copiar Citas
            cLocal.execute('''SELECT  id_cita, uid,fecha as "fecha [timestamp]", anticipacion,id_actuacion FROM citas WHERE id_cita <> 0''')
            for row in cLocal:
                id_actuacion = str(row['id_actuacion'])
                id_cita = str(row['id_cita'])
                fecha = row['fecha']
                anticipacion = row['anticipacion']
                uid = row['uid']
                cMovil.execute('''INSERT INTO citas (id_cita,uid, fecha,anticipacion,id_actuacion, nuevo) VALUES( ?,?,?,?,?,0)''', (id_cita,uid,fecha,anticipacion,id_actuacion))
            
            #Bajar Flags de la base de datos de escritorio
            cLocal.execute('''UPDATE demandantes SET nuevo = 0, modificado = 0''')     
            cLocal.execute('''UPDATE demandados SET nuevo = 0, modificado = 0''')   
            cLocal.execute('''UPDATE juzgados SET nuevo = 0, modificado = 0''')   
            cLocal.execute('''UPDATE categorias SET nuevo = 0, modificado = 0''')
            cLocal.execute('''UPDATE atributos SET nuevo = 0, modificado = 0''')
            cLocal.execute('''UPDATE procesos SET nuevo = 0, modificado = 0''') 
            cLocal.execute('''UPDATE plantillas SET nuevo = 0, modificado = 0''')           
            cLocal.execute('''UPDATE actuaciones SET nuevo = 0, modificado = 0''')   
            cLocal.execute('''UPDATE atributos_proceso SET nuevo = 0, modificado = 0''')   
            cLocal.execute('''UPDATE atributos_plantilla SET nuevo = 0, modificado = 0''')
            cLocal.execute('''UPDATE citas SET nuevo = 0, modificado = 0''')
            
            #Insertar preferencia de sincronizacion
            cMovil.execute(''' INSERT OR IGNORE INTO preferencias(id_preferencia, valor) VALUES(997, datetime('now', 'localtime'))''')
            cMovil.execute(''' UPDATE preferencias SET valor = datetime('now', 'localtime') WHERE id_preferencia = 997''' )
            cLocal.execute(''' INSERT OR IGNORE INTO preferencias(id_preferencia, valor) VALUES(997, datetime('now', 'localtime'))''')
            cLocal.execute(''' UPDATE preferencias SET valor = datetime('now', 'localtime') WHERE id_preferencia = 997''' )
            connMovil.commit()
            connLocal.commit()
            print 'Archivo Movil actualizado'         
        except Exception as e:
            connLocal.rollback()
            connMovil.rollback()
            print "Operations rolled back"
            raise e
        finally:
            connLocal.close()
            connMovil.close()   
            
    def verificarSyncLocal(self, archivo_movil):
        #Verifica si el escritorio nunca ha sido sincronizado y copia la base de datos movil al dispositivo
        ret = False
        try:
            self.__conMgr.prepararBD()
            connLocal = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            connLocal.row_factory = sqlite3.Row
            connMovil = sqlite3.connect(archivo_movil, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            connMovil.row_factory = sqlite3.Row
            cLocal = connLocal.cursor()
            cMovil = connMovil.cursor()
            cLocal.execute('''SELECT * FROM preferencias WHERE id_preferencia = 997''')
            if cLocal.fetchone():
                ret = True
            else:
                #Copiar la base de datos del movil al escritorio
                #Seccion demandantes
                cMovil.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE id_demandante <> 1''')
                listaCMovil = cMovil.fetchall()
                for row in listaCMovil:
                    id_demandante = row['id_demandante']
                    cedula = row['cedula']
                    nombre = row['nombre']
                    telefono = row['telefono']
                    direccion = row['direccion']
                    correo = row['correo']
                    notas = row['notas']
                    cLocal.execute('''INSERT INTO demandantes(cedula, nombre, telefono, direccion, correo, notas, nuevo) VALUES(?,?,?,?,?,?,0)''', (cedula, nombre, telefono, direccion, correo, notas,))
                    _id = cLocal.lastrowid
                    cMovil.execute('''UPDATE procesos SET id_demandante = ? WHERE id_demandante = ? ''', (_id, id_demandante,))
                    cMovil.execute('''UPDATE plantillas SET id_demandante = ? WHERE id_demandante = ? ''', (_id, id_demandante,))
                
                #Seccion demandados
                cMovil.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE id_demandado <> 1''')
                listaCMovil = cMovil.fetchall()
                for row in listaCMovil:
                    id_demandado = row['id_demandado']
                    cedula = row['cedula']
                    nombre = row['nombre']
                    telefono = row['telefono']
                    direccion = row['direccion']
                    correo = row['correo']
                    notas = row['notas']
                    cLocal.execute('''INSERT INTO demandados(cedula, nombre, telefono, direccion, correo, notas, nuevo) VALUES(?,?,?,?,?,?,0)''', (cedula, nombre, telefono, direccion, correo, notas,))
                    _id = cLocal.lastrowid
                    cMovil.execute('''UPDATE procesos SET id_demandado = ? WHERE id_demandado = ? ''', (_id, id_demandado,))
                    cMovil.execute('''UPDATE plantillas SET id_demandado = ? WHERE id_demandado = ? ''', (_id, id_demandado,))            
                
                #Seccion Juzgados
                cMovil.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE id_juzgado <> 1''')
                listaCMovil = cMovil.fetchall()
                for row in listaCMovil:
                    id_juzgado = row['id_juzgado']
                    nombre = row['nombre']
                    ciudad = row['ciudad']
                    telefono = row['telefono']
                    direccion = row['direccion'] 
                    tipo = row['tipo']
                    cLocal.execute('''INSERT INTO juzgados(nombre, ciudad, telefono, direccion, tipo, nuevo) VALUES(?,?,?,?,?,0)''', (nombre, ciudad, telefono, direccion, tipo,))
                    _id = cLocal.lastrowid
                    cMovil.execute('''UPDATE procesos SET id_juzgado = ? WHERE id_juzgado = ? ''', (_id, id_juzgado,))
                    cMovil.execute('''UPDATE plantillas SET id_juzgado = ? WHERE id_juzgado = ? ''', (_id, id_juzgado,))
                    cMovil.execute('''UPDATE actuaciones SET id_juzgado = ? WHERE id_juzgado = ? ''', (_id, id_juzgado,))
                
                #Seccion categorias
                cMovil.execute('''SELECT id_categoria, descripcion FROM categorias WHERE id_categoria <> 1''')
                listaCMovil = cMovil.fetchall()
                for row in listaCMovil:
                    id_categoria = row['id_categoria']
                    descripcion = row['descripcion']
                    cLocal.execute('''INSERT INTO categorias(descripcion, nuevo) VALUES(?,0)''', (descripcion,))
                    _id = cLocal.lastrowid
                    cMovil.execute('''UPDATE procesos SET id_categoria = ? WHERE id_categoria = ? ''', (_id, id_categoria,))
                    cMovil.execute('''UPDATE plantillas SET id_categoria = ? WHERE id_categoria = ? ''', (_id, id_categoria,))
                
                #Seccion Atributos
                cMovil.execute('''SELECT id_atributo, nombre, obligatorio, longitud_max, longitud_min FROM atributos''')
                listaCMovil = cMovil.fetchall()
                for row in listaCMovil:
                    id_atributo = row['id_atributo']
                    nombre = row['nombre']
                    obligatorio = row['obligatorio']
                    longitud_max = row['longitud_max']
                    longitud_min = row['longitud_min']
                    cLocal.execute('''INSERT INTO atributos(nombre, obligatorio, longitud_max, longitud_min, nuevo) VALUES(?,?,?,?,0)''', (nombre, obligatorio, longitud_max, longitud_min,))
                    _id = cLocal.lastrowid
                    cMovil.execute('''UPDATE atributos_proceso SET id_atributo = ? WHERE id_atributo = ? ''', (_id, id_atributo,))
                    cMovil.execute('''UPDATE atributos_plantilla SET id_atributo = ? WHERE id_atributo = ? ''', (_id, id_atributo,))
                
                #Seccion Procesos
                cMovil.execute('''SELECT id_proceso, id_demandante, id_demandado, fecha_creacion as "fecha_creacion [timestamp]", radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM procesos''')
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
                    cLocal.execute('''INSERT INTO procesos(id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, nuevo) VALUES (?,?,?,?,?,?,?,?,?,?,?,0)''', (id_demandante, id_demandado, fecha_creacion, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                    _id = cLocal.lastrowid
                    cMovil.execute('''UPDATE atributos_proceso SET id_proceso = ? WHERE id_proceso = ? ''', (_id, id_proceso,))
                    cMovil.execute('''UPDATE actuaciones SET id_proceso = ? WHERE id_proceso = ? ''', (_id, id_proceso,))
                
                #Seccion Plantillas
                cMovil.execute('''SELECT id_plantilla, nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria FROM plantillas''')
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
                    cLocal.execute('''INSERT INTO plantillas(nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria, nuevo) VALUES (?,?,?,?,?,?,?,?,?,?,?,0)''', (nombre, id_demandante, id_demandado, radicado, radicado_unico, estado, tipo, notas, prioridad, id_juzgado, id_categoria,))
                    _id = cLocal.lastrowid
                    cMovil.execute('''UPDATE atributos_plantilla SET id_plantilla = ? WHERE id_plantilla = ? ''', (_id, id_plantilla,))
                
                #Seccion Actuaciones
                cMovil.execute('''SELECT id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones''')
                for row in cMovil:
                    id_proceso = row['id_proceso']
                    id_juzgado = row['id_juzgado']
                    fecha_creacion = row['fecha_creacion']
                    fecha_proxima = row['fecha_proxima']
                    descripcion = row['descripcion']
                    uid = row['uid']
                    cLocal.execute('''INSERT INTO actuaciones(id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid, nuevo) VALUES(?,?,?,?,?,?,0)''', (id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid,))
    
                #Seccion Atributos por Proceso
                cMovil.execute('''SELECT id_atributo, id_proceso, valor FROM atributos_proceso''')
                for row in cMovil:
                    id_atributo = row['id_atributo']
                    id_proceso = row['id_proceso']
                    valor = row['valor']
                    cLocal.execute('''INSERT INTO atributos_proceso(id_atributo, id_proceso, valor, nuevo) VALUES (?,?,?,0)''', (id_atributo, id_proceso, valor,))
                    
                #Seccion Atributos por plantilla
                cMovil.execute('''SELECT id_atributo, id_plantilla, valor FROM atributos_plantilla''')
                for row in cMovil:
                    id_atributo = row['id_atributo']
                    id_plantilla = row['id_plantilla']
                    valor = row['valor']
                    cLocal.execute('''INSERT INTO atributos_plantilla(id_atributo, id_plantilla, valor, nuevo) VALUES (?,?,?,0)''', (id_atributo, id_plantilla, valor,))
                
                cMovil.execute('''SELECT id_cita, uid,fecha as "fecha [timestamp]", anticipacion,id_actuacion FROM citas''')
                for row in cMovil:
                    id_actuacion = str(row['id_actuacion'])
                    fecha = row['fecha']
                    anticipacion = row['anticipacion']
                    uid = row['uid']
                    cLocal.execute('''INSERT INTO citas (id_cita,uid, fecha,anticipacion,id_actuacion, nuevo) VALUES( NULL,?,?,?,?,0)''', (uid,fecha,anticipacion,id_actuacion))
                ret = False
                print 'Copiado desde el movil al Escritorio'  
                connMovil.commit()
                connLocal.commit()
                   
        except Exception as e:
            connLocal.rollback()
            connMovil.rollback()
            print "Operations rolled back"
            raise e
        finally:
            connLocal.close()
            connMovil.close()  
            return ret 