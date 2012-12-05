# -*- coding: utf-8 -*-
'''
Created on 05/12/2012

@author: elfotografo007
'''
import unittest
from core.Categoria import Categoria

class CategoriaTest(unittest.TestCase):
    '''
    Clase para correr pruebas unitarias sobre la clase Categoria
    '''
    def setUp(self):
        self.categoria = Categoria(descripcion="Privado")
        
    def testCategoriasDiferentes(self):
        self.assertNotEqual(self.categoria, Categoria(descripcion="Particular"), u"Las categorías deben ser diferentes")
        
    def testGetDescripcion(self):
        self.assertEqual(self.categoria.getDescripcion(), "Privado", u"La categoría debe tener como descripción Privado")
        
    def testGetId_Categoria(self):
        self.assertIsNone(self.categoria.getId_categoria(), u"El id_categoria deber ser None")

if __name__ == "__main__":
    unittest.main()