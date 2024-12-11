from PyQt5.QtWidgets import QWidget, QMainWindow
from salesForecast_ui import Ui_SalesForecast


class SalesForecastWindow(QMainWindow):
    def __init__(self):
        super(SalesForecastWindow, self).__init__()
        
        # Instantiate UI class instance
        self.ui = Ui_SalesForecast()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.signinfunction)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnAccount.clicked.connect(self.open_account)
    
    # Button Functions
        
    def open_sales(self):
        from sales import SalesWindow
        self.sales_window = SalesWindow()
        self.sales_window.show()
        self.close()
        
    def open_calendar(self):
        from calendarLogic import CalendarWindow
        self.calendar_window = CalendarWindow()
        self.calendar_window.show()
        self.close()
    
    def open_account(self):
        from account import AccountWindow
        self.account_window = AccountWindow()
        self.account_window.show()
        self.close()
        
    def signinfunction(self):
        from landingPage import LandingPage
        self.landing_page = LandingPage()
        self.landing_page.show()
        self.close()

        # Wrap setupUi logic safely
        self._setup_ui()
        self.setWindowTitle("Sales Forecast")  # Explicitly set the window title

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)
            
    