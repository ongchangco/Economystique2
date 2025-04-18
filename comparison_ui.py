# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Joumongo\Documents\Economystique\comparison.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Comparison(object):
    def setupUi(self, Comparison):
        Comparison.setObjectName("Comparison")
        Comparison.resize(1600, 900)
        self.frame = QtWidgets.QFrame(Comparison)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/pfBtn.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnAccount.setIcon(icon)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Joumongo\\Documents\\Economystique\\img/econologo_transparent_cropped.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDashboard.setIcon(icon1)
        self.btnDashboard.setIconSize(QtCore.QSize(30, 30))
        self.btnDashboard.setObjectName("btnDashboard")
        self.label_2 = QtWidgets.QLabel(Comparison)
        self.label_2.setGeometry(QtCore.QRect(610, 30, 391, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 0px solid white;\n"
"background: #365b6d;\n"
"color: white;\n"
"border-radius: 25px;")
        self.label_2.setLineWidth(1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(Comparison)
        self.tabWidget.setGeometry(QtCore.QRect(20, 130, 1561, 751))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
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
        self.tabMonths = QtWidgets.QWidget()
        self.tabMonths.setObjectName("tabMonths")
        self.gpPerformance = QtWidgets.QWidget(self.tabMonths)
        self.gpPerformance.setGeometry(QtCore.QRect(20, 120, 1221, 561))
        self.gpPerformance.setStyleSheet("QWidget {\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    padding: 0px;\n"
"}")
        self.gpPerformance.setObjectName("gpPerformance")
        self.btnAdd = QtWidgets.QPushButton(self.tabMonths)
        self.btnAdd.setGeometry(QtCore.QRect(400, 30, 211, 61))
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
        self.cbMonth = QtWidgets.QComboBox(self.tabMonths)
        self.cbMonth.setGeometry(QtCore.QRect(140, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbMonth.setFont(font)
        self.cbMonth.setStyleSheet("background: white;")
        self.cbMonth.setObjectName("cbMonth")
        self.label_3 = QtWidgets.QLabel(self.tabMonths)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.tabMonths)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cbYear = QtWidgets.QComboBox(self.tabMonths)
        self.cbYear.setGeometry(QtCore.QRect(140, 70, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbYear.setFont(font)
        self.cbYear.setStyleSheet("background: white;")
        self.cbYear.setObjectName("cbYear")
        self.btnClrGraph = QtWidgets.QPushButton(self.tabMonths)
        self.btnClrGraph.setGeometry(QtCore.QRect(1290, 610, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btnClrGraph.setFont(font)
        self.btnClrGraph.setStyleSheet("QPushButton{\n"
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
        self.btnClrGraph.setObjectName("btnClrGraph")
        self.monthTable = QtWidgets.QTableWidget(self.tabMonths)
        self.monthTable.setGeometry(QtCore.QRect(1260, 120, 281, 461))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.monthTable.setFont(font)
        self.monthTable.setStyleSheet("QTableWidget {\n"
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
        self.monthTable.setObjectName("monthTable")
        self.monthTable.setColumnCount(0)
        self.monthTable.setRowCount(0)
        self.tabWidget.addTab(self.tabMonths, "")
        self.tabYears = QtWidgets.QWidget()
        self.tabYears.setObjectName("tabYears")
        self.gpYPerformance = QtWidgets.QWidget(self.tabYears)
        self.gpYPerformance.setGeometry(QtCore.QRect(20, 120, 1221, 561))
        self.gpYPerformance.setStyleSheet("QWidget {\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    padding: 0px;\n"
"}")
        self.gpYPerformance.setObjectName("gpYPerformance")
        self.label_8 = QtWidgets.QLabel(self.tabYears)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btnYClrGraph = QtWidgets.QPushButton(self.tabYears)
        self.btnYClrGraph.setGeometry(QtCore.QRect(1290, 610, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btnYClrGraph.setFont(font)
        self.btnYClrGraph.setStyleSheet("QPushButton{\n"
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
        self.btnYClrGraph.setObjectName("btnYClrGraph")
        self.cbYYear = QtWidgets.QComboBox(self.tabYears)
        self.cbYYear.setGeometry(QtCore.QRect(140, 40, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbYYear.setFont(font)
        self.cbYYear.setStyleSheet("background: white;")
        self.cbYYear.setObjectName("cbYYear")
        self.btnYAdd = QtWidgets.QPushButton(self.tabYears)
        self.btnYAdd.setGeometry(QtCore.QRect(400, 30, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btnYAdd.setFont(font)
        self.btnYAdd.setStyleSheet("QPushButton{\n"
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
        self.btnYAdd.setObjectName("btnYAdd")
        self.yearTable = QtWidgets.QTableWidget(self.tabYears)
        self.yearTable.setGeometry(QtCore.QRect(1260, 120, 281, 461))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.yearTable.setFont(font)
        self.yearTable.setStyleSheet("QTableWidget {\n"
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
        self.yearTable.setObjectName("yearTable")
        self.yearTable.setColumnCount(0)
        self.yearTable.setRowCount(0)
        self.tabWidget.addTab(self.tabYears, "")

        self.retranslateUi(Comparison)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Comparison)

    def retranslateUi(self, Comparison):
        _translate = QtCore.QCoreApplication.translate
        Comparison.setWindowTitle(_translate("Comparison", "Compare Perofrmance"))
        self.btnSales.setText(_translate("Comparison", "Sales"))
        self.btnInventory.setText(_translate("Comparison", "Inventory"))
        self.btnPOS.setText(_translate("Comparison", "POS"))
        self.btnDashboard.setText(_translate("Comparison", "EconoMystique"))
        self.label_2.setText(_translate("Comparison", "Compare Performance"))
        self.btnAdd.setText(_translate("Comparison", "Add to Graph"))
        self.label_3.setText(_translate("Comparison", "Month:"))
        self.label_7.setText(_translate("Comparison", "Year:"))
        self.btnClrGraph.setText(_translate("Comparison", "Clear Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMonths), _translate("Comparison", "Months"))
        self.label_8.setText(_translate("Comparison", "Year:"))
        self.btnYClrGraph.setText(_translate("Comparison", "Clear Graph"))
        self.btnYAdd.setText(_translate("Comparison", "Add to Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabYears), _translate("Comparison", "Years"))
