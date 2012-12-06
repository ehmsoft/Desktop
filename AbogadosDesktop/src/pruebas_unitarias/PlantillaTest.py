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
from core.Plantilla import Plantilla
from core.Categoria import Categoria
import copy

class PlantillaTest(unittest.TestCase):
    '''
    Clase para correr pruebas unitarias sobre la clase plantilla
    '''
    def setUp(self):
        self.juzgado = Juzgado(nombre="Juzgado Primero", ciudad="Pereira", direccion="Palacio", telefono="33333", tipo="Penal")
        self.campo = CampoPersonalizado(nombre="cumpleanos", valor="10")
        self.demandante = Persona(tipo=1, id="1088279267", nombre="Andres", telefono="3168746839", direccion="Calle", correo="elfotografo007@gmail.com", notas="Esto es una nota")
        self.demandado = Persona(tipo=2, id="1088286673", nombre="Sara", telefono="3117607783", direccion="Barrio", correo="saris021@hotmail.com", notas="Esto es una nota")
        self.categoria = Categoria(descripcion="Privado")
        self.plantilla = Plantilla(nombre="Plantilla1", demandante=self.demandante, demandado=self.demandado, juzgado=self.juzgado, radicado="123", radicadoUnico="1234", estado="Nuevo", categoria=self.categoria, tipo="Penal", notas="Esto es una nota", prioridad=0, campos=[self.campo])
        self.plantilla2 = copy.deepcopy(self.plantilla)
        self.plantilla2.addCampo(CampoPersonalizado(nombre="Juez", valor="10"))
    
    def testPlantillasDiferentes(self):
        self.assertNotEqual(self.plantilla, self.plantilla2, u"Las plantillas deben ser diferentes")
        
    def testGetNombre(self):
        self.assertEqual(self.plantilla.getNombre(), "Plantilla1", u"El nombre de la plantilla debe ser Plantilla1")
    
    def testGetJuzgado(self):
        self.assertEqual(self.plantilla.getJuzgado(), self.juzgado, "El juzgado no coincide")
        
    def testPersonasDiferentes(self):
        self.assertNotEqual(self.plantilla.getDemandante(), self.plantilla.getDemandado(), "El demandante y el demandado deben ser diferentes")
        
    def testDemandante(self):
        self.assertEqual(self.plantilla.getDemandante(), self.demandante, "El demandante no coincide")
        
    def testDemandado(self):
        self.assertEqual(self.plantilla.getDemandado(), self.demandado, "El demandado no coincide")
        
    def testGetNombreJuzgado(self):
        self.assertEqual(self.plantilla.getJuzgado().getNombre(), "Juzgado Primero", "El nombre del juzgado debe ser Juzgado Primero")
        
    def testGetCategoria(self):
        self.assertEqual(self.plantilla.getCategoria(), self.categoria, u"La categoría no coincide")
    
    def testGetRadicados(self):
        self.assertEqual(self.plantilla.getRadicado(), "123", u"El radicado no coincide")
        self.assertEqual(self.plantilla.getRadicadoUnico(), "1234", u"El radicado único no coincide")
        
    def testGetNotas(self):
        self.assertEqual(self.plantilla.getNotas(), "Esto es una nota", u"Las notas deben ser Esto es una nota")
        
    def testGetEstado(self):
        self.assertEqual(self.plantilla.getEstado(), "Nuevo", u"El estado del plantilla debe ser nuevo")
        
    def testGetTipo(self):
        self.assertEqual(self.plantilla.getTipo(), "Penal", u"El tipo debe ser penal")
        
    def testGetId_plantilla(self):
        self.assertIsNone(self.plantilla.getId_plantilla(), u"El id_plantilla deber ser None")
        
    def testAgregarCampo(self):
        campo = CampoPersonalizado("nombre juez", "10")
        self.plantilla.addCampo(campo)
        self.assertEqual(self.plantilla.getCampos()[0], self.campo, "el campo que fue agregado no coincide")
        self.assertEqual(self.plantilla.getCampos()[1], campo, "el campo que fue agregado no coincide")
 
    def testSetCampos(self):
        self.assertRaises(TypeError, self.plantilla.setCampos, None, "No debe dejar hacer setCampos si no es una lista")

if __name__ == "__main__":
    unittest.main()