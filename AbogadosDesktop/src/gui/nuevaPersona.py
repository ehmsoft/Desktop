import sys
from PySide.QtGui import *
from PySide.QtCore import *
import nuevaPersonaScreen
from core.Persona import Persona
from persistence.Persistence import Persistence

class NuevaPersona(QDialog, nuevaPersonaScreen.Ui_nuevaPersona):
    def __init__(self,persona=None,tipo = None,parent=None):
        super(NuevaPersona, self).__init__(parent)
        self.__persona = persona
        self.setupUi(self)
        
        if self.__persona is not None:
            self.__tipo = persona.getTipo()
            self.txtNombre.setText(self.__persona.getNombre())
            self.txtCedula.setText(self.__persona.getId())
            self.txtTelefono.setText(self.__persona.getTelefono())
            self.txtDireccion.setText(self.__persona.getDireccion())
            self.txtCorreo.setText(self.__persona.getCorreo())
            self.txtNotas.setText(self.__persona.getNotas())
        else:
            self.__tipo = tipo

            
    def getPersona(self):
        return self.__persona
            
    def accept(self, *args, **kwargs):
        try:
            p = Persistence()
            if self.__persona is None:
                persona = Persona(self.__tipo)
                persona.setNombre(self.txtNombre.text())
                persona.setId(self.txtCedula.text())
                persona.setTelefono(self.txtTelefono.text())
                persona.setDireccion(self.txtDireccion.text())
                persona.setCorreo(self.txtCorreo.text())
                persona.setNotas(self.txtNotas.text())
                
                p.guardarPersona(persona)
                self.__persona = persona
            else:
                self.__persona = Persona(self.__tipo)
                self.__persona.setNombre(self.txtNombre.text())
                self.__persona.setId(self.txtCedula.text())
                self.__persona.setTelefono(self.txtTelefono.text())
                self.__persona.setDireccion(self.txtDireccion.text())
                self.__persona.setCorreo(self.txtCorreo.text())
                self.__persona.setNotas(self.txtNotas.text())
                p.actualizarPersona(self.__persona)
                
        except Exception, e:
            print e           
                
        return QDialog.accept(self, *args, **kwargs)
    
    def reject(self, *args, **kwargs):
        return QDialog.reject(self, *args, **kwargs)

#persona = Persona(1, nombre = "Harold", telefono = "3117001033",
                #direccion = "Calle 30 # 14 - 32", correo = "sancospi@gmail.com", notas = "Ninguna", id = "1093219325")
        
app = QApplication(sys.argv)
form = NuevaPersona(tipo = 1)
form.show()
app.exec_()
