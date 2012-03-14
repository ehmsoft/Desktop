# -*- coding: utf-8 -*-
from PySide import QtGui

def reject(dialog, dirty):
    if dirty:
        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Question)
        message.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        message.setDefaultButton(QtGui.QMessageBox.No)
        message.setText(unicode("¿Desea descartar los cambios?"))
        ret = message.exec_()
        if ret == QtGui.QMessageBox.Yes:
            return QtGui.QDialog.reject(dialog)
    else:
        return QtGui.QDialog.reject(dialog)
