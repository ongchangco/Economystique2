import pyqtgraph as pg

from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout
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
        self.graph_layout = QVBoxLayout()
        self.ui.graphWidget.setLayout(self.graph_layout)

    def plot_forecast(self, data):
        # Plot the forecast data using pyqtgraph
        plot_widget = pg.PlotWidget()
        self.graph_layout.addWidget(plot_widget)
        
        # Example: Add forecast data to the graph
        months = list(data.keys())
        values = list(data.values())
        plot_widget.plot(months, values, pen=pg.mkPen(color="b", width=2))
    
    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)
            
    