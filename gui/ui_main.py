# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(521, 536)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MainDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(MainDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnUpdateSLA = QtWidgets.QPushButton(MainDialog)
        self.btnUpdateSLA.setObjectName("btnUpdateSLA")
        self.horizontalLayout.addWidget(self.btnUpdateSLA)
        self.btnCreateNode = QtWidgets.QPushButton(MainDialog)
        self.btnCreateNode.setObjectName("btnCreateNode")
        self.horizontalLayout.addWidget(self.btnCreateNode)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(MainDialog)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(MainDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(MainDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(MainDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(MainDialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(MainDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(MainDialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.btnNodeSLA = QtWidgets.QPushButton(MainDialog)
        self.btnNodeSLA.setObjectName("btnNodeSLA")
        self.verticalLayout_2.addWidget(self.btnNodeSLA)

        self.retranslateUi(MainDialog)
        self.btnCreateNode.clicked.connect(MainDialog.createNode)
        self.btnNodeSLA.clicked.connect(MainDialog.getSLA)
        self.btnUpdateSLA.clicked.connect(MainDialog.updateSLAs)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Dialog"))
        self.label.setText(_translate("MainDialog", "Nodes"))
        self.btnUpdateSLA.setText(_translate("MainDialog", "Update SLA\'s"))
        self.btnCreateNode.setText(_translate("MainDialog", "Create Node"))
        self.label_2.setText(_translate("MainDialog", "Server Ip Address"))
        self.label_3.setText(_translate("MainDialog", "Username"))
        self.label_4.setText(_translate("MainDialog", "Latest Backup"))
        self.btnNodeSLA.setText(_translate("MainDialog", "Latest SLA"))
