'''
Created on 26/01/2012

@author: elfotografo007
'''
from PySide.QtGui import *
from PySide.QtCore import *
from gui.VerProcesoScreen import Ui_VerProceso

class VerProceso(QWidget, Ui_VerProceso):
    def __init__(self, proceso = None, parent = None):
        super(VerProceso, self).__init__(parent)
        self.__proceso = proceso
        self.setupUi(self)
    
        if self.__proceso:
            self.lblDemandante.setText(str(self.__proceso.getDemandante()))
            self.lblDemandado.setText(str(self.__proceso.getDemandado()))
            self.dteFecha.setDateTime(self.__proceso.getFecha())
            self.lblJuzgado.setText(str(self.__proceso.getJuzgado()))
            self.lblRadicado.setText(self.__proceso.getRadicado())
            self.lblRadicadoUnico.setText(self.__proceso.getRadicadoUnico())
            self.lblEstado.setText(self.__proceso.getEstado())
            self.lblCategoria.setText(str(self.__proceso.getCategoria()))
            self.lblTipo.setText(str(self.__proceso.getTipo()))
            self.lblPrioridad.setNum(self.__proceso.getPrioridad())
            self.lblNotas.setText(self.__proceso.getNotas())
            
            for campo in self.__proceso.getCampos():
                label = QLabel()
                label.setText('%s:' % campo.getNombre())
                lblBox = QLabel()
                lblBox.setText(campo.getValor())
                self.formLayout.addRow(label,lblBox)
            actuaciones = self.__proceso.getActuaciones()
            if len(actuaciones) is not 0:
                grpboxActuaciones = QGroupBox(self.groupBox)
                grpboxActuaciones.setTitle('Actuaciones:')
                for actuacion in actuaciones:
                    #grpboxActuaciones.addWidget(QLabel(str(actuacion), grpboxActuaciones))
                    QLabel(str(actuacion), grpboxActuaciones)
                    QtGui.


import sys
from core.Proceso import Proceso
from core.Persona import Persona
from core.Actuacion import Actuacion
from core.Categoria import Categoria
from core.Juzgado import Juzgado
from core.CampoPersonalizado import CampoPersonalizado 
from datetime import datetime
app = QApplication(sys.argv)
demandante = Persona(1, '123', 'Andres', '3366858')
demandado =  Persona(2, '123', 'Harold', '3366858', notas= 'hello')
juzgado = Juzgado('Juzgado 1', telefono = '3433123')
juzgado2 = Juzgado('Juzgado 2', telefono = 'Nuevo juzgado')
categoria = Categoria('Categoria 1')
categoria2 = Categoria('Categoria 2')
fecha = datetime.today()
fecha2 = datetime(2010,12,31,5,36)
campo1 = CampoPersonalizado('Campo 1', '10', True, 0, 0)
campo2 = CampoPersonalizado('Campo 2', '5', True, 0,0)
campo3 = CampoPersonalizado('Campo 3', '15', True, 0,0)
campo4 = CampoPersonalizado('Campo 4', '20', True, 0,0)
campos = [campo1, campo2, campo3]
actuacion1 = Actuacion(juzgado, fecha, fecha2, 'Actuacion1')
actuacion2 = Actuacion(juzgado, fecha, fecha2, 'Actuacion2')
actuacion3 = Actuacion(juzgado, fecha, fecha2, 'Actuacion3')
plantilla = Proceso(demandante, demandado, fecha, juzgado, '1234567', '1324566765', [actuacion1], 'Nuevo', categoria, 'Alimentos', 'Esta es una nota', 1,campos)
form1 = VerProceso(plantilla)
form1.show()
app.exec_()