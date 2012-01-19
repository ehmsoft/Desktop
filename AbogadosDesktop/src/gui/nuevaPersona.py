import sys
from PySide.QtCore import *
from PySide.QtGui import *
import nuevaPersonaScreen
from core.Persona import *

class NuevaPersona(QDialog, nuevaPersonaScreen.Ui_nuevaPersona):
    def __init__(self,persona=None,parent=None):
        super(NuevaPersona, self).__init__(parent)
        self.__persona = persona
        self.setupUi(self)
        
        if self.__persona is not None:
            self.txtNombre.setText(self.__persona.getNombre())
            self.txtCedula.setText(self.__persona.getId())
            self.txtTelefono.setText(self.__persona.getTelefono())
            self.txtDireccion.setText(self.__persona.getDireccion())
            self.txtCorreo.setText(self.__persona.getCorreo())
            self.txtNotas.setText(self.__persona.getNotas())
            
    def accept(self, *args, **kwargs):
        return QDialog.accept(self, *args, **kwargs)
    
    def reject(self, *args, **kwargs):
        return QDialog.reject(self, *args, **kwargs)

persona = Persona(1, nombre = "Harold", telefono = "3117001033",
                direccion = "Calle 30 # 14 - 32", correo = "sancospi@gmail.com", notas = "Ninguna", id = "1093219325")
        
app = QApplication(sys.argv)
form = NuevaPersona(persona = persona)
form.show()
app.exec_()
