# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevaPlantilla.ui'
#
# Created: Fri Aug  3 11:28:22 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NuevaPlantilla(object):
    def setupUi(self, NuevaPlantilla):
        NuevaPlantilla.setObjectName("NuevaPlantilla")
        NuevaPlantilla.resize(339, 497)
        self.gridLayout_2 = QtGui.QGridLayout(NuevaPlantilla)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtGui.QFrame(NuevaPlantilla)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(NuevaPlantilla)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(NuevaPlantilla)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 382))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lblNombre = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblNombre.setObjectName("lblNombre")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblNombre)
        self.txtNombre = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtNombre.setObjectName("txtNombre")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtNombre)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.lblDemandante = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblDemandante.setCursor(QtCore.Qt.PointingHandCursor)
        self.lblDemandante.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lblDemandante.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lblDemandante.setStatusTip("")
        self.lblDemandante.setObjectName("lblDemandante")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lblDemandante)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lblDemandado = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblDemandado.setCursor(QtCore.Qt.PointingHandCursor)
        self.lblDemandado.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lblDemandado.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lblDemandado.setObjectName("lblDemandado")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lblDemandado)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lblJuzgado = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblJuzgado.setCursor(QtCore.Qt.PointingHandCursor)
        self.lblJuzgado.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lblJuzgado.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lblJuzgado.setObjectName("lblJuzgado")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lblJuzgado)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtRadicado = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtRadicado.setObjectName("txtRadicado")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtRadicado)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtRadicadoUnico = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtRadicadoUnico.setObjectName("txtRadicadoUnico")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.txtRadicadoUnico)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txtTipo = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtTipo.setObjectName("txtTipo")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.txtTipo)
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtEstado = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.txtEstado.setObjectName("txtEstado")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.txtEstado)
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lblCategoria = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.lblCategoria.setCursor(QtCore.Qt.PointingHandCursor)
        self.lblCategoria.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lblCategoria.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lblCategoria.setObjectName("lblCategoria")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.lblCategoria)
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_9)
        self.sbPrioridad = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.sbPrioridad.setObjectName("sbPrioridad")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.sbPrioridad)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_11)
        self.txtNotas = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.txtNotas.setObjectName("txtNotas")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtNotas)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.btnAdd = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(NuevaPlantilla)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NuevaPlantilla.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NuevaPlantilla.reject)
        QtCore.QMetaObject.connectSlotsByName(NuevaPlantilla)

    def retranslateUi(self, NuevaPlantilla):
        NuevaPlantilla.setWindowTitle(QtGui.QApplication.translate("NuevaPlantilla", "Nueva plantilla", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NuevaPlantilla", "Ingrese los datos de la nueva plantilla:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setText(QtGui.QApplication.translate("NuevaPlantilla", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NuevaPlantilla", "Demandante:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDemandante.setToolTip(QtGui.QApplication.translate("NuevaPlantilla", "Click derecho para más opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDemandante.setText(QtGui.QApplication.translate("NuevaPlantilla", "vacío", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NuevaPlantilla", "Demandado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDemandado.setToolTip(QtGui.QApplication.translate("NuevaPlantilla", "Click derecho para más opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDemandado.setText(QtGui.QApplication.translate("NuevaPlantilla", "vacío", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NuevaPlantilla", "Juzgado:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblJuzgado.setToolTip(QtGui.QApplication.translate("NuevaPlantilla", "Click derecho para más opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.lblJuzgado.setText(QtGui.QApplication.translate("NuevaPlantilla", "vacío", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NuevaPlantilla", "Radicado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("NuevaPlantilla", "Radicado único:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("NuevaPlantilla", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("NuevaPlantilla", "Estado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("NuevaPlantilla", "Categoría:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCategoria.setToolTip(QtGui.QApplication.translate("NuevaPlantilla", "Click derecho para más opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCategoria.setText(QtGui.QApplication.translate("NuevaPlantilla", "Ninguna", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("NuevaPlantilla", "Prioridad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("NuevaPlantilla", "Notas:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setToolTip(QtGui.QApplication.translate("NuevaPlantilla", "Agregar un campo personalizado", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("NuevaPlantilla", "+", None, QtGui.QApplication.UnicodeUTF8))

