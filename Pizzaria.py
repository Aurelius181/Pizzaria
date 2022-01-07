# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:40:18 2021

@author: pihd
"""

import sys
from PyQt5 import QtWidgets, uic #QtCore, QtGui, 
from PyQt5.QtWidgets import QMessageBox

# load GUI
qtCreatorFile = "Pizzaria.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Pizzaria(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pbExit.clicked.connect(self.bye)
        self.rbSmall.toggled.connect(self.CalculatePrice)
        self.rbMedium.toggled.connect(self.CalculatePrice)
        self.rbLarge.toggled.connect(self.CalculatePrice)
        self.cbBeef.stateChanged.connect(self.CalculatePrice)
        self.cbBellPepper.stateChanged.connect(self.CalculatePrice)
        self.cbChicken.stateChanged.connect(self.CalculatePrice)
        self.cbMushroom.stateChanged.connect(self.CalculatePrice)
        self.cbOnion.stateChanged.connect(self.CalculatePrice)
        self.cbPepperoni.stateChanged.connect(self.CalculatePrice)
        self.cbPork.stateChanged.connect(self.CalculatePrice)
        self.cbTomato.stateChanged.connect(self.CalculatePrice)
        self.pbOrder.clicked.connect(self.Message)
        
    def bye(self):
        self.close()

    def CalculatePrice(self):
        price = 0
        if self.rbSmall.isChecked():
            price += 5
        elif self.rbMedium.isChecked():
            price += 10
        elif self.rbLarge.isChecked():
            price += 15

        if self.cbBeef.isChecked():
            price += 4
        if self.cbBellPepper.isChecked():
            price += 1
        if self.cbChicken.isChecked():
            price += 2
        if self.cbMushroom.isChecked():
            price += 1
        if self.cbOnion.isChecked():
            price += 1
        if self.cbPepperoni.isChecked():
            price += 4
        if self.cbPork.isChecked():
            price += 3
        if self.cbTomato.isChecked():
            price += 1

        self.lePrice.setText("{:.2f}".format(price))
        salesTax = float(price) * 0.09
        self.leSalesTax.setText("{:.2f}".format(salesTax))
        Total = "{:.2f}".format(salesTax+float(price))
        self.leTotal.setText(Total)
        return (Total)

    def Message(self, CalculatePrice):
        Total = self.CalculatePrice()
        Note = "Dear Customer,\n\nPlease pay $"+Total +\
            " at cashier and wait for your delicious pizza.\n\n"+\
                "Thanks for your business and have a nice day!\n\n"+\
                    "Pizzaria Management"
        QMessageBox.about(self, "Pizzaria", Note)

if __name__ == "__main__":
    # app main
    app = QtWidgets.QApplication(sys.argv)
    window = Pizzaria()
    window.show()
    sys.exit(app.exec_())