##############################################################################
# File name: login.py                                                        #
# Date     : 2025-07-15                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : Login file of the ERP system (tkinter version)                  #
##############################################################################

from tkinter import *
from tkinter import messagebox
import connection as conn
import mainMenu

class LoginForm():
    def mainScreen(self):
        self.root.destroy()
        mainMenu.MainScreen(self.isAdmin)

    def logIn(self):
        if not self.conn:
            self.conn = conn.Connection()

        self.isLogged, self.isAdmin = self.conn.validateLogin(self.userName.get(), self.userPassword.get())

        if self.isLogged:
            self.mainScreen()
        else:
            messagebox.showerror('Login', 'Invalid username or password!')

    def signUp(self):
        if not self.conn:
            self.conn = conn.Connection()

        if self.conn.userNameExists(self.userName.get()):
            messagebox.showerror('Login', 'User already registered!')
        else:
            self.mainScreen()

    def __init__(self):
        self.conn = False
        self.isAdmin = False

        self.root = Tk()

        self.root.title('RetailSystem ERP :: Login')
        self.root.geometry('300x100')

        Label(self.root, text='User name:').grid(row=0, column=0)
        self.userName = Entry(self.root)
        self.userName.grid(row=0, column=1)

        Label(self.root, text='Password:').grid(row=1, column=0)
        self.userPassword = Entry(self.root, show='*')
        self.userPassword.grid(row=1, column=1)

        Button(self.root, text='Log In', width=10, command=self.logIn).grid(row=3, column=0, padx=5, pady=5)
        Button(self.root, text='Sign Up', width=10, command=self.signUp).grid(row=3, column=1, padx=5, pady=5)

        self.root.mainloop()