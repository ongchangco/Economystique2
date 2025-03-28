# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Joumongo\Documents\Economystique\addPrExisting.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPrExisting(object):
    def setupUi(self, AddPrExisting):
        AddPrExisting.setObjectName("AddPrExisting")
        AddPrExisting.resize(400, 215)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/econologo_bkgd 200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddPrExisting.setWindowIcon(icon)
        AddPrExisting.setStyleSheet("background-color: #f4f4ec;")
        self.cbProducts = QtWidgets.QComboBox(AddPrExisting)
        self.cbProducts.setGeometry(QtCore.QRect(122, 31, 261, 31))
        self.cbProducts.setStyleSheet("background: white;")
        self.cbProducts.setObjectName("cbProducts")
        self.buttonBox = QtWidgets.QDialogButtonBox(AddPrExisting)
        self.buttonBox.setGeometry(QtCore.QRect(30, 160, 341, 41))
        self.buttonBox.setStyleSheet("QPushButton{\n"
"    background: #365b6d;\n"
"    color: white;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius:10px;\n"
"    border-color: black;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #53786d;\n"
"    border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(AddPrExisting)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 91, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.teAmount = QtWidgets.QTextEdit(AddPrExisting)
        self.teAmount.setGeometry(QtCore.QRect(120, 70, 261, 31))
        self.teAmount.setStyleSheet("background: #ffffff")
        self.teAmount.setFrameShape(QtWidgets.QFrame.Panel)
        self.teAmount.setTabChangesFocus(True)
        self.teAmount.setObjectName("teAmount")
        self.teExpDate = QtWidgets.QTextEdit(AddPrExisting)
        self.teExpDate.setGeometry(QtCore.QRect(120, 110, 261, 31))
        self.teExpDate.setStyleSheet("background: #ffffff")
        self.teExpDate.setFrameShape(QtWidgets.QFrame.Panel)
        self.teExpDate.setTabChangesFocus(True)
        self.teExpDate.setObjectName("teExpDate")

        self.retranslateUi(AddPrExisting)
        QtCore.QMetaObject.connectSlotsByName(AddPrExisting)

    def retranslateUi(self, AddPrExisting):
        _translate = QtCore.QCoreApplication.translate
        AddPrExisting.setWindowTitle(_translate("AddPrExisting", "Add Existing Product"))
        self.label_3.setText(_translate("AddPrExisting", "Product to Add"))
        self.label_4.setText(_translate("AddPrExisting", "Amount"))
        self.label.setText(_translate("AddPrExisting", "Expiry Date"))
        self.teAmount.setHtml(_translate("AddPrExisting", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.teExpDate.setHtml(_translate("AddPrExisting", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
