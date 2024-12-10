from PyQt5.QtWidgets import QApplication, QMainWindow
from signIn import SignUp
from PyQt5.QtGui import QPixmap

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()

        from login_ui import Ui_Login
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        # Connect sign up button
        self.ui.signUpButton.clicked.connect(self.open_signUp)
        
    def open_signUp(self):
        self.sign_up = SignUp()
        self.sign_up.show()
        self.close()
        
    #def loginfunction(self):
    #    user = self.emailfield.text()
    #    password = self.passwordfield.text()
        
    #    if len(user)==0 or len(password)==0:
    #        self.error.setText("Please complete all fields")