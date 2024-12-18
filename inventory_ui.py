# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Patricia\Economystique2\inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inventoryManagement(object):
    def setupUi(self, inventoryManagement):
        inventoryManagement.setObjectName("inventoryManagement")
        inventoryManagement.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Patricia\\Economystique2\\img/econologo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        inventoryManagement.setWindowIcon(icon)
        inventoryManagement.setStyleSheet("background-color: #f4f4ec;\n"
"color: black;\n"
"")
        self.frame = QtWidgets.QFrame(inventoryManagement)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.frame.setStyleSheet("background: #365b6d;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: white;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.btnCalendar = QtWidgets.QPushButton(self.frame)
        self.btnCalendar.setGeometry(QtCore.QRect(660, 0, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnCalendar.setFont(font)
        self.btnCalendar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalendar.setStyleSheet("QPushButton {\n"
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
        self.btnCalendar.setObjectName("btnCalendar")
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
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Patricia\\Economystique2\\img/pfBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAccount.setIcon(icon1)
        self.btnAccount.setIconSize(QtCore.QSize(40, 40))
        self.btnAccount.setObjectName("btnAccount")
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
        self.tabWidget = QtWidgets.QTabWidget(inventoryManagement)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 801, 511))
        self.tabWidget.setStyleSheet("background-color: white;\n"
"color: black;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.btnSave = QtWidgets.QPushButton(inventoryManagement)
        self.btnSave.setGeometry(QtCore.QRect(750, 560, 41, 31))
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Patricia\\Economystique2\\img/saveIcon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnSave.setIcon(icon2)
        self.btnSave.setFlat(True)
        self.btnSave.setObjectName("btnSave")
        self.btnBack = QtWidgets.QPushButton(inventoryManagement)
        self.btnBack.setGeometry(QtCore.QRect(20, 560, 93, 28))
        self.btnBack.setStyleSheet("color: red;")
        self.btnBack.setFlat(True)
        self.btnBack.setObjectName("btnBack")
        self.btnEdit = QtWidgets.QPushButton(inventoryManagement)
        self.btnEdit.setGeometry(QtCore.QRect(710, 560, 41, 31))
        self.btnEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEdit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Patricia\\Economystique2\\img/editPfp.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnEdit.setIcon(icon3)
        self.btnEdit.setFlat(True)
        self.btnEdit.setObjectName("btnEdit")

        self.retranslateUi(inventoryManagement)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(inventoryManagement)

    def retranslateUi(self, inventoryManagement):
        _translate = QtCore.QCoreApplication.translate
        inventoryManagement.setWindowTitle(_translate("inventoryManagement", "EconoMystique"))
        self.titleLabel.setText(_translate("inventoryManagement", "EconoMystique"))
        self.btnCalendar.setText(_translate("inventoryManagement", "Calendar"))
        self.btnSales.setText(_translate("inventoryManagement", "Sales"))
        self.btnInventory.setText(_translate("inventoryManagement", "Inventory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("inventoryManagement", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("inventoryManagement", "Tab 2"))
        self.btnBack.setText(_translate("inventoryManagement", "<< Go Back"))
