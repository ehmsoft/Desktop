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
from core.Archivo import Archivo

class Persistence(object):
    '''
    Clase Persistence
    '''


    def __init__(self):
        self.__conMgr = ConnectionManager()
    
    #Metodos de Guardado
    def actualizarPersona(self, persona):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            if persona.getTipo() == 1:
                c.execute('''UPDATE demandantes SET cedula = ?,''' + ''' nombre = ?,''' + ''' telefono = ?, direccion = ?,''' + '''correo= ?,''' + '''notas = ?,''' + ''' fecha_mod = datetime('now','localtime'), modificado =1 WHERE id_demandante = ?''', (persona.getId(), persona.getNombre(), persona.getTelefono(), persona.getDireccion(), persona.getCorreo(), persona.getNotas(), persona.getId_persona(),))
            elif persona.getTipo() == 2:
                c.execute('''UPDATE demandados SET cedula = ?,''' + ''' nombre = ?,''' + ''' telefono = ?,''' + ''' direccion = ?,''' + '''correo= ?,''' + ''' notas = ?,''' + ''' fecha_mod = datetime('now','localtime'), modificado =1 WHERE id_demandado = ?''', (persona.getId(), persona.getNombre(), persona.getTelefono(), persona.getDireccion(), persona.getCorreo(), persona.getNotas(), persona.getId_persona(),))
            else:
                print("eso no es asi")  
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def guardarPersona(self, persona):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            if persona.getTipo() == 1:
                c.execute('''INSERT INTO demandantes (id_demandante,cedula,nombre,telefono,direccion,correo,notas,nuevo,fecha_mod) VALUES(NULL,?,?,?,?,?,?,1,datetime('now','localtime'))''', (persona.getId(), persona.getNombre(), persona.getTelefono(), persona.getDireccion(), persona.getCorreo(), persona.getNotas()))
            elif persona.getTipo() == 2:
                c.execute('''INSERT INTO demandados (id_demandado,cedula,nombre,telefono,direccion,correo,notas,nuevo,fecha_mod) VALUES(NULL,?,?,?,?,?,?,1,datetime('now','localtime'))''', (persona.getId(), persona.getNombre(), persona.getTelefono(), persona.getDireccion(), persona.getCorreo(), persona.getNotas()))
            else:
                print("eso no es asi")
            conn.commit() 
            persona.setId_persona(str(c.lastrowid))  
                     
        except Exception as e:
            raise e
        finally:
            conn.close()
            
        if persona.getTipo() == 1:
            campos = persona.getCampos()
            for campo in campos:
                self.guardarCampoDemandante(campo, persona.getId_persona())
        elif persona.getTipo() == 2:
            campos = persona.getCampos()
            for campo in campos:
                self.guardarCampoDemandado(campo, persona.getId_persona())
        else:
            print("eso no es asi")
         
        
    def borrarPersona(self, persona):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            if persona.getTipo() == 1:
                c.execute('''UPDATE demandantes SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_demandante = ?''', (persona.getId_persona(),))
                c.execute('''UPDATE procesos SET id_demandante = 1 WHERE id_demandante = ?''', (persona.getId_persona(),))
                c.execute('''UPDATE plantillas SET id_demandante = 1 WHERE id_demandante = ?''', (persona.getId_persona(),))

            elif persona.getTipo() == 2:
                c.execute('''UPDATE demandados SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_demandado = ?''', (persona.getId_persona(),))
                c.execute('''UPDATE procesos SET id_demandado = 1 WHERE id_demandado = ?''', (persona.getId_persona(),))
                c.execute('''UPDATE plantillas SET id_demandado = 1 WHERE id_demandado = ?''', (persona.getId_persona(),))

            else:
                print("eso no es asi") 
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarJuzgado(self, juzgado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE juzgados SET nombre = ?,''' + ''' ciudad = ?,''' + ''' telefono = ?,''' + ''' direccion= ?,''' + ''' tipo = ?,''' + ''' modificado =1, fecha_mod = datetime('now','localtime') WHERE id_juzgado = ?''', (juzgado.getNombre(), juzgado.getCiudad(), juzgado.getTelefono(), juzgado.getDireccion(), juzgado.getTipo(), juzgado.getId_juzgado()))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def guardarJuzgado(self, juzgado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO juzgados (id_juzgado,nombre,ciudad,telefono,direccion,tipo,nuevo, fecha_mod) VALUES( NULL,?,?,?,?,?,1,datetime('now','localtime'))''', (juzgado.getNombre(), juzgado.getCiudad(), juzgado.getTelefono(), juzgado.getDireccion(), juzgado.getTipo()))
            conn.commit()  
            juzgado.setId_juzgado(str(c.lastrowid))
                      
        except Exception as e:
            raise e
        finally:
            conn.close()
        campos = juzgado.getCampos()
        for campo in campos:
            self.guardarCampoJuzgado(campo, juzgado.getId_juzgado())
    def borrarJuzgado(self, juzgado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE juzgados SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_juzgado = ?''', (juzgado.getId_juzgado(),))
            c.execute('''UPDATE procesos SET id_juzgado = 1 WHERE id_juzgado = ?''', (juzgado.getId_juzgado(),))
            c.execute('''UPDATE actuaciones SET id_juzgado = 1 WHERE id_juzgado = ?''', (juzgado.getId_juzgado(),))
            c.execute('''UPDATE plantillas SET id_juzgado = 1 WHERE id_juzgado = ?''', (juzgado.getId_juzgado(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarActuacion(self, actuacion):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE actuaciones SET id_juzgado = ?,''' + ''' fecha_creacion = datetime(?),''' + ''' fecha_proxima = datetime(?),''' + ''' descripcion = (?),''' + ''' uid = ?,''' + ''' modificado =1, fecha_mod = datetime('now','localtime') WHERE id_actuacion = ?''', (actuacion.getJuzgado().getId_juzgado(), actuacion.getFecha(), actuacion.getFechaProxima(), actuacion.getDescripcion(), actuacion.getUid(), actuacion.getId_actuacion()))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def guardarActuacion(self, actuacion, id_proceso):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO actuaciones (id_actuacion,id_proceso, id_juzgado, fecha_creacion, fecha_proxima, descripcion, uid, nuevo, fecha_mod) VALUES( NULL,?,?,datetime(?),datetime(?),?,?,1,datetime('now','localtime'))''', (id_proceso, actuacion.getJuzgado().getId_juzgado(), actuacion.getFecha(), actuacion.getFechaProxima(), actuacion.getDescripcion(), actuacion.getUid()))
            conn.commit()
            actuacion.setId_actuacion(str(c.lastrowid))
                        
        except Exception as e:
            raise e
        finally:
            conn.close()
            
        campos = actuacion.getCampos()
        for campo in campos:
            self.guardarCampoActuacion(campo, actuacion.getId_actuacion())
    def borrarActuacion(self, actuacion):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE actuaciones SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_actuacion = ?''', (actuacion.getId_actuacion(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarCampoPersonalizado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_proceso SET valor = ?, modificado =1,fecha_mod = datetime('now','localtime') WHERE id_atributo_proceso = ?''', (campoPersonalizado.getValor(), campoPersonalizado.getId_campo()))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close    
    def guardarCampoPersonalizado(self, campoPersonalizado, id_proceso):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO atributos_proceso (id_atributo_proceso, id_atributo, id_proceso, valor, nuevo, fecha_mod) VALUES( NULL,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getId_atributo(), id_proceso, campoPersonalizado.getValor()))
            conn.commit()
            campoPersonalizado.setId_campo(str(c.lastrowid))
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarCampoPersonalizado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_proceso SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo_proceso = ?''', (campoPersonalizado.getId_campo(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarAtributo(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            obligatorio = 0
            if(campoPersonalizado.isObligatorio()):
                obligatorio = 1                   
            c.execute('''UPDATE atributos SET nombre = ?,''' + ''' obligatorio = ?,''' + ''' longitud_max = ?,''' + ''' longitud_min = ?,''' + ''' modificado =1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getNombre(), obligatorio, campoPersonalizado.getLongitudMax(), campoPersonalizado.getLongitudMin(), campoPersonalizado.getId_atributo()))                
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
        
    def guardarAtributo(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            obligatorio = 0
            if(campoPersonalizado.isObligatorio()):
                obligatorio = 1                   
            c.execute('''INSERT INTO atributos (id_atributo, nombre, obligatorio, longitud_max, longitud_min,nuevo, fecha_mod) VALUES( NULL,?,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getNombre(), obligatorio, campoPersonalizado.getLongitudMax(), campoPersonalizado.getLongitudMin()))                
            conn.commit()  
            campoPersonalizado.setId_atributo(str(c.lastrowid))
                      
        except Exception as e:
            raise e
        finally:
            conn.close()
       
    def borrarAtributo(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_atributo(),))
            c.execute('''UPDATE atributos_proceso SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_atributo(),))
            c.execute('''UPDATE atributos_plantilla SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_atributo(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarProceso(self, proceso):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            demandante = "1"
            if demandante != None:
                demandante = proceso.getDemandante().getId_persona()
            demandado = "1"
            if demandado != None:
                proceso.getDemandado().getId_persona()
            juzgado = "1"
            if juzgado != None:
                proceso.getJuzgado().getId_juzgado()
                
            c.execute('''UPDATE procesos SET id_demandante = ?,''' + ''' id_demandado = ?,''' + ''' fecha_creacion = datetime(?),''' + ''' radicado = ?,''' + ''' radicado_unico = ?,''' + ''' estado = ?,''' + ''' tipo = ?,''' + ''' notas = ?,''' + ''' prioridad = ?,''' + ''' id_juzgado = ?,''' + ''' id_categoria = ?,''' + ''' modificado =1, fecha_mod = datetime('now','localtime') WHERE id_proceso = ?''', (demandante, demandado, proceso.getFecha(), proceso.getRadicado(), proceso.getRadicadoUnico(), proceso.getEstado(), proceso.getTipo(), proceso.getNotas(), proceso.getPrioridad(), juzgado, proceso.getCategoria().getId_categoria(), proceso.getId_proceso()))                                                         
            conn.commit()
                      
        except Exception as e:
            raise e
        finally:
            conn.close()
        campos = proceso.getCampos()
        for campo in campos:
            self.guardarCampoPersonalizado(campo, proceso.getId_proceso())
            
    def guardarProceso(self, proceso):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO procesos (id_proceso,id_demandante,id_demandado,fecha_creacion,radicado,radicado_unico,estado,tipo,notas,prioridad,id_juzgado,id_categoria,nuevo,fecha_mod) VALUES(NULL,?,?,datetime(?),?,?,?,?,?,?,?,?,1,datetime('now','localtime'))''', (proceso.getDemandante().getId_persona(), proceso.getDemandado().getId_persona(), proceso.getFecha(), proceso.getRadicado(), proceso.getRadicadoUnico(), proceso.getEstado(), proceso.getTipo(), proceso.getNotas(), proceso.getPrioridad(), proceso.getJuzgado().getId_juzgado(), proceso.getCategoria().getId_categoria()))                                                         
            conn.commit()
            proceso.setId_proceso(str(c.lastrowid))
            
                
        except Exception as e:
            raise e
        finally:
            conn.close()
        
        campos = proceso.getCampos()
        for campo in campos:
            self.guardarCampoPersonalizado(campo, proceso.getId_proceso())
        actuaciones = proceso.getActuaciones()
        for actuacion in actuaciones:
            self.guardarActuacion(actuacion, proceso.getId_proceso())   
        
        
    def borrarProceso(self, proceso):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE procesos SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_proceso = ?''', (proceso.getId_proceso(),))
            c.execute('''UPDATE actuaciones SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_proceso = ?''', (proceso.getId_proceso(),))
            c.execute('''UPDATE atributos_proceso SET eliminado = 1,fecha_mod = datetime('now','localtime') WHERE id_proceso = ?''', (proceso.getId_proceso(),))
            proceso.setId_proceso = str(c.lastrowid)
            conn.commit()
                
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarCategoria(self, categoria):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE categorias SET descripcion = ?, modificado =1,fecha_mod = datetime('now','localtime') WHERE id_categoria = ?''', (categoria.getDescripcion(), categoria.getId_categoria()))        
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def guardarCategoria(self, categoria):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO categorias (id_categoria,descripcion,nuevo,fecha_mod) VALUES( NULL,?,1,datetime('now','localtime'))''', (categoria.getDescripcion(),))        
            conn.commit()
            categoria.setId_categoria(str(c.lastrowid))
                        
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarCategoria(self, categoria):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE categorias SET eliminado = 1,fecha_mod = datetime('now','localtime') WHERE id_categoria = ?''', (categoria.getId_categoria(),))        
            c.execute('''UPDATE procesos SET id_categoria = 1 WHERE id_categoria = ?''', (categoria.getId_categoria(),))        
            c.execute('''UPDATE plantillas SET id_categoria = 1 WHERE id_categoria = ?''', (categoria.getId_categoria(),))        

            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarPlantilla(self, plantilla):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            demandante = "1"
            if demandante != None:
                demandante = plantilla.getDemandante().getId_persona()
            demandado = "1"
            if demandado != None:
                plantilla.getDemandado().getId_persona()
            juzgado = "1"
            if juzgado != None:
                plantilla.getJuzgado().getId_juzgado()
                
            c.execute('''UPDATE plantillas SET nombre=?,''' + '''id_demandante = ?,''' + ''' id_demandado = ?,''' + ''' fecha_creacion = datetime(?),''' + ''' radicado = ?,''' + ''' radicado_unico = ?,''' + ''' estado = ?,''' + ''' tipo = ?,''' + ''' notas = ?,''' + ''' prioridad = ?,''' + ''' id_juzgado = ?,''' + ''' id_categoria = ?,''' + ''' modificado =1, fecha_mod = datetime('now','localtime') WHERE id_plantilla = ?''', (plantilla.getNombre(), demandante, demandado, plantilla.getFecha(), plantilla.getRadicado(), plantilla.getRadicadoUnico(), plantilla.getEstado(), plantilla.getTipo(), plantilla.getNotas(), plantilla.getPrioridad(), juzgado, plantilla.getCategoria().getId_categoria(), plantilla.getId_plantilla()))                                                         
            conn.commit()
                      
        except Exception as e:
            raise e
        finally:
            conn.close()
        campos = plantilla.getCampos()
        for campo in campos:
            self.guardarCampoPersonalizado(campo, plantilla.getId_proceso())

    def guardarPlantilla(self, plantilla):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO plantillas (id_plantilla,nombre,id_demandante,id_demandado,radicado,radicado_unico,estado,tipo,notas,prioridad,id_juzgado,id_categoria,nuevo, fecha_mod) VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,1,datetime('now','localtime'))''', (plantilla.getNombre(), plantilla.getDemandante().getId_persona(), plantilla.getDemandado().getId_persona(), plantilla.getRadicado(), plantilla.getRadicadoUnico(), plantilla.getEstado(), plantilla.getTipo(), plantilla.getNotas(), plantilla.getPrioridad(), plantilla.getJuzgado().getId_juzgado(), plantilla.getCategoria().getId_categoria()))                                                         
            conn.commit()
            plantilla.setId_plantilla(str(c.lastrowid))
        except Exception as e:
            raise e
        finally:
            conn.close()
        
        campos = plantilla.getCampos()
        for campo in campos:
            self.guardarCampoPlantilla(campo, plantilla.getId_plantilla())
        
    def borrarPlantilla(self, plantilla):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE plantillas SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_plantilla = ?''', (plantilla.getId_proceso(),))
            c.execute('''UPDATE atributos_plantilla SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_plantilla = ?''', (plantilla.getId_proceso(),))
            
            conn.commit()
                
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarCampoPlantilla(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_plantilla SET valor = ?, modificado =1,fecha_mod = datetime('now','localtime'),  WHERE id_atributo_plantilla = ?''', (campoPersonalizado.getValor(), campoPersonalizado.getId_campo()))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def guardarCampoPlantilla(self, campoPersonalizado, id_plantilla):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO atributos_plantilla (id_atributo_plantilla, id_atributo, id_plantilla, valor, nuevo, fecha_mod) VALUES( NULL,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getId_atributo(), id_plantilla, campoPersonalizado.getValor()))
            conn.commit()
            campoPersonalizado.setId_campo(str(c.lastrowid))
                        
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarCampoPlantilla(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_plantilla SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo_plantilla = ?''', (campoPersonalizado.getId_campo(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarPreferencia(self, id_preferencia, valor):
        pass
    
    def borrarPreferencia(self, id_preferencia):
      
    
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE preferencias SET valor=20001 WHERE id_preferencia = 10101''')
            c.execute('''UPDATE preferencias SET valor=1 WHERE id_preferencia = 10102''')
            c.execute('''UPDATE preferencias SET valor=0 WHERE id_preferencia =10201''')
            c.execute('''UPDATE preferencias SET valor=1 WHERE id_preferencia = 10301''')
            c.execute('''UPDATE preferencias SET valor= 'Usuario' WHERE id_preferencia = 10401''')
            c.execute('''UPDATE preferencias SET valor=10 WHERE id_preferencia = 10501''')
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
        
    def actualizarAtributoPersona(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            obligatorio = 0
            if(campoPersonalizado.isObligatorio()):
                obligatorio = 1                   
            c.execute('''UPDATE atributosPersona SET nombre = ?,''' + ''' obligatorio = ?,''' + ''' longitud_max = ?,''' + ''' longitud_min = ?,''' + ''' modificado =1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getNombre(), obligatorio, campoPersonalizado.getLongitudMax(), campoPersonalizado.getLongitudMin(), campoPersonalizado.getId_atributo()))                
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def guardarAtributoPersona(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            obligatorio = 0
            if(campoPersonalizado.isObligatorio()):
                obligatorio = 1                   
            c.execute('''INSERT INTO atributosPersona (id_atributo, nombre, obligatorio, longitud_max, longitud_min,nuevo, fecha_mod) VALUES( NULL,?,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getNombre(), obligatorio, campoPersonalizado.getLongitudMax(), campoPersonalizado.getLongitudMin()))                
            conn.commit()     
            campoPersonalizado.setId_atributo(str(c.lastrowid))
            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarAtributoPersona(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributosPersona SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_atributo(),))
            c.execute('''UPDATE atributos_demandante SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_atributo(),))
            c.execute('''UPDATE atributos_demandado SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_atributo(),))
            
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    def actualizarCampoDemandante(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_demandante SET valor = ?, modificado =1,fecha_mod = datetime('now','localtime') WHERE id_atributo_demandante = ?''', (campoPersonalizado.getValor(), campoPersonalizado.getId_campo()))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close    
    def guardarCampoDemandante(self, campoPersonalizado, id_demandante):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO atributos_demandante (id_atributo_demandante, id_atributo, id_demandante, valor, nuevo, fecha_mod) VALUES( NULL,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getId_atributo(), id_demandante, campoPersonalizado.getValor()))
            conn.commit()
            campoPersonalizado.setId_campo(str(c.lastrowid))
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarCampoDemandante(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_demandante SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo_demandante = ?''', (campoPersonalizado.getId_campo(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    
    def actualizarCampoDemandado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_demandado SET valor = ?, modificado =1,fecha_mod = datetime('now','localtime') WHERE id_atributo_demandado = ?''', (campoPersonalizado.getValor(), campoPersonalizado.getId_campo()))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close    
    def guardarCampoDemandado(self, campoPersonalizado, id_demandado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO atributos_demandado (id_atributo_demandado, id_atributo, id_demandado, valor, nuevo, fecha_mod) VALUES( NULL,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getId_atributo(), id_demandado, campoPersonalizado.getValor()))
            conn.commit()     
            campoPersonalizado.setId_campo(str(c.lastrowid))
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarCampoDemandado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_demandado SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo_demandado = ?''', (campoPersonalizado.getId_campo(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    
    def actualizarAtributoJuzgado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            obligatorio = 0
            if(campoPersonalizado.isObligatorio()):
                obligatorio = 1                   
            c.execute('''UPDATE atributosJuzgado SET nombre = ?,''' + ''' obligatorio = ?,''' + ''' longitud_max = ?,''' + ''' longitud_min = ?,''' + ''' modificado =1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getNombre(), obligatorio, campoPersonalizado.getLongitudMax(), campoPersonalizado.getLongitudMin(), campoPersonalizado.getId_atributo()))                
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def guardarAtributoJuzgado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            obligatorio = 0
            if(campoPersonalizado.isObligatorio()):
                obligatorio = 1                   
            c.execute('''INSERT INTO atributosJuzgado (id_atributo, nombre, obligatorio, longitud_max, longitud_min,nuevo, fecha_mod) VALUES( NULL,?,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getNombre(), obligatorio, campoPersonalizado.getLongitudMax(), campoPersonalizado.getLongitudMin()))                
            conn.commit()
            campoPersonalizado.setId_atributo(str(c.lastrowid))
                        
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarAtributoJuzgado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributosJuzgado SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_campo(),))
            c.execute('''UPDATE atributos_juzgado SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_campo(),))
            
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    
    def actualizarCampoJuzgado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_juzgado SET valor = ?, modificado =1,fecha_mod = datetime('now','localtime') WHERE id_atributo_juzgado = ?''', (campoPersonalizado.getValor(), campoPersonalizado.getId_campo()))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close    
    def guardarCampoJuzgado(self, campoPersonalizado, id_juzgado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO atributos_juzgado (id_atributo_juzgado, id_atributo, id_juzgado, valor, nuevo, fecha_mod) VALUES( NULL,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getId_atributo(), id_juzgado, campoPersonalizado.getValor()))
            conn.commit()
            campoPersonalizado.setId_campo(str(c.lastrowid))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarCampoJuzgado(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_juzgado SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo_juzgado = ?''', (campoPersonalizado.getId_campo(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    
    def actualizarAtributoActuacion(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            obligatorio = 0
            if(campoPersonalizado.isObligatorio()):
                obligatorio = 1                   
            c.execute('''UPDATE atributosActuacion SET nombre = ?,''' + ''' obligatorio = ?,''' + ''' longitud_max = ?,''' + ''' longitud_min = ?''' + ''', modificado =1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getNombre(), obligatorio, campoPersonalizado.getLongitudMax(), campoPersonalizado.getLongitudMin(), campoPersonalizado.getId_atributo()))                
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    def guardarAtributoActuacion(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            obligatorio = 0
            if(campoPersonalizado.isObligatorio()):
                obligatorio = 1                   
            c.execute('''INSERT INTO atributosActuacion (id_atributo, nombre, obligatorio, longitud_max, longitud_min,nuevo, fecha_mod) VALUES( NULL,?,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getNombre(), obligatorio, campoPersonalizado.getLongitudMax(), campoPersonalizado.getLongitudMin()))                
            conn.commit()
            campoPersonalizado.setId_atributo(str(c.lastrowid))
          
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarAtributoActuacion(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributosActuacion SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_campo(),))
            c.execute('''UPDATE atributos_actuacion SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo = ?''', (campoPersonalizado.getId_campo(),))
            
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    
    def actualizarCampoActuacion(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_actuacion SET valor = ?, modificado =1,fecha_mod = datetime('now','localtime') WHERE id_atributo_actuacion = ?''', (campoPersonalizado.getValor(), campoPersonalizado.getId_campo()))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close    
    def guardarCampoActuacion(self, campoPersonalizado, id_actuacion):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''INSERT INTO atributos_actuacion (id_atributo_actuacion, id_atributo, id_actuacion, valor, nuevo, fecha_mod) VALUES( NULL,?,?,?,1,datetime('now','localtime'))''', (campoPersonalizado.getId_atributo(), id_actuacion, campoPersonalizado.getValor()))
            conn.commit()
            campoPersonalizado.setId_campo(str(c.lastrowid))
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarCampoActuacion(self, campoPersonalizado):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE atributos_actuacion SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_atributo_actuacion = ?''', (campoPersonalizado.getId_campo(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    
    def actualizarArchivoProceso(self, archivo):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE archivos_proceso SET id_proceso = ?,''' + '''ruta = ?,''' + ''' modificado =1,fecha_mod = datetime('now','localtime') WHERE id_archivo_proceso = ?''', (archivo.getId_proceso(), archivo.getRuta(), archivo.getId_archivo_proceso(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close   
    def guardarArchivoProceso(self, archivo, id_proceso):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()                  
            c.execute('''INSERT INTO archivos_proceso (id_archivo_proceso, id_proceso, ruta,nuevo, fecha_mod) VALUES( NULL,?,?,1,datetime('now','localtime'))''', (archivo.getId_proceso(), archivo.getRuta()))                
            conn.commit()
            archivo.setId_archivo_proceso(str(c.lastrowid))
         
        except Exception as e:
            raise e
        finally:
            conn.close()
    def borrarArchivoProceso(self, archivo):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation())
            c = conn.cursor()
            c.execute('''UPDATE archivo_proceso SET eliminado = 1, fecha_mod = datetime('now','localtime') WHERE id_archivo_proceso = ?''', (archivo.getId_archivo_proceso(),))
            conn.commit()            
        except Exception as e:
            raise e
        finally:
            conn.close()
    
    #Metodos de Cargado
    
    def consultarDemandantes(self):
        demandantes = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE eliminado = 0 ORDER BY nombre''')
            demandantes = []
            for row in c:
                id_demandante = str(row['id_demandante'])
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']            
                correo = row['correo']
                notas = row['notas']
                demandante = Persona(1, cedula, nombre, telefono, direccion, correo, notas, id_demandante)
                demandantes.append(demandante)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for deman_act in demandantes:
            deman_act.setCampos(self.consultarCamposDemandante(deman_act))
            
        return demandantes
    
    def consultarDemandados(self):
        demandados = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE eliminado = 0 ORDER BY nombre''')
            for row in c:
                id_demandado = str(row['id_demandado'])
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']            
                correo = row['correo']
                notas = row['notas']
                demandado = Persona(2, cedula, nombre, telefono, direccion, correo, notas, id_demandado)
                demandados.append(demandado)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for deman_act in demandados:
            deman_act.setCampos(self.consultarCamposDemandado(deman_act))
        return demandados
    
    def consultarPersonas(self):
        personas = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE eliminado = 0 ORDER BY nombre''')
            for row in c:
                id_demandado = str(row['id_demandado'])
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']            
                correo = row['correo']
                notas = row['notas']
                demandado = Persona(2, cedula, nombre, telefono, direccion, correo, notas, id_demandado)
                personas.append(demandado)
            c.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE eliminado = 0 ORDER BY nombre''')
            for row in c:
                id_demandante = str(row['id_demandante'])
                cedula = row['cedula']
                nombre = row['nombre']
                telefono = row['telefono']
                direccion = row['direccion']            
                correo = row['correo']
                notas = row['notas']
                demandante = Persona(1, cedula, nombre, telefono, direccion, correo, notas, id_demandante)
                personas.append(demandante)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for deman_act in personas:
            if deman_act.getTipo() == 1:
                deman_act.setCampos(self.consultarCamposDemandante(deman_act))
            else:
                deman_act.setCampos(self.consultarCamposDemandado(deman_act))
        return personas
            
    def consultarPersona(self, id_persona, tipo):
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            persona = None
            if tipo == 1:
                c.execute('''SELECT id_demandante, cedula, nombre, telefono, direccion, correo, notas FROM demandantes WHERE id_demandante = ?''', (id_persona,))
                row = c.fetchone()
                if row:
                    id_demandante = str(row['id_demandante'])
                    cedula = row['cedula']
                    nombre = row['nombre']
                    telefono = row['telefono']
                    direccion = row['direccion']            
                    correo = row['correo']
                    notas = row['notas']
                    persona = Persona(1, cedula, nombre, telefono, direccion, correo, notas, id_demandante)
            elif tipo == 2:
                c.execute('''SELECT id_demandado, cedula, nombre, telefono, direccion, correo, notas FROM demandados WHERE id_demandado = ?''', (id_persona,))
                row = c.fetchone()
                if row:
                    id_demandado = str(row['id_demandado'])
                    cedula = row['cedula']
                    nombre = row['nombre']
                    telefono = row['telefono']
                    direccion = row['direccion']            
                    correo = row['correo']
                    notas = row['notas']
                    persona = Persona(2, cedula, nombre, telefono, direccion, correo, notas, id_demandado)
            else:
                raise ValueError('El tipo de persona no es correcto')
        except Exception as e:
            raise e
        finally:
            conn.close()
        if tipo == 1:
            persona.setCampos(self.consultarCamposDemandante(persona))
        else:
            persona.setCampos(self.consultarCamposDemandado(persona))
        
        return persona
    
    def consultarProcesos(self):
        procesos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT p.id_proceso, p.id_demandante, p.id_demandado, p.fecha_creacion as "fecha_creacion [timestamp]", p.radicado, p.radicado_unico, p.estado, p.tipo, p.notas, p.prioridad, p.id_juzgado, p.id_categoria FROM procesos p WHERE eliminado = 0''')
            for row in c:
                id_proceso = str(row['id_proceso'])
                id_demandante = str(row['id_demandante'])
                id_demandado = str(row['id_demandado'])
                fecha_creacion = row['fecha_creacion']
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = int(row['prioridad'])
                id_juzgado = str(row['id_juzgado'])
                id_categoria = str(row['id_categoria'])
                demandante = Persona(1, id_persona = id_demandante)
                demandado = Persona(2, id_persona = id_demandado)
                juzgado = Juzgado(id_juzgado = id_juzgado)
                categoria = Categoria(id_categoria = id_categoria)
                proceso = Proceso(demandante = demandante, demandado = demandado, fecha = fecha_creacion, juzgado = juzgado, radicado = radicado, radicadoUnico = radicado_unico, actuaciones = [], estado = estado, categoria = categoria, tipo = tipo, notas = notas, campos = [], prioridad = prioridad, id_proceso = id_proceso)
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT p.id_proceso, p.id_demandante, p.id_demandado, p.fecha_creacion as "fecha_creacion [timestamp]", p.radicado, p.radicado_unico, p.estado, p.tipo, p.notas, p.prioridad, p.id_juzgado, p.id_categoria FROM procesos p WHERE p.id_proceso = ?''', (id_proceso,))
            row = c.fetchone()
            if row:
                id_proceso = str(row['id_proceso'])
                id_demandante = str(row['id_demandante'])
                id_demandado = str(row['id_demandado'])
                fecha_creacion = row['fecha_creacion']
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = int(row['prioridad'])
                id_juzgado = str(row['id_juzgado'])
                id_categoria = str(row['id_categoria'])
                demandante = Persona(1, id_persona = id_demandante)
                demandado = Persona(2, id_persona = id_demandado)
                juzgado = Juzgado(id_juzgado = id_juzgado)
                categoria = Categoria(id_categoria = id_categoria)
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE id_proceso = ? AND eliminado = 0 ORDER BY fecha_creacion, fecha_proxima''', (proceso.getId_proceso(),))
            for row in c:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = row['descripcion']
                uid = row['uid']
                juzgado = Juzgado(id_juzgado = id_juzgado)
                actuacion = Actuacion(juzgado, fecha_creacion, fecha_proxima, descripcion, id_actuacion, uid)
                actuaciones.append(actuacion)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for act in actuaciones:
            act.setJuzgado(self.consultarJuzgado(act.getJuzgado().getId_juzgado()))
            act.setCampos(self.consultarCamposActuacion(act))
        return actuaciones
        
    def consultarActuacion(self, id_actuacion):
        actuacion = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE id_actuacion = ?''', (id_actuacion,))
            row = c.fetchone()
            if row:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = row['descripcion']
                uid = row['uid']
                juzgado = Juzgado(id_juzgado = id_juzgado)
                actuacion = Actuacion(juzgado, fecha_creacion, fecha_proxima, descripcion, id_actuacion, uid)  
        except Exception as e:
            raise e
        finally:
            conn.close()
        actuacion.setCampos(self.consultarCamposActuacion(actuacion))
        return actuacion
    
    def consultarActuacionesCriticas(self, cantidad):
        actuaciones = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_actuacion, id_proceso, id_juzgado, fecha_creacion as "fecha_creacion [timestamp]", fecha_proxima as "fecha_proxima [timestamp]", descripcion, uid FROM actuaciones WHERE fecha_proxima >= date() AND eliminado = 0 ORDER BY fecha_proxima LIMIT ?''', (cantidad,))
            for row in c:
                id_actuacion = str(row['id_actuacion'])
                id_juzgado = str(row['id_juzgado'])
                fecha_creacion = row['fecha_creacion']
                fecha_proxima = row['fecha_proxima']
                descripcion = row['descripcion']
                uid = row['uid']
                juzgado = Juzgado(id_juzgado = id_juzgado)
                actuacion = Actuacion(juzgado, fecha_creacion, fecha_proxima, descripcion, id_actuacion, uid)
                actuaciones.append(actuacion)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for act in actuaciones:
            act.setJuzgado(self.consultarJuzgado(act.getJuzgado().getId_juzgado()))
            act.setCampos(self.consultarCamposActuacion(act))
        return actuaciones
            
    def consultarJuzgados(self):
        juzgados = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE eliminado = 0 ORDER BY nombre''')
            for row in c:
                id_juzgado = str(row['id_juzgado'])
                nombre = row['nombre']
                ciudad = row['ciudad']
                telefono = row['telefono']
                direccion = row['direccion']
                tipo = row['tipo']
                juzgado = Juzgado(nombre, ciudad, direccion, telefono, tipo, id_juzgado)
                juzgados.append(juzgado)
        except Exception as e:
            raise e
        finally:
            conn.close()
        for juz in juzgados:
            juz.setCampos(self.consultarCamposJuzgado(juz))
        return juzgados 
       
    def consultarJuzgado(self, id_juzgado):
        juzgado = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_juzgado, nombre, ciudad, telefono, direccion, tipo FROM juzgados WHERE id_juzgado = ?''', (id_juzgado,))
            row = c.fetchone()
            if row:
                id_juzgado = str(row['id_juzgado'])
                nombre = row['nombre']
                ciudad = row['ciudad']
                telefono = row['telefono']
                direccion = row['direccion']
                tipo = row['tipo']
                juzgado = Juzgado(nombre, ciudad, direccion, telefono, tipo, id_juzgado)            
        except Exception as e:
            raise e
        finally:
            conn.close()
        juzgado.setCampos(self.consultarCamposJuzgado(juzgado))
        return juzgado
        
    def consultarCategoria(self, id_categoria):
        categoria = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_categoria, descripcion FROM categorias WHERE id_categoria = ?''', (id_categoria,))
            row = c.fetchone()
            if row:
                id_categoria = str(row['id_categoria'])
                descripcion = row['descripcion']
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_categoria, descripcion FROM categorias WHERE eliminado = 0 ORDER BY descripcion''')
            for row in c:
                id_categoria = str(row['id_categoria'])
                descripcion = row['descripcion']
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_proceso, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_proceso at, atributos a WHERE at.id_atributo = a.id_atributo AND at.id_proceso = ? AND at.eliminado = 0''', (proceso.getId_proceso(),))
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
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
        atributos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_atributo, nombre,obligatorio,longitud_max, longitud_min FROM  atributos WHERE eliminado = 0''')
            for row in c:
                id_atributo = str(row['id_atributo'])
                nombre = row['nombre']
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False 
                campo = CampoPersonalizado(id_atributo = id_atributo, nombre = nombre, obligatorio = obligatorio, longitudMax = longitud_max, longitudMin = longitud_min)    
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT p.id_plantilla, p.id_demandante, p.id_demandado, p.radicado, p.radicado_unico, p.estado, p.tipo, p.notas, p.prioridad, p.id_juzgado, p.id_categoria, p.nombre FROM plantillas p WHERE eliminado = 0''')
            for row in c:
                id_plantilla = str(row['id_plantilla'])
                id_demandante = str(row['id_demandante'])
                id_demandado = str(row['id_demandado'])
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = int(row['prioridad'])
                id_juzgado = str(row['id_juzgado'])
                id_categoria = str(row['id_categoria'])
                nombre = row['nombre']
                demandante = Persona(1, id_persona = id_demandante)
                demandado = Persona(2, id_persona = id_demandado)
                juzgado = Juzgado(id_juzgado = id_juzgado)
                categoria = Categoria(id_categoria = id_categoria)
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT p.id_plantilla, p.id_demandante, p.id_demandado, p.radicado, p.radicado_unico, p.estado, p.tipo, p.notas, p.prioridad, p.id_juzgado, p.id_categoria, p.nombre FROM plantillas p WHERE p.id_plantilla = ?''', (id_plantilla,))
            row = c.fetchone()
            if row:
                id_plantilla = str(row['id_plantilla'])
                id_demandante = str(row['id_demandante'])
                id_demandado = str(row['id_demandado'])
                radicado = row['radicado']
                radicado_unico = row['radicado_unico']
                estado = row['estado']
                tipo = row['tipo']
                notas = row['notas']
                prioridad = int(row['prioridad'])
                id_juzgado = str(row['id_juzgado'])
                id_categoria = str(row['id_categoria'])
                nombre = row['nombre']
                demandante = Persona(1, id_persona = id_demandante)
                demandado = Persona(2, id_persona = id_demandado)
                juzgado = Juzgado(id_juzgado = id_juzgado)
                categoria = Categoria(id_categoria = id_categoria)
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_plantilla, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_plantilla at, atributos a WHERE at.id_atributo = a.id_atributo AND at.id_plantilla = ? AND at.eliminado = 0''', (plantilla.getId_plantilla(),))
            for row in c:
                id_atributo_plantilla = str(row['id_atributo_plantilla'])
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
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_plantilla, id_atributo)
                campos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campos
    
    def consultarCampoPlantilla(self, id_campo):
        campo = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_plantilla, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_plantilla at, atributos a WHERE at.id_atributo = a.id_atributo AND at.id_atributo_plantilla = ?''', (id_campo,))
            row = c.fetchone()
            if row:
                id_atributo_plantilla = str(row['id_atributo_plantilla'])
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_atributo, nombre,obligatorio,longitud_max, longitud_min FROM  atributosPersona WHERE eliminado = 0''')
            for row in c:
                id_atributo = str(row['id_atributo'])
                nombre = row['nombre']
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False 
                campo = CampoPersonalizado(id_atributo = id_atributo, nombre = nombre, obligatorio = obligatorio, longitudMax = longitud_max, longitudMin = longitud_min)    
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_demandante, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_demandante at, atributosPersona a WHERE at.id_atributo = a.id_atributo AND at.id_demandante = ? AND at.eliminado = 0''', (demandante.getId_persona(),))
            for row in c:
                id_atributo_demandante = str(row['id_atributo_demandante'])
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
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_demandante, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_demandante at, atributosPersona a WHERE at.id_atributo = a.id_atributo AND at.id_atributo_demandante = ?''', (id_campo,))
            row = c.fetchone()
            if row:
                id_atributo_demandante = str(row['id_atributo_demandante'])
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
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_demandante, id_atributo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campo
    
    #Cargar los campos personalizados de un demandado
    def consultarCamposDemandado(self, demandado):
        campos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_demandado, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_demandado at, atributosPersona a WHERE at.id_atributo = a.id_atributo AND at.id_demandado = ? AND at.eliminado = 0''', (demandado.getId_persona(),))
            for row in c:
                id_atributo_demandado = str(row['id_atributo_demandado'])
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
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_demandado, id_atributo)
                campos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campos    
    
    #Cargar un campo personalizado de demandado especifico
    def consultarCampoDemandado(self, id_campo):
        campo = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_demandado, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_demandado at, atributosPersona a WHERE at.id_atributo = a.id_atributo AND at.id_atributo_demandado = ?''', (id_campo,))
            row = c.fetchone()
            if row:
                id_atributo_demandado = str(row['id_atributo_demandado'])
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
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_demandado, id_atributo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campo
    
    def consultarAtributosJuzgado(self):
        atributos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_atributo, nombre,obligatorio,longitud_max, longitud_min FROM  atributosJuzgado WHERE eliminado = 0''')
            for row in c:
                id_atributo = str(row['id_atributo'])
                nombre = row['nombre']
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False 
                campo = CampoPersonalizado(id_atributo = id_atributo, nombre = nombre, obligatorio = obligatorio, longitudMax = longitud_max, longitudMin = longitud_min)    
                atributos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return atributos

    #Cargar los campos personalizados de un juzgado
    def consultarCamposJuzgado(self, juzgado):
        campos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_juzgado, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_juzgado at, atributosJuzgado a WHERE at.id_atributo = a.id_atributo AND at.id_juzgado = ? AND at.eliminado = 0''', (juzgado.getId_juzgado(),))
            for row in c:
                id_atributo_juzgado = str(row['id_atributo_juzgado'])
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
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_juzgado, id_atributo)
                campos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campos    
    
    #Cargar un campo personalizado de juzgado especifico
    def consultarCampoJuzgado(self, id_campo):
        campo = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_juzgado, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_juzgado at, atributosJuzgado a WHERE at.id_atributo = a.id_atributo AND at.id_atributo_juzgado = ?''', (id_campo,))
            row = c.fetchone()
            if row:
                id_atributo_juzgado = str(row['id_atributo_juzgado'])
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
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_juzgado, id_atributo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campo

    def consultarAtributosActuacion(self):
        atributos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_atributo, nombre,obligatorio,longitud_max, longitud_min FROM  atributosActuacion WHERE eliminado = 0''')
            for row in c:
                id_atributo = str(row['id_atributo'])
                nombre = row['nombre']
                ob = row['obligatorio']
                longitud_max = row['longitud_max']
                longitud_min = row['longitud_min']
                #Pasar el obligatorio a Boolean:
                if ob == 1:
                    obligatorio = True
                else:
                    obligatorio = False 
                campo = CampoPersonalizado(id_atributo = id_atributo, nombre = nombre, obligatorio = obligatorio, longitudMax = longitud_max, longitudMin = longitud_min)    
                atributos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return atributos   

    #Cargar los campos personalizados de un actuacion
    def consultarCamposActuacion(self, actuacion):
        campos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_actuacion, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_actuacion at, atributosActuacion a WHERE at.id_atributo = a.id_atributo AND at.id_actuacion = ? AND at.eliminado = 0''', (actuacion.getId_actuacion(),))
            for row in c:
                id_atributo_actuacion = str(row['id_atributo_actuacion'])
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
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_actuacion, id_atributo)
                campos.append(campo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campos    
    
    #Cargar un campo personalizado de actuacion especifico
    def consultarCampoActuacion(self, id_campo):
        campo = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT at.id_atributo_actuacion, at.id_atributo, at.valor, a.nombre,a.obligatorio,a.longitud_max, a.longitud_min FROM atributos_actuacion at, atributosActuacion a WHERE at.id_atributo = a.id_atributo AND at.id_atributo_actuacion = ?''', (id_campo,))
            row = c.fetchone()
            if row:
                id_atributo_actuacion = str(row['id_atributo_actuacion'])
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
                campo = CampoPersonalizado(nombre, valor, obligatorio, longitud_max, longitud_min, id_atributo_actuacion, id_atributo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return campo
    
    def consultarArchivosProceso(self, proceso):
        archivos = []
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_archivo_proceso, ruta FROM archivos_proceso WHERE id_proceso = ? AND eliminado = 0''', (proceso.getId_proceso(),))
            for row in c:
                id_archivo_proceso = str(row['id_archivo_proceso'])
                ruta_proceso = row['ruta']
                archivo = Archivo(ruta = ruta_proceso, id_archivo = id_archivo_proceso)
                archivos.append(archivo)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return archivos
    
    def consultarArchivo(self, id_archivo_proceso):
        archivo = None
        try:
            self.__conMgr.prepararBD()
            conn = sqlite3.connect(self.__conMgr.getDbLocation(), detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('''SELECT id_archivo_proceso, ruta FROM archivos_proceso WHERE id_archivo_proceso = ? AND eliminado = 0''', (id_archivo_proceso,))
            row = c.fetchone()
            if row:
                id_archivo_proceso = str(row['id_archivo_proceso'])
                ruta_proceso = row['ruta']
                archivo = Archivo(ruta = ruta_proceso, id_archivo = id_archivo_proceso)
        except Exception as e:
            raise e
        finally:
            conn.close()
        return archivo
