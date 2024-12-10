import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_ui import Ui_Login
from signIn import SignUp
from landingPage import LandingPage
from PyQt5.QtGui import QPixmap
import sqlite3

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()

        from login_ui import Ui_Login
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        # Connect sign up button
        self.ui.signUpButton.clicked.connect(self.open_signUp)
        #for login button on login == go to landingPage
        self.ui.pushButton.clicked.connect(self.loginfunction)
        
    def open_signUp(self):
        self.sign_up = SignUp()
        self.sign_up.show()
        self.close()
        
    #for when may user na
    '''def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        
        if len(user)==0 or len(password)==0:
            self.error.setText("Please complete all fields")
            
        else:
            conn = sqlite3.connect("user_data.db")
            cur = conn.cursor()
            query = 'SELECT password FROM users WHERE username =\''+user+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                print("Successfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")'''
                
    def loginfunction(self):
        self.landing_page = LandingPage()
        self.landing_page.show()
        self.close()