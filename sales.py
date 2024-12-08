from PyQt5.QtWidgets import QWidget, QMainWindow
from sales_ui import Ui_Sales


class SalesForecastWindow(QMainWindow):
    def __init__(self):
        super(SalesForecastWindow, self).__init__()
        
        # Instantiate UI class instance
        self.ui = Ui_Sales()

        # Wrap setupUi logic safely
        self._setup_ui()
        self.setWindowTitle("Sales")  # Explicitly set the window title

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)