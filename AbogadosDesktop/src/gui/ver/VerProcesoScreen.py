# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/verProceso.ui'
#
# Created: Fri Oct 19 10:02:06 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VerProceso(object):
    def setupUi(self, VerProceso):
        VerProceso.setObjectName("VerProceso")
        VerProceso.resize(396, 523)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VerProceso.sizePolicy().hasHeightForWidth())
        VerProceso.setSizePolicy(sizePolicy)
        VerProceso.setMinimumSize(QtCore.QSize(350, 450))
        self.gridLayout_2 = QtGui.QGridLayout(VerProceso)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtGui.QTabWidget(VerProceso)
        self.tabWidget.setMinimumSize(QtCore.QSize(375, 490))
        self.tabWidget.setObjectName("tabWidget")
        self.tabProceso = QtGui.QWidget()
        self.tabProceso.setMinimumSize(QtCore.QSize(370, 430))
        self.tabProceso.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabProceso.setObjectName("tabProceso")
        self.gridLayout = QtGui.QGridLayout(self.tabProceso)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtGui.QScrollArea(self.tabProceso)
        self.scrollArea.setMinimumSize(QtCore.QSize(350, 400))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 348, 455))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(-1, -1, 10, -1)
        self.formLayout.setObjectName("formLayout")
        self.lbl1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl1.sizePolicy().hasHeightForWidth())
        self.lbl1.setSizePolicy(sizePolicy)
        self.lbl1.setObjectName("lbl1")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl1)
        self.lblDemandante = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblDemandante.setText("")
        self.lblDemandante.setObjectName("lblDemandante")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblDemandante)
        self.lbl2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl2.sizePolicy().hasHeightForWidth())
        self.lbl2.setSizePolicy(sizePolicy)
        self.lbl2.setObjectName("lbl2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbl2)
        self.lblDemandado = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblDemandado.setText("")
        self.lblDemandado.setObjectName("lblDemandado")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lblDemandado)
        self.lbl3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl3.sizePolicy().hasHeightForWidth())
        self.lbl3.setSizePolicy(sizePolicy)
        self.lbl3.setObjectName("lbl3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl3)
        self.dteFecha = QtGui.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dteFecha.setEnabled(False)
        self.dteFecha.setObjectName("dteFecha")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dteFecha)
        self.lbl4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl4.sizePolicy().hasHeightForWidth())
        self.lbl4.setSizePolicy(sizePolicy)
        self.lbl4.setObjectName("lbl4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl4)
        self.lblJuzgado = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblJuzgado.setText("")
        self.lblJuzgado.setObjectName("lblJuzgado")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lblJuzgado)
        self.lbl5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl5.sizePolicy().hasHeightForWidth())
        self.lbl5.setSizePolicy(sizePolicy)
        self.lbl5.setObjectName("lbl5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbl5)
        self.lblRadicado = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblRadicado.setText("")
        self.lblRadicado.setObjectName("lblRadicado")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lblRadicado)
        self.lbl6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl6.sizePolicy().hasHeightForWidth())
        self.lbl6.setSizePolicy(sizePolicy)
        self.lbl6.setObjectName("lbl6")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.lbl6)
        self.lblRadicadoUnico = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblRadicadoUnico.setText("")
        self.lblRadicadoUnico.setObjectName("lblRadicadoUnico")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lblRadicadoUnico)
        self.lbl7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl7.setObjectName("lbl7")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.lbl7)
        self.lblCategoria = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblCategoria.setText("")
        self.lblCategoria.setObjectName("lblCategoria")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lblCategoria)
        self.lbl8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl8.setObjectName("lbl8")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.lbl8)
        self.lblEstado = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblEstado.setText("")
        self.lblEstado.setObjectName("lblEstado")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.lblEstado)
        self.lbl9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl9.setObjectName("lbl9")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.lbl9)
        self.lblTipo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblTipo.setText("")
        self.lblTipo.setObjectName("lblTipo")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.lblTipo)
        self.lbl11 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl11.setObjectName("lbl11")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.lbl11)
        self.lblPrioridad = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblPrioridad.setText("")
        self.lblPrioridad.setObjectName("lblPrioridad")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.lblPrioridad)
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbl10 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lbl10.setObjectName("lbl10")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl10)
        self.lblNotas = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.lblNotas.setObjectName("lblNotas")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblNotas)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabProceso, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(VerProceso)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VerProceso)

    def retranslateUi(self, VerProceso):
        VerProceso.setWindowTitle(QtGui.QApplication.translate("VerProceso", "Ver Proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl1.setText(QtGui.QApplication.translate("VerProceso", "Cliente:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDemandante.setToolTip(QtGui.QApplication.translate("VerProceso", "El nombre del cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDemandante.setStatusTip(QtGui.QApplication.translate("VerProceso", "El nombre del cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl2.setText(QtGui.QApplication.translate("VerProceso", "Contraparte:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDemandado.setToolTip(QtGui.QApplication.translate("VerProceso", "El nombre de la contraparte", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDemandado.setStatusTip(QtGui.QApplication.translate("VerProceso", "El nombre de la contraparte", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl3.setText(QtGui.QApplication.translate("VerProceso", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.dteFecha.setToolTip(QtGui.QApplication.translate("VerProceso", "La fecha de creación del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.dteFecha.setStatusTip(QtGui.QApplication.translate("VerProceso", "La fecha de creación del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl4.setText(QtGui.QApplication.translate("VerProceso", "Juzgado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblJuzgado.setToolTip(QtGui.QApplication.translate("VerProceso", "El nombre del juzgado del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lblJuzgado.setStatusTip(QtGui.QApplication.translate("VerProceso", "El nombre del juzgado del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl5.setText(QtGui.QApplication.translate("VerProceso", "Radicado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRadicado.setToolTip(QtGui.QApplication.translate("VerProceso", "El radicado del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRadicado.setStatusTip(QtGui.QApplication.translate("VerProceso", "El radicado del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl6.setText(QtGui.QApplication.translate("VerProceso", "Radicado Único:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRadicadoUnico.setToolTip(QtGui.QApplication.translate("VerProceso", "El radicado único del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRadicadoUnico.setStatusTip(QtGui.QApplication.translate("VerProceso", "El radicado único del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl7.setText(QtGui.QApplication.translate("VerProceso", "Categoría:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCategoria.setToolTip(QtGui.QApplication.translate("VerProceso", "La categoría donde está el proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCategoria.setStatusTip(QtGui.QApplication.translate("VerProceso", "La categoría donde está el proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl8.setText(QtGui.QApplication.translate("VerProceso", "Estado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblEstado.setToolTip(QtGui.QApplication.translate("VerProceso", "El estado del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lblEstado.setStatusTip(QtGui.QApplication.translate("VerProceso", "El estado del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl9.setText(QtGui.QApplication.translate("VerProceso", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipo.setToolTip(QtGui.QApplication.translate("VerProceso", "El tipo de proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTipo.setStatusTip(QtGui.QApplication.translate("VerProceso", "El tipo de proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl11.setText(QtGui.QApplication.translate("VerProceso", "Prioridad:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPrioridad.setToolTip(QtGui.QApplication.translate("VerProceso", "La prioridad del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPrioridad.setStatusTip(QtGui.QApplication.translate("VerProceso", "La prioridad del proceso", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl10.setText(QtGui.QApplication.translate("VerProceso", "Notas:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProceso), QtGui.QApplication.translate("VerProceso", "Info. Proceso", None, QtGui.QApplication.UnicodeUTF8))

