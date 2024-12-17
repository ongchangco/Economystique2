import sys
import json
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from inventory_ui import Ui_inventoryManagement


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

        # Connect the save button
        self.ui.btnSave.clicked.connect(self.save_table)

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
        # Setup the tabs and tables for September, October, and November
        for month in ["September", "October", "November"]:
            data = self.data.get(month, [])
            table_widget = self.create_table(data)
            self.tables[month] = table_widget
            tab_layout = QVBoxLayout()
            tab_layout.addWidget(table_widget)

            # Add tab layout for each month
            tab_widget_container = QWidget()
            tab_widget_container.setLayout(tab_layout)
            self.ui.tabWidget.addTab(tab_widget_container, month)

    def create_table(self, data):
        table_widget = QTableWidget()
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(7)  # Now we have 7 columns
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

        # Update data and save
        self.data[current_tab_name] = new_data
        self.save_data()

        QtWidgets.QMessageBox.information(self, "Saved", "Data saved successfully.")


# Main
app = QApplication(sys.argv)
inventory = Inventory()
widget = QtWidgets.QStackedWidget()
widget.addWidget(inventory)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
widget.closeEvent = lambda event: app.quit()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
