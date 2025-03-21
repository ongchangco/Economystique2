import sys, sqlite3, os, json, torch, openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QMessageBox, QAbstractItemView, QHeaderView, QPushButton, QDialog, QFileDialog, QInputDialog, QListView, QTabWidget,QVBoxLayout, QLabel, QWidget, QTableView, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QStringListModel, pyqtSignal, QMetaObject, QTimer
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem, QIcon, QColor
from transformers import pipeline, GPTNeoForCausalLM, GPT2Tokenizer
from concurrent.futures import ThreadPoolExecutor

#additional imports for each page
from login_ui import Ui_Login
from signIn_ui import Ui_signUp
from dashboard_ui import Ui_Dashboard
from salesForecast_ui import Ui_SalesForecast
from account_ui import Ui_account
from sales_ui import Ui_Sales
from inventory_ui import Ui_inventoryManagement
from add_item_ui import Ui_Dialog
from restock_ui import Ui_Restock
from productRestock_ui import Ui_PrRestock
from addCritical_ui import Ui_AddCritical
from addExisting_ui import Ui_AddExisting
from addPrExisting_ui import Ui_AddPrExisting
from addPrNew_ui import Ui_addPrNew
from pos_ui import Ui_pos

class MainWindow(QMainWindow):
    switch_to_login = pyqtSignal()
    def __init__(self, icon_path):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Economystique")
        self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(1600, 900)

        # Create your stacked widget for Dashboard, Inventory, etc.
        self.widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.widget)

        # Initialize pages
        self.dashboard = Dashboard()
        self.inventory = Inventory(self.widget)
        self.sales = SalesWindow(self.widget)
        self.POS = POSWindow(self.widget)
        self.account = AccountWindow(self.widget)

        # Add widgets to stackedWidget
        self.widget.addWidget(self.dashboard)
        self.widget.addWidget(self.inventory)
        self.widget.addWidget(self.sales)
        self.widget.addWidget(self.POS)
        self.widget.addWidget(self.account)

        # Connect widget signals to handlers
        self.dashboard.go_to_inventory.connect(self.show_inventory)
        self.dashboard.go_to_sales.connect(self.show_sales)
        self.dashboard.go_to_pos.connect(self.show_pos)
        self.dashboard.go_to_account.connect(self.show_account)
        self.dashboard.critical_item_selected.connect(self.focus_critical_item)
        
        self.inventory.go_to_dashboard.connect(self.show_dashboard)
        self.inventory.go_to_sales.connect(self.show_sales)
        self.inventory.go_to_pos.connect(self.show_pos)
        self.inventory.go_to_account.connect(self.show_account)
        
        self.sales.go_to_inventory.connect(self.show_inventory)
        self.sales.go_to_dashboard.connect(self.show_dashboard)
        self.sales.go_to_pos.connect(self.show_pos)
        self.sales.go_to_account.connect(self.show_account)
        
        self.POS.go_to_inventory.connect(self.show_inventory)
        self.POS.go_to_sales.connect(self.show_sales)
        self.POS.go_to_dashboard.connect(self.show_dashboard)
        self.POS.go_to_account.connect(self.show_account)
        
        self.account.go_to_inventory.connect(self.show_inventory)
        self.account.go_to_sales.connect(self.show_sales)
        self.account.go_to_pos.connect(self.show_pos)
        self.account.go_to_dashboard.connect(self.show_dashboard)
        self.account.switch_to_login.connect(self.logout_to_login)

        # Landing Page
        self.widget.setCurrentWidget(self.dashboard)

    def show_dashboard(self):
        self.widget.setCurrentWidget(self.dashboard)
    
    def show_inventory(self):
        self.widget.setCurrentWidget(self.inventory)

    def show_sales(self):
        self.widget.setCurrentWidget(self.sales)

    def show_pos(self):
        self.widget.setCurrentWidget(self.POS)

    def show_account(self):
        self.widget.setCurrentWidget(self.account)
        
    def focus_critical_item(self, inventory_id):
        self.widget.setCurrentWidget(self.inventory)
        self.inventory.focus_on_item(inventory_id)
        
    def logout_to_login(self):
        self.switch_to_login.emit()
        self.close()

