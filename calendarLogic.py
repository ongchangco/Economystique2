from PyQt5.QtWidgets import QWidget, QMainWindow
from calendar_ui import Ui_Calendar


class CalendarWindow(QMainWindow):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        
        # Instantiate UI class instance
        self.ui = Ui_Calendar()

        # Wrap setupUi logic safely
        self._setup_ui()
        self.setWindowTitle("Events Calendar")  # Explicitly set the window title
        
        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnAccount.clicked.connect(self.open_account)

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)
            
    # Button Functions
    def open_inventory(self):
        from landingPage import LandingPage
        self.inventory_window = LandingPage()
        self.inventory_window.show()
        self.close()
        
    def open_sales(self):
        from sales import SalesWindow
        self.sales_window = SalesWindow()
        self.sales_window.show()
        self.close()
    
    def open_account(self):
        from account import AccountWindow
        self.account_window = AccountWindow()
        self.account_window.show()
        self.close()