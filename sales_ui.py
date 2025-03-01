# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Joumongo\Documents\Economystique\sales.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sales(object):
    def setupUi(self, Sales):
        Sales.setObjectName("Sales")
        Sales.resize(802, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\../.designer/backup/img/econoLogo2.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Sales.setWindowIcon(icon)
        Sales.setStyleSheet("background: #f4f4ec;\n"
"color: black;\n"
"")
        self.frame = QtWidgets.QFrame(Sales)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.frame.setStyleSheet("background: #365b6d;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titleLabel_2 = QtWidgets.QLabel(self.frame)
        self.titleLabel_2.setGeometry(QtCore.QRect(0, 0, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.titleLabel_2.setFont(font)
        self.titleLabel_2.setStyleSheet("color: white;")
        self.titleLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.btnSales = QtWidgets.QPushButton(self.frame)
        self.btnSales.setGeometry(QtCore.QRect(570, 0, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnSales.setFont(font)
        self.btnSales.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSales.setStyleSheet("QPushButton {\n"
"    background-color: #365b6d;\n"
"    color: white;\n"
"    border-radius: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5b8ca4;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}\n"
"")
        self.btnSales.setObjectName("btnSales")
        self.btnInventory = QtWidgets.QPushButton(self.frame)
        self.btnInventory.setGeometry(QtCore.QRect(480, 0, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnInventory.setFont(font)
        self.btnInventory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInventory.setStyleSheet("QPushButton {\n"
"    background-color: #365b6d;\n"
"    color: white;\n"
"    border-radius: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5b8ca4;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}\n"
"")
        self.btnInventory.setObjectName("btnInventory")
        self.btnPOS = QtWidgets.QPushButton(self.frame)
        self.btnPOS.setGeometry(QtCore.QRect(660, 0, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnPOS.setFont(font)
        self.btnPOS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPOS.setStyleSheet("QPushButton {\n"
"    background-color: #365b6d;\n"
"    color: white;\n"
"    border-radius: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5b8ca4;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}\n"
"")
        self.btnPOS.setObjectName("btnPOS")
        self.btnAccount = QtWidgets.QPushButton(self.frame)
        self.btnAccount.setGeometry(QtCore.QRect(750, 0, 51, 41))
        self.btnAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccount.setStyleSheet("QPushButton {\n"
"    background-color: #365b6d;\n"
"    color: white;\n"
"    border-radius: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5b8ca4;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}\n"
"")
        self.btnAccount.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/pfBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAccount.setIcon(icon1)
        self.btnAccount.setIconSize(QtCore.QSize(40, 40))
        self.btnAccount.setObjectName("btnAccount")
        self.SalesRecords = QtWidgets.QLabel(Sales)
        self.SalesRecords.setGeometry(QtCore.QRect(9, 47, 781, 71))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(18)
        self.SalesRecords.setFont(font)
        self.SalesRecords.setAlignment(QtCore.Qt.AlignCenter)
        self.SalesRecords.setObjectName("SalesRecords")
        self.productTable = QtWidgets.QTableWidget(Sales)
        self.productTable.setGeometry(QtCore.QRect(10, 131, 781, 331))
        self.productTable.setStyleSheet("background: #ffffff")
        self.productTable.setFrameShape(QtWidgets.QFrame.Panel)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(0)
        self.productTable.setRowCount(0)
        self.label = QtWidgets.QLabel(Sales)
        self.label.setGeometry(QtCore.QRect(10, 500, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lblTotal = QtWidgets.QLabel(Sales)
        self.lblTotal.setGeometry(QtCore.QRect(100, 500, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTotal.setFont(font)
        self.lblTotal.setStyleSheet("background: white;\n"
"")
        self.lblTotal.setFrameShape(QtWidgets.QFrame.Box)
        self.lblTotal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblTotal.setText("")
        self.lblTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTotal.setObjectName("lblTotal")
        self.btnAssessment = QtWidgets.QPushButton(Sales)
        self.btnAssessment.setGeometry(QtCore.QRect(460, 510, 161, 41))
        self.btnAssessment.setStyleSheet("QPushButton{\n"
"    background: #365b6d;\n"
"    color: white;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius:10px;\n"
"    border-color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #53786d;\n"
"    border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}")
        self.btnAssessment.setObjectName("btnAssessment")
        self.forecastButton = QtWidgets.QPushButton(Sales)
        self.forecastButton.setGeometry(QtCore.QRect(630, 510, 161, 41))
        self.forecastButton.setStyleSheet("QPushButton{\n"
"    background: #365b6d;\n"
"    color: white;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius:10px;\n"
"    border-color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #53786d;\n"
"    border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/econologo_transparent_cropped.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forecastButton.setIcon(icon2)
        self.forecastButton.setIconSize(QtCore.QSize(15, 40))
        self.forecastButton.setObjectName("forecastButton")
        self.label_2 = QtWidgets.QLabel(Sales)
        self.label_2.setGeometry(QtCore.QRect(460, 560, 331, 21))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Sales)
        QtCore.QMetaObject.connectSlotsByName(Sales)

    def retranslateUi(self, Sales):
        _translate = QtCore.QCoreApplication.translate
        Sales.setWindowTitle(_translate("Sales", "EconoMystique"))
        self.titleLabel_2.setText(_translate("Sales", "EconoMystique"))
        self.btnSales.setText(_translate("Sales", "Sales"))
        self.btnInventory.setText(_translate("Sales", "Inventory"))
        self.btnPOS.setText(_translate("Sales", "POS"))
        self.SalesRecords.setText(_translate("Sales", "Sales"))
        self.label.setText(_translate("Sales", "Total"))
        self.btnAssessment.setText(_translate("Sales", "See Assessment"))
        self.forecastButton.setText(_translate("Sales", "Generate Forecast"))
        self.label_2.setText(_translate("Sales", "Powered by: GPT Neo"))
