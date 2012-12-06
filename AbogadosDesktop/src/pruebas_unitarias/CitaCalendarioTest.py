# -*- coding: utf-8 -*-
'''
Created on 06/12/2012

@author: elfotografo007
'''
import unittest
from core.CitaCalendario import CitaCalendario
from datetime import datetime

class CitaCalendarioTest(unittest.TestCase):
    '''
    Clase para correr pruebas unitarias sobre la clase CitaCalendario
    '''
    def setUp(self):
        self.fecha = datetime.today()
        self.cita = CitaCalendario(fecha=self.fecha, anticipacion=0, descripcion="Audiencia")
        
    def testCitasDiferentes(self):
        self.assertNotEqual(self.cita, CitaCalendario(fecha=datetime.today(), anticipacion=0, descripcion="Audiencia"), u"Las citas deben ser diferentes")
        
    def testGetDescripcion(self):
        self.assertEqual(self.cita.getDescripcion(), "Audiencia", u"La cita debe tener como descripción Audiencia")
        
    def testGetId_Categoria(self):
        self.assertIsNone(self.cita.getId_cita(), u"El id_cita debe ser None")

if __name__ == "__main__":
    unittest.main()