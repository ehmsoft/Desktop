# -*- coding: utf-8 -*-
'''
Created on 06/12/2012

@author: elfotografo007
'''
import unittest
from core.Actuacion import Actuacion
from datetime import datetime
from core.CampoPersonalizado import CampoPersonalizado
from core.Juzgado import Juzgado
from core.Persona import Persona
from core.Proceso import Proceso
from core.Categoria import Categoria
import copy

class ProcesoTest(unittest.TestCase):
    '''
    Clase para correr pruebas unitarias sobre la clase Proceso
    '''
    def setUp(self):
        self.juzgado = Juzgado(nombre="Juzgado Primero", ciudad="Pereira", direccion="Palacio", telefono="33333", tipo="Penal")
        self.fecha = datetime.now()
        self.fechaProxima = datetime.now()
        self.campo = CampoPersonalizado(nombre="cumpleanos", valor="10")
        self.demandante = Persona(tipo=1, id="1088279267", nombre="Andres", telefono="3168746839", direccion="Calle", correo="elfotografo007@gmail.com", notas="Esto es una nota")
        self.demandado = Persona(tipo=2, id="1088286673", nombre="Sara", telefono="3117607783", direccion="Barrio", correo="saris021@hotmail.com", notas="Esto es una nota")
        self.actuacion = Actuacion(juzgado=self.juzgado, fecha=self.fecha, fechaProxima=self.fechaProxima, descripcion="Audiencia")
        self.actuacionCampos = Actuacion(juzgado=self.juzgado, fecha=self.fecha, fechaProxima=self.fechaProxima, descripcion="Audiencia", campos=[self.campo])
        self.categoria = Categoria(descripcion="Privado")
        self.proceso = Proceso(demandante=self.demandante, demandado=self.demandado, fecha=self.fecha, juzgado=self.juzgado, radicado="123", radicadoUnico="1234", actuaciones=[self.actuacion], estado="Nuevo", categoria=self.categoria, tipo="Penal", notas="Esto es una nota", prioridad=0, campos=[self.campo])
        self.proceso2 = copy.deepcopy(self.proceso)
        self.proceso2.addActuacion(self.actuacionCampos)
    
    def testProcesosDiferentes(self):
        self.assertNotEqual(self.proceso, self.proceso2, u"Los procesos deben ser diferentes")
    
    def testGetJuzgado(self):
        self.assertEqual(self.proceso.getJuzgado(), self.juzgado, "El juzgado no coincide")
        
    def testGetFecha(self):
        self.assertEqual(self.proceso.getFecha(), self.fecha, "La fecha no coincide")
        
    def testPersonasDiferentes(self):
        self.assertNotEqual(self.proceso.getDemandante(), self.proceso.getDemandado(), "El demandante y el demandado deben ser diferentes")
        
    def testDemandante(self):
        self.assertEqual(self.proceso.getDemandante(), self.demandante, "El demandante no coincide")
        
    def testDemandado(self):
        self.assertEqual(self.proceso.getDemandado(), self.demandado, "El demandado no coincide")
        
    def testGetNombreJuzgado(self):
        self.assertEqual(self.proceso.getJuzgado().getNombre(), "Juzgado Primero", "El nombre del juzgado debe ser Juzgado Primero")
        
    def testGetCategoria(self):
        self.assertEqual(self.proceso.getCategoria(), self.categoria, u"La categoría no coincide")
    
    def testGetRadicados(self):
        self.assertEqual(self.proceso.getRadicado(), "123", u"El radicado no coincide")
        self.assertEqual(self.proceso.getRadicadoUnico(), "1234", u"El radicado único no coincide")
        
    def testGetNotas(self):
        self.assertEqual(self.proceso.getNotas(), "Esto es una nota", u"Las notas deben ser Esto es una nota")
        
    def testGetEstado(self):
        self.assertEqual(self.proceso.getEstado(), "Nuevo", u"El estado del proceso debe ser nuevo")
        
    def testGetTipo(self):
        self.assertEqual(self.proceso.getTipo(), "Penal", u"El tipo debe ser penal")
        
    def testGetId_proceso(self):
        self.assertIsNone(self.proceso.getId_proceso(), u"El id_proceso deber ser None")
        
    def testGetActuaciones(self):
        self.assertEqual(self.proceso.getActuaciones()[0], self.actuacion, "La actuacion no coincide")
        
    def testAgregarCampo(self):
        campo = CampoPersonalizado("nombre juez", "10")
        self.proceso.addCampo(campo)
        self.assertEqual(self.proceso.getCampos()[0], self.campo, "el campo que fue agregado no coincide")
        self.assertEqual(self.proceso.getCampos()[1], campo, "el campo que fue agregado no coincide")
 
    def testSetCampos(self):
        self.assertRaises(TypeError, self.proceso.setCampos, None, "No debe dejar hacer setCampos si no es una lista")

if __name__ == "__main__":
    unittest.main()