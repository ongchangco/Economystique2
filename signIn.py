'''import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from landingPage import LandingPage
from PyQt5.QtGui import QPixmap

class SignUp(QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        
        from signIn_ui import Ui_signUp
        self.ui = Ui_signUp()
        self.ui.setupUi(self)
        
        # Connect login button
        self.ui.loginButton.clicked.connect(self.open_Login)
        #for signin button on signup == go to landingPage
        self.ui.pushButton.clicked.connect(self.signinfunction)
        
    def open_Login(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def signinfunction(self):
        landing_page = LandingPage()
        widget.addWidget(landing_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()

        from login_ui import Ui_Login
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        # Connect sign up button
        self.ui.signUpButton.clicked.connect(self.open_signUp)
        
    def open_signUp(self):
        sign_up = SignUp()
        widget.addWidget(sign_up)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
#main
app = QApplication(sys.argv)
signUp = SignUp()
widget = QtWidgets.QStackedWidget()
widget.addWidget(signUp)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")'''