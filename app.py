import sys
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import openpyxl

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QFileDialog, QInputDialog, QListView, QTabWidget,QVBoxLayout, QLabel, QWidget, QTableView, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QStringListModel, pyqtSignal, QMetaObject, QThread
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from transformers import pipeline, GPTNeoForCausalLM, GPT2Tokenizer
from concurrent.futures import ThreadPoolExecutor

#additional imports for each page
from login_ui import Ui_Login
from signIn_ui import Ui_signUp
from landingPage_ui import Ui_landingPage
from salesForecast_ui import Ui_SalesForecast
from calendar_ui import Ui_Calendar
from account_ui import Ui_account
from sales_ui import Ui_Sales
from inventory_ui import Ui_inventoryManagement
from mainInventory_ui import Ui_mainInventory
#import sqlite3

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.signUpButton.clicked.connect(self.open_signUp)
        self.ui.pushButton.clicked.connect(self.loginfunction)
        
    def open_signUp(self):
        sign_up = SignUp()
        widget.addWidget(sign_up)
        widget.setCurrentIndex(widget.currentIndex()+1)
                
    def loginfunction(self):
        main_inventory = MainInventory()
        widget.addWidget(main_inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class SignUp(QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = Ui_signUp()
        self.ui.setupUi(self)
        
        self.ui.loginButton.clicked.connect(self.open_Login)
        self.ui.pushButton.clicked.connect(self.signinfunction)
        
    def open_Login(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def signinfunction(self):
        main_inventory = MainInventory()
        widget.addWidget(main_inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MainInventory(QMainWindow):
    def __init__(self):
        super(MainInventory, self).__init__()
        self.ui = Ui_mainInventory()
        self.ui.setupUi(self)

        # Load data from JSON
        self.data = self.load_cake_data()

        # Populate the product table
        self.populate_table()

        # Connect go to inventory button
        self.ui.goToInventory.clicked.connect(self.open_inventory)
        self.ui.recommendationButton.clicked.connect(self.open_forecast)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnAccount.clicked.connect(self.open_account)

        # Connect the click event of the table
        self.ui.productTable.cellClicked.connect(self.sell_product)

    def load_cake_data(self):
        try:
            with open("cake_data.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If no file or corrupt file exists, return empty data (editable)
            return []

    def populate_table(self):
        # Check if data is empty
        if not self.data:
            print("No data to populate the table.")
            return

        # Set the row count based on the number of products
        self.ui.productTable.setRowCount(len(self.data))

        # Set the column count to 5 for Product ID, Product Name, Quantity, Price, and Quantity Sold
        self.ui.productTable.setColumnCount(5)

        # Set the headers for the columns
        self.ui.productTable.setHorizontalHeaderLabels(
            ["Product ID", "Product Name", "Quantity", "Price", "Quantity Sold"])

        # Loop through each product and populate the table
        for row, product in enumerate(self.data):
            self.ui.productTable.setItem(row, 0, QTableWidgetItem(str(product["Product ID"])))
            self.ui.productTable.setItem(row, 1, QTableWidgetItem(product["Product Name"]))
            self.ui.productTable.setItem(row, 2, QTableWidgetItem(str(product["Quantity"])))
            self.ui.productTable.setItem(row, 3, QTableWidgetItem(str(product["Price"])))
            self.ui.productTable.setItem(row, 4, QTableWidgetItem(str(product["Quantity Sold"])))

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
    
    def open_inventory(self):
        inventory_window = Inventory()
        widget.addWidget(inventory_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def open_forecast(self):
        from salesForecast import SalesForecastWindow
        self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.show()

    def sell_product(self, row, column):
        if column == 0:  # Only if the Product ID column is clicked
            product_id = self.ui.productTable.item(row, 0).text()
            product_name = self.ui.productTable.item(row, 1).text()
            quantity = int(self.ui.productTable.item(row, 2).text())
            quantity_sold = int(self.ui.productTable.item(row, 4).text())

            # Ask the user how much was sold
            amount_sold, ok = QInputDialog.getInt(self, "Amount Sold", f"How many {product_name} were sold?", 1, 1, quantity)

            if ok and amount_sold > 0:
                # Update the quantities
                new_quantity = quantity - amount_sold
                new_quantity_sold = quantity_sold + amount_sold

                # Update the table view
                self.ui.productTable.setItem(row, 2, QTableWidgetItem(str(new_quantity)))
                self.ui.productTable.setItem(row, 4, QTableWidgetItem(str(new_quantity_sold)))

                # Update the data
                for product in self.data:
                    if product["Product ID"] == product_id:
                        product["Quantity"] = new_quantity
                        product["Quantity Sold"] = new_quantity_sold
                        break

                # Save the updated data
                self.save_cake_data()

    def save_cake_data(self):
        with open("cake_data.json", "w") as f:
            json.dump(self.data, f, indent=4)

class Inventory(QMainWindow):
    def __init__(self):
        super(Inventory, self).__init__()
        self.ui = Ui_inventoryManagement()
        self.ui.setupUi(self)

        # Load data from JSON
        self.data = self.load_data()

        # Initialize UI
        self.tables = {}
        tab_widget = self.ui.tabWidget
        tab_widget.clear()
        self.setup_tabs()

        # Connect buttons
        self.ui.btnSave.clicked.connect(self.save_table)
        self.ui.btnEdit.clicked.connect(self.toggle_edit_mode)
        self.ui.btnBack.clicked.connect(self.main_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnAccount.clicked.connect(self.open_account)

        self.edit_mode = False

    def main_inventory(self):
        main_inventory_window = MainInventory()
        widget.addWidget(main_inventory_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
    
    def load_data(self):
        try:
            with open("inventory_data.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If no file or corrupt file exists, return empty data (editable)
            return {}

    def save_data(self):
        with open("inventory_data.json", "w") as f:
            json.dump(self.data, f, indent=4)

    def setup_tabs(self):
        # Setup the tabs and tables for existing data
        for month, data in self.data.items():
            self.create_tab(month, data)

    def create_tab(self, name, data):
        table_widget = self.create_table(data)
        self.tables[name] = table_widget
        tab_layout = QVBoxLayout()
        tab_layout.addWidget(table_widget)

        tab_widget_container = QWidget()
        tab_widget_container.setLayout(tab_layout)
        self.ui.tabWidget.addTab(tab_widget_container, name)

    def create_table(self, data):
        table_widget = QTableWidget()
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(7)  # 7 columns as per the original example
        table_widget.setHorizontalHeaderLabels(
            ["Inventory ID", "Description", "Brand", "Unit", "On Hand", "Owed", "Due-In"])

        for row in range(len(data)):
            for col in range(len(data[row])):
                item = QTableWidgetItem(str(data[row][col]))
                table_widget.setItem(row, col, item)
        return table_widget

    def save_table(self):
        current_tab_name = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())
        table_widget = self.tables[current_tab_name]
        new_data = []

        for row in range(table_widget.rowCount()):
            row_data = []
            for col in range(table_widget.columnCount()):
                item = table_widget.item(row, col)
                row_data.append(item.text() if item else "")
            new_data.append(row_data)

        self.data[current_tab_name] = new_data
        self.save_data()

        QtWidgets.QMessageBox.information(self, "Saved", "Data saved successfully.")

        # Turn off edit mode after saving
        if self.edit_mode:
            self.toggle_edit_mode()

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode

        for table in self.tables.values():
            table.setEditTriggers(QTableWidget.AllEditTriggers if self.edit_mode else QTableWidget.NoEditTriggers)

        self.ui.tabWidget.setTabsClosable(self.edit_mode)
        if self.edit_mode:
            self.ui.tabWidget.tabBar().tabCloseRequested.connect(self.delete_tab)
            self.add_tab_button = QPushButton("+")
            self.add_tab_button.clicked.connect(self.add_tab)
            self.ui.tabWidget.setCornerWidget(self.add_tab_button, Qt.TopRightCorner)
        else:
            self.ui.tabWidget.tabBar().tabCloseRequested.disconnect(self.delete_tab)
            self.ui.tabWidget.setCornerWidget(None)

    def add_tab(self):
        new_tab_name, ok = QInputDialog.getText(self, "Add Tab", "Enter tab name:")
        if ok and new_tab_name:
            self.create_tab(new_tab_name, [])
            self.data[new_tab_name] = []
            self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.count() - 1)

    def delete_tab(self, index):
        tab_name = self.ui.tabWidget.tabText(index)
        self.ui.tabWidget.removeTab(index)
        if tab_name in self.data:
            del self.data[tab_name]
        if tab_name in self.tables:
            del self.tables[tab_name]
   
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

        # Initialize the sales_forecast_window attribute to None
        self.sales_forecast_window = None

        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnCalendar.clicked.connect(self.open_calendar)
        self.ui.btnAccount.clicked.connect(self.open_account)
        self.ui.forecastButton.clicked.connect(self.generate_sales_forecast)
        
        # Setup thread pool for async processing
        self.executor = ThreadPoolExecutor(max_workers=1)

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
        main_inventory = MainInventory()
        widget.addWidget(main_inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def open_calendar(self):
        calendar_window = CalendarWindow()
        widget.addWidget(calendar_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def open_account(self):
        account_window = AccountWindow()
        widget.addWidget(account_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def generate_sales_forecast(self):
        # Use a separate thread for the forecast generation
        self.executor.submit(self.generate_forecast)
    
    def generate_forecast(self):
        """Generate the sales forecast in a background thread."""
        try:
            # Read data from the Excel files
            sales_data = []
            for file_path in self.file_map_2.values():
                df = pd.read_excel(file_path)
                sales_data.append(df)

            # Combine sales data into a single DataFrame
            combined_data = pd.concat(sales_data, ignore_index=True)

            # Prepare data for GPT-Neo
            sales_prompt = self.prepare_sales_prompt(combined_data)

            # Create and start the worker thread for forecast generation
            self.forecast_worker = ForecastWorker(sales_prompt, self.file_map_2)
            self.forecast_worker.forecast_generated.connect(self.open_forecast)
            self.forecast_worker.start()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate sales forecast:\n{str(e)}")

    def prepare_sales_prompt(self, data):
        # Summarize data into a plain text format for GPT-Neo
        summary = "Sales data for the past months:\n"
        for _, row in data.iterrows():
            summary += f"{row.to_dict()}\n"
        summary += "\nPredict the sales for the next month based on this data:"
        return summary
        
    def open_forecast(self, forecast):
        from salesForecast import SalesForecastWindow
        if forecast is None:
            QMessageBox.warning(self, "Warning", "No forecast data available to display.")
            return

        self.sales_forecast_window = SalesForecastWindow()
        self.sales_forecast_window.ui.textBrowser.setText(forecast)
        self.sales_forecast_window.show()
        
class ForecastWorker(QThread):
    # Define a signal to pass the generated forecast back to the main thread
    forecast_generated = pyqtSignal(str)

    def __init__(self, sales_prompt, file_map_2):
        super().__init__()
        self.sales_prompt = sales_prompt
        self.file_map_2 = file_map_2

    def run(self):
        try:
            # Load tokenizer and model
            tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
            model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

            # Move model to GPU if available
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            model.to(device)

            # Tokenize the input
            inputs = tokenizer(self.sales_prompt, return_tensors="pt", truncation=True, max_length=512, padding=False)
            inputs = {key: value.to(device) for key, value in inputs.items()}

            # Generate forecast
            outputs = model.generate(
                inputs["input_ids"],
                attention_mask=inputs.get("attention_mask", None),
                max_new_tokens=50,
                num_beams=1,  # Greedy search for faster decoding
                pad_token_id=tokenizer.eos_token_id
            )

            forecast = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Emit the forecast using the signal
            self.forecast_generated.emit(forecast)

        except Exception as e:
            self.forecast_generated.emit(f"Error: {str(e)}")
        
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
        main_inventory = MainInventory()
        widget.addWidget(main_inventory)
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
        main_inventory = MainInventory()
        widget.addWidget(main_inventory)
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
    
    def get_first_file_path(self):
        """Returns the file path of the first file in the fileListView."""
        if self.ui.fileListView.model().rowCount() > 0:
            # Get the first item in the list view and return the file path
            first_item = self.ui.fileListView.model().index(0, 0).data()  # Get the first file name
            return self.file_map.get(first_item)  # Return the file path
        return None  # Return None if no files are listed
    
    def load_file_paths(self):
        """Load file paths from file_list.txt."""
        file_paths = []
        if os.path.exists('file_list.txt'):
            try:
                with open('file_list.txt', 'r') as f:
                    for line in f:
                        display_name, file_path = line.strip().split('||')
                        file_paths.append(file_path)  # Add file path to the list
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file paths:\n{str(e)}")
        return file_paths
    
    def load_inventory_data(self, file_path):
        """Load inventory data from Excel and return relevant columns."""
        inventory_data = {"on_hand": [], "owed": [], "due_in": []}
        
        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb.active
            
            for row in sheet.iter_rows(min_row=2, values_only=True):  # Skipping the header row
                inventory_name = row[1] 
                on_hand = row[4] 
                owed = row[5] 
                due_in = row[6]  
                
                if on_hand is not None:
                    inventory_data["on_hand"].append(f"{inventory_name}: {on_hand}")
                if owed is not None:
                    inventory_data["owed"].append(f"{inventory_name}: {owed}")
                if due_in is not None:
                    inventory_data["due_in"].append(f"{inventory_name}: {due_in}")
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load inventory data:\n{str(e)}")
        
        return inventory_data

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