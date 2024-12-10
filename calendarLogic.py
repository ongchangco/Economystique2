from PyQt5.QtWidgets import QWidget, QMainWindow
from calendar_ui import Ui_Calendar


class CalendarWindow(QMainWindow):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        
        # Instantiate UI class instance
        self.ui = Ui_Calendar()

        # Wrap setupUi logic safely
        self._setup_ui()
        self.setWindowTitle("Events Calendar")  # Explicitly set the window title

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)