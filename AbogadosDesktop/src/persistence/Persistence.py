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
            c.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE eliminado = 0 ORDER BY nombre''')
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
            c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE eliminado = 0 ORDER BY nombre''')
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
            c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE eliminado = 0 ORDER BY nombre''')
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
            c.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE eliminado = 0 ORDER BY nombre''')
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
        procesos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT p.id_proceso, p.id_demandante, p.id_demandado, p.fecha_creacion as "fecha_creacion [timestamp]", p.radicado, p.radicado_unico, p.estado, p.tipo, p.notas, p.prioridad, p.id_juzgado, p.id_categoria FROM procesos p WHERE eliminado = 0''')
            for row in c:
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
                demandante = Persona(1, id_persona=id_demandante)
                demandado = Persona(2, id_persona=id_demandado)
                juzgado = Juzgado(id_juzgado=id_juzgado)
                categoria = Categoria(id_categoria=id_categoria)
                proceso = Proceso(demandante, demandado, fecha_creacion, juzgado, radicado, radicado_unico, [], estado, categoria, tipo, notas, [], prioridad, id_proceso)
                procesos.append(proceso)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for proceso_act in procesos:
            proceso_act.setDemandante(self.consultarPersona(proceso_act.getDemandante().getId_persona(), 1))
            proceso_act.setDemandado(self.consultarPersona(proceso_act.getDemandado().getId_persona(), 2))
            proceso_act.setJuzgado(self.consultarJuzgado(proceso_act.getJuzgado().getId_juzgado()))
            proceso_act.setActuaciones(self.consultarActuaciones(proceso_act))
            proceso_act.setCampos(self.consultarCampos(proceso_act))
            proceso_act.setCategoria(self.consultarCategoria(proceso_act.getCategoria().getId_categoria()))
        return procesos
    
    def consultarProceso(self, id_proceso):
        proceso = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT p.id_proceso, p.id_demandante, p.id_demandado, p.fecha_creacion as "fecha_creacion [timestamp]", p.radicado, p.radicado_unico, p.estado, p.tipo, p.notas, p.prioridad, p.id_juzgado, p.id_categoria FROM procesos p WHERE p.id_proceso = ?''', (id_proceso,))
            row = c.fetchone()
            if row:
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
                demandante = Persona(1, id_persona=id_demandante)
                demandado = Persona(2, id_persona=id_demandado)
                juzgado = Juzgado(id_juzgado=id_juzgado)
                categoria = Categoria(id_categoria=id_categoria)
                proceso = Proceso(demandante, demandado, fecha_creacion, juzgado, radicado, radicado_unico, [], estado, categoria, tipo, notas, [], prioridad, id_proceso)
        except Exception as e:
            raise e
        finally:
            conn.close()
        proceso.setDemandante(self.consultarPersona(proceso.getDemandante().getId_persona(), 1))
        proceso.setDemandado(self.consultarPersona(proceso.getDemandado().getId_persona(), 2))
        proceso.setJuzgado(self.consultarJuzgado(proceso.getJuzgado().getId_juzgado()))
        proceso.setActuaciones(self.consultarActuaciones(proceso))
        proceso.setCampos(self.consultarCampos(proceso))
        proceso.setCategoria(self.consultarCategoria(proceso.getCategoria().getId_categoria()))
        return proceso
    
    def consultarActuaciones(self, proceso):
        actuaciones = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE id_proceso = ? AND eliminado = 0 ORDER BY fecha_creacion, fecha_proxima''', (proceso.getId_proceso(),))
            for row in c:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = str(row['descripcion'])
                uid = str(row['uid'])
                juzgado = Juzgado(id_juzgado=id_juzgado)
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
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE id_actuacion = ?''', (id_actuacion,))
            row = c.fetchone()
            if row:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = str(row['descripcion'])
                uid = str(row['uid'])
                juzgado = Juzgado(id_juzgado=id_juzgado)
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
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE fecha_proxima >= date() AND eliminado = 0 ORDER BY fecha_proxima LIMIT ?''', (cantidad,))
            for row in c:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = str(row['descripcion'])
                uid = str(row['uid'])
                juzgado = Juzgado(id_juzgado=id_juzgado)
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
            c.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE eliminado = 0 ORDER BY nombre''')
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
            c.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE id_juzgado = ?''', (id_juzgado,))
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
            c.execute('''SELECT id_categoria, descripcion FROM categorias WHERE eliminado = 0 ORDER BY descripcion''')
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
            c.execute('''SELECT at.id_atributo_proceso, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_proceso at, atributos a WHERE at.id_atributo = a.id_atributo AND at.id_proceso = ? AND at.eliminado = 0''', (proceso.getId_proceso(),))
            for row in c:
                id_atributo_proceso = str(row['id_atributo_proceso'])
                id_atributo = str(row['id_atributo'])
                valor = str(row['valor'])
                nombre = str(row['nombre'])
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
                valor = str(row['valor'])
                nombre = str(row['nombre'])
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
        atributos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_atributo, nombre,obligatorio,longitud_max, longitud_min FROM  atributos WHERE eliminado = 0''')
            for row in c:
                id_atributo = str(row['id_atributo'])
                nombre = str(row['nombre'])
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False 
                campo = CampoPersonalizado(id_atributo=id_atributo, nombre=nombre, obligatorio=obligatorio, longitudMax=longitud_max, longitudMin=longitud_min)    
                atributos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return atributos
     
    def consultarPlantillas(self):
        plantillas = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT p.id_plantilla, p.id_demandante, p.id_demandado, p.radicado, p.radicado_unico, p.estado, p.tipo, p.notas, p.prioridad, p.id_juzgado, p.id_categoria, p.nombre FROM plantillas p WHERE eliminado = 0''')
            for row in c:
                id_plantilla = str(row['id_plantilla'])
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
                nombre = str(row['nombre'])
                demandante = Persona(1, id_persona=id_demandante)
                demandado = Persona(2, id_persona=id_demandado)
                juzgado = Juzgado(id_juzgado=id_juzgado)
                categoria = Categoria(id_categoria=id_categoria)
                plantilla = Plantilla(nombre, demandante, demandado, juzgado, radicado, radicado_unico, estado, categoria, tipo, notas, [], prioridad, id_plantilla)
                plantillas.append(plantilla)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for plantilla_act in plantillas:
            plantilla_act.setDemandante(self.consultarPersona(plantilla_act.getDemandante().getId_persona(), 1))
            plantilla_act.setDemandado(self.consultarPersona(plantilla_act.getDemandado().getId_persona(), 2))
            plantilla_act.setJuzgado(self.consultarJuzgado(plantilla_act.getJuzgado().getId_juzgado()))
            plantilla_act.setCampos(self.consultarCamposPlantilla(plantilla_act))
            plantilla_act.setCategoria(self.consultarCategoria(plantilla_act.getCategoria().getId_categoria()))
        return plantillas 
    
    def consultarPlantilla(self, id_plantilla):
        plantilla = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT p.id_plantilla, p.id_demandante, p.id_demandado, p.radicado, p.radicado_unico, p.estado, p.tipo, p.notas, p.prioridad, p.id_juzgado, p.id_categoria, p.nombre FROM plantillas p WHERE p.id_plantilla = ?''', (id_plantilla,))
            row = c.fetchone()
            if row:
                id_plantilla = str(row['id_plantilla'])
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
                nombre = str(row['nombre'])
                demandante = Persona(1, id_persona=id_demandante)
                demandado = Persona(2, id_persona=id_demandado)
                juzgado = Juzgado(id_juzgado=id_juzgado)
                categoria = Categoria(id_categoria=id_categoria)
                plantilla = Plantilla(nombre, demandante, demandado, juzgado, radicado, radicado_unico, estado, categoria, tipo, notas, [], prioridad, id_plantilla)
        except Exception as e:
            raise e
        finally:
            conn.close()
        plantilla.setDemandante(self.consultarPersona(plantilla.getDemandante().getId_persona(), 1))
        plantilla.setDemandado(self.consultarPersona(plantilla.getDemandado().getId_persona(), 2))
        plantilla.setJuzgado(self.consultarJuzgado(plantilla.getJuzgado().getId_juzgado()))
        plantilla.setCampos(self.consultarCamposPlantilla(plantilla))
        plantilla.setCategoria(self.consultarCategoria(plantilla.getCategoria().getId_categoria()))
        return plantilla
    
    def consultarCamposPlantilla(self, plantilla):
        campos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_plantilla, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_plantilla at, atributos a WHERE at.id_atributo = a.id_atributo AND at.id_plantilla = ? AND at.eliminado = 0''', (plantilla.getId_plantilla(),))
            for row in c:
                id_atributo_plantilla = str(row['id_atributo_plantilla'])
                id_atributo = str(row['id_atributo'])
                valor = str(row['valor'])
                nombre = str(row['nombre'])
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_plantilla, id_atributo)
                campos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campos
    
    def consultarCampoPlantilla(self, id_plantilla):
        campo = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_plantilla, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_plantilla at, atributos a WHERE at.id_atributo = a.id_atributo AND at.id_atributo_plantilla = ?''', (id_plantilla,))
            row = c.fetchone()
            if row:
                id_atributo_plantilla = str(row['id_atributo_plantilla'])
                id_atributo = str(row['id_atributo'])
                valor = str(row['valor'])
                nombre = str(row['nombre'])
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_plantilla, id_atributo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campo
      
    def consultarPreferencia(self, id_preferencia):
        valor = 0
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT valor FROM preferencias WHERE id_preferencia = ? ''', (id_preferencia,))
            row = c.fetchone()
            if row:
                valor = row['valor']
        except Exception as e:
            raise e
        finally:
            conn.close()
        return valor
    
    #Campos personalizados para las personas    
    def consultarAtributosPersona(self):
        atributos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_atributo, nombre,obligatorio,longitud_max, longitud_min FROM  atributosPersona WHERE eliminado = 0''')
            for row in c:
                id_atributo = str(row['id_atributo'])
                nombre = str(row['nombre'])
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False 
                campo = CampoPersonalizado(id_atributo=id_atributo, nombre=nombre, obligatorio=obligatorio, longitudMax=longitud_max, longitudMin=longitud_min)    
                atributos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return atributos
    
    #Cargar los campos personalizados de un demandante
    def consultarCamposDemandante(self, demandante):
        campos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_demandante, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_demandante at, atributosPersona a WHERE at.id_atributo = a.id_atributo AND at.id_demandante = ? AND at.eliminado = 0''', (demandante.getId_persona(),))
            for row in c:
                id_atributo_demandante = str(row['id_atributo_demandante'])
                id_atributo = str(row['id_atributo'])
                valor = str(row['valor'])
                nombre = str(row['nombre'])
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_demandante, id_atributo)
                campos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campos    
    
    #Cargar un campo personalizado de demandante especifico
    def consultarCampoDemandante(self, id_campo):
        campo = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_demandante, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_demandante at, atributosPersona a WHERE at.id_atributo = a.id_atributo AND at.id_atributo_demandante = ?''', (id_campo,))
            row = c.fetchone()
            if row:
                id_atributo_demandante = str(row['id_atributo_demandante'])
                id_atributo = str(row['id_atributo'])
                valor = str(row['valor'])
                nombre = str(row['nombre'])
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_demandante, id_atributo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campo
    
    def consultarAtributosJuzgado(self):
        atributos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_atributo, nombre,obligatorio,longitud_max, longitud_min FROM  atributosJuzgado WHERE eliminado = 0''')
            for row in c:
                id_atributo = str(row['id_atributo'])
                nombre = str(row['nombre'])
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False 
                campo = CampoPersonalizado(id_atributo=id_atributo, nombre=nombre, obligatorio=obligatorio, longitudMax=longitud_max, longitudMin=longitud_min)    
                atributos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return atributos

    def consultarAtributosActuacion(self):
        atributos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_atributo, nombre,obligatorio,longitud_max, longitud_min FROM  atributosActuacion WHERE eliminado = 0''')
            for row in c:
                id_atributo = str(row['id_atributo'])
                nombre = str(row['nombre'])
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False 
                campo = CampoPersonalizado(id_atributo=id_atributo, nombre=nombre, obligatorio=obligatorio, longitudMax=longitud_max, longitudMin=longitud_min)    
                atributos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return atributos   
