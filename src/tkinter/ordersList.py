##############################################################################
# File name: ordersList.py                                                   #
# Date     : 2025-07-12                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : Orders list of the ERP system (tkinter version)                 #
##############################################################################

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connection as conn

class OrdersList():
    def listOrders(self):
        if not self.conn:
            self.conn = conn.Connection()

        self.tree.delete(*self.tree.get_children())

        orders = self.conn.listOrders();

        for order in orders:
            o = list()

            o.append(order['PRODUCT'])
            o.append(order['QUANTITY'])
            o.append(order['DELIVERY_ADDR'])
            o.append(order['NOTES'])

            self.tree.insert('', END, values=o, iid=order['ID'], tag=1)
            o.clear()

    def registerDelivery(self):
        ok = messagebox.askyesno('Please confirm', 'Do you want to register the delivery the order?')

        if ok:
            if not self.conn:
                self.conn = conn.Connection()

            id = int(self.tree.selection()[0])

            success = self.conn.registerDelivery(id)

            if success:
                self.listOrders()
                messagebox.showinfo ('Order Delivery', 'Order delivered successfully!')

    def __init__(self):
        self.conn = False

        self.root = Tk()
        self.root.title('RetailSystem ERP :: Orders List')
        self.root.geometry("700x270")

        Button(self.root, text="Register Delivery", width=15, command=self.registerDelivery).grid(row=0, column=0)
        Button(self.root, text="Refresh", width=15, command=self.listOrders).grid(row=0, column=1)

        self.tree = ttk.Treeview(self.root, selectmode='browse', columns=('column1', 'column2', 'column3', 'column4'), show='headings')

        self.tree.column('column1', width=200, minwidth=50, stretch=NO)
        self.tree.heading('#1', text='Product')

        self.tree.column('column2', width=80, minwidth=50, stretch=NO)
        self.tree.heading('#2', text='Quantity')

        self.tree.column('column3', width=200, minwidth=50, stretch=NO)
        self.tree.heading('#3', text='Delivery Address')

        self.tree.column('column4', width=200, minwidth=50, stretch=NO)
        self.tree.heading('#4', text='Notes')

        self.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5)        

        self.listOrders()

        self.root.mainloop()