from PyQt5.QtWidgets import QWidget, QMainWindow
from account_ui import Ui_account


class AccountWindow(QMainWindow):
    def __init__(self):
        super(AccountWindow, self).__init__()
        
        # Instantiate UI class instance
        self.ui = Ui_account()

        # Wrap setupUi logic safely
        self._setup_ui()
        self.setWindowTitle("Account")  # Explicitly set the window title

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)