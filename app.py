import sys
from PyQt5.QtWidgets import QApplication
from landingPage import LandingPage
from login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())