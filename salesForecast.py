from PyQt5 import QtWidgets
from salesForecast_ui import Ui_SalesForecast


class SalesForecastWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SalesForecast()
        self.ui.setupUi(self)

        # Place any custom logic here
        self.ui.label.setText("Welcome to the Forecast Window!")