from PyQt5.QtWidgets import QApplication, QMainWindow # type: ignore
from Test import Ui_MainWindow  # Import generated UI

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Setup the UI

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()