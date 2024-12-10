from PyQt5.QtWidgets import QWidget, QMainWindow
from sales_ui import Ui_Sales

from calendarLogic import CalendarWindow
from account import AccountWindow
from salesForecast import SalesForecastWindow
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
    
    # Button Functions
        
    def open_inventory(self):
        from landingPage import LandingPage
        self.sales_forecast_window = LandingPage()
        self.sales_forecast_window.show()
        self.close()
        
    def open_calendar(self):
        self.sales_forecast_window = CalendarWindow()
        self.sales_forecast_window.show()
        self.close()
    
    def open_account(self):
        self.sales_forecast_window = AccountWindow()
        self.sales_forecast_window.show()
        self.close()
        
    def open_forecast(self):
        self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.show()
        self.close()

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)