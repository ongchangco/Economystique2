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

        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnOpenFile.clicked.connect(self.open_file)
        self.ui.btnDeleteFile.clicked.connect(self.delete_file)
        self.ui.btnAddFile.clicked.connect(self.add_file)

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
    
    def open_calendar(self):
        from calendarLogic import CalendarWindow
        self.account_window = CalendarWindow()
        self.account_window.show()
        self.close()
        
    def delete_file(self):
        #Palceholder
        from calendarLogic import CalendarWindow
        self.account_window = CalendarWindow()
        self.account_window.show()
        self.close()
        
    def open_file(self):
        #Palceholder
        from calendarLogic import CalendarWindow
        self.account_window = CalendarWindow()
        self.account_window.show()
        self.close()
        
    def add_file(self):
        