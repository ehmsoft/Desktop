# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'syncConflictDialog.ui'
#
# Created: Wed Mar 21 21:34:26 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SyncConflictDialog(object):
    def setupUi(self, SyncConflictDialog):
        SyncConflictDialog.setObjectName("SyncConflictDialog")
        SyncConflictDialog.resize(404, 144)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SyncConflictDialog.sizePolicy().hasHeightForWidth())
        SyncConflictDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QtGui.QVBoxLayout(SyncConflictDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblTextoDialogo = QtGui.QLabel(SyncConflictDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTextoDialogo.sizePolicy().hasHeightForWidth())
        self.lblTextoDialogo.setSizePolicy(sizePolicy)
        self.lblTextoDialogo.setScaledContents(False)
        self.lblTextoDialogo.setWordWrap(True)
        self.lblTextoDialogo.setObjectName("lblTextoDialogo")
        self.verticalLayout_5.addWidget(self.lblTextoDialogo)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(SyncConflictDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lblFechaLocal = QtGui.QLabel(SyncConflictDialog)
        self.lblFechaLocal.setText("")
        self.lblFechaLocal.setObjectName("lblFechaLocal")
        self.horizontalLayout_4.addWidget(self.lblFechaLocal)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.localLayout = QtGui.QVBoxLayout()
        self.localLayout.setObjectName("localLayout")
        self.verticalLayout.addLayout(self.localLayout)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.btnSeleccionLocal = QtGui.QPushButton(SyncConflictDialog)
        self.btnSeleccionLocal.setObjectName("btnSeleccionLocal")
        self.horizontalLayout_8.addWidget(self.btnSeleccionLocal)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtGui.QLabel(SyncConflictDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lblFechaMovil = QtGui.QLabel(SyncConflictDialog)
        self.lblFechaMovil.setText("")
        self.lblFechaMovil.setObjectName("lblFechaMovil")
        self.horizontalLayout_5.addWidget(self.lblFechaMovil)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.mobileLayout = QtGui.QVBoxLayout()
        self.mobileLayout.setObjectName("mobileLayout")
        self.verticalLayout_2.addLayout(self.mobileLayout)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.btnSeleccionMovil = QtGui.QPushButton(SyncConflictDialog)
        self.btnSeleccionMovil.setObjectName("btnSeleccionMovil")
        self.horizontalLayout_9.addWidget(self.btnSeleccionMovil)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SyncConflictDialog)
        QtCore.QMetaObject.connectSlotsByName(SyncConflictDialog)

    def retranslateUi(self, SyncConflictDialog):
        SyncConflictDialog.setWindowTitle(QtGui.QApplication.translate("SyncConflictDialog", "Conflicto de Sincronización", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTextoDialogo.setText(QtGui.QApplication.translate("SyncConflictDialog", "Ha habido un conflicto en la sincronización, el mismo registro ha sido modificado en el móvil y en el escritorio, seleccione con cuál se va a quedar:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SyncConflictDialog", "Versión local:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSeleccionLocal.setText(QtGui.QApplication.translate("SyncConflictDialog", "Seleccionar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SyncConflictDialog", "Versión Móvil:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSeleccionMovil.setText(QtGui.QApplication.translate("SyncConflictDialog", "Seleccionar", None, QtGui.QApplication.UnicodeUTF8))

