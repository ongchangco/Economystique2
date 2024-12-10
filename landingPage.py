from PyQt5.QtWidgets import QApplication, QMainWindow
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
        
    def open_forecast(self):
        from salesForecast import SalesForecastWindow
        self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.show()
        
    
        
    