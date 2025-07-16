##############################################################################
# File name: productsMenu.py                                                 #
# Date     : 2025-07-12                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : This is products main menu of the ERP system                    #
##############################################################################

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connection as conn
import tkinter as tk

class ProductsMenu():
    

    def clearGUID(self):
        self.name.delete(0, 'end')
        self.ingredients.delete(0, 'end')
        self.category.delete(0, 'end')
        self.price.delete(0, 'end')

    def listProducts(self):
        if not self.conn:
            self.conn = conn.Connection()

        self.tree.delete(*self.tree.get_children())

        products = self.conn.listProducts();

        for product in products:
            p = list()

            p.append(product['NAME'])
            p.append(product['INGREDIENTS'])
            p.append(product['CATEGORY'])
            p.append(product['PRICE'])

            self.tree.insert('', END, values=p, iid=product['ID'], tag=1)
            p.clear()

    def addProduct(self):
        if not self.conn:
            self.conn = conn.Connection()

        name = self.name.get()
        ingredients = self.ingredients.get()
        category = self.category.get()
        price = float(self.price.get())

        success = self.conn.saveProduct(0, name, ingredients, category, price)

        if success:
            self.clearGUID()
            self.listProducts()
            messagebox.showinfo ('Product', 'Product registered successfully!!')

    def deleteProduct(self):
        ok = messagebox.askyesno('Please confirm', 'Do you wish to permanently delete this product?')

        if ok:
            if not self.conn:
                self.conn = conn.Connection()

            id = int(self.tree.selection()[0])

            success = self.conn.deleteProduct(id)

            if success:
                self.clearGUID()
                self.listProducts()
                messagebox.showinfo ('Product', 'Product deleted successfully!!')

    def __init__(self, isAdmin):
        self.conn = False

        self.root = Tk()
        self.root.title('RetailSystem ERP :: Products')
        self.root.geometry("700x360")

        buttonAdd = Button(self.root, text="Add", width=10, command=self.addProduct)
        buttonAdd.grid(row=0, column=0)
        buttonRefresh = Button(self.root, text="Refresh", width=10, command=self.listProducts)
        buttonRefresh.grid(row=0, column=1)
        buttonDelete = Button(self.root, text="Delete", width=10, command=self.deleteProduct)
        buttonDelete.grid(row=0, column=2)

        if not isAdmin:
            buttonAdd.config(state=tk.DISABLED)
            buttonDelete.config(state=tk.DISABLED)            

        self.tree = ttk.Treeview(self.root, selectmode='browse', columns=('column1', 'column2', 'column3', 'column4'), show='headings')

        self.tree.column('column1', width=210, minwidth=50, stretch=NO)
        self.tree.heading('#1', text='Name')

        self.tree.column('column2', width=320, minwidth=50, stretch=NO)
        self.tree.heading('#2', text='Ingredients')

        self.tree.column('column3', width=100, minwidth=50, stretch=NO)
        self.tree.heading('#3', text='Category')

        self.tree.column('column4', width=50, minwidth=50, stretch=NO)
        self.tree.heading('#4', text='Price')

        self.tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        Label(self.root, text='Name').grid(row=2, column=0)
        self.name = Entry(self.root)
        self.name.grid(row=2, column=1, columnspan=2)

        Label(self.root, text='Ingredients').grid(row=3, column=0)
        self.ingredients = Entry(self.root)
        self.ingredients.grid(row=3, column=1, columnspan=2)

        Label(self.root, text='Category').grid(row=4, column=0)
        self.category = Entry(self.root)
        self.category.grid(row=4, column=1, columnspan=2)

        Label(self.root, text='Price').grid(row=5, column=0)
        self.price = Entry(self.root)
        self.price.grid(row=5, column=1, columnspan=2)

        self.listProducts()

        self.root.mainloop()