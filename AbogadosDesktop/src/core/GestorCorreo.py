# -*- coding: utf-8 -*-
'''
Created on 15/08/2012

@author: sancospi
'''
import smtplib
from PySide.QtCore import QThread
from email.mime.text import MIMEText


class Correo(QThread):
    def run(self):
        self.enviarCorreo(cita=self.cita, correo=self.correo)
        self.flag = True
        self.exec_()

    def enviarCorreo(self, cita, correo):
        
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login("info@ehmsoft.com","NcPtlc.32")
        
        msg = MIMEText(repr(cita))
        
        msg['Subject'] = u'Notificación de cita %s' % cita.getDescripcion().encode('utf-8')
        msg['From'] = 'info@ehmsoft.com'
        msg['To'] = correo
        
        try:
            mailServer.sendmail('info@ehmsoft.com', correo, msg.as_string())
            mailServer.quit()
        except:
            self.flag = False
            self.respuesta = u"Error al enviar correo electrónico de notificación de una cita. Por favor verifique su conexión a internet e intente de nuevo. Si el problema persiste por favor comuníquese con nuestro personal de soporte técnico: soporte@ehmsoft.com"
        finally:
            self.exit()