# -*- coding: utf-8 -*-
'''
Created on 15/08/2012

@author: sancospi
'''
import smtplib
from email.mime.text import MIMEText

def enviarCorreo(cita, correo):
    
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login("info@ehmsoft.com","NcPtlc.32")
    
    msg = MIMEText(str(cita))
    
    msg['Subject'] = 'Notificación de cita ' + cita.getDescripcion()
    msg['From'] = 'info@ehmsoft.com'
    msg['To'] = correo
    
    
    mailServer.sendmail('info@ehmsoft.com', correo, msg.as_string())
    mailServer.quit()