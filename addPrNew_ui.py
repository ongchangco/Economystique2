# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Joumongo\Documents\Economystique\addPrNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addPrNew(object):
    def setupUi(self, addPrNew):
        addPrNew.setObjectName("addPrNew")
        addPrNew.resize(1000, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/econologo_bkgd 200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addPrNew.setWindowIcon(icon)
        addPrNew.setStyleSheet("background-color: #f4f4ec;")
        self.btnRemove = QtWidgets.QPushButton(addPrNew)
        self.btnRemove.setGeometry(QtCore.QRect(680, 500, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btnRemove.setFont(font)
        self.btnRemove.setStyleSheet("QPushButton{\n"
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
        self.btnRemove.setObjectName("btnRemove")
        self.btnCancel = QtWidgets.QPushButton(addPrNew)
        self.btnCancel.setGeometry(QtCore.QRect(500, 590, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btnCancel.setFont(font)
        self.btnCancel.setStyleSheet("QPushButton{\n"
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
        self.btnCancel.setObjectName("btnCancel")
        self.btnConfirm = QtWidgets.QPushButton(addPrNew)
        self.btnConfirm.setGeometry(QtCore.QRect(350, 590, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btnConfirm.setFont(font)
        self.btnConfirm.setStyleSheet("QPushButton{\n"
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
        self.btnConfirm.setObjectName("btnConfirm")
        self.btnAdd = QtWidgets.QPushButton(addPrNew)
        self.btnAdd.setGeometry(QtCore.QRect(160, 500, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btnAdd.setFont(font)
        self.btnAdd.setStyleSheet("QPushButton{\n"
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
        self.btnAdd.setObjectName("btnAdd")
        self.tabPrIngredients = QtWidgets.QTableWidget(addPrNew)
        self.tabPrIngredients.setGeometry(QtCore.QRect(510, 80, 471, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabPrIngredients.sizePolicy().hasHeightForWidth())
        self.tabPrIngredients.setSizePolicy(sizePolicy)
        self.tabPrIngredients.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabPrIngredients.setStyleSheet("background: #ffffff")
        self.tabPrIngredients.setFrameShape(QtWidgets.QFrame.Panel)
        self.tabPrIngredients.setObjectName("tabPrIngredients")
        self.tabPrIngredients.setColumnCount(0)
        self.tabPrIngredients.setRowCount(0)
        self.verticalLayoutWidget = QtWidgets.QWidget(addPrNew)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 79, 171, 121))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(addPrNew)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 410, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(addPrNew)
        self.label_16.setGeometry(QtCore.QRect(10, 360, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.cbItems = QtWidgets.QComboBox(addPrNew)
        self.cbItems.setGeometry(QtCore.QRect(140, 410, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.cbItems.setFont(font)
        self.cbItems.setStyleSheet("background: white;")
        self.cbItems.setObjectName("cbItems")
        self.frame = QtWidgets.QFrame(addPrNew)
        self.frame.setGeometry(QtCore.QRect(190, 80, 301, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lePrID = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lePrID.sizePolicy().hasHeightForWidth())
        self.lePrID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.lePrID.setFont(font)
        self.lePrID.setAutoFillBackground(False)
        self.lePrID.setStyleSheet("background: white;")
        self.lePrID.setFrame(False)
        self.lePrID.setAlignment(QtCore.Qt.AlignCenter)
        self.lePrID.setObjectName("lePrID")
        self.gridLayout.addWidget(self.lePrID, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(addPrNew)
        self.frame_2.setGeometry(QtCore.QRect(190, 120, 301, 31))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lePrName = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lePrName.sizePolicy().hasHeightForWidth())
        self.lePrName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.lePrName.setFont(font)
        self.lePrName.setAutoFillBackground(False)
        self.lePrName.setStyleSheet("background: white;")
        self.lePrName.setFrame(False)
        self.lePrName.setAlignment(QtCore.Qt.AlignCenter)
        self.lePrName.setObjectName("lePrName")
        self.gridLayout_2.addWidget(self.lePrName, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(addPrNew)
        self.frame_3.setGeometry(QtCore.QRect(140, 450, 351, 31))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.leAmount = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leAmount.sizePolicy().hasHeightForWidth())
        self.leAmount.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.leAmount.setFont(font)
        self.leAmount.setAutoFillBackground(False)
        self.leAmount.setStyleSheet("background: white;")
        self.leAmount.setFrame(False)
        self.leAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.leAmount.setObjectName("leAmount")
        self.gridLayout_3.addWidget(self.leAmount, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(addPrNew)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 961, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(addPrNew)
        self.label_13.setGeometry(QtCore.QRect(10, 220, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.lblImage = QtWidgets.QLabel(addPrNew)
        self.lblImage.setGeometry(QtCore.QRect(320, 210, 150, 140))
        self.lblImage.setStyleSheet("background: #ffffff;\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.lblImage.setText("")
        self.lblImage.setPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/cake_default.png"))
        self.lblImage.setScaledContents(True)
        self.lblImage.setObjectName("lblImage")
        self.btnImage = QtWidgets.QPushButton(addPrNew)
        self.btnImage.setGeometry(QtCore.QRect(100, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btnImage.setFont(font)
        self.btnImage.setStyleSheet("QPushButton{\n"
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
        self.btnImage.setObjectName("btnImage")
        self.frame_4 = QtWidgets.QFrame(addPrNew)
        self.frame_4.setGeometry(QtCore.QRect(190, 160, 301, 31))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lePrice = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lePrice.sizePolicy().hasHeightForWidth())
        self.lePrice.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.lePrice.setFont(font)
        self.lePrice.setAutoFillBackground(False)
        self.lePrice.setStyleSheet("background: white;")
        self.lePrice.setFrame(False)
        self.lePrice.setAlignment(QtCore.Qt.AlignCenter)
        self.lePrice.setObjectName("lePrice")
        self.gridLayout_4.addWidget(self.lePrice, 0, 0, 1, 1)

        self.retranslateUi(addPrNew)
        QtCore.QMetaObject.connectSlotsByName(addPrNew)

    def retranslateUi(self, addPrNew):
        _translate = QtCore.QCoreApplication.translate
        addPrNew.setWindowTitle(_translate("addPrNew", "New Product"))
        self.btnRemove.setText(_translate("addPrNew", "Remove"))
        self.btnCancel.setText(_translate("addPrNew", "❌Cancel"))
        self.btnConfirm.setText(_translate("addPrNew", "✔️ Confirm"))
        self.btnAdd.setText(_translate("addPrNew", "Add Ingredient"))
        self.label_11.setText(_translate("addPrNew", "Product ID"))
        self.label_12.setText(_translate("addPrNew", "Product Name"))
        self.label_17.setText(_translate("addPrNew", "Price"))
        self.label_14.setText(_translate("addPrNew", "Ingredient"))
        self.label_15.setText(_translate("addPrNew", "Amount"))
        self.label_16.setText(_translate("addPrNew", "Add Ingredient"))
        self.label_9.setText(_translate("addPrNew", "Add New Product"))
        self.label_13.setText(_translate("addPrNew", "Image"))
        self.btnImage.setText(_translate("addPrNew", "Add"))
