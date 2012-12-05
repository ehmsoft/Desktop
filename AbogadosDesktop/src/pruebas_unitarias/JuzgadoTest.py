# -*- coding: utf-8 -*-
'''
Created on 05/12/2012

@author: elfotografo007
'''
import unittest
from core.Juzgado import Juzgado
from core.CampoPersonalizado import CampoPersonalizado

class JuzgadoTest(unittest.TestCase):
    '''
    Clase para correr pruebas unitarias sobre la clase Juzgado
    '''
    def setUp(self):
        campo = CampoPersonalizado(nombre="cumpleanos", valor="10")
        self.juzgado = Juzgado(nombre="Juzgado Primero", ciudad="Pereira", direccion="Palacio", telefono="33333", tipo="Penal")
        self.juzgadoCampos = Juzgado(nombre="Juzgado Primero", ciudad="Pereira", direccion="Palacio", telefono="33333", tipo="Penal", campos=[campo])
        
    def testJuzgadosDiferentes(self):
        self.assertNotEqual(self.juzgado, self.juzgadoCampos, "Los juzgados deben ser diferentes")
        
    def testGetNombre(self):
        self.assertEqual(self.juzgado.getNombre(), "Juzgado Primero", "El nombre del juzgado debe ser Juzgado Primero")
    
    def testGetCiudad(self):
        self.assertEqual(self.juzgado.getCiudad(), "Pereira", "La ciudad del juzgado debe ser Pereira")
    
    def testGetTelefono(self):
        self.assertEqual(self.juzgado.getTelefono(), "33333", u"El teléfono del juzgado debe ser 33333")
    
    def testGetDireccion(self):
        self.assertEqual(self.juzgado.getDireccion(), "Palacio", u"La dirección del juzgado debe ser Palacio")

    def testGetTipo(self):
        self.assertEqual(self.juzgado.getTipo(), "Penal", "El tipo del juzgado debe ser Penal")
        
    def testAgregarCampo(self):
        campo = CampoPersonalizado("nombre juez", "10")
        self.juzgado.addCampo(campo)
        self.assertEqual(self.juzgado.getCampos()[0], campo, "el campo que fue agregado no coincide")
 
    def testSetCampos(self):
        self.assertRaises(TypeError, self.juzgado.setCampos, None, "No debe dejar hacer setCampos si no es una lista")

        
if __name__ == "__main__":
    unittest.main()