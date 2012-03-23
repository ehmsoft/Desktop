'''
Created on 22/03/2012

@author: elfotografo007
'''
import csv
from persistence.Persistence import Persistence
from core.Proceso import Proceso
from core.Juzgado import Juzgado
from core.Persona import Persona
from core.Actuacion import Actuacion

def exportarProcesosCSV(archivo, tab=False):
    if tab:
        writer = csv.writer(open(archivo,'wb'), dialect='excel-tab')
    else:
        writer = csv.writer(open(archivo,'wb'), dialect='excel')
    procesos = Persistence().consultarProcesos()
    writer.writerow(Proceso.getHeaders())
    csvProcesos = [proceso.toCSV() for proceso in procesos]
    writer.writerows(csvProcesos)
        
def exportarJuzgadosCSV(archivo, tab=False):
    if tab:
        writer = csv.writer(open(archivo,'wb'), dialect='excel-tab')
    else:
        writer = csv.writer(open(archivo,'wb'), dialect='excel')
    juzgados = Persistence().consultarJuzgados()
    writer.writerow(Juzgado.getHeaders())
    csvJuzgados = [juzgado.toCSV() for juzgado in juzgados]
    writer.writerows(csvJuzgados)

def exportarDemandantesCSV(archivo, tab=False):
    if tab:
        writer = csv.writer(open(archivo,'wb'), dialect='excel-tab')
    else:
        writer = csv.writer(open(archivo,'wb'), dialect='excel')
    demandantes = Persistence().consultarDemandantes()
    writer.writerow(Persona.getHeaders())
    csvDemandantes = [demandante.toCSV() for demandante in demandantes]
    writer.writerows(csvDemandantes)

def exportarDemandadosCSV(archivo, tab=False):
    if tab:
        writer = csv.writer(open(archivo,'wb'), dialect='excel-tab')
    else:
        writer = csv.writer(open(archivo,'wb'), dialect='excel')
    demandados = Persistence().consultarDemandados()
    writer.writerow(Persona.getHeaders())
    csvDemandados = [demandante.toCSV() for demandante in demandados]
    writer.writerows(csvDemandados)
    
def exportarActuacionesCSV(archivo, proceso, tab=False):
    if tab:
        writer = csv.writer(open(archivo,'wb'), dialect='excel-tab')
    else:
        writer = csv.writer(open(archivo,'wb'), dialect='excel')
    if not isinstance(proceso, Proceso):
        proceso = Persistence().consultarProceso(proceso)
    actuaciones = proceso.getActuaciones()
    writer.writerow(Actuacion.getHeaders())
    csvActuaciones = [actuacion.toCSV() for actuacion in actuaciones]
    writer.writerows(csvActuaciones)
    
def exportarActuacionesCriticasCSV(archivo, cantidadActuaciones, tab=False):
    if tab:
        writer = csv.writer(open(archivo,'wb'), dialect='excel-tab')
    else:
        writer = csv.writer(open(archivo,'wb'), dialect='excel')
    actuaciones = Persistence().consultarActuacionesCriticas(cantidadActuaciones)
    writer.writerow(Actuacion.getHeaders())
    csvActuaciones = [actuacion.toCSV() for actuacion in actuaciones]
    writer.writerows(csvActuaciones)

    
        