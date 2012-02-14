'''

Created on 24/01/2012

@author: esteban
'''

from PySide.QtGui import QDialog, QMessageBox
from NuevaCategoriaScreen import Ui_NuevaCategoria
from core.Categoria import Categoria
from persistence.Persistence import Persistence


class NuevaCategoria(QDialog, Ui_NuevaCategoria):
    def __init__(self,categoria=None,parent=None):
        super(NuevaCategoria, self).__init__(parent)
        self.__categoria = categoria
        self.setupUi(self)        
        if self.__categoria is not None:
            self.txtCategoria.setText(self.__categoria.getDescripcion())
            
        
    def getCategoria(self):
        return self.__categoria
    
    def guardar(self):
        try:
            p = Persistence()
            if self.__categoria is None:
                categoria = Categoria()
                categoria.setDescripcion(self.txtCategoria.text())
                p.guardarCategoria(categoria)
                self.__categoria = categoria
            else:
                self.__categoria.setDescripcion(self.txtCategoria.text())
                p.actualizarCategoria(self.__categoria)
                    
        except Exception, e:
            print e
        finally:
            return QDialog.accept(self)

    
    def accept(self):
        if self.txtCategoria.text().__len__() == 0 :
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText("La descripcion se considera obligatoria")
            message.exec_()
            self.txtCategoria.setFocus()                 
        else:
            self.guardar()
            
  
    
    
    
    
    
    
    
    
    
    
    
    
        