class Login(QMainWindow):
    switch_to_signup = pyqtSignal()
    switch_to_main = pyqtSignal()

    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(800, 600)
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.loginfunction)
        self.ui.signUpButton.clicked.connect(self.open_signUp)  # Example button name for SignUp

    def open_signUp(self):
        self.switch_to_signup.emit()
        self.close()

    def loginfunction(self):
        self.switch_to_main.emit()
        self.close()
        
class SignUp(QMainWindow):
    switch_to_login = pyqtSignal()
    switch_to_main = pyqtSignal()

    def __init__(self):
        super(SignUp, self).__init__()
        self.setWindowTitle("Sign Up")
        self.setFixedSize(800, 600)
        self.ui = Ui_signUp()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.open_Login)
        self.ui.pushButton.clicked.connect(self.signinfunction)

    def open_Login(self):
        self.switch_to_login.emit()
        self.close()

    def signinfunction(self):
        self.switch_to_main.emit()
        self.close()

class Dashboard(QMainWindow):
    go_to_inventory = pyqtSignal()
    go_to_sales = pyqtSignal()
    go_to_pos = pyqtSignal()
    go_to_account = pyqtSignal()
    critical_item_selected = pyqtSignal(str)
    def __init__(self):
        super(Dashboard, self).__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        self.populate_crit_list()
        
        # Connect Buttons
        self.ui.btnInventory.clicked.connect(self.go_to_inventory.emit)
        self.ui.btnSales.clicked.connect(self.go_to_sales.emit)
        self.ui.btnPOS.clicked.connect(self.go_to_pos.emit)
        self.ui.btnAccount.clicked.connect(self.go_to_account.emit)
        self.ui.lsCritical.itemDoubleClicked.connect(self.on_critical_item_clicked)
        
    def populate_crit_list(self):
        # Get DB Connection
        db_path = os.path.join("db", "inventory_db.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT inventory_id, description, on_hand, unit FROM inventory WHERE on_hand <= rop
            """)
        critItems = cursor.fetchall()
        self.ui.lsCritical.clear()
        # Loop through results and format each item
        for inventory_id, description, on_hand, unit in critItems:
            list_item_text = f"{inventory_id} - {description} @ {int(on_hand)} {unit}"
            self.ui.lsCritical.addItem(list_item_text)
        conn.close()
        
    def on_critical_item_clicked(self, item):
        inventory_id = item.text().split(' - ')[0]
        # You can emit a different signal with data if you want:
        self.critical_item_selected.emit(inventory_id)
    
class Inventory(QMainWindow):
    go_to_dashboard = pyqtSignal()
    go_to_sales = pyqtSignal()
    go_to_pos = pyqtSignal()
    go_to_account = pyqtSignal()
    def __init__(self, widget=None):
        super(Inventory, self).__init__()
        self.ui = Ui_inventoryManagement()
        self.ui.setupUi(self)
        self.widget = widget
        self.populate_ingredients()
        self.populate_products()
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabIngredientTable.itemDoubleClicked.connect(self.restock_ROP)
        # Connect buttons
        self.ui.btnRestock.clicked.connect(self.restock)
        self.ui.btnAddProduct.clicked.connect(self.addProduct)
        self.ui.btnDashboard.clicked.connect(self.go_to_dashboard.emit)
        self.ui.btnSales.clicked.connect(self.go_to_sales.emit)
        self.ui.btnPOS.clicked.connect(self.go_to_pos.emit)
        self.ui.btnAccount.clicked.connect(self.go_to_account.emit)
    
    def populate_ingredients(self):
        # Get database connection
        db_path = os.path.join("db", "inventory_db.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Fetch all items from the inventory table INCLUDING rop
        cursor.execute("""
            SELECT inventory_id, description, brand, unit, on_hand, rop
            FROM inventory
        """)
        inventory_items = cursor.fetchall()
        # Set up the table
        self.ui.tabIngredientTable.setRowCount(len(inventory_items)) 
        self.ui.tabIngredientTable.setColumnCount(5)  # Still 5 columns shown (excluding rop)
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
            inventory_id, description, brand, unit, on_hand, rop = item
            # Safe type conversion
            on_hand = int(on_hand) if on_hand is not None else 0
            rop = int(rop) if rop is not None else 0
            # Prepare the row values (excluding rop from the table display)
            row_values = [inventory_id, description, brand, unit, on_hand]
            # Loop through each column and insert items
            for col, value in enumerate(row_values):
                table_item = QTableWidgetItem(str(value))
                table_item.setTextAlignment(Qt.AlignCenter)
                # ROP Checker
                if on_hand <= rop:
                    table_item.setForeground(QColor("red"))
                    table_item.setBackground(QColor("#f4f4ec"))

                self.ui.tabIngredientTable.setItem(row, col, table_item)
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
    
    def focus_on_item(self, inventory_id):
        table = self.ui.tabIngredientTable
        row_to_focus = -1

        for row in range(table.rowCount()):
            item = table.item(row, 0)  # Column 0 = inventory_id
            if item and item.text() == inventory_id:
                row_to_focus = row
                break

        if row_to_focus >= 0:
            table.selectRow(row_to_focus)
            table.scrollToItem(table.item(row_to_focus, 0), QtWidgets.QAbstractItemView.PositionAtCenter)
            table.setFocus()
    
    def restock_ROP(self, item):
        row = item.row()
        first_item = self.ui.tabIngredientTable.item(row, 0)

        if first_item and first_item.foreground().color() == QColor("red"):
            # Get inventory_id and description from the row
            inventory_id_item = self.ui.tabIngredientTable.item(row, 0)
            description_item = self.ui.tabIngredientTable.item(row, 1)
            unit_item = self.ui.tabIngredientTable.item(row, 3)

            inventory_id = inventory_id_item.text() if inventory_id_item else ""
            description = description_item.text() if description_item else ""
            unit = unit_item.text() if description_item else ""
            
            # Open the AddCritical dialog and pass inventory_id & description
            conn = sqlite3.connect(os.path.join("db", "inventory_db.db"))
            add_critical_window = AddCritical(conn, inventory_id, description, unit)
            
            # Connect the signal to refresh after restocking
            add_critical_window.restockConfirmed.connect(self.populate_ingredients)

            add_critical_window.exec_()
            conn.close()
    
    def restock(self):
        restock_window = Restock()
        restock_window.restockConfirmed.connect(self.populate_ingredients)
        restock_window.exec_()
        
    def addProduct(self):
        addProduct_window = PrRestock()
        addProduct_window.restockConfirmed.connect(self.populate_products)
        addProduct_window.exec_()
        
class AddCritical(QDialog):
    restockConfirmed = pyqtSignal()
    def __init__(self, conn, inventory_id=None, description=None, unit=None):
        super(AddCritical, self).__init__()
        self.ui = Ui_AddCritical()
        self.ui.setupUi(self)
        self.db_connection = conn
        self.inventory_id = inventory_id 
        self.unit = unit
        self.ui.lblCriticalItem.setText(f"{inventory_id} - {description}")
        self.ui.lblAmount.setText(f"Amount to add (in {unit})")
        # Connect Buttons
        self.ui.buttonBox.accepted.connect(self.confirm)
        self.ui.buttonBox.rejected.connect(self.close)
        
        
    def confirm(self):
        try:
            amount_text = self.ui.teAmount.toPlainText()
            # Validate amount is provided
            if not amount_text.strip():
                QMessageBox.warning(self, "Input Error", "Amount cannot be empty.")
                return
            # Convert amount to float
            amount = float(amount_text)
            cursor = self.db_connection.cursor()
            # Fetch current on_hand
            cursor.execute("""
                SELECT on_hand FROM inventory WHERE inventory_id = ?
            """, (self.inventory_id,))
            result = cursor.fetchone()
            if result is None:
                QMessageBox.critical(self, "Error", "Item not found in inventory.")
                return
            current_on_hand = result[0] if result[0] is not None else 0
            # Calculate new on_hand
            new_on_hand = current_on_hand + amount
            # Update the on_hand in inventory table
            cursor.execute("""
                UPDATE inventory
                SET on_hand = ?
                WHERE inventory_id = ?
            """, (new_on_hand, self.inventory_id))
            self.db_connection.commit()
            QMessageBox.information(self, "Success", f"Stock updated! \nNew On Hand: {new_on_hand}")
            # Emit the signal to refresh the inventory table
            self.restockConfirmed.emit()

            # Close the dialog
            self.accept()

        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter a valid numerical amount.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            
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
            inventory_id, description, brand, unit, amount, rop = restock_entry
            # Check if inventory_id exists in inventory
            inv_cursor.execute("SELECT on_hand FROM inventory WHERE inventory_id = ?", (inventory_id,))
            existing_entry = inv_cursor.fetchone()
            if existing_entry:
                # If exists, update on_hand quantity
                new_on_hand = existing_entry[0] + amount
                inv_cursor.execute("UPDATE inventory SET on_hand = ? WHERE inventory_id = ?", (new_on_hand, inventory_id))
            else:
                # If not exists, insert new entry
                inv_cursor.execute("INSERT INTO inventory (inventory_id, description, brand, unit, on_hand, rop) VALUES (?, ?, ?, ?, ?, ?)", 
                            (inventory_id, description, brand, unit, amount, rop))
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
        headers = ["Product ID", "Product Name", "Amount", "Expiration Date"]
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
        conn = self.connect_rsDB()
        add_item_window = AddPrNew(conn) 
        add_item_window.exec_()
        conn.close()
        self.populate_restock_table()
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
            self.ui.cbItems.addItem(display_text, inventory_id)
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
        self.ui.buttonBox.rejected.connect(self.reject)
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
            rop = float(self.ui.teROP.toPlainText())

            # Ensure Inventory ID is provided or unique
            if not inventory_id:
                QMessageBox.warning(self, "Input Error", "Inventory ID is required.")
                return

            # Insert into database
            cursor = self.db_connection.cursor()
            cursor.execute("""
            INSERT INTO restock (inventory_id, description, brand, unit, amount, rop)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (inventory_id, description, brand, unit, amount, rop))
            self.db_connection.commit()
            self.accept() 
            
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please ensure all numerical fields have valid numbers.")
        except sqlite3.IntegrityError as e:
            QMessageBox.critical(self, "Database Error", f"Failed to add item: {e}")
