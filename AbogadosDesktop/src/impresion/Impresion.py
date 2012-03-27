'''
Created on 22/03/2012

@author: esteban
'''

from persistence.Persistence import Persistence
from PySide.QtCore import *
from PySide.QtGui import *
import gui.resources


class Impresion(object):
    def __init__(self, parent = None):
        pass
    
    def imprimirJuzgados(self, juzgados=None):
        html = self.imprimirLogo()
        html +=("<HEAD><TITLE>LISTA JUZGADOS </TITLE></HEAD><BODY><FONT SIZE='+2'><B>Lista de Juzgados: </B></FONT><BR><BR>")
        html += ("<TABLE BORDER =1 CELLSPACING = 0 WIDTH ='98%'  ><TR><TH><B>Nombre</B></TH><TH><B>Telefono</B></TH><TH><B>Direccion</B></TH><TH><B>Ciudad</B></TH><TH><B>Tipo</B></TH></TR>")
        if juzgados is None:
            p = Persistence()
            juzgados = p.consultarJuzgados()
             
        for juzgado in juzgados:
            if juzgado.getId_juzgado() != "1":
                html +=("<TR>")
                html = html + "<TD>"+ juzgado.getNombre() + "</TD>"
                html = html + "<TD>"+ juzgado.getTelefono() + "</TD>"
                html = html + "<TD>"+ juzgado.getDireccion() + "</TD>"
                html = html + "<TD>"+ juzgado.getCiudad() + "</TD>"
                html = html + "<TD>"+ juzgado.getTipo() + "</TD>"
                html +=("</TR>")
        html +=("</TABLE></BODY>")
        return html
        

    def imprimirPersonas(self,tipo,personas=None):
        html = self.imprimirLogo()
        if tipo == 1:
            html += "<HEAD><TITLE>LISTA DE DEMANDANTES</TITLE></HEAD><BODY><FONT SIZE= '+2'><B>Lista de Demandantes:</B></FONT><BR><BR>"
            if personas is None:
                p = Persistence()
                personas = p.consultarDemandantes()            
        elif tipo == 2:
            html += "<HEAD><TITLE>LISTA DE DEMANDADOS</TITLE></HEAD><BODY><FONT SIZE= '+2'><B>Lista de Demandos:</B></FONT><BR><BR>"
            if personas is None:
                p = Persistence()
                personas = p.consultarDemandados()
        else:
            raise Exception('el tipo de persona no existe') 
        html += ("<TABLE BORDER =1 CELLSPACING = 0 WIDTH ='98%'  ><TR><TH><B>Nombre</B></TH><TH><B>Cedula</B></TH><TH><B>Telefono</B></TH><TH><B>Direccion</B></TH><TH><B>Correo</B></TH><TH><B>Notas</B></TH></TR>")
        for persona in personas:
            if persona.getId_persona() != "1":
                html +=("<TR>")
                html = html + "<TD>"+ persona.getNombre() + "</TD>"
                html = html + "<TD>"+ persona.getId() + "</TD>"
                html = html + "<TD>"+ persona.getTelefono() + "</TD>"
                html = html + "<TD>"+ persona.getDireccion() + "</TD>"
                html = html + "<TD>"+ persona.getCorreo() + "</TD>"
                html = html + "<TD>"+ persona.getNotas() + "</TD>"
                html +=("</TR>")
        html +=("</TABLE></BODY>")
        return html

    def imprimirProcesos(self,procesos=None):
        html = self.imprimirLogo()
        html +=("<HEAD><TITLE>LISTA DE PROCESOS </TITLE></HEAD><BODY><FONT SIZE='+2'><B>Lista de Procesos: </B></FONT><BR><BR>")
        html += ("<TABLE BORDER =1 CELLSPACING = 0 WIDTH ='98%'><TR><TH>Radicado</TH><TH>Radicado Unico</TH><TH>Demandante</TH><TH>Demandado</TH><TH>Juzgado</TH><TH>Fecha</TH><TH>Estado</TH><TH>Categoria</TH><TH>Tipo</TH><TH>Notas</TH>")
        if procesos is None:
            p = Persistence()
            procesos = p.consultarProcesos()
        for proceso in procesos:
            html +=("<TR>")
            html = html + "<TD>"+ proceso.getRadicado() + "</TD>"
            html = html + "<TD>"+ proceso.getRadicadoUnico() + "</TD>"
            html = html + "<TD>"+ proceso.getDemandante().getNombre() + "</TD>"
            html = html + "<TD>"+ proceso.getDemandado().getNombre() + "</TD>"
            html = html + "<TD>"+ proceso.getJuzgado().getNombre() + "</TD>"
            html = html + "<TD>"+ '{:%d-%m-%Y}'.format(proceso.getFecha()) + "</TD>"
            html = html + "<TD>"+ proceso.getEstado() + "</TD>"
            html = html + "<TD>"+ proceso.getCategoria().getDescripcion() + "</TD>"
            html = html + "<TD>"+ proceso.getTipo() + "</TD>"
            html = html + "<TD>"+ proceso.getNotas() + "</TD>"
            html +=("</TR>")
        html +=("</TABLE></BODY>")
        return html
    
    def imprimirActuaciones(self,proceso= None ,actuaciones=None):
        
        if actuaciones is None:
            html = self.imprimirLogo()
            p = Persistence()
            actuaciones = p.consultarActuaciones(proceso)
            html +=("<HEAD><TITLE>LISTA DE ACTUACIONES </TITLE></HEAD><BODY><FONT SIZE='+2'><B>Lista de Actuaciones: </B></FONT><BR><BR>")
        else:
            html =("<HEAD><TITLE>LISTA DE ACTUACIONES </TITLE></HEAD><BODY><FONT SIZE='+2'><B>Lista de Actuaciones: </B></FONT><BR><BR>")
        
        html += ("<TABLE BORDER =1 CELLSPACING = 0 WIDTH ='98%'  ><TR><TH><B>Descripcion</B></TH><TH><B>Juzgado</B></TH><TH><B>Fecha Proxima</B></TH><TH><B>Fecha de creacion</B></TH></TR>")
        
        for actuacion in actuaciones:
            html +=("<TR>")
            html = html + "<TD>"+ actuacion.getDescripcion() + "</TD>"
            html = html + "<TD>"+ actuacion.getJuzgado().getNombre() + "</TD>"
            html = html + "<TD>"+ '{:%d-%m-%Y}'.format(actuacion.getFechaProxima()) + "</TD>"
            html = html + "<TD>"+ '{:%d-%m-%Y}'.format(actuacion.getFecha()) + "</TD>"
            html +=("</TR>")
        html +=("</TABLE></BODY>")
        return html
    
    def imprimirEventosProximos(self):
        cantidad = QInputDialog.getInt(None,'Ingrese un valor','Ingrese la cantidad de eventos proximos a imprimir')
        if cantidad[1] == True:
            html = self.imprimirLogo()
            html +=("<HEAD><TITLE>EVENTOS PROXIMOS </TITLE></HEAD><BODY><FONT SIZE='+2'><B>Eventos Proximos: </B></FONT><BR><BR>")
            html += ("<TABLE BORDER =1 CELLSPACING = 0 WIDTH ='95%'  ><TR><TH><B>Descripcion</B></TH><TH><B>Juzgado</B></TH><TH><B>Fecha Proxima</B></TH><TH><B>Fecha de creacion</B></TH></TR>")
            p = Persistence()
            actuaciones = p.consultarActuacionesCriticas(cantidad[0])
            for actuacion in actuaciones:
                html +=("<TR>")
                html = html + "<TD>"+ actuacion.getDescripcion() + "</TD>"
                html = html + "<TD>"+ actuacion.getJuzgado().getNombre() + "</TD>"
                html = html + "<TD>"+ '{:%d-%m-%Y}'.format(actuacion.getFechaProxima()) + "</TD>"
                html = html + "<TD>"+ '{:%d-%m-%Y}'.format(actuacion.getFecha()) + "</TD>"
                html +=("</TR>")
            html +=("</TABLE></BODY>")
            return html
    
    def imprimirJuzgado(self, juzgado):    
        html = self.imprimirLogo()      
        html +="<HEAD><TITLE>"+ juzgado.getNombre() + "</TITLE></HEAD><BODY><BR><FONT SIZE='+1'><B>" + juzgado.getNombre() + "</B></FONT>"
        if juzgado.getTelefono() != "":
            html += "<FONT SIZE='+1'><B>, </B></FONT>" + juzgado.getTelefono() + "<BR>"
        else:
            html += "<BR>"
        if juzgado.getCiudad != "":
            html += juzgado.getCiudad()
            if juzgado.getDireccion != "":
                html += ", " + juzgado.getDireccion() + "<BR>"
            else:
                html += "<BR>"
        else:
            if juzgado.getDireccion != "":
                html += juzgado.getDireccion() + "<BR>"
        if juzgado.getTipo():
            html += "Tipo: " + juzgado.getTipo() + "<BR>"
        for campo in juzgado.getCampos():
            html += campo.getNombre() + ": " + campo.getValor() + "<BR>"
        html +=("</TABLE></BODY>")
        return html
        
    def imprimirPersona(self, persona):
        html = self.imprimirLogo()
        html +="<HEAD><TITLE>"+ persona.getNombre() + "</TITLE></HEAD><BODY><BR><FONT SIZE='+1'><B>" + persona.getNombre() + "</B></FONT>"
        if persona.getId() != "":
            html += "<FONT SIZE='+1'><B>, </B></FONT>"+ persona.getId() +"<BR>"
        else:
            html += "<BR>"
        if persona.getTelefono() != "":
            html += persona.getTelefono()
            if persona.getDireccion() != "":
                html  += ", "+ persona.getDireccion() + "<BR>"
            else:
                html += "<BR>"
        else:
            if persona.getDireccion() != "":
                html  = persona.getDireccion() + "<BR>"
        if persona.getCorreo() != "":
            html += persona.getCorreo() + "<BR>"
        if persona.getTipo() == 1:
            html += "Tipo: Demandante <BR>"
        elif persona.getTipo() == 2:
            html += "Tipo: Demandado <BR>"
        else:
            raise Exception('el tipo de persona no existe')                            
        if persona.getNotas() != "":
            html += "Notas: " + persona.getNotas() + "<BR>"    
        for campo in persona.getCampos():
            html += campo.getNombre() + ": " + campo.getValor() + "<BR>"
        html +=("</TABLE></BODY>")
        return html   
             
    def imprimirProceso(self, proceso):
        html = self.imprimirLogo()
        html += "<HEAD><TITLE>INFORMACION DEL PROCESO</TITLE></HEAD><BODY><BR><FONT SIZE= '+2'><B>Informacion del Proceso:</B></FONT><BR><BR>"
        if proceso.getRadicado() != "":
            html += "<B>Radicado: " + proceso.getRadicado() + "</B><BR><BR>"
            
        if proceso.getRadicadoUnico() != "":
            html += "Radicado Unico: " + proceso.getRadicadoUnico() + "<BR>"
        html+="Demandante: "+ proceso.getDemandante().getNombre() +"<BR>"+"Demandado: "+ proceso.getDemandado().getNombre() +"<BR>"+"Juzgado: "+ proceso.getJuzgado().getNombre() +"<BR>"+"Categoria: "+ proceso.getCategoria().getDescripcion()+"<BR>"
        if proceso.getFecha() != "":
            html+= "Fecha: " + '{:%d-%m-%Y}'.format(proceso.getFecha()) + "<BR>"
        if proceso.getEstado() != "":
            html += "Estado: " + proceso.getEstado() + "<BR>"
        if proceso.getTipo() != "":
            html += "Tipo: " + proceso.getTipo() + "<BR>"
        if proceso.getNotas() != "":
            html += "Notas: " + proceso.getNotas() + "<BR>"
        for campo in proceso.getCampos():
            html += campo.getNombre() + ": " + campo.getValor() + "<BR>"
        if proceso.getActuaciones() != []:
            html+=self.imprimirActuaciones(actuaciones = proceso.getActuaciones())
        html += "<HEAD><TITLE>INFORMACION DEL PROCESO</TITLE></HEAD>"
        html +=("</TABLE></BODY>")
        return html
        
    def imprimirLogo(self):
        
        html = "<TABLE align=right><TR><TH><img src=':/images/logoB100.png' WIDTH = '85' HEIGHT = '26'></TH><TH><PRE>     </PRE></TH></TR></TABLE>"
        html += "<p align=right><TABLE ><TR><TD><FONT SIZE = '-2'><I>Procesos Judiciales</I></FONT></TD><TD><PRE>     </PRE></TD></TR></TABLE></P>"

        return html