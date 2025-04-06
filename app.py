import sys, sqlite3, os, json, torch, openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QToolTip, QComboBox, QPushButton, QApplication, QMainWindow, QMessageBox, QAbstractItemView, QHeaderView, QDialog, QTableWidgetItem, QVBoxLayout, QGraphicsDropShadowEffect, QTextEdit, QLineEdit, QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import  QValidator, QIntValidator, QDoubleValidator, QStandardItemModel, QStandardItem, QIcon, QColor
from transformers import pipeline, GPTNeoForCausalLM, GPT2Tokenizer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

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
from sales_utils import fetch_sales_data

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
        self.salesForecast = SalesForecastWindow(self.widget)
        self.POS = POSWindow(self.widget)
        self.account = AccountWindow(self.widget)

        # Update Listeners
        self.POS.inventory_update.connect(self.inventory.populate_products)
        self.POS.sales_update.connect(self.sales.load_sales_data)
        
        # Add widgets to stackedWidget
        self.widget.addWidget(self.dashboard)
        self.widget.addWidget(self.inventory)
        self.widget.addWidget(self.sales)
        self.widget.addWidget(self.salesForecast)
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
        self.sales.go_to_salesForecast.connect(self.show_salesForecast)
        
        self.salesForecast.go_to_dashboard.connect(self.show_dashboard)
        self.salesForecast.go_to_inventory.connect(self.show_inventory)
        self.salesForecast.go_to_sales.connect(self.show_sales)
        self.salesForecast.go_to_pos.connect(self.show_pos)
        self.salesForecast.go_to_account.connect(self.show_account)
        
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
        
    def show_salesForecast(self):
        self.widget.setCurrentWidget(self.salesForecast)

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
        self.populate_product_list()
        # Matplotlib Canvas for Sales Graph
        self.sales_canvas = FigureCanvas(plt.figure())
        layout = QVBoxLayout()
        layout.addWidget(self.sales_canvas)
        self.ui.gpPerformance.setLayout(layout)
        self.display_sales_performance()
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
    def populate_product_list(self):
        # Get DB Connection
        db_path = os.path.join("db", "product_db.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT product_id, product_name, on_hand FROM products_on_hand""")
        avProducts = cursor.fetchall()
        self.ui.lsProduct.clear()
        # Loop through results and format each item
        for product_id, product_name, on_hand in avProducts:
            list_item_text = f"{product_id} - {product_name} @ {on_hand} pcs"
            self.ui.lsProduct.addItem(list_item_text)
        conn.close()
    # AAAAAAAAAAIIIIIIIIIIIIIIIIIIII
    def display_sales_performance(self):
        """ Fetch sales data and display it as a linear graph """
        sales_data = fetch_sales_data()  # Fetch fresh data
        self.plot_sales_graph(sales_data)  # Update graph
        performance_message = self.compare_sales_performance(sales_data)  # AI-generated message
        self.ui.lblPerformance.setText(performance_message)  # Update performance label
        self.display_best_selling_product()  # Update best-selling product label
        
    def plot_sales_graph(self, sales_data):
        """ Plot a linear sales graph using Matplotlib """
        self.sales_canvas.figure.clf()  # Clear figure to remove old data

        # Extract fresh data
        x_values = list(range(len(sales_data)))
        y_values = sales_data["TotalSales"].tolist()

        # Create new plot
        ax = self.sales_canvas.figure.add_subplot(111)
        ax.plot(x_values, y_values, marker="o", linestyle="-", color="b", label="Total Sales")
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Sales")
        ax.set_title("Sales Performance Over Time")
        ax.grid(True)
        ax.legend()

        # Explicitly trigger re-rendering
        self.sales_canvas.figure.tight_layout()  # Ensure proper layout
        self.sales_canvas.draw_idle()  # This ensures it redraws properly


    def compare_sales_performance(self, sales_data):
        """ Compare this month's sales to December and generate a performance message. """
        this_month_sales = sales_data[sales_data["Month"] == "this_month"]["TotalSales"].values
        this_month_value = this_month_sales[0] if len(this_month_sales) > 0 else 0

        # Get December sales safely
        december_sales = sales_data[sales_data["Month"] == "december"]["TotalSales"].values
        december_value = december_sales[0] if len(december_sales) > 0 else 0

        # Calculate percentage change
        if december_value > 0:
            change_percentage = ((this_month_value - december_value) / december_value) * 100
        else:
            change_percentage = 100 if this_month_value > 0 else 0  # If no Dec data, assume 100% increase or no change

        # Generate message
        if change_percentage > 0:
            message = f"This month's sales improved by {change_percentage:.2f}% compared last month."
        elif change_percentage < 0:
            message = f"This month's sales declined by {abs(change_percentage):.2f}% compared last month."
        else:
            message = "Sales remained the same compared to December."

        return message
    def display_best_selling_product(self):
        """Fetch the product with the highest total sales value (price * quantity_sold) from this_month."""
        db_path = os.path.join("db", "sales_db.db")  # Adjust the path if needed
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT product_name, price * quantity_sold AS total_value 
            FROM this_month 
            ORDER BY total_value DESC 
            LIMIT 1
        """)
        result = cursor.fetchone()
        conn.close()

        if result:
            product_name, total_value = result
            self.ui.lblBestProduct.setText(f"The top product: {product_name} with ₱{total_value:.2f} in sales!")
        else:
            self.ui.lblBestProduct.setText("No sales data for this month yet.")
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
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; font-size: 20px; font-weight: bold;}")
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
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; font-size: 20px; font-weight: bold;}")
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
        addProduct_window.restockConfirmed.connect(self.populate_ingredients)
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

        inv_path = os.path.join("db", "inventory_db.db")
        inv_conn = sqlite3.connect(inv_path)
        inv_cursor = inv_conn.cursor()

        ing_path = os.path.join("db", "ingredients_db.db")
        ing_conn = sqlite3.connect(ing_path)
        ing_cursor = ing_conn.cursor()

        # Fetch all entries from restock
        res_cursor.execute("SELECT * FROM restock_product")
        restock_entries = res_cursor.fetchall()

        for restock_entry in restock_entries:
            product_id, product_name, amount, exp_date = restock_entry

            # Update or insert into products_on_hand
            pr_cursor.execute("SELECT on_hand FROM products_on_hand WHERE product_id = ?", (product_id,))
            existing_entry = pr_cursor.fetchone()

            if existing_entry:
                new_on_hand = existing_entry[0] + amount
                pr_cursor.execute("UPDATE products_on_hand SET on_hand = ? WHERE product_id = ?", (new_on_hand, product_id))
                pr_cursor.execute("UPDATE products_on_hand SET exp_date = ? WHERE product_id = ?", (exp_date, product_id))
            else:
                pr_cursor.execute("INSERT INTO products_on_hand (product_id, product_name, on_hand, exp_date) VALUES (?, ?, ?, ?)", 
                            (product_id, product_name, amount, exp_date))

            # Subtract ingredients from inventory
            ing_cursor.execute(f"SELECT inventory_id, {product_id} FROM ingredients WHERE {product_id} IS NOT NULL")
            ingredient_list = ing_cursor.fetchall()

            for inventory_id, required_amount_per_unit in ingredient_list:
                if required_amount_per_unit is not None:
                    total_required = required_amount_per_unit * amount
                    inv_cursor.execute("SELECT on_hand FROM inventory WHERE inventory_id = ?", (inventory_id,))
                    inventory_entry = inv_cursor.fetchone()

                    if inventory_entry and inventory_entry[0] >= total_required:
                        new_inventory = inventory_entry[0] - total_required
                        inv_cursor.execute("UPDATE inventory SET on_hand = ? WHERE inventory_id = ?", (new_inventory, inventory_id))
                    else:
                        QMessageBox.warning(self, "Stock Warning", f"Not enough stock for ingredient {inventory_id}")

        # Commit changes
        pr_conn.commit()
        res_conn.commit()
        inv_conn.commit()
        ing_conn.commit()

        # Close connections
        pr_conn.close()
        inv_conn.close()
        ing_conn.close()

        # Clear restock table
        res_cursor.execute("DELETE FROM restock_product")
        res_conn.commit()
        res_conn.close()
        
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
        self.ui.teAmount.textChanged.connect(self.validate_input)
        self.apply_shadow_effects()
        # Set validator for the amount input field (teAmount)
        int_validator = QIntValidator(1, 2147483647)  # Min, Max
        self.ui.teAmount.setValidator(int_validator)
    
    # GUI
    def apply_shadow_effects(self):
        # Add shadow effect to all QLineEdit, QPushButton, QComboBox
        for entity in self.findChildren(QLineEdit):
            self.add_shadow_effect(entity)
        for entity in self.findChildren(QPushButton):
            self.add_shadow_effect(entity)
        for entity in self.findChildren(QComboBox):
            self.add_shadow_effect(entity)
    
    def add_shadow_effect(self, entity):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setOffset(1, 1)
        shadow.setColor(QColor(0, 0, 0, 160))
        entity.setGraphicsEffect(shadow)
        
    def validate_input(self):
        # Get the input from lineEdit (teAmount)
        input_text = self.ui.teAmount.text().strip()

        # Create a validator to validate the input
        validator = self.ui.teAmount.validator()
        
        # Validate the input using the QDoubleValidator
        state, _, _ = validator.validate(input_text, 0)

        # Check if the input is valid
        if state != QValidator.Acceptable:
            # Display tooltip and visual feedback for invalid input
            QToolTip.showText(self.ui.teAmount.mapToGlobal(self.ui.teAmount.rect().bottomLeft()),
                          "Please enter a positive whole number",
                          self.ui.teAmount)
            self.ui.teAmount.setStyleSheet("border: 1px solid red; border-radius: 5px; background: white;")
        else:
            # Clear the tooltip and reset the style if input is valid
            self.ui.teAmount.setToolTip("")
            self.ui.teAmount.setStyleSheet("border: 1px solid black; border-radius: 5px; background: white;")
            QToolTip.hideText()
    def populate_combobox(self):
        pr_path = os.path.join("db", "product_db.db")
        pr_conn = sqlite3.connect(pr_path)
        pr_cursor = pr_conn.cursor()
        # Fetch product_id, product_name
        pr_cursor.execute("SELECT product_id, product_name FROM products_on_hand")
        self.product_items = pr_cursor.fetchall()
        # Clear existing items in the combo box
        self.ui.cbProducts.clear()
        # Populate the combo box with formatted entries
        for item in self.product_items:
            product_id, product_name = item
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
            product_id, product_name = self.product_items[index]
            amount_text = self.ui.teAmount.text()
            if not amount_text.strip():
                QMessageBox.warning(self, "Input Error", "Amount cannot be empty.")
                return
            amount = int(amount_text)
            newExpDate = self.ui.teExpDate.text()
            # Insert into the restock database
            cursor = self.db_connection.cursor()
            cursor.execute("""
                INSERT INTO restock_product (product_id, product_name, amount, exp_date)
                VALUES (?, ?, ?, ?)
            """, (product_id, product_name, amount, newExpDate))
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
        self.populate_table()
        # Connect buttons
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnConfirm.clicked.connect(self.confirm)
        self.ui.btnRemove.clicked.connect(self.remove)
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
    def populate_table(self):
        data_path = os.path.join("db", "prrestock_db.db")
        data_conn = sqlite3.connect(data_path)
        data_cursor = data_conn.cursor()
        # Fetch inventory_id, description, and amount
        data_cursor.execute("""
            SELECT inventory_id, description, amount
            FROM new_product_data
        """)
        prData = data_cursor.fetchall()
        # Set up the table
        self.ui.tabPrIngredients.setRowCount(len(prData)) 
        self.ui.tabPrIngredients.setColumnCount(3)
        self.ui.tabPrIngredients.verticalHeader().hide()
        # Set headers for the table
        headers = ["Inventory ID", "Description", "Amount"]
        self.ui.tabPrIngredients.setHorizontalHeaderLabels(headers)
        header = self.ui.tabPrIngredients.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; }")
        header.setSectionResizeMode(QHeaderView.Stretch)
        # Set Table to Read-Only
        self.ui.tabPrIngredients.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tabPrIngredients.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # Populate the table with the data
        for row, item in enumerate(prData):
            inventory_id, description, amount = item
            row_values = [inventory_id, description, amount]
            # Loop through each column and insert items
            for col, value in enumerate(row_values):
                table_item = QTableWidgetItem(str(value))
                table_item.setTextAlignment(Qt.AlignCenter)

                self.ui.tabPrIngredients.setItem(row, col, table_item)
        self.ui.tabPrIngredients.resizeRowsToContents()
        data_cursor.close()
    def add(self):
        inventory_id = self.ui.cbItems.currentData()  # Get selected inventory_id
        amount = self.ui.leAmount.text().strip()  # Get entered amount

        if not inventory_id or not amount:
            QMessageBox.warning(self, "Input Error", "Please select an ingredient and enter an amount.")
            return

        try:
            amount = float(amount)  # Ensure valid numeric input
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Amount must be a number.")
            return

        # Fetch the description from inventory
        description = next((desc for inv_id, desc, _ in self.inventory_items if inv_id == inventory_id), None)

        if not description:
            QMessageBox.warning(self, "Database Error", "Failed to fetch ingredient description.")
            return

        # Insert into prrestock_db.db
        prrestock_path = os.path.join("db", "prrestock_db.db")
        pr_conn = sqlite3.connect(prrestock_path)
        pr_cursor = pr_conn.cursor()

        try:
            pr_cursor.execute(
                "INSERT INTO new_product_data (inventory_id, description, amount) VALUES (?, ?, ?)",
                (inventory_id, description, amount)
            )
            pr_conn.commit()
            self.populate_table()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "This ingredient is already added.")
        finally:
            pr_cursor.close()
            pr_conn.close()
    def remove(self):
        # Get selected items
        selected_items = self.ui.tabPrIngredients.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "No item selected. Please select an ingredient to delete.")
            return

        # Identify unique rows from selected cells
        rows_to_delete = sorted(set(item.row() for item in selected_items), reverse=True)

        # Connect to the database
        prrestock_path = os.path.join("db", "prrestock_db.db")
        pr_conn = sqlite3.connect(prrestock_path)
        pr_cursor = pr_conn.cursor()

        try:
            for row in rows_to_delete:
                # Retrieve the inventory_id from the first column
                inventory_item = self.ui.tabPrIngredients.item(row, 0) 
                if inventory_item:
                    inventory_id = inventory_item.text()

                    # Delete the item from the database
                    pr_cursor.execute("DELETE FROM new_product_data WHERE inventory_id = ?", (inventory_id,))

                    # Remove the row from the table widget
                    self.ui.tabPrIngredients.removeRow(row)
                else:
                    QMessageBox.warning(self, "Missing Data", f"Could not find Inventory ID for row {row + 1}.")

            # Commit changes to the database
            pr_conn.commit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to remove item(s): {e}")
        finally:
            pr_conn.close()

        self.populate_table()
    def confirm(self):
        prrestock_path = os.path.join("db", "prrestock_db.db")
        product_path = os.path.join("db", "product_db.db")
        ingredients_path = os.path.join("db", "ingredients_db.db")

        product_id = self.ui.lePrID.text().strip()
        product_name = self.ui.lePrName.text().strip()

        if not product_id or not product_name:
            QMessageBox.warning(self, "Input Error", "Please enter a Product ID and Product Name.")
            return

        pr_conn = sqlite3.connect(prrestock_path)
        pr_cursor = pr_conn.cursor()
        
        product_conn = sqlite3.connect(product_path)
        product_cursor = product_conn.cursor()

        ingredients_conn = sqlite3.connect(ingredients_path)
        ingredients_cursor = ingredients_conn.cursor()

        try:
            product_cursor.execute("""
                INSERT INTO products_on_hand (product_id, product_name, on_hand, exp_date) 
                VALUES (?, ?, 0, 'N/A')
            """, (product_id, product_name))
            product_conn.commit()

            pr_cursor.execute("SELECT inventory_id, description, amount FROM new_product_data")
            new_ingredients = pr_cursor.fetchall()

            if not new_ingredients:
                QMessageBox.warning(self, "Data Error", "You have new ingredients for the new product!")
                return

            ingredients_cursor.execute("PRAGMA table_info(ingredients)")
            existing_columns = [col[1] for col in ingredients_cursor.fetchall()] 
            
            if product_id not in existing_columns:
                ingredients_cursor.execute(f"ALTER TABLE ingredients ADD COLUMN '{product_id}' REAL DEFAULT 0")
                ingredients_conn.commit()

            for inventory_id, description, amount in new_ingredients:
                # Check if inventory_id exists in ingredients database
                ingredients_cursor.execute("SELECT inventory_id FROM ingredients WHERE inventory_id = ?", (inventory_id,))
                existing_ingredient = ingredients_cursor.fetchone()

                if existing_ingredient:
                    # Update existing ingredient with new amount
                    ingredients_cursor.execute(f"UPDATE ingredients SET '{product_id}' = ? WHERE inventory_id = ?", (amount, inventory_id))
                else:
                    # Insert new ingredient, setting all other product columns to 0
                    other_columns = ", ".join([f"'{col}'" for col in existing_columns if col != "inventory_id" and col != "description"])
                    default_values = ", ".join(["0"] * (len(existing_columns) - 2))  # Excluding inventory_id & description
                    
                    ingredients_cursor.execute(f"""
                        INSERT INTO ingredients (inventory_id, description, {other_columns}, '{product_id}') 
                        VALUES (?, ?, {default_values}, ?)
                    """, (inventory_id, description, amount))
            
            ingredients_conn.commit()

            pr_cursor.execute("DELETE FROM new_product_data")
            pr_conn.commit()

            QMessageBox.information(self, "Success", "Product and ingredients updated successfully!")
            self.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to confirm: {e}")
        finally:
            pr_cursor.close()
            pr_conn.close()
            product_cursor.close()
            product_conn.close()
            ingredients_cursor.close()
            ingredients_conn.close()
class SalesWindow(QMainWindow):
    go_to_dashboard = pyqtSignal()
    go_to_inventory = pyqtSignal()
    go_to_pos = pyqtSignal()
    go_to_account = pyqtSignal()
    go_to_salesForecast = pyqtSignal()
    def __init__(self, widget=None):
        super(SalesWindow, self).__init__()
        self.ui = Ui_Sales()
        self.ui.setupUi(self)
        self.widget = widget
        self.ui.cbMonth.addItems(["January","February","March","April","May",
                                  "June","July","August","September","October",
                                  "November","December"])
        self.ui.cbMonth.setCurrentIndex(0)
        self.ui.cbMYear.addItems(["2025","2024","2023"])
        self.ui.cbYear.addItems(["2025","2024","2023"])
        self.ui.cbYear.setCurrentIndex(0)
        self.load_sales_data()
        self.load_monthly_data()
        self.load_yearly_data()
        # Connect buttons
        self.ui.cbMonth.currentIndexChanged.connect(self.load_monthly_data)
        self.ui.cbMYear.currentIndexChanged.connect(self.update_month_selection)
        self.ui.cbYear.currentIndexChanged.connect(self.load_yearly_data)
        self.ui.btnDashboard.clicked.connect(self.go_to_dashboard)
        self.ui.btnInventory.clicked.connect(self.go_to_inventory)
        self.ui.btnPOS.clicked.connect(self.go_to_pos)
        self.ui.btnAccount.clicked.connect(self.go_to_account)
        self.ui.btnForecast.clicked.connect(self.go_to_salesForecast)
        
    def update_month_selection(self):
        selected_year = self.ui.cbMYear.currentText()
        db_name = f"sales_{selected_year}.db"
        sales_path = os.path.join("db", db_name)

        if not os.path.exists(sales_path):
            print(f"Database {db_name} not found.")  # Debug message
            self.ui.cbMonth.clear()
            return

        sales_conn = sqlite3.connect(sales_path)
        sales_cursor = sales_conn.cursor()

        try:
            # Fetch the list of tables in the selected year's database
            sales_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = {row[0] for row in sales_cursor.fetchall()}  # Convert to set for easy lookup

            # Month mappings (database table names vs. UI names)
            month_map = {
                "jan": "January", "feb": "February", "mar": "March", "apr": "April",
                "may": "May", "jun": "June", "jul": "July", "aug": "August",
                "sep": "September", "oct": "October", "nov": "November", "dec": "December"
            }

            # Filter available months based on existing tables
            available_months = [month_map[m] for m in month_map if m in tables]

            # Update cbMonth with available months
            self.ui.cbMonth.clear()
            self.ui.cbMonth.addItems(available_months)
            self.ui.cbMonth.setCurrentIndex(0)  # Reset to first available month

            # Load data for the first available month
            self.load_monthly_data()

        except sqlite3.Error as e:
            print(f"Error checking tables: {e}")

        finally:
            sales_conn.close()
    def load_yearly_data(self):
        selected_year = self.ui.cbYear.currentText()  # Get selected year
        db_name = f"sales_{selected_year}.db"  # Construct database filename
        year_table = "year_total"  # Yearly summary table
        
        sales_path = os.path.join("db", db_name)
        
        if not os.path.exists(sales_path):
            print(f"Database {db_name} not found.")
            self.ui.yProductTable.setRowCount(0)
            self.ui.lblYTotal.setText("0.00")
            return  
        
        sales_conn = sqlite3.connect(sales_path)
        sales_cursor = sales_conn.cursor()

        try:
            # Fetch yearly data
            sales_cursor.execute(f"SELECT product_id, product_name, price, quantity_sold FROM {year_table}")
            products = sales_cursor.fetchall()

            # Set up the table
            self.ui.yProductTable.setRowCount(len(products))
            self.ui.yProductTable.setColumnCount(4)
            self.ui.yProductTable.verticalHeader().hide()

            headers = ["Product ID", "Product Name", "Price", "Quantity Sold"]
            self.ui.yProductTable.setHorizontalHeaderLabels(headers)
            header = self.ui.yProductTable.horizontalHeader()
            header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; font-size: 20px; font-weight: bold;}")
            header.setSectionResizeMode(QHeaderView.Stretch)

            # Populate the table
            for row, item in enumerate(products):
                for col, value in enumerate(item):
                    table_item = QTableWidgetItem(str(value))
                    table_item.setTextAlignment(Qt.AlignCenter)
                    self.ui.yProductTable.setItem(row, col, table_item)

            # Compute & Display Total Sales
            total = sum(item[2] * item[3] for item in products)  # price * quantity_sold
            self.ui.lblYTotal.setText(f"{total:,.2f}")  # Add thousands separator

        except sqlite3.OperationalError as e:
            print(f"Error loading yearly data: {e}")
            self.ui.yProductTable.setRowCount(0)  # Clear table if query fails
            self.ui.lblYTotal.setText("0.00")  # Reset total

        finally:
            sales_conn.close()
    def load_monthly_data(self):
        selected_month = self.ui.cbMonth.currentText().lower()[:3]  # Convert to short form (e.g., "January" → "jan")
        selected_year = self.ui.cbMYear.currentText()
        db_name = f"sales_{selected_year}.db"
        sales_path = os.path.join("db", db_name)

        if not os.path.exists(sales_path):
            print(f"Database {db_name} not found.")  # Debug message
            self.ui.mProductTable.setRowCount(0)  # Clear table
            self.ui.lblMTotal.setText("0.00")  # Reset total
            return

        sales_conn = sqlite3.connect(sales_path)
        sales_cursor = sales_conn.cursor()

        try:
            query = f"SELECT product_id, product_name, price, quantity_sold FROM {selected_month}"
            sales_cursor.execute(query)
            products = sales_cursor.fetchall()

            # Set up the table
            self.ui.mProductTable.setRowCount(len(products))
            self.ui.mProductTable.setColumnCount(4)
            self.ui.mProductTable.verticalHeader().hide()

            headers = ["Product ID", "Product Name", "Price", "Quantity Sold"]
            self.ui.mProductTable.setHorizontalHeaderLabels(headers)
            header = self.ui.mProductTable.horizontalHeader()
            header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; font-size: 20px; font-weight: bold;}")
            header.setSectionResizeMode(QHeaderView.Stretch)

            # Populate the table
            for row, item in enumerate(products):
                for col, value in enumerate(item):
                    table_item = QTableWidgetItem(str(value))
                    table_item.setTextAlignment(Qt.AlignCenter)
                    self.ui.mProductTable.setItem(row, col, table_item)

            # Compute & Display Total Sales
            total = sum(item[2] * item[3] for item in products)
            self.ui.lblMTotal.setText(f"{total:,.2f}")

        except sqlite3.OperationalError as e:
            print(f"Error loading data: {e}")
            self.ui.mProductTable.setRowCount(0)  # Clear table if query fails
            self.ui.lblMTotal.setText("0.00")  # Reset total

        finally:
            sales_conn.close()
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
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; font-size: 20px; font-weight: bold;}")
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
class SalesForecastWindow(QMainWindow):
    go_to_dashboard = pyqtSignal()
    go_to_sales = pyqtSignal()
    go_to_pos = pyqtSignal()
    go_to_inventory = pyqtSignal()
    go_to_account = pyqtSignal()
    def __init__(self, widget=None):
        super(SalesForecastWindow, self).__init__()
        self.ui = Ui_SalesForecast()
        self.ui.setupUi(self)
        self.setWindowTitle("Sales Forecast")
        self.widget = widget
        self.populate_products()
        self.update_forecast()
        
        # Connect buttons to functions
        self.ui.btnDashboard.clicked.connect(self.go_to_dashboard)
        self.ui.btnInventory.clicked.connect(self.go_to_inventory)
        self.ui.btnSales.clicked.connect(self.go_to_sales)
        self.ui.btnPOS.clicked.connect(self.go_to_pos)
        self.ui.btnAccount.clicked.connect(self.go_to_account)
        self.ui.cbProduct.currentIndexChanged.connect(self.update_forecast)
    
    def populate_products(self):
        db_path = os.path.join("db", "product_db.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT product_id, product_name FROM products_on_hand")
        products = cursor.fetchall()
        
        self.ui.cbProduct.clear()
        for product in products:
            self.ui.cbProduct.addItem(f"{product[0]} - {product[1]}")

        conn.close()
        
    def get_sales_data(self, product_id):
        months_2024 = ["apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        months_2025 = ["jan", "feb", "mar"]
        
        sales_data = []
        
        sales_2024_path = os.path.join("db", "sales_2024.db")
        if os.path.exists(sales_2024_path):
            conn = sqlite3.connect(sales_2024_path)
            cursor = conn.cursor()

            for month in months_2024:
                cursor.execute(f"SELECT quantity_sold FROM {month} WHERE product_id = ?", (product_id,))
                result = cursor.fetchone()
                sales_data.append(result[0] if result else 0)

            conn.close()
        else:
            print("sales_2024.db not found.")
        
        sales_2025_path = os.path.join("db", "sales_2025.db")
        if os.path.exists(sales_2025_path):
            conn = sqlite3.connect(sales_2025_path)
            cursor = conn.cursor()

            for month in months_2025:
                cursor.execute(f"SELECT quantity_sold FROM {month} WHERE product_id = ?", (product_id,))
                result = cursor.fetchone()
                sales_data.append(result[0] if result else 0)

            conn.close()
        else:
            print("sales_2025.db not found.")
        
        return sales_data
    
    def forecast_sales(self, product_id):
        sales_2023_path = os.path.join("db", "sales_2023.db")
        sales_2024_path = os.path.join("db", "sales_2024.db")
        
        past_april_sales = []
        
        for db_path in [sales_2023_path, sales_2024_path]:
            if not os.path.exists(db_path):
                continue

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            try:
                cursor.execute("SELECT quantity_sold FROM apr WHERE product_id = ?", (product_id,))
                result = cursor.fetchone()
                if result:
                    past_april_sales.append(result[0])
            except sqlite3.OperationalError:
                pass

            conn.close()

        if not past_april_sales:
            return None

        forecasted_value = self.use_gpt_neo_forecast(past_april_sales)
        return forecasted_value
    
    def use_gpt_neo_forecast(self, past_data):
        from statsmodels.tsa.holtwinters import Holt
        from statsmodels.tsa import seasonal
        from statsmodels.tsa import exponential_smoothing
        
        import numpy as np

        if len(past_data) < 2 or all(x == past_data[0] for x in past_data):
            return past_data[-1] if past_data else 0  # Avoid division errors

        data = np.array(past_data, dtype=float)

        model = Holt(data).fit()
        forecasted_value = model.forecast(1)[0]
        return round(forecasted_value)
    
    def generate_comment(self, forecast):
        if forecast is None:
            return "No historical data available to forecast."

        # Get the March sales (the last value in past_sales list)
        march_sales = self.past_sales[-1] if len(self.past_sales) > 0 else 0

        # Calculate the percentage change from March sales to forecasted sales
        if march_sales > 0:  # Avoid division by zero
            change_percentage = ((forecast - march_sales) / march_sales) * 100
        else:
            change_percentage = 0  # No change if March sales were 0

        # Generate comment based on the change
        if forecast > march_sales:
            return f"Sales are expected to <span style='color: #7ff58d;'>INCREASE</span> in April by {round(change_percentage, 2)}% compared to last month."
        elif forecast < march_sales:
            return f"Sales are expected to <span style='color: #f5737c;'>DECREASE</span> in April by {round(abs(change_percentage), 2)}% compared to last month."
        else:
            return "Sales are predicted to remain stable in April compared to last month."
        
    def plot_forecast(self, past_sales, forecasted_value):
        # Ensure gpPerformance has a layout
        if self.ui.gpPerformance.layout() is None:
            self.ui.gpPerformance.setLayout(QVBoxLayout())

        layout = self.ui.gpPerformance.layout()

        # Remove old plots
        while layout.count() > 0:
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Create a new figure
        fig, ax = plt.subplots(figsize=(6, 4))

        months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr (Forecast)"]

        # Combine past sales data with forecasted value for April 2025
        values = past_sales + [forecasted_value]

        # Plot historical data (Apr-Dec 2024 and Jan-Mar 2025)
        ax.plot(months[:-1], values[:-1], marker="o", linestyle="-", color="blue", label="Past Sales")

        # Highlight the forecasted value for April 2025 (this should be the last point)
        ax.plot(months[-1], forecasted_value, marker="o", color="red", markersize=8, label="Forecasted Value")

        # Connect the forecasted point to the last point (March 2025)
        ax.plot([months[-2], months[-1]], [values[-2], forecasted_value], linestyle="--", color="red")

        # Labels and title
        ax.set_xlabel("Month")
        ax.set_ylabel("Quantity Sold")
        ax.set_title("Sales Forecast for April 2025")
        ax.legend()

        # Embed the plot into the QWidget
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        
    def update_forecast(self):
        selected_product = self.ui.cbProduct.currentText()
        if not selected_product:
            return

        product_id = selected_product.split(" - ")[0]  # Extract product_id

        # Fetch past sales data
        self.past_sales = self.get_sales_data(product_id)
        forecasted_value = self.forecast_sales(product_id)

        # Update Graph
        self.plot_forecast(self.past_sales, forecasted_value)

        # Update lblComment
        self.ui.lblComment.setText(self.generate_comment(forecasted_value))
class ForecastWorker(QThread):
    forecast_generated = pyqtSignal(str)

    def __init__(self, sales_prompt):
        super().__init__()
        self.sales_prompt = sales_prompt

    def run(self):
        try:
            tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
            model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            model.to(device)

            inputs = tokenizer(self.sales_prompt, return_tensors="pt", truncation=True, max_length=512)
            inputs = {key: value.to(device) for key, value in inputs.items()}

            outputs = model.generate(inputs["input_ids"], max_new_tokens=50, num_beams=1, pad_token_id=tokenizer.eos_token_id)
            forecast = tokenizer.decode(outputs[0], skip_special_tokens=True)

            self.forecast_generated.emit(forecast)

        except Exception as e:
            self.forecast_generated.emit(f"Error: {str(e)}")
class POSWindow(QMainWindow):
    inventory_update = pyqtSignal()
    sales_update = pyqtSignal()
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
        sales_path = os.path.join("db", "sales_db.db")
        product_path = os.path.join("db", "product_db.db")

        # Check product availability
        product_conn = sqlite3.connect(product_path)
        product_cursor = product_conn.cursor()
        product_cursor.execute("SELECT on_hand FROM products_on_hand WHERE product_id = ?", (product_id,))
        result = product_cursor.fetchone()
        product_conn.close()

        if not result or result[0] <= 0:
            QMessageBox.warning(self, "Out of Stock", f"Product {product_id} is out of stock!")
            return

        available_stock = result[0]  # Get the available stock

        # Fetch product details from sales database
        sales_conn = sqlite3.connect(sales_path)
        sales_cursor = sales_conn.cursor()
        sales_cursor.execute("SELECT product_name, price FROM sales WHERE product_id = ?", (product_id,))
        product_data = sales_cursor.fetchone()
        sales_conn.close()

        if not product_data:
            QMessageBox.warning(self, "Error", f"Product {product_id} not found in sales database!")
            return

        product_name, price = product_data

        # Check if item already exists in cart
        for i in range(self.cart_model.rowCount()):
            item = self.cart_model.item(i)
            if item.text().startswith(f"{product_id} - {product_name} @ {price}"):
                # Extract current quantity
                parts = item.text().split(" x")
                current_qty = int(parts[1]) if len(parts) > 1 else 1

                # Prevent exceeding available stock
                if current_qty + 1 > available_stock:
                    QMessageBox.warning(self, "Stock Limit Reached",
                                        f"Only {available_stock} units of {product_name} are available!")
                    return

                # Update quantity
                new_qty = current_qty + 1
                item.setText(f"{product_id} - {product_name} @ {price} x{new_qty}")
                self.total_price += price
                self.update_total_label()
                return

        # If product is not in the cart, add a new entry (only if stock allows)
        if available_stock > 0:
            new_item = QStandardItem(f"{product_id} - {product_name} @ {price} x1")
            self.cart_model.appendRow(new_item)
            self.total_price += price
            self.update_total_label()
    def clear_cart(self):
        self.cart_model.clear()
        self.total_price = 0.0
        self.update_total_label()
    def update_total_label(self):
        # Update the lblTotal label with the total price
        self.ui.lblTotal.setText(f"Total: {self.total_price:.2f}")
    def checkout(self):
        if self.cart_model.rowCount() == 0:
            QMessageBox.warning(self, "Empty Cart", "Your cart is empty. Add items before checkout.")
            return

        product_path = os.path.join("db", "product_db.db")
        sales_path = os.path.join("db", "sales_db.db")

        product_conn = sqlite3.connect(product_path)
        product_cursor = product_conn.cursor()
        sales_conn = sqlite3.connect(sales_path)
        sales_cursor = sales_conn.cursor()

        try:
            # Process each item in the cart
            for i in range(self.cart_model.rowCount()):
                item_text = self.cart_model.item(i).text()
                parts = item_text.split(" x")
                if len(parts) != 2:
                    continue  # Skip malformed entries

                product_info, quantity = parts[0], int(parts[1])
                product_id = product_info.split(" - ")[0]

                # Get current stock
                product_cursor.execute("SELECT on_hand FROM products_on_hand WHERE product_id = ?", (product_id,))
                result = product_cursor.fetchone()
                if not result:
                    QMessageBox.warning(self, "Error", f"Product {product_id} not found in products_on_hand!")
                    continue

                current_stock = result[0]
                new_stock = max(0, current_stock - quantity)

                # Update product stock
                product_cursor.execute("UPDATE products_on_hand SET on_hand = ? WHERE product_id = ?", (new_stock, product_id))

                # Update quantity_sold in sales database
                sales_cursor.execute("SELECT quantity_sold FROM sales WHERE product_id = ?", (product_id,))
                result = sales_cursor.fetchone()
                if result:
                    new_quantity_sold = result[0] + quantity
                    sales_cursor.execute("UPDATE sales SET quantity_sold = ? WHERE product_id = ?", (new_quantity_sold, product_id))

            # Commit changes
            product_conn.commit()
            sales_conn.commit()

            QMessageBox.information(self, "Success", "Transaction completed successfully!")
            self.clear_cart()
            
            # Update Other Tables
            self.inventory_update.emit()
            self.sales_update.emit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            product_conn.rollback()
            sales_conn.rollback()

        finally:
            product_conn.close()
            sales_conn.close()
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
if __name__ == "__main__":
    app = QApplication(sys.argv)

    controller = AppController()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Exiting: {e}")