class AddPrNew(QDialog):     
    def __init__(self, conn):
        super(AddPrNew, self).__init__()
        self.ui = Ui_addPrNew()
        self.ui.setupUi(self)
        self.db_connection = conn
        self.populate_combobox()
        # Connect buttons
        self.ui.btnCancel.clicked.connect(self.close)
    #sakit ng shoulders    
    def populate_ingredients(self):
        pass
    def populate_combobox(self):
        inv_path = os.path.join("db", "inventory_db.db")
        inv_conn = sqlite3.connect(inv_path)
        inv_cursor = inv_conn.cursor()
        # Fetch inventory_id, description, and brand
        inv_cursor.execute("SELECT inventory_id, description, unit FROM inventory")
        self.inventory_items = inv_cursor.fetchall()
        # Clear existing items in the combo box
        self.ui.cbItems.clear()
        # Populate the combo box with formatted entries
        for item in self.inventory_items:
            inventory_id, description, unit = item
            display_text = f"{inventory_id} - {description} (in {unit})"
            self.ui.cbItems.addItem(display_text, inventory_id)  # Store inventory_id as userData
        inv_cursor.close()
    def add(self):
        pass
    def remove(self):
        pass
    def confirm(self):
        pass
    
class SalesWindow(QMainWindow):
    go_to_dashboard = pyqtSignal()
    go_to_inventory = pyqtSignal()
    go_to_pos = pyqtSignal()
    go_to_account = pyqtSignal()
    def __init__(self, widget=None):
        super(SalesWindow, self).__init__()
        self.ui = Ui_Sales()
        self.ui.setupUi(self)
        self.widget = widget
        self.load_sales_data()

        # Connect buttons
        self.ui.btnDashboard.clicked.connect(self.go_to_dashboard)
        self.ui.btnInventory.clicked.connect(self.go_to_inventory)
        self.ui.btnPOS.clicked.connect(self.go_to_pos)
        self.ui.btnAccount.clicked.connect(self.go_to_account)
        
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
        self.ui.productTable.verticalHeader().hide()
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
    go_to_dashboard = pyqtSignal()
    go_to_sales = pyqtSignal()
    go_to_inventory = pyqtSignal()
    go_to_account = pyqtSignal()
    def __init__(self, widget=None):
        super(POSWindow, self).__init__()
        self.ui = Ui_pos()
        self.ui.setupUi(self)
        self.setWindowTitle("POS")
        self.widget = widget

        # Create a model for the QListView
        self.cart_model = QStandardItemModel()
        self.ui.cartList.setModel(self.cart_model)
        
        self.total_price = 0.0
        self.update_total_label()

        # Connect buttons to functions
        self.ui.btnDashboard.clicked.connect(self.go_to_dashboard)
        self.ui.btnInventory.clicked.connect(self.go_to_inventory)
        self.ui.btnSales.clicked.connect(self.go_to_sales)
        self.ui.btnAccount.clicked.connect(self.go_to_account)
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
    
