# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'columnaSync.ui'
#
# Created: Wed Mar 14 22:49:53 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ColumnaSync(object):
    def setupUi(self, ColumnaSync):
        ColumnaSync.setObjectName("ColumnaSync")
        ColumnaSync.resize(306, 392)
        self.gridLayout = QtGui.QGridLayout(ColumnaSync)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtGui.QTextBrowser(ColumnaSync)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(163, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.btnSincronizar = QtGui.QPushButton(ColumnaSync)
        self.btnSincronizar.setObjectName("btnSincronizar")
        self.gridLayout.addWidget(self.btnSincronizar, 1, 1, 1, 1)

        self.retranslateUi(ColumnaSync)
        QtCore.QMetaObject.connectSlotsByName(ColumnaSync)

    def retranslateUi(self, ColumnaSync):
        ColumnaSync.setWindowTitle(QtGui.QApplication.translate("ColumnaSync", "Sincronizar", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("ColumnaSync", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Para sincronizar su dispositivo haga lo siguiente:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Conecte el dispositivo mediante cable USB al computador.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. En la pantalla del dispositivo seleccione <span style=\" font-weight:600;\">&quot;Unidad USB&quot;</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Presione el botón sincronizar.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSincronizar.setText(QtGui.QApplication.translate("ColumnaSync", "Sincronizar", None, QtGui.QApplication.UnicodeUTF8))

