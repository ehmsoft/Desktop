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
        demandantes = []
        try:
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
        except Exception as e:
            raise e
        finally:
            conn.close()
        return demandantes
    
    def consultarDemandados(self):
        demandados = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados order by nombre''')
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
        except Exception as e:
            raise e
        finally:
            conn.close()
        return demandados
    
    def consultarPersonas(self):
        personas = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados order by nombre''')
            for row in c:
                id_demandado = str(row['id_demandado'])
                cedula = str(row['cedula'])
                nombre = str(row['nombre'])
                telefono = str(row['telefono'])
                direccion = str(row['direccion'])            
                correo = str(row['correo'])
                notas = str(row['notas'])
                demandado = Persona(2, cedula, nombre, telefono, direccion, correo, notas, id_demandado)
                personas.append(demandado)
            c.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes order by nombre''')
            for row in c:
                id_demandante = str(row['id_demandante'])
                cedula = str(row['cedula'])
                nombre = str(row['nombre'])
                telefono = str(row['telefono'])
                direccion = str(row['direccion'])            
                correo = str(row['correo'])
                notas = str(row['notas'])
                demandante = Persona(1, cedula, nombre, telefono, direccion, correo, notas, id_demandante)
                personas.append(demandante)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return personas
            
    def consultarPersona(self, id_persona, tipo):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            persona = None
            if tipo == 1:
                c.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE id_demandante = ?''', (id_persona,))
                row = c.fetchone()
                if row:
                    id_demandante = str(row['id_demandante'])
                    cedula = str(row['cedula'])
                    nombre = str(row['nombre'])
                    telefono = str(row['telefono'])
                    direccion = str(row['direccion'])            
                    correo = str(row['correo'])
                    notas = str(row['notas'])
                    persona = Persona(1, cedula, nombre, telefono, direccion, correo, notas, id_demandante)
            elif tipo == 2:
                c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE id_demandado = ?''', (id_persona,))
                row = c.fetchone()
                if row:
                    id_demandado = str(row['id_demandado'])
                    cedula = str(row['cedula'])
                    nombre = str(row['nombre'])
                    telefono = str(row['telefono'])
                    direccion = str(row['direccion'])            
                    correo = str(row['correo'])
                    notas = str(row['notas'])
                    persona = Persona(2, cedula, nombre, telefono, direccion, correo, notas, id_demandado)
            else:
                raise ValueError('El tipo de persona no es correcto')
        except Exception as e:
            raise e
        finally:
            conn.close()
        return persona
    def consultarProcesos(self):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(''' ''')
        except Exception as e:
            raise e
        finally:
            conn.close()
            
    def consultarProceso(self, id_proceso):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(''' ''')
        except Exception as e:
            raise e
        finally:
            conn.close()
            
    def consultarActuaciones(self, proceso):
        actuaciones = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE id_proceso = ? ORDER BY fecha_creacion, fecha_proxima''', (proceso.getId_proceso(),))
            for row in c:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = str(row['descripcion'])
                uid = str(row['uid'])
                juzgado = Juzgado(id_juzgado = id_juzgado)
                actuacion = Actuacion(juzgado, fecha_creacion, fecha_proxima, descripcion, id_actuacion, uid)
                actuaciones.append(actuacion)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for act in actuaciones:
            act.setJuzgado(self.consultarJuzgado(act.getJuzgado().getId_juzgado()))
        return actuaciones
        
    def consultarActuacion(self, id_actuacion):
        actuacion = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE id_actuacion = ?''',(id_actuacion,))
            row = c.fetchone()
            if row:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = str(row['descripcion'])
                uid = str(row['uid'])
                juzgado = Juzgado(id_juzgado = id_juzgado)
                actuacion = Actuacion(juzgado, fecha_creacion, fecha_proxima, descripcion, id_actuacion, uid)  
        except Exception as e:
            raise e
        finally:
            conn.close()
        return actuacion
    def consultarActuacionesCriticas(self, cantidad):
        actuaciones = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE fecha_proxima >= date() ORDER BY fecha_proxima LIMIT ?''', (cantidad,))
            for row in c:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = str(row['descripcion'])
                uid = str(row['uid'])
                juzgado = Juzgado(id_juzgado = id_juzgado)
                actuacion = Actuacion(juzgado, fecha_creacion, fecha_proxima, descripcion, id_actuacion, uid)
                actuaciones.append(actuacion)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for act in actuaciones:
            act.setJuzgado(self.consultarJuzgado(act.getJuzgado().getId_juzgado()))
        return actuaciones
            
    def consultarJuzgados(self):
        juzgados = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados ORDER BY nombre''')
            for row in c:
                id_juzgado = str(row['id_juzgado'])
                nombre = str(row['nombre'])
                ciudad = str(row['ciudad'])
                telefono = str(row['telefono'])
                direccion = str(row['direccion'])
                tipo = str(row['tipo'])
                juzgado = Juzgado(nombre, ciudad, direccion, telefono, tipo, id_juzgado)
                juzgados.append(juzgado)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return juzgados    
    def consultarJuzgado(self, id_juzgado):
        juzgado = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE id_juzgado = ?''',(id_juzgado,))
            row = c.fetchone()
            if row:
                id_juzgado = str(row['id_juzgado'])
                nombre = str(row['nombre'])
                ciudad = str(row['ciudad'])
                telefono = str(row['telefono'])
                direccion = str(row['direccion'])
                tipo = str(row['tipo'])
                juzgado = Juzgado(nombre, ciudad, direccion, telefono, tipo, id_juzgado)            
        except Exception as e:
            raise e
        finally:
            conn.close()
        return juzgado    
    def consultarCategoria(self, id_categoria):
        categoria = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_categoria, descripcion FROM categorias WHERE id_categoria = ?''', (id_categoria,))
            row = c.fetchone()
            if row:
                id_categoria = str(row['id_categoria'])
                descripcion = str(row['descripcion'])
                categoria = Categoria(descripcion, id_categoria)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return categoria
    
    def consultarCategorias(self):
        categorias = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_categoria, descripcion FROM categorias ORDER BY descripcion''')
            for row in c:
                id_categoria = str(row['id_categoria'])
                descripcion = str(row['descripcion'])
                categoria = Categoria(descripcion, id_categoria)
                categorias.append(categoria)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return categorias
    
    def consultarCampos(self, proceso):
        campos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_proceso, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_proceso at, atributos a WHERE at.id_atributo = a.id_atributo AND at.id_proceso = ?''', (proceso.getId_proceso(),))
            for row in c:
                id_atributo_proceso = str(row['id_atributo_proceso'])
                id_atributo = str(row['id_atributo'])
                valor = row['valor']
                nombre = row['nombre']
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_proceso, id_atributo)
                campos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campos
    
    def consultarCampo(self, id_campo):
        campo = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_proceso, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_proceso at, atributos a WHERE at.id_atributo = a.id_atributo AND at.id_atributo_proceso = ?''', (id_campo,))
            row = c.fetchone()
            if row:
                id_atributo_proceso = str(row['id_atributo_proceso'])
                id_atributo = str(row['id_atributo'])
                valor = row['valor']
                nombre = row['nombre']
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_proceso, id_atributo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campo 
    def consultarAtributos(self):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(''' ''')
        except Exception as e:
            raise e
        finally:
            conn.close()
            
    def consultarPlantillas(self):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(''' ''')
        except Exception as e:
            raise e
        finally:
            conn.close()
            
    def consultarPlantilla(self, id_plantilla):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(''' ''')
        except Exception as e:
            raise e
        finally:
            conn.close()
            
    def consultarCamposPlantilla(self, plantilla):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(''' ''')
        except Exception as e:
            raise e
        finally:
            conn.close()
            
    def consultarCampoPlantilla(self, id_plantilla):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(''' ''')
        except Exception as e:
            raise e
        finally:
            conn.close()
            
    def consultarPreferencia(self, id_preferencia):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(''' ''')
        except Exception as e:
            raise e
        finally:
            conn.close()