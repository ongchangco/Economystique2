# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Joumongo\Documents\Economystique\inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inventoryManagement(object):
    def setupUi(self, inventoryManagement):
        inventoryManagement.setObjectName("inventoryManagement")
        inventoryManagement.resize(1600, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/econologo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inventoryManagement.setWindowIcon(icon)
        inventoryManagement.setStyleSheet("color: black;")
        self.InventoryStatus = QtWidgets.QLabel(inventoryManagement)
        self.InventoryStatus.setGeometry(QtCore.QRect(650, 30, 311, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.InventoryStatus.setFont(font)
        self.InventoryStatus.setStyleSheet("border: 0px solid white;\n"
"background: #365b6d;\n"
"color: white;\n"
"border-radius: 25px;")
        self.InventoryStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.InventoryStatus.setWordWrap(True)
        self.InventoryStatus.setObjectName("InventoryStatus")
        self.tabWidget = QtWidgets.QTabWidget(inventoryManagement)
        self.tabWidget.setGeometry(QtCore.QRect(20, 130, 1561, 751))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid white;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    background-color: rgba(255,255,255,164);\n"
"}\n"
"QTabBar::tab {\n"
"    background: #365b6d;\n"
"    border: 1px solid white;\n"
"    padding: 8px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    min-width: 100px;\n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #53786d;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #53786d;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tabIngredients = QtWidgets.QWidget()
        self.tabIngredients.setStyleSheet("")
        self.tabIngredients.setObjectName("tabIngredients")
        self.tabIngredientTable = QtWidgets.QTableWidget(self.tabIngredients)
        self.tabIngredientTable.setGeometry(QtCore.QRect(0, 0, 1561, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabIngredientTable.sizePolicy().hasHeightForWidth())
        self.tabIngredientTable.setSizePolicy(sizePolicy)
        self.tabIngredientTable.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabIngredientTable.setFont(font)
        self.tabIngredientTable.setStyleSheet("QTableWidget {\n"
"        background-color: rgba(255, 255, 255, 50);\n"
"        selection-background-color: #087cd4;\n"
"        selection-color: white;\n"
"        border: none;\n"
"    }\n"
"    QHeaderView::section {\n"
"        background-color: rgba(255, 255, 255, 50);\n"
"    }\n"
"    QTableWidget::item {\n"
"        background-color: rgba(255, 255, 255, 50);\n"
"    }\n"
"QTableWidget::item:selected { \n"
"        background-color: #087cd4;\n"
"        color: white;\n"
"    }")
        self.tabIngredientTable.setFrameShape(QtWidgets.QFrame.Panel)
        self.tabIngredientTable.setObjectName("tabIngredientTable")
        self.tabIngredientTable.setColumnCount(0)
        self.tabIngredientTable.setRowCount(0)
        self.btnRestock = QtWidgets.QPushButton(self.tabIngredients)
        self.btnRestock.setGeometry(QtCore.QRect(580, 620, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRestock.setFont(font)
        self.btnRestock.setStyleSheet("QPushButton{\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/restock_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRestock.setIcon(icon1)
        self.btnRestock.setObjectName("btnRestock")
        self.btnWastage = QtWidgets.QPushButton(self.tabIngredients)
        self.btnWastage.setGeometry(QtCore.QRect(780, 620, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnWastage.setFont(font)
        self.btnWastage.setStyleSheet("QPushButton{\n"
"    background: #9c272e;\n"
"    color: white;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius:10px;\n"
"    border-color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f7525d;\n"
"    border: 2px solid black;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}")
        self.btnWastage.setObjectName("btnWastage")
        self.tabWidget.addTab(self.tabIngredients, "")
        self.tabProducts = QtWidgets.QWidget()
        self.tabProducts.setStyleSheet("")
        self.tabProducts.setObjectName("tabProducts")
        self.tabProductTable = QtWidgets.QTableWidget(self.tabProducts)
        self.tabProductTable.setGeometry(QtCore.QRect(0, 0, 1561, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabProductTable.sizePolicy().hasHeightForWidth())
        self.tabProductTable.setSizePolicy(sizePolicy)
        self.tabProductTable.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabProductTable.setFont(font)
        self.tabProductTable.setStyleSheet("QTableWidget {\n"
"        background-color: rgba(255, 255, 255, 50);\n"
"        selection-background-color: #087cd4;\n"
"        selection-color: white;\n"
"        border: none;\n"
"    }\n"
"    QHeaderView::section {\n"
"        background-color: rgba(255, 255, 255, 50);\n"
"    }\n"
"    QTableWidget::item {\n"
"        background-color: rgba(255, 255, 255, 50);\n"
"    }\n"
"QTableWidget::item:selected { \n"
"        background-color: #087cd4;\n"
"        color: white;\n"
"    }")
        self.tabProductTable.setFrameShape(QtWidgets.QFrame.Panel)
        self.tabProductTable.setObjectName("tabProductTable")
        self.tabProductTable.setColumnCount(0)
        self.tabProductTable.setRowCount(0)
        self.btnAddProduct = QtWidgets.QPushButton(self.tabProducts)
        self.btnAddProduct.setGeometry(QtCore.QRect(710, 620, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAddProduct.setFont(font)
        self.btnAddProduct.setStyleSheet("QPushButton{\n"
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
        self.btnAddProduct.setIcon(icon1)
        self.btnAddProduct.setObjectName("btnAddProduct")
        self.tabWidget.addTab(self.tabProducts, "")
        self.frame = QtWidgets.QFrame(inventoryManagement)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1601, 61))
        self.frame.setStyleSheet("background: #365b6d;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnSales = QtWidgets.QPushButton(self.frame)
        self.btnSales.setGeometry(QtCore.QRect(1312, 0, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.btnInventory.setGeometry(QtCore.QRect(1202, 0, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.btnPOS.setGeometry(QtCore.QRect(1422, 0, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.btnAccount.setGeometry(QtCore.QRect(1530, 0, 71, 61))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/pfBtn.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnAccount.setIcon(icon2)
        self.btnAccount.setIconSize(QtCore.QSize(50, 50))
        self.btnAccount.setObjectName("btnAccount")
        self.btnDashboard = QtWidgets.QPushButton(self.frame)
        self.btnDashboard.setGeometry(QtCore.QRect(0, 0, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        self.btnDashboard.setFont(font)
        self.btnDashboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDashboard.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/econologo_transparent_cropped.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDashboard.setIcon(icon3)
        self.btnDashboard.setIconSize(QtCore.QSize(30, 30))
        self.btnDashboard.setObjectName("btnDashboard")

        self.retranslateUi(inventoryManagement)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(inventoryManagement)

    def retranslateUi(self, inventoryManagement):
        _translate = QtCore.QCoreApplication.translate
        inventoryManagement.setWindowTitle(_translate("inventoryManagement", "EconoMystique"))
        self.InventoryStatus.setText(_translate("inventoryManagement", "Inventory Status"))
        self.btnRestock.setText(_translate("inventoryManagement", " Restock"))
        self.btnWastage.setText(_translate("inventoryManagement", "Declare Wastage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIngredients), _translate("inventoryManagement", "Ingredients"))
        self.btnAddProduct.setText(_translate("inventoryManagement", "Add Product"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProducts), _translate("inventoryManagement", "Products"))
        self.btnSales.setText(_translate("inventoryManagement", "Sales"))
        self.btnInventory.setText(_translate("inventoryManagement", "Inventory"))
        self.btnPOS.setText(_translate("inventoryManagement", "POS"))
        self.btnDashboard.setText(_translate("inventoryManagement", "EconoMystique"))
