import sys, sqlite3, os, json, torch, openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QDialog, QFileDialog, QInputDialog, QListView, QTabWidget,QVBoxLayout, QLabel, QWidget, QTableView, QTableWidget, QTableWidgetItem
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
from pos_ui import Ui_pos
from db_setup import inv_database
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

        # Connect buttons
        self.ui.btnAddItem.clicked.connect(self.add_item)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnPOS.clicked.connect(self.open_POS)
        self.ui.btnAccount.clicked.connect(self.open_account)

    def connect_to_database():
        # Database Path
        db_path = os.path.join("db", "inventory_db.db")
        return sqlite3.connect(db_path)
    
    def save_inventory_item(inventory_id, description, brand, unit, on_hand, owed, due_in):
        try:
            conn = connect_to_database()
            cursor = conn.cursor()
            
            # Insert into the inventory table
            cursor.execute("""
            INSERT INTO inventory (inventory_id, description, brand, unit, on_hand, owed, due_in)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (inventory_id, description, brand, unit, on_hand, owed, due_in))
            
            conn.commit()
            print("Item saved successfully.")
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
        finally:
            conn.close()
    
    def add_item(self):
        add_item_window = AddItem()
        add_item_window.exec_()
    
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
     
class AddItem(QDialog):     
    def __init__(self):
        super(AddItem, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.buttonBox.accepted.connect(self.confirm)
    
    def confirm(self):
        try:
            inventory_id = self.ui.teInvID.toPlainText()
            description = self.ui.teDescription.toPlainText()
            brand = self.ui.teBrand.toPlainText()
            unit = self.ui.teUnit.toPlainText()
            on_hand = int(self.ui.teOnHand.toPlainText())
            owed = int(self.ui.teOwed.toPlainText())
            due_in = int(self.ui.teDueIn.toPlainText())

            # Ensure Inventory ID is provided or unique
            if not inventory_id:
                QMessageBox.warning(self, "Input Error", "Inventory ID is required.")
                return

            # Insert into database
            self.parent().cursor.execute("""
            INSERT INTO inventory (inventory_id, description, brand, unit, on_hand, owed, due_in)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (inventory_id, description, brand, unit, on_hand, owed, due_in))
            self.parent().db_connection.commit()

            QMessageBox.information(self, "Success", "Item added successfully!")
            self.accept()  # Close the dialog
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please ensure all numerical fields have valid numbers.")
        except sqlite3.IntegrityError as e:
            QMessageBox.critical(self, "Database Error", f"Failed to add item: {e}")
        
class SalesWindow(QMainWindow):
    def __init__(self):
        super(SalesWindow, self).__init__()
        self.ui = Ui_Sales()
        self._setup_ui()
        self.setWindowTitle("Sales")

        # Load data from JSON
        self.data = self.load_cake_data()

        # Populate the product table
        self.populate_table()

        # Initialize the sales_forecast_window attribute to None
        self.sales_forecast_window = None

        # Connect the click event of the table
        self.ui.productTable.cellClicked.connect(self.sell_product)

        # Connect buttons
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnPOS.clicked.connect(self.open_POS)
        self.ui.btnAccount.clicked.connect(self.open_account)
        self.ui.forecastButton.clicked.connect(self.generate_sales_forecast)
        
        # Setup thread pool for async processing
        self.executor = ThreadPoolExecutor(max_workers=1)

    def _setup_ui(self):
        try:
            self.ui.setupUi(self)
        except RecursionError as e:
            print("Recursion error detected during UI setup:", e)

    def load_cake_data(self):
        try:
            file_path = os.path.join("json","cake_data.json")
            with open(file_path, "r") as f:
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

    def sell_product(self, row, column):
        if column == 4:  # Only if the Sold column is clicked
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
        file_path = os.path.join("json","cake_data.json")
        with open(file_path, "w") as f:
            json.dump(self.data, f, indent=4)

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
        
class POSWindow(QMainWindow):
    def __init__(self):
        super(POSWindow, self).__init__()
        self.ui = Ui_pos()
        self.ui.setupUi(self)
        self.setWindowTitle("POS")

        #add editable amount on add to cart (should show amount when a product is clicked (C001 x3))

        # Data for POS
        self.cart = []
        self.products = {
            "C001": ("Chocolate Moist", 850.00),
            "C002": ("Yema Vanilla", 760.00),
            "C003": ("Caramel Cake", 820.00),
            "C004": ("Ube Caramel", 750.00),
            "C005": ("Red Velvet", 850.00),
            "C006": ("Pandan Cake", 760.00),
            "C007": ("Strawberry Cake", 780.00),
            "C008": ("Biscoff Mocha", 900.00),
            "C009": ("Bento Cake", 370.00),
            "C010": ("Cupcake", 40.00),
        }

        # Connect buttons to functions
        self.ui.btnInventory.clicked.connect(self.open_inventory)
        self.ui.btnSales.clicked.connect(self.open_sales)
        self.ui.btnAccount.clicked.connect(self.open_account)
        
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

        self.ui.btnClear.clicked.connect(self.clear_cart)
        self.ui.btnCheckout.clicked.connect(self.checkout)

    def add_to_cart(self, product_code):
        """Add product to cart."""
        product_name, price = self.products[product_code]
        self.cart.append((product_name, price))
        self.update_cart_display()

    def update_cart_display(self):
        """Update the cart display."""
        if self.cart:
            cart_summary = "\n".join([f"{item[0]} - ₱{item[1]:.2f}" for item in self.cart])
            self.ui.cartlabel.setText(cart_summary)
            
            total = sum(item[1] for item in self.cart)
            self.ui.checkoutlabel.setText(f"\n\nTotal: ₱{total:.2f}")
            
        else:
            self.ui.cartlabel.setText("Cart is empty")
            self.ui.checkoutlabel.setText("Total: ₱0.00")
        
    def clear_cart(self):
        """Clear the cart."""
        self.cart.clear()
        self.update_cart_display()

    def checkout(self):
        """Process checkout."""
        if not self.cart:
            QMessageBox.warning(self, "Checkout Error", "Cart is empty!")
            return

        # Create Receipt
        counter_path = os.path.join("json","receipt_counter.json")
        with open(counter_path, "r") as json_file:
            rcptNum = json.load(json_file)
            
        counter_update = rcptNum + 1
        receipt = f"R#{counter_update:05}.json"
        file_path = os.path.join("receipts", receipt)
        
        # Write data to the JSON file
        with open(file_path, "w") as json_file:
            json.dump(self.cart, json_file, indent=4)
        
        # Update Receipt Counter
        with open(counter_path, "w") as json_file:
            json.dump(counter_update, json_file)
        
        total = sum(item[1] for item in self.cart)
        QMessageBox.information(self, "Checkout", f"Total Amount: ₱{total:.2f}\nThank you for your purchase!")
        self.clear_cart()
    
    #for menu buttons
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