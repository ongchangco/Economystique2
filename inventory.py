import sys
import json
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QVBoxLayout, QWidget, QInputDialog, QPushButton
from PyQt5.QtCore import Qt
from mainInventory_ui import Ui_mainInventory
from inventory_ui import Ui_inventoryManagement


class MainInventory(QMainWindow):
    def __init__(self):
        super(MainInventory, self).__init__()
        self.ui = Ui_mainInventory()
        self.ui.setupUi(self)
        
        # Load data from JSON
        self.data = self.load_cake_data()
        
        self.ui.goToInventory.clicked.connect(self.open_inventory)
        
    def load_cake_data(self):
        try:
            with open("cake_data.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If no file or corrupt file exists, return empty data (editable)
            return {}
        
    def open_inventory(self):
        inventory_window = Inventory()
        widget.addWidget(inventory_window)
        widget.setCurrentIndex(widget.currentIndex()+1)


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
        
        self.edit_mode = False
        
    def main_inventory(self):
        main_inventory_window = MainInventory()
        widget.addWidget(main_inventory_window)
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
        table_widget.setHorizontalHeaderLabels(["Inventory ID", "Description", "Brand", "Unit", "On Hand", "Owed", "Due-In"])

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


# Main
app = QApplication(sys.argv)
mainInventory = MainInventory()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainInventory)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
widget.closeEvent = lambda event: app.quit()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
