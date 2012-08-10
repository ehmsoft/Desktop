# -*- coding: utf-8 -*-
'''
Created on 24/04/2012

@author: elfotografo007
'''
from PySide import QtCore
class MyTranslator(QtCore.QTranslator):
    '''
    Clase que se encarga de traducir los botones y cudaros de dialogo de la app al idioma castellano
    '''
    def __init__(self,parent =None):
        super(MyTranslator, self).__init__(parent)
        
    def translate(self,context, sourceText, disambiguation, n=0):
        if sourceText == 'OK':
            return 'Aceptar'
        elif sourceText == 'Cancel':
            return 'Cancelar'
        elif sourceText == 'About %1':
            return 'Acerca de %1'
        elif sourceText == 'Quit':
            return 'Salir de'
        elif sourceText == 'Exit':
            return 'Salir'
        elif sourceText == '&Yes':
            return u'&Sí'
        elif sourceText == 'Continue':
            return u'Siguiente'
        elif sourceText == 'Go Back':
            return u'Atrás'
        elif sourceText == 'Done':
            return u'Finalizar'
        return super(MyTranslator,self).translate(context, sourceText,disambiguation, n)
        