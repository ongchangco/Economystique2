from PyQt5.QtWidgets import QWidget, QMainWindow
from login_ui import Ui_Login
from signIn_ui import Ui_signUp
from PyQt5.QtGui import QPixmap

class SignUp(QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        
        from signIn_ui import Ui_signUp
        self.ui = Ui_signUp()
        self.ui.setupUi(self)
        
        # Connect login button
        self.ui.loginButton.clicked.connect(self.open_Login)
        
    def open_Login(self):
        self.login = Login()
        self.login.show()
        self.close()
        
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