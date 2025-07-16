##############################################################################
# File name: mainMenu.py                                                     #
# Date     : 2025-07-15                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : Statistic file of the ERP system (tkinter version)              #
##############################################################################

from tkinter import messagebox
import connection as conn
import matplotlib.pyplot as plt 

class Statistics():
    def __init__(self):
        self.conn = False
    
    def statisticsProductValue(self):
        if not self.conn:
            self.conn = conn.Connection()

        res = self.conn.statisticsProduct()

        if len(res) > 0:
            plt.title('Sales Statistics: Product vs Value')
            plt.plot([p['NAME'] for p in res], [p['VALUE'] for p in res])
            plt.xlabel('Product Name')
            plt.ylabel('Sales Value')
            plt.show()     
        else:
            messagebox.showinfo ('Sales Statistics', 'No statistics found to display.')

    def statisticsProductQuantity(self):
        if not self.conn:
            self.conn = conn.Connection()

        res = self.conn.statisticsProduct()

        if len(res) > 0:
            plt.title('Sales Statistics: Product vs Quantity')
            plt.plot([p['NAME'] for p in res], [p['QUANTITY'] for p in res])
            plt.xlabel('Product Name')
            plt.ylabel('Quantity Sold')
            plt.show()
        else:
            messagebox.showinfo ('Sales Statistics', 'No statistics found to display.')

    def statisticsCategoryValue(self):
        if not self.conn:
            self.conn = conn.Connection()

        res = self.conn.statisticsCategory()

        if len(res) > 0:
            plt.title('Sales Statistics: Category vs Sales Value')
            plt.plot([p['CATEGORY'] for p in res], [p['VALUE'] for p in res])
            plt.xlabel('Product Category')
            plt.ylabel('Quantity Sold')
            plt.show()
        else:
            messagebox.showinfo ('Sales Statistics', 'No statistics found to display.')

    def statisticsCategoryQuantity(self):
        if not self.conn:
            self.conn = conn.Connection()

        res = self.conn.statisticsCategory()

        if len(res) > 0:
                plt.title('Sales Statistics: Product vs Quantity')
                plt.plot([p['CATEGORY'] for p in res], [p['QUANTITY'] for p in res])
                plt.xlabel('Product Name')
                plt.ylabel('Quantity Sold')
                plt.show()
        else:
            messagebox.showinfo ('Sales Statistics', 'No statistics found to display.')
