'''
Created on 25/01/2012

@author: elfotografo007
'''
from PySide import QtGui
from gui.ver.VerPersonaScreen import Ui_VerPersona

class VerPersona(QtGui.QWidget, Ui_VerPersona):
    def __init__(self, persona=None, parent=None):
        super(VerPersona, self).__init__(parent)
        self.__persona = persona
        self.setupUi(self)
    
        if self.__persona:
            self.__tipo = self.__persona.getTipo()
            self.lblNombre.setWordWrap(True)
            self.lblCedula.setWordWrap(True)
            self.lblTelefono.setWordWrap(True)
            self.lblDireccion.setWordWrap(True)
            self.lblCorreo.setWordWrap(True)
            self.lblNotas.setWordWrap(True)
            self.lblNombre.setToolTip(self.__persona.getNombre())
            self.lblCedula.setToolTip(self.__persona.getId())
            self.lblTelefono.setToolTip(self.__persona.getTelefono())
            self.lblDireccion.setToolTip(self.__persona.getDireccion())
            self.lblCorreo.setToolTip(self.__persona.getCorreo())
            self.lblNombre.setText(self.__persona.getNombre())
            self.lblCedula.setText(self.__persona.getId())
            self.lblTelefono.setText(self.__persona.getTelefono())
            self.lblDireccion.setText(self.__persona.getDireccion())
            self.lblCorreo.setText(self.__persona.getCorreo())
            self.lblNotas.setText(self.__persona.getNotas())
            for campo in self.__persona.getCampos():
                label = QtGui.QLabel()
                label.setWordWrap(True)
                label.setText(u'{0}:'.format(campo.getNombre()))
                lblBox = QtGui.QLabel()
                lblBox.setWordWrap(True)
                lblBox.setToolTip(campo.getValor())
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label, lblBox)
            
            if self.__tipo == 1:
                self.setWindowTitle('Ver Demandante')
            else:
                self.setWindowTitle('Ver Demandado')
