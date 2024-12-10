from PyQt5.QtWidgets import QWidget, QMainWindow
from sales_ui import Ui_Sales
from PyQt5.QtGui import QPixmap

class SalesWindow(QMainWindow):
    def __init__(self):
        super(SalesWindow, self).__init__()
        
        # Instantiate UI class instance
        self.ui = Ui_Sales()

        # Wrap setupUi logic safely
        self._setup_ui()
        self.setWindowTitle("Sales")  # Explicitly set the window title

        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnAccount.clicked.connect(self.open_account)
        self.ui.forecastButton.clicked.connect(self.open_forecast)
    
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
        
    def open_forecast(self):
        from salesForecast import SalesForecastWindow
        self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.show()