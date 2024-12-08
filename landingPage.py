from PyQt5.QtWidgets import QMainWindow
from landingPage_ui import Ui_MainWindow
from salesForecast import SalesForecastWindow


class LandingPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize a placeholder for logic windows
        self.sales_forecast_window = None

        # Connect button signal to custom method
        self.recommendationButton.clicked.connect(self.open_forecast)

    def open_forecast(self):
        if not self.sales_forecast_window:
            self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.show()