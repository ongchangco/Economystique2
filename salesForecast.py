from PyQt5.QtWidgets import QWidget, QMainWindow
from salesForecast_ui import Ui_SalesForecast


class SalesForecastWindow(QMainWindow):
    def __init__(self):
        super(SalesForecastWindow, self).__init__()
        
        # Instantiate UI class instance
        self.ui = Ui_SalesForecast()
        self.ui.setupUi(self)
        

        # Wrap setupUi logic safely
        self._setup_ui()
        self.setWindowTitle("Sales Forecast")  # Explicitly set the window title

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)
            
    