# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmInit.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmInit(object):
    def setupUi(self, frmInit):
        frmInit.setObjectName("frmInit")
        frmInit.resize(437, 266)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmInit.sizePolicy().hasHeightForWidth())
        frmInit.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmInit.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(frmInit)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(frmInit)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(frmInit)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cmbLanguage = QtWidgets.QComboBox(frmInit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLanguage.sizePolicy().hasHeightForWidth())
        self.cmbLanguage.setSizePolicy(sizePolicy)
        self.cmbLanguage.setObjectName("cmbLanguage")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbLanguage)
        self.lblServer = QtWidgets.QLabel(frmInit)
        self.lblServer.setObjectName("lblServer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblServer)
        self.txtServer = QtWidgets.QLineEdit(frmInit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtServer.sizePolicy().hasHeightForWidth())
        self.txtServer.setSizePolicy(sizePolicy)
        self.txtServer.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtServer.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtServer.setObjectName("txtServer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtServer)
        self.lblPort = QtWidgets.QLabel(frmInit)
        self.lblPort.setObjectName("lblPort")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblPort)
        self.txtPort = QtWidgets.QLineEdit(frmInit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPort.sizePolicy().hasHeightForWidth())
        self.txtPort.setSizePolicy(sizePolicy)
        self.txtPort.setObjectName("txtPort")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtPort)
        self.lblUser = QtWidgets.QLabel(frmInit)
        self.lblUser.setObjectName("lblUser")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblUser)
        self.txtUser = QtWidgets.QLineEdit(frmInit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtUser.sizePolicy().hasHeightForWidth())
        self.txtUser.setSizePolicy(sizePolicy)
        self.txtUser.setObjectName("txtUser")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtUser)
        self.lblPass = QtWidgets.QLabel(frmInit)
        self.lblPass.setObjectName("lblPass")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblPass)
        self.txtPass = QtWidgets.QLineEdit(frmInit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPass.sizePolicy().hasHeightForWidth())
        self.txtPass.setSizePolicy(sizePolicy)
        self.txtPass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtPass)
        self.label_3 = QtWidgets.QLabel(frmInit)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtXulpymoney = QtWidgets.QLineEdit(frmInit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtXulpymoney.sizePolicy().hasHeightForWidth())
        self.txtXulpymoney.setSizePolicy(sizePolicy)
        self.txtXulpymoney.setObjectName("txtXulpymoney")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtXulpymoney)
        self.verticalLayout.addLayout(self.formLayout)
        self.cmdCreate = QtWidgets.QPushButton(frmInit)
        self.cmdCreate.setObjectName("cmdCreate")
        self.verticalLayout.addWidget(self.cmdCreate)
        self.line = QtWidgets.QFrame(frmInit)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(frmInit)
        QtCore.QMetaObject.connectSlotsByName(frmInit)
        frmInit.setTabOrder(self.txtPass, self.txtXulpymoney)
        frmInit.setTabOrder(self.txtXulpymoney, self.cmdCreate)
        frmInit.setTabOrder(self.cmdCreate, self.cmbLanguage)
        frmInit.setTabOrder(self.cmbLanguage, self.txtServer)
        frmInit.setTabOrder(self.txtServer, self.txtPort)
        frmInit.setTabOrder(self.txtPort, self.txtUser)

    def retranslateUi(self, frmInit):
        _translate = QtCore.QCoreApplication.translate
        frmInit.setWindowTitle(_translate("frmInit", "Initializating Xulpymoney database"))
        self.label_4.setText(_translate("frmInit", "<html><head/><body><p>Pressing the button below, you will create needed database to run Xulpymoney. It\'ll be created in the language selected</p></body></html>"))
        self.label.setText(_translate("frmInit", "Database language"))
        self.lblServer.setText(_translate("frmInit", "Server"))
        self.txtServer.setText(_translate("frmInit", "127.0.0.1"))
        self.lblPort.setText(_translate("frmInit", "Port"))
        self.txtPort.setText(_translate("frmInit", "5432"))
        self.lblUser.setText(_translate("frmInit", "User"))
        self.txtUser.setText(_translate("frmInit", "postgres"))
        self.lblPass.setText(_translate("frmInit", "Password"))
        self.label_3.setText(_translate("frmInit", "Xulpymoney Database"))
        self.txtXulpymoney.setText(_translate("frmInit", "xulpymoney"))
        self.cmdCreate.setText(_translate("frmInit", "Create database"))

import xulpymoney.images.xulpymoney_rc
