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
from landingPage_ui import Ui_landingPage
from salesForecast_ui import Ui_SalesForecast
from account_ui import Ui_account
from sales_ui import Ui_Sales
from inventory_ui import Ui_inventoryManagement
from add_item_ui import Ui_Dialog
from restock_ui import Ui_Restock
from pos_ui import Ui_pos
from inv_db_setup import inv_database
from sales_db_setup import sales_database
from ingredients_db_setup import ingredients_database
from restock_db_setup import restock_database
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
     
        self.populate_inventory_table()
        
        # Connect buttons
        self.ui.btnRestock.clicked.connect(self.restock)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnPOS.clicked.connect(self.open_POS)
        self.ui.btnAccount.clicked.connect(self.open_account)

    def connect_to_database(self):
        # Database Path
        db_path = os.path.join("db", "inventory_db.db")
        return sqlite3.connect(db_path)
    
    def populate_inventory_table(self):
        # Get database connection
        conn = self.connect_to_database()
        cursor = conn.cursor()

        # Fetch all items from the inventory table
        cursor.execute("SELECT inventory_id, description, brand, unit, on_hand, owed, due_in FROM inventory")
        inventory_items = cursor.fetchall()

        # Set up the table
        self.ui.tab1Table.setRowCount(len(inventory_items)) 
        self.ui.tab1Table.setColumnCount(7)

        # Set headers for the table
        headers = ["Inventory_ID", "Description", "Brand", "Unit", "On_Hand", "Owed", "Due_In"]
        self.ui.tab1Table.setHorizontalHeaderLabels(headers)
        header = self.ui.tab1Table.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; }")
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Populate the table with the data
        for row, item in enumerate(inventory_items):
            for col, value in enumerate(item):
                table_item = QTableWidgetItem(str(value))
                table_item.setTextAlignment(Qt.AlignCenter)
                self.ui.tab1Table.setItem(row, col, table_item)
                                             
        # Adjust column widths to fit content
        self.ui.tab1Table.resizeRowsToContents()
        conn.close()    
    
    def restock(self):
        restock_database()
        restock_window = Restock()
        restock_window.exec_()
    
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
    def __init__(self):
        super(Restock, self).__init__()
        self.ui = Ui_Restock()
        self.ui.setupUi(self)
        
        self.populate_restock_table()
        
        # Connect Buttons
        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnRemove.clicked.connect(self.removeItem)
        self.ui.btnConfirm.clicked.connect(self.confirmItems)
        self.ui.btnCancel.clicked.connect(self.close)
    
    def confirmItems(self):
        conn = self.connect_rsDB()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM restock")
        conn.commit()
        conn.close()
        self.close()
        
    def connect_rsDB(self):
        # Database Path
        db_path = os.path.join("db", "restock_db.db")
        return sqlite3.connect(db_path)
        
    def populate_restock_table(self):
        # Get database connection
        conn = self.connect_rsDB()
        cursor = conn.cursor()

        # Fetch all items from the inventory table
        cursor.execute("SELECT inventory_id, description, brand, unit, amount FROM restock")
        restock_items = cursor.fetchall()

        # Set up the table
        self.ui.tabRestockTable.setRowCount(len(restock_items)) 
        self.ui.tabRestockTable.setColumnCount(5)

        # Set headers for the table
        headers = ["Inventory_ID", "Description", "Brand", "Unit", "Amount"]
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
        # Connect to the sales database
        connection = sqlite3.connect("db/sales_db.db")
        cursor = connection.cursor()

        # Query all rows from the sales table
        cursor.execute("SELECT * FROM sales")
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]  # Get column names
        connection.close()

        # Set column count and headers in QTableWidget
        self.ui.productTable.setColumnCount(len(column_names))
        self.ui.productTable.setHorizontalHeaderLabels(column_names)

        self.ui.productTable.setRowCount(len(rows))

        # Populate the table with data
        for row_index, row_data in enumerate(rows):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.productTable.setItem(row_index, col_index, item)

        # Adjust column widths to evenly fill the table
        header = self.ui.productTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStyleSheet("QHeaderView::section { background-color: #365b6d; color: white; }")
        
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
inv_database()
sales_database()
ingredients_database()
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