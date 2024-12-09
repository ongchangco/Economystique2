# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Patricia\Economystique2\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Patricia\\Economystique2\\img/econologo_bkgd.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-color: #f4f4ec;\n"
"color: black;\n"
"")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 601))
        self.frame.setStyleSheet("background: #365b6d;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-50, 80, 341, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\Patricia\\Economystique2\\img/econologo_bkgd.png"))
        self.label.setObjectName("label")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setGeometry(QtCore.QRect(530, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet("color: #365b6d;")
        self.loginLabel.setObjectName("loginLabel")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(450, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(450, 190, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user.setFont(font)
        self.user.setAutoFillBackground(False)
        self.user.setStyleSheet("color: black;")
        self.user.setText("")
        self.user.setObjectName("user")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(450, 260, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(450, 290, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("color: black;")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 380, 311, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 91, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #365b6d;\n"
"    color: white;\n"
"    border: 2px solid #365b6d;\n"
"    border-radius: 50px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #289dd2;\n"
"    border: 2px solid #289dd2;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #365b6d;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 470, 161, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(610, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signUpButton.setFont(font)
        self.signUpButton.setStyleSheet("QPushButton {\n"
"    background-color: #53786d;\n"
"    color: white;\n"
"    border: 2px solid #53786d;\n"
"    border-radius: 50px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #289dd2;\n"
"    border: 2px solid #289dd2;\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: #53786d;\n"
"}\n"
"")
        self.signUpButton.setObjectName("signUpButton")
        self.forgotPass = QtWidgets.QPushButton(self.centralwidget)
        self.forgotPass.setGeometry(QtCore.QRect(650, 320, 111, 31))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.forgotPass.setFont(font)
        self.forgotPass.setStyleSheet("color: red;")
        self.forgotPass.setFlat(True)
        self.forgotPass.setObjectName("forgotPass")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(450, 350, 311, 16))
        self.error.setStyleSheet("color: red;\n"
"")
        self.error.setText("")
        self.error.setObjectName("error")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "EconoMystique"))
        self.loginLabel.setText(_translate("Login", "LOGIN"))
        self.usernameLabel.setText(_translate("Login", "Username:"))
        self.passwordLabel.setText(_translate("Login", "Password:"))
        self.pushButton.setText(_translate("Login", "LOGIN"))
        self.label_2.setText(_translate("Login", "I don\'t have an account yet"))
        self.signUpButton.setText(_translate("Login", "Sign Up"))
        self.forgotPass.setText(_translate("Login", "Forgot password?"))
