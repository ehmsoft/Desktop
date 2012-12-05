# -*- coding: utf-8 -*-
'''
Created on 05/12/2012

@author: elfotografo007
'''
import unittest
from core.Persona import Persona
from core.CampoPersonalizado import CampoPersonalizado

class PersonaTest(unittest.TestCase):
    '''
    Clase para correr pruebas unitarias sobre la clase Persona
    '''
    def setUp(self):
        self.demandante = Persona(tipo=1, id="1088279267", nombre="Andres", telefono="3168746839", direccion="Calle", correo="elfotografo007@gmail.com", notas="Esto es una nota")
        self.demandado = Persona(tipo=2, id="1088286673", nombre="Sara", telefono="3117607783", direccion="Barrio", correo="saris021@hotmail.com", notas="Esto es una nota")
        
    def testPersonasDiferentes(self):
        self.assertNotEqual(self.demandante, self.demandado, "El demandante y el demandado deben ser diferentes")
        
    def testGetNombre(self):
        self.assertEqual(self.demandante.getNombre(), "Andres", "El nombre del demandante debe ser Andres")
        self.assertEqual(self.demandado.getNombre(), "Sara", "El nombre del demandado deber ser Sara")
        
    def testGetId(self):
        self.assertEqual(self.demandante.getId(), "1088279267", u"La cédula del demandante debe ser 1088279267")
        self.assertEqual(self.demandado.getId(), "1088286673", u"La cédula del demandado deber ser 1088286673")
        
    def testGetTelefono(self):
        self.assertEqual(self.demandante.getTelefono(), "3168746839", u"El teléfono del demandante debe ser 3168746839")
        self.assertEqual(self.demandado.getTelefono(), "3117607783", "El teléfono del demandado deber ser 3117607783")
    
    def testGetDireccion(self):
        self.assertEqual(self.demandante.getDireccion(), "Calle", u"La dirección del demandante debe ser Calle")
        self.assertEqual(self.demandado.getDireccion(), "Barrio", u"La dirección del demandado deber ser Barrio")
        
    def testGetCorreos(self):
        self.assertEqual(self.demandante.getCorreo(), "elfotografo007@gmail.com", u"El correo del demandante debe ser elfotografo007@gmail.com")
        self.assertEqual(self.demandado.getCorreo(), "saris021@hotmail.com", u"El correo del demandado deber ser saris021@hotmail.com")
        
    def testGetNotas(self):
        self.assertEqual(self.demandante.getNotas(), "Esto es una nota", u"Las notas del demandante debe ser Esto es una nota")
        self.assertEqual(self.demandado.getNotas(), "Esto es una nota", u"Las notas del demandado deber ser Esto es una nota")
    
    def testGetId_persona(self):
        self.assertIsNone(self.demandante.getId_persona(), "El id_persona del demandante debe ser None")
        self.assertIsNone(self.demandado.getId_persona(), "El id_persona del demandado debe ser None")
        
    def testAgregarCampo(self):
        campo = CampoPersonalizado(nombre="cumpleanos", valor="10")
        self.demandante.addCampo(campo)
        self.demandado.addCampo(campo)
        self.assertListEqual(self.demandante.getCampos(), self.demandado.getCampos(), "Se debe devolver una lista con el campo personalizado cumpleanos")
        
    def testSetCampos(self):
        self.assertRaises(TypeError, self.demandante.setCampos, None)
        self.assertRaises(TypeError, self.demandado.setCampos, None)
        
if __name__ == "__main__":
    unittest.main()