class AccountWindow(QMainWindow):
    go_to_dashboard = pyqtSignal()
    go_to_sales = pyqtSignal()
    go_to_pos = pyqtSignal()
    go_to_inventory = pyqtSignal()
    switch_to_login = pyqtSignal()
    def __init__(self, widget=None):
        super(AccountWindow, self).__init__()
        self.ui = Ui_account()
        self.ui.setupUi(self)
        self.setWindowTitle("Account")
        self.widget = widget
        
        # Connect buttons
        self.ui.btnDashboard.clicked.connect(self.go_to_dashboard)
        self.ui.btnInventory.clicked.connect(self.go_to_inventory)
        self.ui.btnSales.clicked.connect(self.go_to_sales)
        self.ui.btnPOS.clicked.connect(self.go_to_pos)
        self.ui.btnLogOut.clicked.connect(self.switch_to_login)

# MAIN APP CONTROLLER
class AppController:
    def __init__(self):
        self.basedir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(self.basedir, "img", "econologo_transparent_cropped.png")

        self.login_window = Login()
        self.signup_window = None
        self.main_window = None

        # Connect signals
        self.login_window.switch_to_signup.connect(self.show_signup)
        self.login_window.switch_to_main.connect(self.show_main)

        # Start the app
        self.login_window.show()

    def show_signup(self):
        self.signup_window = SignUp()
        self.signup_window.switch_to_login.connect(self.show_login)
        self.signup_window.switch_to_main.connect(self.show_main)
        self.signup_window.show()

    def show_login(self):
        self.login_window = Login()
        self.login_window.switch_to_signup.connect(self.show_signup)
        self.login_window.switch_to_main.connect(self.show_main)
        self.login_window.show()

    def show_main(self):
        self.main_window = MainWindow(self.icon_path)
        self.main_window.switch_to_login.connect(self.show_login)
        self.main_window.show()
        self.login_window.close()

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)

    controller = AppController()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Exiting: {e}")