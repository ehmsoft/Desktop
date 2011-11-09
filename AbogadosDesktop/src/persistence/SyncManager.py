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
            
            
            
            connMovil.commit()
            connLocal.commit()            
        except Exception as e:
            raise e
        finally:
            connLocal.close()
            connMovil.close()
       
        
        