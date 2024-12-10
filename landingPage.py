from PyQt5.QtWidgets import QApplication, QMainWindow
from sales import SalesWindow
from calendarLogic import CalendarWindow
from account import AccountWindow
from salesForecast import SalesForecastWindow
from PyQt5.QtGui import QPixmap

class LandingPage(QMainWindow):
    def __init__(self):
        super(LandingPage, self).__init__()
        
        from landingPage_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        
        # Connect buttons
        self.ui.recommendationButton.clicked.connect(self.open_forecast)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnAccount.clicked.connect(self.open_account)
    
    # Button Functions
        
    def open_sales(self):
        self.sales_forecast_window = SalesWindow()
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
        
    
        
    