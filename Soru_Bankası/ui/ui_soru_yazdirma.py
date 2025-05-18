from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textAlan = QtWidgets.QTextEdit(Form)
        self.textAlan.setObjectName("textAlan")
        self.verticalLayout.addWidget(self.textAlan)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.btnSec = QtWidgets.QPushButton(Form)
        self.btnSec.setObjectName("btnSec")
        self.buttonLayout.addWidget(self.btnSec)
        self.btnYazdir = QtWidgets.QPushButton(Form)
        self.btnYazdir.setObjectName("btnYazdir")
        self.buttonLayout.addWidget(self.btnYazdir)
        self.verticalLayout.addLayout(self.buttonLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form - toplu2.ui"))
        self.btnSec.setText(_translate("Form", "Yazdırılacak Soru Bankasını Seçiniz"))
        self.btnYazdir.setText(_translate("Form", "Yazdır"))