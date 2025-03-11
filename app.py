import sys, sqlite3, os, json, torch, openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QMessageBox, QAbstractItemView, QHeaderView, QPushButton, QDialog, QFileDialog, QInputDialog, QListView, QTabWidget,QVBoxLayout, QLabel, QWidget, QTableView, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QStringListModel, pyqtSignal, QMetaObject, QThread
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem, QIcon
from transformers import pipeline, GPTNeoForCausalLM, GPT2Tokenizer
from concurrent.futures import ThreadPoolExecutor

#additional imports for each page
from login_ui import Ui_Login
from signIn_ui import Ui_signUp
from salesForecast_ui import Ui_SalesForecast
from account_ui import Ui_account
from sales_ui import Ui_Sales
from inventory_ui import Ui_inventoryManagement
from add_item_ui import Ui_Dialog
from restock_ui import Ui_Restock
from productRestock_ui import Ui_PrRestock
from addExisting_ui import Ui_AddExisting
from addPrExisting_ui import Ui_AddPrExisting
from pos_ui import Ui_pos
#import sqlite3

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.loginfunction)
        
    def open_signUp(self):
        sign_up = SignUp()
        widget.addWidget(sign_up)
        widget.setCurrentIndex(widget.currentIndex()+1)
                
    def loginfunction(self):
        inventory = Inventory()
        widget.addWidget(inventory)
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
        inventory = Inventory()
        widget.addWidget(inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Inventory(QMainWindow):
    def __init__(self):
        super(Inventory, self).__init__()
        self.ui = Ui_inventoryManagement()
        self.ui.setupUi(self)
        self.populate_ingredients()
        self.populate_products()
        self.ui.tabWidget.setCurrentIndex(0)
        # Connect buttons
        self.ui.btnRestock.clicked.connect(self.restock)
        self.ui.btnAddProduct.clicked.connect(self.addProduct)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnPOS.clicked.connect(self.open_POS)
        self.ui.btnAccount.clicked.connect(self.open_account)
        
    def populate_ingredients(self):
        # Get database connection
        db_path = os.path.join("db", "inventory_db.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Fetch all items from the inventory table
        cursor.execute("SELECT inventory_id, description, brand, unit, on_hand FROM inventory")
        inventory_items = cursor.fetchall()
        # Set up the table
        self.ui.tabIngredientTable.setRowCount(len(inventory_items)) 
        self.ui.tabIngredientTable.setColumnCount(5)
        self.ui.tabIngredientTable.verticalHeader().hide()
        # Set headers for the table
        headers = ["Inventory ID", "Description", "Brand", "Unit", "On Hand"]
        self.ui.tabIngredientTable.setHorizontalHeaderLabels(headers)
        header = self.ui.tabIngredientTable.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; }")
        header.setSectionResizeMode(QHeaderView.Stretch)
        # Set Table to Read-Only
        self.ui.tabIngredientTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tabIngredientTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # Populate the table with the data
        for row, item in enumerate(inventory_items):
            for col, value in enumerate(item):
                table_item = QTableWidgetItem(str(value))
                table_item.setTextAlignment(Qt.AlignCenter)
                self.ui.tabIngredientTable.setItem(row, col, table_item)
        # Adjust column widths to fit content
        self.ui.tabIngredientTable.resizeRowsToContents()
        conn.close()
        
    def populate_products(self):
        db_path = os.path.join("db", "product_db.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT product_id, product_name, on_hand, exp_date FROM products_on_hand")
        products = cursor.fetchall()
        self.ui.tabProductTable.setRowCount(len(products)) 
        self.ui.tabProductTable.setColumnCount(4)
        self.ui.tabProductTable.verticalHeader().hide()
        headers = ["Product ID", "Name of Product", "On Hand", "Expiry Date"]
        self.ui.tabProductTable.setHorizontalHeaderLabels(headers)
        header = self.ui.tabProductTable.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; }")
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tabProductTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tabProductTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        for row, item in enumerate(products):
            for col, value in enumerate(item):
                table_item = QTableWidgetItem(str(value))
                table_item.setTextAlignment(Qt.AlignCenter)
                self.ui.tabProductTable.setItem(row, col, table_item)
        self.ui.tabProductTable.resizeRowsToContents()
        conn.close()    
    
    def restock(self):
        restock_window = Restock()
        restock_window.restockConfirmed.connect(self.populate_ingredients)
        restock_window.exec_()
    def addProduct(self):
        addProduct_window = PrRestock()
        addProduct_window.restockConfirmed.connect(self.populate_products)
        addProduct_window.exec_()
    def open_sales(self):
        sales_window = SalesWindow()
        widget.addWidget(sales_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def open_POS(self):
        POS_window = POSWindow()
        widget.addWidget(POS_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def open_account(self):
        account_window = AccountWindow()
        widget.addWidget(account_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Restock(QDialog):
    restockConfirmed = pyqtSignal()     
    def __init__(self):
        super(Restock, self).__init__()
        self.ui = Ui_Restock()
        self.ui.setupUi(self)
        self.populate_restock_table()
        # Connect Buttons
        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnAddNew.clicked.connect(self.addNew)
        self.ui.btnRemove.clicked.connect(self.removeItem)
        self.ui.btnConfirm.clicked.connect(self.confirmItems)
        self.ui.btnCancel.clicked.connect(self.close)
    
    def connect_rsDB(self):
        db_path = os.path.join("db", "restock_db.db")
        return sqlite3.connect(db_path)
        
    def populate_restock_table(self):
        conn = self.connect_rsDB()
        cursor = conn.cursor()

        # Fetch all items from the restock table
        cursor.execute("SELECT inventory_id, description, brand, unit, amount FROM restock")
        restock_items = cursor.fetchall()

        # Set up the table
        self.ui.tabRestockTable.setRowCount(len(restock_items)) 
        self.ui.tabRestockTable.setColumnCount(5)

        # Set headers for the table
        headers = ["Inventory ID", "Description", "Brand", "Unit", "Amount"]
        self.ui.tabRestockTable.setHorizontalHeaderLabels(headers)
        header = self.ui.tabRestockTable.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; }")
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Populate the table with the data
        for row, item in enumerate(restock_items):
            for col, value in enumerate(item):
                table_item = QTableWidgetItem(str(value))
                table_item.setTextAlignment(Qt.AlignCenter)
                self.ui.tabRestockTable.setItem(row, col, table_item)
                                             
        # Adjust column widths to fit content
        self.ui.tabRestockTable.resizeRowsToContents()
        conn.close()
    
    def add(self):
        conn = self.connect_rsDB()
        add_existing_window = AddExisting(conn)
        add_existing_window.exec_()
        conn.close()
        self.populate_restock_table()
    
    def addNew(self):
        conn = self.connect_rsDB()
        add_item_window = AddItem(conn) 
        add_item_window.exec_()
        conn.close()
        self.populate_restock_table()
        
    def removeItem(self):
        # Get selected items
        selected_items = self.ui.tabRestockTable.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "No item selected. Please select a row to delete.")
            return

        # Identify unique rows from selected cells
        rows_to_delete = sorted(set(item.row() for item in selected_items), reverse=True)

        reply = QMessageBox.question(self, "Remove Item", "Are you sure you want to remove the selected items?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return

        # Connect to the database
        conn = self.connect_rsDB()
        cursor = conn.cursor()

        try:
            for row in rows_to_delete:
                # Retrieve the inventory_id from the first column
                inventory_item = self.ui.tabRestockTable.item(row, 0) 
                if inventory_item:
                    inventory_id = inventory_item.text()

                    # Delete the item from the database
                    cursor.execute("DELETE FROM restock WHERE inventory_id = ?", (inventory_id,))

                    # Remove the row from the table widget
                    self.ui.tabRestockTable.removeRow(row)
                else:
                    QMessageBox.warning(self, "Missing Data", f"Could not find Inventory ID for row {row + 1}.")

            # Commit changes to the database
            conn.commit()
            QMessageBox.information(self, "Success", "Selected item(s) removed successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to remove item(s): {e}")
        finally:
            conn.close()

        # Refresh the table to reflect the updated database
        self.populate_restock_table()
        
    def confirmItems(self):
        inv_path = os.path.join("db", "inventory_db.db")
        inv_conn = sqlite3.connect(inv_path)
        inv_cursor = inv_conn.cursor()
        
        res_conn = self.connect_rsDB()
        res_cursor = res_conn.cursor()
        
        # Fetch all entries from restock
        res_cursor.execute("SELECT * FROM restock")
        restock_entries = res_cursor.fetchall()

        for restock_entry in restock_entries:
            inventory_id, description, brand, unit, amount = restock_entry

            # Check if inventory_id exists in inventory
            inv_cursor.execute("SELECT on_hand FROM inventory WHERE inventory_id = ?", (inventory_id,))
            existing_entry = inv_cursor.fetchone()

            if existing_entry:
                # If exists, update on_hand quantity
                new_on_hand = existing_entry[0] + amount
                inv_cursor.execute("UPDATE inventory SET on_hand = ? WHERE inventory_id = ?", (new_on_hand, inventory_id))
            else:
                # If not exists, insert new entry
                inv_cursor.execute("INSERT INTO inventory (inventory_id, description, brand, unit, on_hand) VALUES (?, ?, ?, ?, ?)", 
                            (inventory_id, description, brand, unit, amount))
        
        inv_conn.commit()
        inv_conn.close()
        # Empty Restock Database        
        res_cursor.execute("DELETE FROM restock")
        res_conn.commit()
        res_conn.close()
        
        # Emit signal before closing
        self.restockConfirmed.emit()
        self.close()
        QMessageBox.information(self, "Success", "Item(s) added successfully.")
class PrRestock(QDialog):
    restockConfirmed = pyqtSignal()     
    def __init__(self):
        super(PrRestock, self).__init__()
        self.ui = Ui_PrRestock()
        self.ui.setupUi(self)
        self.populate_restock_table()
        # Connect Buttons
        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnAddNew.clicked.connect(self.addNew)
        self.ui.btnRemove.clicked.connect(self.removeProduct)
        self.ui.btnConfirm.clicked.connect(self.confirmProducts)
        self.ui.btnCancel.clicked.connect(self.close)
    
    def connect_rsDB(self):
        db_path = os.path.join("db", "prrestock_db.db")
        return sqlite3.connect(db_path)
        
    def populate_restock_table(self):
        conn = self.connect_rsDB()
        cursor = conn.cursor()
        cursor.execute("SELECT product_id, product_name, amount, exp_date FROM restock_product")
        restock_products = cursor.fetchall()
        self.ui.tabPrRestockTable.setRowCount(len(restock_products)) 
        self.ui.tabPrRestockTable.setColumnCount(4)
        self.ui.tabPrRestockTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.tabPrRestockTable.verticalHeader().hide()
        headers = ["Product ID", "Name of Product", "Amount to Add", "Expiration Date"]
        self.ui.tabPrRestockTable.setHorizontalHeaderLabels(headers)
        header = self.ui.tabPrRestockTable.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; }")
        header.setSectionResizeMode(QHeaderView.Stretch)
        for row, item in enumerate(restock_products):
            for col, value in enumerate(item):
                table_item = QTableWidgetItem(str(value))
                table_item.setTextAlignment(Qt.AlignCenter)
                self.ui.tabPrRestockTable.setItem(row, col, table_item)
        self.ui.tabPrRestockTable.resizeRowsToContents()
        conn.close()
    
    def add(self):
        conn = self.connect_rsDB()
        add_existing_window = AddPrExisting(conn)
        add_existing_window.exec_()
        conn.close()
        self.populate_restock_table()
        
    def addNew(self):
        pass
    def removeProduct(self):
        # Get selected items
        selected_items = self.ui.tabPrRestockTable.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "No item selected. Please select a row to delete.")
            return
        # Identify unique rows from selected cells
        rows_to_delete = sorted(set(item.row() for item in selected_items), reverse=True)
        reply = QMessageBox.question(self, "Remove Item", "Are you sure you want to remove the selected items?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        # Connect to the database
        conn = self.connect_rsDB()
        cursor = conn.cursor()
        try:
            for row in rows_to_delete:
                # Retrieve the product_id from the first column
                product_item = self.ui.tabPrRestockTable.item(row, 0) 
                if product_item:
                    product_id = product_item()

                    # Delete the item from the database
                    cursor.execute("DELETE FROM restock_product WHERE product_id = ?", (product_id,))

                    # Remove the row from the table widget
                    self.ui.tabPrRestockTable.removeRow(row)
                else:
                    QMessageBox.warning(self, "Missing Data", f"Could not find Product ID for row {row + 1}.")
            # Commit changes to the database
            conn.commit()
            QMessageBox.information(self, "Success", "Selected item(s) removed successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to remove item(s): {e}")
        finally:
            conn.close()
        # Refresh the table to reflect the updated database
        self.populate_restock_table()
        
    def confirmProducts(self):
        pr_path = os.path.join("db", "product_db.db")
        pr_conn = sqlite3.connect(pr_path)
        pr_cursor = pr_conn.cursor()
        
        res_conn = self.connect_rsDB()
        res_cursor = res_conn.cursor()
        
        # Fetch all entries from restock
        res_cursor.execute("SELECT * FROM restock_product")
        restock_entries = res_cursor.fetchall()

        for restock_entry in restock_entries:
            product_id, product_name, amount, exp_date = restock_entry

            # Check if product_id exists in products_on_hand
            # hayy pagod na ako (-_-)
            pr_cursor.execute("SELECT on_hand FROM products_on_hand WHERE product_id = ?", (product_id,))
            existing_entry = pr_cursor.fetchone()

            if existing_entry:
                # If exists, update on_hand quantity
                new_on_hand = existing_entry[0] + amount
                pr_cursor.execute("UPDATE products_on_hand SET on_hand = ? WHERE product_id = ?", (new_on_hand, product_id))
            else:
                # If not exists, insert new entry
                pr_cursor.execute("INSERT INTO products_on_hand (product_id, product_name, on_hand, exp_date) VALUES (?, ?, ?, ?)", 
                            (product_id, product_name, amount, exp_date))
        
        pr_conn.commit()
        pr_conn.close()
        # Empty Restock Database        
        res_cursor.execute("DELETE FROM restock_product")
        res_conn.commit()
        res_conn.close()
        
        # Emit signal before closing
        self.restockConfirmed.emit()
        self.close()
        QMessageBox.information(self, "Success", "Item(s) added successfully.")

class AddExisting(QDialog):     
    def __init__(self, conn): 
        super(AddExisting, self).__init__()
        self.ui = Ui_AddExisting()
        self.ui.setupUi(self)
        self.db_connection = conn 
        self.populate_combobox()
        self.ui.cbItems.currentIndexChanged.connect(self.update_unit_label)
        self.ui.buttonBox.accepted.connect(self.confirm)
    def populate_combobox(self):
        inv_path = os.path.join("db", "inventory_db.db")
        inv_conn = sqlite3.connect(inv_path)
        inv_cursor = inv_conn.cursor()
        # Fetch inventory_id, description, and brand
        inv_cursor.execute("SELECT inventory_id, description, brand, unit FROM inventory")
        self.inventory_items = inv_cursor.fetchall()
        # Clear existing items in the combo box
        self.ui.cbItems.clear()
        # Populate the combo box with formatted entries
        for item in self.inventory_items:
            inventory_id, description, brand, unit = item
            display_text = f"{inventory_id} - {description} ({brand})"
            self.ui.cbItems.addItem(display_text, inventory_id)  # Store inventory_id as userData
        inv_cursor.close()
        # Set initial unit label if there's at least one item
        if self.inventory_items:
            self.update_unit_label()
    def update_unit_label(self):
        index = self.ui.cbItems.currentIndex()
        if index >= 0:
            unit = self.inventory_items[index][3]
            self.ui.lblUnit.setText(f"(in {unit})")
        else:
            self.ui.lblUnit.setText("Unit: N/A")
    def confirm(self):
        try:
            index = self.ui.cbItems.currentIndex()
            if index < 0:
                QMessageBox.warning(self, "Selection Error", "Please select an item.")
                return
            # Retrieve selected item details
            inventory_id, description, brand, unit = self.inventory_items[index]
            amount_text = self.ui.teAmount.toPlainText()
            if not amount_text.strip():
                QMessageBox.warning(self, "Input Error", "Amount cannot be empty.")
                return
            amount = float(amount_text)  # Convert to float
            # Insert into the restock database
            cursor = self.db_connection.cursor()
            cursor.execute("""
                INSERT INTO restock (inventory_id, description, brand, unit, amount)
                VALUES (?, ?, ?, ?, ?)
            """, (inventory_id, description, brand, unit, amount))
            self.db_connection.commit()
            self.accept()
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter a valid numerical amount.")
        except sqlite3.IntegrityError as e:
            QMessageBox.critical(self, "Database Error", f"Failed to add item: {e}")
            
class AddPrExisting(QDialog):     
    def __init__(self, conn): 
        super(AddPrExisting, self).__init__()
        self.ui = Ui_AddPrExisting()
        self.ui.setupUi(self)
        self.db_connection = conn 
        self.populate_combobox()
        self.ui.buttonBox.accepted.connect(self.confirm)
    def populate_combobox(self):
        pr_path = os.path.join("db", "product_db.db")
        pr_conn = sqlite3.connect(pr_path)
        pr_cursor = pr_conn.cursor()
        # Fetch product_id, product_name
        pr_cursor.execute("SELECT product_id, product_name, exp_date FROM products_on_hand")
        self.product_items = pr_cursor.fetchall()
        # Clear existing items in the combo box
        self.ui.cbProducts.clear()
        # Populate the combo box with formatted entries
        for item in self.product_items:
            product_id, product_name, exp_date = item
            display_text = f"{product_id} - {product_name}"
            self.ui.cbProducts.addItem(display_text, product_id)
        pr_cursor.close()
    def confirm(self):
        try:
            index = self.ui.cbProducts.currentIndex()
            if index < 0:
                QMessageBox.warning(self, "Selection Error", "Please select an item.")
                return
            # Retrieve selected item details
            product_id, product_name, exp_date = self.product_items[index]
            amount_text = self.ui.teAmount.toPlainText()
            if not amount_text.strip():
                QMessageBox.warning(self, "Input Error", "Amount cannot be empty.")
                return
            amount = int(amount_text)
            # Insert into the restock database
            cursor = self.db_connection.cursor()
            cursor.execute("""
                INSERT INTO restock_product (product_id, product_name, amount, exp_date)
                VALUES (?, ?, ?, ?)
            """, (product_id, product_name, amount, exp_date))
            self.db_connection.commit()
            self.accept()
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter a valid numerical amount.")
        except sqlite3.IntegrityError as e:
            QMessageBox.critical(self, "Database Error", f"Failed to add item: {e}")

class AddItem(QDialog):     
    def __init__(self, conn):
        super(AddItem, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db_connection = conn
        # Connect buttons
        self.ui.buttonBox.accepted.connect(self.confirm)
        
    def confirm(self):
        try:
            inventory_id = self.ui.teInvID.toPlainText()
            description = self.ui.teDescription.toPlainText()
            brand = self.ui.teBrand.toPlainText()
            unit = self.ui.teUnit.toPlainText()
            amount = float(self.ui.teAmount.toPlainText())

            # Ensure Inventory ID is provided or unique
            if not inventory_id:
                QMessageBox.warning(self, "Input Error", "Inventory ID is required.")
                return

            # Insert into database
            cursor = self.db_connection.cursor()
            cursor.execute("""
            INSERT INTO restock (inventory_id, description, brand, unit, amount)
            VALUES (?, ?, ?, ?, ?)
            """, (inventory_id, description, brand, unit, amount))
            self.db_connection.commit()
            self.accept() 
            
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please ensure all numerical fields have valid numbers.")
        except sqlite3.IntegrityError as e:
            QMessageBox.critical(self, "Database Error", f"Failed to add item: {e}")
        
class SalesWindow(QMainWindow):
    def __init__(self):
        super(SalesWindow, self).__init__()
        self.ui = Ui_Sales()
        self.ui.setupUi(self)
       
        self.load_sales_data()

        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnPOS.clicked.connect(self.open_POS)
        self.ui.btnAccount.clicked.connect(self.open_account)
        
    def load_sales_data(self):
        sales_path = os.path.join("db", "sales_db.db")
        sales_conn = sqlite3.connect(sales_path)
        sales_cursor = sales_conn.cursor()
        # Fetch all items from the inventory table
        sales_cursor.execute("SELECT product_id, product_name, price, quantity_sold FROM sales")
        products = sales_cursor.fetchall()

        # Set up the table
        self.ui.productTable.setRowCount(len(products)) 
        self.ui.productTable.setColumnCount(4)

        # Set headers for the table
        headers = ["Product ID", "Product Name", "Price", "Quantity Sold"]
        self.ui.productTable.setHorizontalHeaderLabels(headers)
        header = self.ui.productTable.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; }")
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Populate the table with the data
        for row, item in enumerate(products):
            for col, value in enumerate(item):
                table_item = QTableWidgetItem(str(value))
                table_item.setTextAlignment(Qt.AlignCenter)
                self.ui.productTable.setItem(row, col, table_item)
        
        # Compute & Display Total Sales
        total = sum(item[2] * item[3] for item in products)
        self.ui.lblTotal.setText(f"{total:.2f}")
            
    # Button Functions  
    def open_inventory(self):
        inventory = Inventory()
        widget.addWidget(inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def open_POS(self):
        POS_window = POSWindow()
        widget.addWidget(POS_window)
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
        
'''
class ForecastWorker(QThread):
    # Signal to pass the generated forecast back to the main thread
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
'''
class POSWindow(QMainWindow):
    def __init__(self):
        super(POSWindow, self).__init__()
        self.ui = Ui_pos()
        self.ui.setupUi(self)
        self.setWindowTitle("POS")

        # Create a model for the QListView
        self.cart_model = QStandardItemModel()
        self.ui.cartList.setModel(self.cart_model)
        
        self.total_price = 0.0
        self.update_total_label()

        # Connect buttons to functions
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnAccount.clicked.connect(self.open_account)
        
        self.ui.btnClear.clicked.connect(self.clear_cart)
        self.ui.btnCheckout.clicked.connect(self.checkout)
        
        # Connect product buttons to their respective functions
        self.ui.btnC001.clicked.connect(lambda: self.add_to_cart("C001"))
        self.ui.btnC002.clicked.connect(lambda: self.add_to_cart("C002"))
        self.ui.btnC003.clicked.connect(lambda: self.add_to_cart("C003"))
        self.ui.btnC004.clicked.connect(lambda: self.add_to_cart("C004"))
        self.ui.btnC005.clicked.connect(lambda: self.add_to_cart("C005"))
        self.ui.btnC006.clicked.connect(lambda: self.add_to_cart("C006"))
        self.ui.btnC007.clicked.connect(lambda: self.add_to_cart("C007"))
        self.ui.btnC008.clicked.connect(lambda: self.add_to_cart("C008"))
        self.ui.btnC009.clicked.connect(lambda: self.add_to_cart("C009"))
        self.ui.btnC010.clicked.connect(lambda: self.add_to_cart("C010"))
    
    def add_to_cart(self, product_id):
        # Connect to the sales database
        connection = sqlite3.connect("db/sales_db.db")
        cursor = connection.cursor()

        # Query the sales table for the product
        cursor.execute("SELECT product_name, price FROM sales WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()  # Fetch one result
        connection.close()

        if product:
            # Check if the product is already in the cart
            existing_items = [self.cart_model.item(row) for row in range(self.cart_model.rowCount())]
            product_details = f"{product[0]} @ {product[1]:.2f}"

            # Add the product price to the total price
            self.total_price += product[1]
            self.update_total_label()

            for item in existing_items:
                if item.text().startswith(product[0]):  # Check if product already in cart
                    # If already in the cart, increase the quantity (optional step)
                    item.setText(item.text() + " (Qty: 2)")  # Modify this part to handle actual quantity increment
                    return  # Exit if the product already exists

            # Add the product details to the cart model if not already added
            item = QStandardItem(product_details)
            self.cart_model.appendRow(item)
    
    def clear_cart(self):
        self.cart_model.clear()
        self.total_price = 0.0
        self.update_total_label()
        
    def update_total_label(self):
        # Update the lblTotal label with the total price
        self.ui.lblTotal.setText(f"Total: {self.total_price:.2f}")
        
    def checkout(self):
        # Check if the cart is empty
        if self.cart_model.rowCount() == 0:
            QMessageBox.warning(self, "Error", "Your cart is empty.", QMessageBox.Ok)
            return

        confirmation = QMessageBox.question(
            self, "Confirm Checkout", "Are you sure you want to check out with these products?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if confirmation == QMessageBox.No:
            return  # Exit if "No" is clicked

        # Process the checkout and update the sales and inventory database
        for row in range(self.cart_model.rowCount()):
            product_details = self.cart_model.item(row).text()
            product_name = product_details.split(" @")[0]  # Extract product_name
            quantity = 1  # Adjust this to reflect how many of the product were bought (if applicable)

            # Connect to the sales database
            connection = sqlite3.connect("db/sales_db.db")
            cursor = connection.cursor()

            cursor.execute("SELECT product_id, price FROM sales WHERE product_name = ?", (product_name,))
            product = cursor.fetchone()
            connection.close()

            if product:
                product_id = product[0]
                # Update the quantity_sold in the sales table
                connection = sqlite3.connect("db/sales_db.db")
                cursor = connection.cursor()
                cursor.execute(""" 
                    UPDATE sales
                    SET quantity_sold = quantity_sold + ?
                    WHERE product_id = ?
                """, (quantity, product_id))
                connection.commit()
                connection.close()

                # Now update the inventory by subtracting the ingredients
                connection = sqlite3.connect("db/ingredients_db.db")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM ingredients WHERE product_id = ?", (product_id,))
                ingredients = cursor.fetchone()  # Get the ingredients for the product

                if ingredients:
                    # Loop through the ingredient columns (IN001, IN002, IN003, etc.)
                    for i, ingredient_quantity in enumerate(ingredients[1:], start=1):  # Skip the first column (product_id)
                        if ingredient_quantity:  # If the quantity for the ingredient is not zero
                            ingredient_id = f"IN{str(i).zfill(3)}"  # Construct the ingredient_id (e.g., IN001, IN002, ...)
                            
                            # Fetch the current inventory for this ingredient
                            connection_inventory = sqlite3.connect("db/inventory_db.db")
                            cursor_inventory = connection_inventory.cursor()
                            cursor_inventory.execute("SELECT on_hand FROM inventory WHERE inventory_id = ?", (ingredient_id,))
                            inventory = cursor_inventory.fetchone()

                            if inventory:
                                on_hand = inventory[0]
                                # Subtract the quantity sold of this ingredient from the on_hand
                                new_on_hand = on_hand - (ingredient_quantity * quantity)  # Adjust for the sold quantity

                                # Check if there's enough stock to subtract
                                if new_on_hand < 0:
                                    QMessageBox.warning(self, "Error", f"Not enough stock for ingredient {ingredient_id}.")
                                    return  # Stop the checkout process if any ingredient is out of stock

                                # Update the inventory by subtracting the quantity
                                cursor_inventory.execute("""
                                    UPDATE inventory
                                    SET on_hand = ?
                                    WHERE inventory_id = ?
                                """, (new_on_hand, ingredient_id))
                                connection_inventory.commit()
                                connection_inventory.close()
                connection.close()

        QMessageBox.information(self, "Success", "Checkout successful!", QMessageBox.Ok)

        # Clear the cart and reset the total
        self.clear_cart()
        self.total_price = 0.0
        self.update_total_label()

    # Button Functions
    def open_sales(self):
        sales_window = SalesWindow()
        widget.addWidget(sales_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def open_account(self):
        account_window = AccountWindow()
        widget.addWidget(account_window)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def open_inventory(self):
        inventory_window = Inventory()
        widget.addWidget(inventory_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
class AccountWindow(QMainWindow):
    def __init__(self):
        super(AccountWindow, self).__init__()
        self.ui = Ui_account()
        self._setup_ui()
        self.setWindowTitle("Account")
        
        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnPOS.clicked.connect(self.open_POS)
        self.ui.btnLogOut.clicked.connect(self.open_login)
    
    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)

    def open_inventory(self):
        inventory = Inventory()
        widget.addWidget(inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def open_sales(self):
        sales_window = SalesWindow()
        widget.addWidget(sales_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def open_POS(self):
        POS_window = POSWindow()
        widget.addWidget(POS_window)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def open_login(self):
        account_login = Login()
        widget.addWidget(account_login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
# main
app = QApplication(sys.argv)
login = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
windowIconPath = os.path.join(os.path.dirname(__file__), "img", "econologo_bkgd.png")
widget.setWindowIcon(QIcon(windowIconPath))
widget.setWindowTitle("Economystique")
widget.show()
widget.closeEvent = lambda event: app.quit()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")