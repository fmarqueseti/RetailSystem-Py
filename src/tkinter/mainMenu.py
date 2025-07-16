##############################################################################
# File name: mainMenu.py                                                     #
# Date     : 2025-07-15                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : Main menu file of the ERP system (tkinter version)              #
##############################################################################

from tkinter import *
import connection as conn
import productsMenu
import ordersList
import statistics
import webbrowser

class MainScreen():
    def products(self):
        productsMnu = productsMenu.ProductsMenu(self.isAdmin)

    def listOrders(self):
        listOrders = ordersList.OrdersList()

    def statisticsProductValue(self):
        s = statistics.Statistics()
        s.statisticsProductValue()

    def statisticsProductQuantity(self):
        s = statistics.Statistics()
        s.statisticsProductQuantity()

    def statisticsCategoryValue(self):
        s = statistics.Statistics()
        s.statisticsCategoryValue()

    def statisticsCategoryQuantity(self):
        s = statistics.Statistics()
        s.statisticsCategoryQuantity()

    def visitRepository(self):
        webbrowser.open('www.github.com/fmarqueseti/RetailSystem-Py', new=0, autoraise=True)

    def helpAbout(self):
        self.about = Tk()
        self.about.title('RetailSystem ERP :: About')
        self.about.geometry("450x200")

        Label(self.about, text='RetailSystem ERP (tkinter version)').grid(row=0, column=0, columnspan=2)
        Label(self.about, text='An educational sales management system built with Python.').grid(row=1, column=0, columnspan=2)

        Label(self.about, text='').grid(row=2, column=0)

        Label(self.about, text='Course: Python from Beginner to Advanced + Artificial Intelligence').grid(row=3, column=0, columnspan=2)
        Label(self.about, text='Instructor: Caio Sampaio — Pythonando', justify='left').grid(row=4, column=0, columnspan=2)
        
        Label(self.about, text='').grid(row=5, column=0)

        Label(self.about, text='Developed and enhanced by: Fábio Marques').grid(row=6, column=0, columnspan=2)

        Label(self.about, text='').grid(row=7, column=0)

        Button(self.about, text='Close', command=self.about.destroy).grid(row=8, column=0)
        Button(self.about, text='Visit repository', command=self.visitRepository).grid(row=8, column=1)

        self.about.mainloop()

    def __init__(self, isAdmin):
        self.isAdmin = isAdmin

        self.root = Tk()
        self.root.title('RetailSystem ERP :: Main Menu')
        self.root.geometry("800x600")

        self.mainMenu = Menu(self.root)

        self.statisticsMenu = Menu(self.mainMenu, tearoff=0)
        self.statisticsMenu.add_command(label='Product vs Sales Value', command=self.statisticsProductValue)
        self.statisticsMenu.add_command(label='Product vs Quantity Sold', command=self.statisticsProductQuantity)
        self.statisticsMenu.add_command(label='Category vs Sales Value', command=self.statisticsCategoryValue)
        self.statisticsMenu.add_command(label='Category vs Quantity Sold', command=self.statisticsCategoryQuantity)

        self.ordersMenu = Menu(self.mainMenu, tearoff=0)
        self.ordersMenu.add_command(label='List', command=self.listOrders)
        self.ordersMenu.add_cascade(label='Statistics', menu=self.statisticsMenu)

        self.fileMenu = Menu(self.mainMenu, tearoff=0)
        self.fileMenu.add_command(label='Product', command=self.products)
        self.fileMenu.add_cascade(label='Orders', menu=self.ordersMenu)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Exit', command=self.root.destroy)

        self.helpMenu = Menu(self.mainMenu, tearoff=0)
        self.helpMenu.add_command(label='Welcome')
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label='About', command=self.helpAbout)
        self.helpMenu.entryconfig('Welcome', state='disabled')

        self.mainMenu.add_cascade(label='File', menu=self.fileMenu)
        self.mainMenu.add_cascade(label='Help', menu=self.helpMenu)

        self.root.config(menu=self.mainMenu)

        self.root.mainloop()