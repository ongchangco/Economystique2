import os
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QListView, QMainWindow
from PyQt5.QtCore import QStringListModel
from account_ui import Ui_account

class AccountWindow(QMainWindow):
    def __init__(self):
        super(AccountWindow, self).__init__()

        # Instantiate UI class instance
        self.ui = Ui_account()

        # Wrap setupUi logic safely
        self._setup_ui()
        self.setWindowTitle("Account") # Explicitly set the window title

        # Set up the model for QListView
        self.file_model = QStringListModel()
        self.ui.fileListView.setModel(self.file_model)
        self.file_list = [] # Stores file paths

        # Load files from storage
        self.load_files()

        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnOpenFile.clicked.connect(self.open_file)
        self.ui.btnDeleteFile.clicked.connect(self.delete_file)
        self.ui.btnAddFile.clicked.connect(self.add_file)
        self.ui.btnLogOut.clicked.connect(self.log_out)

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)

    def open_inventory(self):
        from landingPage import LandingPage
        self.inventory_window = LandingPage()
        self.inventory_window.show()
        self.close()

    def open_sales(self):
        from sales import SalesWindow
        self.sales_window = SalesWindow()
        self.sales_window.show()
        self.close()

    def open_calendar(self):
        from calendarLogic import CalendarWindow
        self.account_window = CalendarWindow()
        self.account_window.show()
        self.close()

    def delete_file(self):
        """Delete the selected file from the list."""
        selected_indexes = self.ui.fileListView.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Warning", "Please select a file to delete.")
            return

        selected_index = selected_indexes[0] # Only allow single selection
        file_path = self.file_list[selected_index.row()]

        # Confirm deletion
        reply = QMessageBox.question(
            self, "Confirm Deletion",
            f"Are you sure you want to delete:\n{file_path}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.file_list.pop(selected_index.row())
            self.file_model.setStringList(self.file_list)
            self.save_files()

    def open_file(self):
        """Open the selected file."""
        selected_indexes = self.ui.fileListView.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Warning", "Please select a file to open.")
            return

        selected_index = selected_indexes[0] # Only allow single selection
        file_path = self.file_list[selected_index.row()]

        # Open the file (use an appropriate library for Excel files if needed)
        try:
            os.startfile(file_path) # Windows-specific; use subprocess for other platforms
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open file:\n{str(e)}")

    def add_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select an Excel File", "",
            "Excel Files (*.xls *.xlsx);;All Files (*)",
            options=options
        )
        if file_path:
            self.file_list.append(file_path)
            self.file_model.setStringList(self.file_list)
            self.save_files()

    def save_files(self):
        """Save the file list to a local file."""
        try:
            with open('file_list.txt', 'w') as f:
                for file_path in self.file_list:
                    f.write(file_path + '\n')
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save files:\n{str(e)}")

    def load_files(self):
        """Load the file list from a local file."""
        if os.path.exists('file_list.txt'):
            try:
                with open('file_list.txt', 'r') as f:
                    self.file_list = [line.strip() for line in f.readlines()]
                self.file_model.setStringList(self.file_list)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load files:\n{str(e)}")

    def log_out(self):
        from login import Login
        self.sales_window = Login()
        self.sales_window.show()
        self.close()