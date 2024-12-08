from PyQt5.QtWidgets import QMainWindow
from landingPage_ui import Ui_MainWindow
from salesForecast import SalesForecastWindow


class LandingPage(QMainWindow):
    def __init__(self):
        super(LandingPage, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Prepare button logic to open the sales forecast window
        self.sales_forecast_window = None
        self.ui.recommendationButton.clicked.connect(self.open_forecast)

    def open_forecast(self):
        if self.sales_forecast_window is None:
            # Instantiate the window only once
            self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.show()