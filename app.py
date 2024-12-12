import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QListView, QTabWidget,QVBoxLayout, QLabel, QWidget, QTableView
from PyQt5.QtCore import Qt, QStringListModel, pyqtSignal
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem

#additional imports for each page
from login_ui import Ui_Login
from signIn_ui import Ui_signUp
from landingPage_ui import Ui_MainWindow
from salesForecast_ui import Ui_SalesForecast
from calendar_ui import Ui_Calendar
from account_ui import Ui_account
from sales_ui import Ui_Sales
#import sqlite3

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # Connect sign up button
        self.ui.signUpButton.clicked.connect(self.open_signUp)
        #for login button on login == go to landingPage
        self.ui.pushButton.clicked.connect(self.loginfunction)
        
    def open_signUp(self):
        sign_up = SignUp()
        widget.addWidget(sign_up)
        widget.setCurrentIndex(widget.currentIndex()+1)
                
    def loginfunction(self):
        landing_page = LandingPage()
        widget.addWidget(landing_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class SignUp(QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = Ui_signUp()
        self.ui.setupUi(self)
        
        # Connect login button
        self.ui.loginButton.clicked.connect(self.open_Login)
        #for signin button on signup == go to landingPage
        self.ui.pushButton.clicked.connect(self.signinfunction)
        
    def open_Login(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def signinfunction(self):
        landing_page = LandingPage()
        widget.addWidget(landing_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class LandingPage(QMainWindow):
    def __init__(self):
        super(LandingPage, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Inventory Status")
        
        # Connect buttons
        self.ui.recommendationButton.clicked.connect(self.open_forecast)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnAccount.clicked.connect(self.open_account)
    
    # Button Functions
    def open_sales(self):
        sales_window = SalesWindow()
        widget.addWidget(sales_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def open_calendar(self):
        calendar_window = CalendarWindow()
        widget.addWidget(calendar_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def open_account(self):
        account_window = AccountWindow()
        widget.addWidget(account_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def open_forecast(self):
        from salesForecast import SalesForecastWindow
        self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.show()
        
class SalesWindow(QMainWindow):
    def __init__(self):
        super(SalesWindow, self).__init__()
        self.ui = Ui_Sales()
        self._setup_ui()
        self.setWindowTitle("Sales")

        # Load file list from storage and update tabs
        self.file_map_2 = {}
        self.load_files_2()
        self.update_tabs(list(self.file_map_2.keys()))

        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnAccount.clicked.connect(self.open_account)
        self.ui.forecastButton.clicked.connect(self.open_forecast)

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)

    def update_tabs(self, file_list):
        """Update QTabWidget based on the file list and display Excel contents."""
        tab_widget = self.ui.tabWidget
        tab_widget.clear()  # Clear existing tabs

        for file_name in file_list:
            tab = QWidget()  # Create a new tab
            tab_layout = QVBoxLayout(tab)  # Add layout to the tab

            table_view = QTableView()  # Create a QTableView
            tab_layout.addWidget(table_view)  # Add QTableView to the layout

            # Load the Excel file and populate the table
            file_path = self.file_map_2.get(file_name)
            if file_path:
                try:
                    # Read Excel file using pandas
                    df = pd.read_excel(file_path)

                    # Convert pandas DataFrame to QStandardItemModel
                    model = self._dataframe_to_model(df)

                    # Set the model to the QTableView
                    table_view.setModel(model)
                except Exception as e:
                    error_label = QLabel(f"Failed to load file {file_name}: {str(e)}")
                    tab_layout.addWidget(error_label)

            tab_widget.addTab(tab, file_name)  # Add the tab to QTabWidget

    def _dataframe_to_model(self, dataframe):
        """Convert a pandas DataFrame to a QStandardItemModel."""
        model = QStandardItemModel()
        model.setColumnCount(len(dataframe.columns))
        model.setHorizontalHeaderLabels(dataframe.columns)

        for row_idx, row in dataframe.iterrows():
            items = [QStandardItem(str(value)) for value in row]
            model.appendRow(items)

        return model

    def load_files_2(self):
        """Load files from storage."""
        if os.path.exists('file_list_2.txt'):
            try:
                with open('file_list_2.txt', 'r') as f:
                    for line in f:
                        display_name, file_path = line.strip().split('||')
                        self.file_map_2[display_name] = file_path
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load files:\n{str(e)}")
    
    # Button Functions  
    def open_inventory(self):
        inventory_window = LandingPage()
        widget.addWidget(inventory_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def open_calendar(self):
        calendar_window = CalendarWindow()
        widget.addWidget(calendar_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def open_account(self):
        account_window = AccountWindow()
        widget.addWidget(account_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def open_forecast(self):
        from salesForecast import SalesForecastWindow
        self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.show()
        
class CalendarWindow(QMainWindow):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.ui = Ui_Calendar()
        self._setup_ui()
        self.setWindowTitle("Events Calendar")
        
        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnAccount.clicked.connect(self.open_account)

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)
            
    # Button Functions
    def open_inventory(self):
        inventory_window = LandingPage()
        widget.addWidget(inventory_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def open_sales(self):
        sales_window = SalesWindow()
        widget.addWidget(sales_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def open_account(self):
        account_window = AccountWindow()
        widget.addWidget(account_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class AccountWindow(QMainWindow):
    file_list_updated_2 = pyqtSignal(list)  # Signal to emit file list
    
    def __init__(self):
        super(AccountWindow, self).__init__()
        self.ui = Ui_account()
        self._setup_ui()
        self.setWindowTitle("Account")
        
        # Set up the model for QListViews
        self.file_map = {}
        self.file_model = QStringListModel()
        self.ui.fileListView.setModel(self.file_model)
        self.file_list = []
        
        self.file_map_2 = {}
        self.file_model_2 = QStringListModel()
        self.ui.fileListView_2.setModel(self.file_model_2)
        self.file_list_2 = []

        # Load files from storage
        self.load_files()
        self.load_files_2()

        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnOpenFile.clicked.connect(self.open_file)
        self.ui.btnDeleteFile.clicked.connect(self.delete_file)
        self.ui.btnAddFile.clicked.connect(self.add_file)
        self.ui.btnOpenFile_2.clicked.connect(self.open_file_2)
        self.ui.btnDeleteFile_2.clicked.connect(self.delete_file_2)
        self.ui.btnAddFile_2.clicked.connect(self.add_file_2)
        self.ui.btnLogOut.clicked.connect(self.open_login)
    
    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)

    def open_inventory(self):
        inventory_window = LandingPage()
        widget.addWidget(inventory_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def open_sales(self):
        sales_window = SalesWindow()
        widget.addWidget(sales_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        # Connect the signal to the slot in SalesWindow
        self.file_list_updated_2.connect(sales_window.update_tabs)
        self.emit_file_list_updated_2()

    def open_calendar(self):
        account_window = CalendarWindow()
        widget.addWidget(account_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def open_login(self):
        account_login = Login()
        widget.addWidget(account_login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def delete_file(self):
        selected_indexes = self.ui.fileListView.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Warning", "Please select a file to delete.")
            return

        selected_index = selected_indexes[0]  # Only allow single selection
        display_name = self.file_model.data(selected_index, Qt.DisplayRole)
        
        # Get the corresponding file path from the file_map
        file_path = self.file_map.get(display_name)

        if not file_path:
            QMessageBox.warning(self, "Error", "File not found for deletion.")
            return
        
        del self.file_map[display_name]
        self.file_list = list(self.file_map.values())
        
        # Update the model with the new file list
        self.file_model.setStringList(list(self.file_map.keys()))
        self.save_files()

    def open_file(self):
        """Open the selected file."""
        selected_indexes = self.ui.fileListView.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Warning", "Please select a file to open.")
            return

        selected_index = selected_indexes[0]  # Only allow single selection
        display_name = self.file_model.data(selected_index, Qt.DisplayRole)
        file_path = self.file_map.get(display_name)

        if not file_path:
            QMessageBox.critical(self, "Error", f"File not found for: {display_name}")
            return

        # Attempt to open the file
        try:
            os.startfile(file_path)
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
            # Extract filename and store mapping
            display_name = os.path.basename(file_path)  # Get the filename
            self.file_map[display_name] = file_path

            # Update list view with new file
            self.file_model.setStringList(list(self.file_map.keys()))
            self.save_files()
            
    def save_files(self):
        try:
            with open('file_list.txt', 'w') as f:
                for display_name, file_path in self.file_map.items():
                    f.write(f"{display_name}||{file_path}\n")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save files:\n{str(e)}")

    def load_files(self):
        if os.path.exists('file_list.txt'):
            try:
                with open('file_list.txt', 'r') as f:
                    for line in f:
                        display_name, file_path = line.strip().split('||')
                        self.file_map[display_name] = file_path
                self.file_model.setStringList(list(self.file_map.keys()))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load files:\n{str(e)}")
                
    #Buttons for Sales Files
    def emit_file_list_updated_2(self):
        """Emit the updated file list."""
        self.file_list_updated_2.emit(list(self.file_map_2.keys()))
        
    def delete_file_2(self):
        selected_indexes = self.ui.fileListView_2.selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            display_name = self.file_model_2.data(selected_index, Qt.DisplayRole)
            self.file_map_2.pop(display_name, None)
            self.file_model_2.setStringList(list(self.file_map_2.keys()))
            self.save_files_2()
            
        else:
            QMessageBox.warning(self, "Warning", "Please select a file to delete.")
        
        self.emit_file_list_updated_2()

    def open_file_2(self):
        """Open the selected file."""
        selected_indexes = self.ui.fileListView_2.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Warning", "Please select a file to open.")
            return

        selected_index = selected_indexes[0]  # Only allow single selection
        display_name = self.file_model_2.data(selected_index, Qt.DisplayRole)
        file_path = self.file_map_2.get(display_name)

        if not file_path:
            QMessageBox.critical(self, "Error", f"File not found for: {display_name}")
            return

        # Attempt to open the file
        try:
            os.startfile(file_path)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open file:\n{str(e)}")

    def add_file_2(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select an Excel File", "",
            "Excel Files (*.xls *.xlsx);;All Files (*)",
            options=options
        )
        if file_path:
            # Extract filename and store mapping
            display_name = os.path.basename(file_path)  # Get the filename
            self.file_map_2[display_name] = file_path

            # Update list view with new file
            self.file_model_2.setStringList(list(self.file_map_2.keys()))
            self.save_files_2()
            self.emit_file_list_updated_2()
            
    def save_files_2(self):
        try:
            with open('file_list_2.txt', 'w') as f:
                for display_name, file_path in self.file_map_2.items():
                    f.write(f"{display_name}||{file_path}\n")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save files:\n{str(e)}")

    def load_files_2(self):
        if os.path.exists('file_list_2.txt'):
            try:
                with open('file_list_2.txt', 'r') as f:
                    for line in f:
                        display_name, file_path = line.strip().split('||')
                        self.file_map_2[display_name] = file_path
                self.file_model_2.setStringList(list(self.file_map_2.keys()))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load files:\n{str(e)}")
    
# main
app = QApplication(sys.argv)
login = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
widget.closeEvent = lambda event: app.quit()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")