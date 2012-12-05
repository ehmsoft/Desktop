# -*- coding: utf-8 -*-
'''
Created on 05/12/2012

@author: elfotografo007
'''
import unittest
from core.Actuacion import Actuacion
from datetime import datetime
from core.CampoPersonalizado import CampoPersonalizado
from core.Juzgado import Juzgado
class ActuacionTest(unittest.TestCase):
    '''
    Clase para correr pruebas unitarias sobre la clase Actuacion
    '''
    def setUp(self):
        self.juzgado = Juzgado(nombre="Juzgado Primero", ciudad="Pereira", direccion="Palacio", telefono="33333", tipo="Penal")
        self.fecha = datetime.now()
        self.fechaProxima = datetime.now()
        campo = CampoPersonalizado(nombre="cumpleanos", valor="10")
        self.actuacion = Actuacion(juzgado=self.juzgado, fecha=self.fecha, fechaProxima=self.fechaProxima, descripcion="Audiencia")
        self.actuacionCampos = Actuacion(juzgado=self.juzgado, fecha=self.fecha, fechaProxima=self.fechaProxima, descripcion="Audiencia", campos=[campo])
        
    def testActuacionesDiferentes(self):
        self.assertNotEqual(self.actuacion, self.actuacionCampos, u"Las actuaciones deben ser diferentes")
    
    def testGetJuzgado(self):
        self.assertEqual(self.actuacion.getJuzgado(), self.juzgado, "El juzgado no coincide")
        
    def testGetFecha(self):
        self.assertEqual(self.actuacion.getFecha(), self.fecha, "La fecha no coincide")
        self.assertEqual(self.actuacion.getFechaProxima(), self.fechaProxima, "La fecha Proxima no coincide")
        
    def testGetDescripcion(self):
        self.assertEqual(self.actuacion.getDescripcion(), "Audiencia", u"La actuacion debe tener como descripción Audiencia")
        
    def testGetId_actuacion(self):
        self.assertIsNone(self.actuacion.getId_actuacion(), u"El id_actuacion deber ser None")
        
    def testAgregarCampo(self):
        campo = CampoPersonalizado("nombre juez", "10")
        self.actuacion.addCampo(campo)
        self.assertEqual(self.actuacion.getCampos()[0], campo, "el campo que fue agregado no coincide")
 
    def testSetCampos(self):
        self.assertRaises(TypeError, self.actuacionCampos.setCampos, None, "No debe dejar hacer setCampos si no es una lista")

if __name__ == "__main__":
    unittest.main()