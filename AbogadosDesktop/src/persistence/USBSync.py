'''
Created on 29/02/2012

@author: harold
'''

import os
import sys
import shutil
import hashlib

#El modulo realiza la copia por defecto desde /databases/ehmSoft/databases.ehm hacia 
#la carpeta en la que se ejecuta el modulo/databaseMobile.ehm

class USBSync(object):
    def __init__(self, remoto = 'databases/ehmSoft', archivo = 'database.ehm', archivoTemp = 'databaseMobile.ehm', local = os.getcwd()):
        self.path = ''
        self.dirRemoto = remoto
        self.archivo = archivo
        self.archivoTemp = archivoTemp
        self.dirEncontrado = ''
        self.dirLocal = local
        self.os = sys.platform.lower()
        
    def getLocalMobilePath(self):
        if len(self.dirEncontrado) is 0:
            self.traer()
        return self.dirEncontrado
    
    def traer(self):
        arbol = self.__getNodos()
        if arbol is None or len(arbol) is 0:
            raise NoDeviceError
        else:
            for nodo in arbol:
                origen = os.path.join(self.path, nodo, self.dirRemoto, self.archivo)
                if os.path.isfile(origen):
                    destino = os.path.join(self.dirLocal, self.archivoTemp)
                    if self.__copiar(origen, destino):
                        self.dirEncontrado = origen
                        break
                    else:
                        raise IOError('Error al copiar')
    
    def llevar(self):
        if len(self.dirEncontrado) is not 0:
            destino = self.dirEncontrado
            origen = os.path.join(self.dirLocal, self.archivoTemp)
            if os.path.isdir(destino) and os.path.isfile(origen):
                self.copiar(origen, destino)
                os.remove(origen)
        else:
            arbol = self.__getNodos()
            if arbol is None or len(arbol) is 0:
                raise NoDeviceError
            else:
                for nodo in arbol:
                    temp = os.path.join(self.path, nodo, self.dirRemoto)
                    if os.path.isdir(temp):
                        origen = os.path.join(self.dirLocal, self.archivoTemp)
                        destino = os.path.join(temp, self.archivo)
                        if os.path.isfile(origen):
                            if self.__copiar(origen, destino):
                                self.dirEncontrado = temp
                                os.remove(origen)
                                break
                            else:
                                raise IOError('Error al copiar')
                        else:
                            raise IOError('Archivo origen no existe')

    def __getNodos(self):
        if self.os == 'darwin':
            self.path = '/Volumes'
            return os.listdir(self.path)
        elif self.os == 'win32':
            unidades = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            activas = []
            for u in unidades:
                if os.path.isdir('%s:' % u):
                    activas.append('%s:' % u)
            return activas
        elif 'linux' in self.os:
            self.path = '/media'
            return os.listdir(self.path)
                            
    def __copiar(self, origen, destino):
        hashOrigen = self.__hashfile(open(origen))
        intentos = 0
        while intentos < 5:
            shutil.copy(origen, destino)
            hashDestino = self.__hashfile(open(destino))
            if hashDestino == hashOrigen:
                return True
            else:
                intentos += 1
        if intentos >= 5:
            return False
                            
    def __hashfile(self, afile, blocksize = 65536):
        hasher = hashlib.md5()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        return hasher.hexdigest()
    
class NoDeviceError(Exception):
    def __init__(self):
        self.valor = 'No se encuentra ningun dispositivo montado'
        
    def __str__(self):
        return 'Error %s' % str(self.valor)