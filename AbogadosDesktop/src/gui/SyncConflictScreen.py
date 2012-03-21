# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'syncConflictDialog.ui'
#
# Created: Wed Mar 21 16:07:54 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SyncConflictDialog(object):
    def setupUi(self, SyncConflictDialog):
        SyncConflictDialog.setObjectName("SyncConflictDialog")
        SyncConflictDialog.resize(574, 412)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SyncConflictDialog.sizePolicy().hasHeightForWidth())
        SyncConflictDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(SyncConflictDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lblTextoDialogo = QtGui.QLabel(SyncConflictDialog)
        self.lblTextoDialogo.setWordWrap(True)
        self.lblTextoDialogo.setObjectName("lblTextoDialogo")
        self.gridLayout.addWidget(self.lblTextoDialogo, 0, 0, 1, 4)
        self.label = QtGui.QLabel(SyncConflictDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SyncConflictDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.verLocal = QtGui.QWidget(SyncConflictDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verLocal.sizePolicy().hasHeightForWidth())
        self.verLocal.setSizePolicy(sizePolicy)
        self.verLocal.setObjectName("verLocal")
        self.gridLayout.addWidget(self.verLocal, 2, 0, 1, 2)
        self.verMovil = QtGui.QWidget(SyncConflictDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verMovil.sizePolicy().hasHeightForWidth())
        self.verMovil.setSizePolicy(sizePolicy)
        self.verMovil.setObjectName("verMovil")
        self.gridLayout.addWidget(self.verMovil, 2, 2, 1, 2)
        self.btnSeleccionLocal = QtGui.QPushButton(SyncConflictDialog)
        self.btnSeleccionLocal.setObjectName("btnSeleccionLocal")
        self.gridLayout.addWidget(self.btnSeleccionLocal, 3, 1, 1, 1)
        self.btnSeleccionMovil = QtGui.QPushButton(SyncConflictDialog)
        self.btnSeleccionMovil.setObjectName("btnSeleccionMovil")
        self.gridLayout.addWidget(self.btnSeleccionMovil, 3, 3, 1, 1)

        self.retranslateUi(SyncConflictDialog)
        QtCore.QMetaObject.connectSlotsByName(SyncConflictDialog)

    def retranslateUi(self, SyncConflictDialog):
        SyncConflictDialog.setWindowTitle(QtGui.QApplication.translate("SyncConflictDialog", "Conflicto de Sincronización", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTextoDialogo.setText(QtGui.QApplication.translate("SyncConflictDialog", "Ha habido un conflicto en la sincronización, el mismo registro ha sido modificado en el móvil y en el escritorio, seleccione con cuál se va a quedar:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SyncConflictDialog", "Versión local:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SyncConflictDialog", "Versión Móvil:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSeleccionLocal.setText(QtGui.QApplication.translate("SyncConflictDialog", "Seleccionar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSeleccionMovil.setText(QtGui.QApplication.translate("SyncConflictDialog", "Seleccionar", None, QtGui.QApplication.UnicodeUTF8))

