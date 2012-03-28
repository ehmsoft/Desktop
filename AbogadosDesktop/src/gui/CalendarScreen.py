# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created: Tue Mar 27 17:13:56 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.resize(258, 250)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Calendar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtGui.QTabWidget(Calendar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lista = QtGui.QListWidget(self.tab)
        self.lista.setLayoutMode(QtGui.QListView.SinglePass)
        self.lista.setViewMode(QtGui.QListView.ListMode)
        self.lista.setModelColumn(0)
        self.lista.setObjectName("lista")
        self.verticalLayout.addWidget(self.lista)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnAgregar = QtGui.QPushButton(self.tab)
        self.btnAgregar.setObjectName("btnAgregar")
        self.horizontalLayout_3.addWidget(self.btnAgregar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lista2 = QtGui.QListWidget(self.tab_2)
        self.lista2.setObjectName("lista2")
        self.verticalLayout_2.addWidget(self.lista2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(Calendar)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        Calendar.setWindowTitle(QtGui.QApplication.translate("Calendar", "Calendario", None, QtGui.QApplication.UnicodeUTF8))
        self.lista.setSortingEnabled(False)
        self.btnAgregar.setText(QtGui.QApplication.translate("Calendar", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Calendar", "Todas", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Calendar", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Calendar", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))

