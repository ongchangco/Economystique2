import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        MainWindow.setStyleSheet("background: #f4f4ec;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.assessmentListView = QtWidgets.QListView(self.centralwidget)
        self.assessmentListView.setGeometry(QtCore.QRect(500, 190, 279, 221))
        self.assessmentListView.setObjectName("assessmentListView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(290, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InventoryStatus = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.InventoryStatus.setFont(font)
        self.InventoryStatus.setObjectName("InventoryStatus")
        self.verticalLayout.addWidget(self.InventoryStatus)
        self.summaryListView = QtWidgets.QListView(self.centralwidget)
        self.summaryListView.setGeometry(QtCore.QRect(10, 190, 279, 319))
        self.summaryListView.setObjectName("summaryListView")
        self.recommendationButton = QtWidgets.QPushButton(self.centralwidget)
        self.recommendationButton.setGeometry(QtCore.QRect(520, 430, 241, 61))
        self.recommendationButton.setObjectName("recommendationButton")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(310, 190, 161, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dueInButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.dueInButton.setMinimumSize(QtCore.QSize(0, 50))
        self.dueInButton.setObjectName("dueInButton")
        self.verticalLayout_2.addWidget(self.dueInButton)
        self.onHandButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.onHandButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.onHandButton.setFont(font)
        self.onHandButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.onHandButton.setDefault(False)
        self.onHandButton.setFlat(False)
        self.onHandButton.setObjectName("onHandButton")
        self.verticalLayout_2.addWidget(self.onHandButton)
        self.owedButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.owedButton.setMinimumSize(QtCore.QSize(0, 50))
        self.owedButton.setObjectName("owedButton")
        self.verticalLayout_2.addWidget(self.owedButton)
        self.Summary = QtWidgets.QLabel(self.centralwidget)
        self.Summary.setGeometry(QtCore.QRect(10, 100, 281, 78))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Summary.setFont(font)
        self.Summary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Summary.setAlignment(QtCore.Qt.AlignCenter)
        self.Summary.setObjectName("Summary")
        self.Assessment = QtWidgets.QLabel(self.centralwidget)
        self.Assessment.setGeometry(QtCore.QRect(500, 100, 281, 78))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Assessment.setFont(font)
        self.Assessment.setAlignment(QtCore.Qt.AlignCenter)
        self.Assessment.setObjectName("Assessment")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menubar.setStyleSheet("background: #365b6d;\n"
            "color:white;")
        self.menubar.setObjectName("menubar")
        self.menuInventory = QtWidgets.QMenu(self.menubar)
        self.menuInventory.setObjectName("menuInventory")
        self.menuSales = QtWidgets.QMenu(self.menubar)
        self.menuSales.setObjectName("menuSales")
        self.menuCalendar = QtWidgets.QMenu(self.menubar)
        self.menuCalendar.setObjectName("menuCalendar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuInventory.menuAction())
        self.menubar.addAction(self.menuSales.menuAction())
        self.menubar.addAction(self.menuCalendar.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())

        # Connect the Sales menu to the slot
        self.menuSales.triggered.connect(self.open_sales)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.InventoryStatus.setText(_translate("MainWindow", "Inventory Status"))
        self.recommendationButton.setText(_translate("MainWindow", "REQUEST RECOMMENDATION"))
        self.dueInButton.setText(_translate("MainWindow", "DUE-IN STOCKS"))
        self.onHandButton.setText(_translate("MainWindow", "ON-HAND STOCKS"))
        self.owedButton.setText(_translate("MainWindow", "OWED STOCKS"))
        self.Summary.setText(_translate("MainWindow", "SUMMARY"))
        self.Assessment.setText(_translate("MainWindow", "ASSESSMENT"))
        self.menuInventory.setTitle(_translate("MainWindow", "Account"))
        self.menuSales.setTitle(_translate("MainWindow", "Calendar"))
        self.menuCalendar.setTitle(_translate("MainWindow", "Sales"))
        self.menuAccount.setTitle(_translate("MainWindow", "Inventory"))
    def open_sales(self):
        """Open the sales.py file as a new process."""
        try:
            subprocess.run(["python", "sales_ui.py"], check=True)
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Could not open sales.py:\n{e}")