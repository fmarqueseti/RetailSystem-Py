##############################################################################
# File name: myERP.py                                                        #
# Date     : 2025-07-12                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : This main file of the ERP system                                #
##############################################################################

import getpass
import mysql_conn as myConn # MySQL connection
import myUtil               # Utilitary functions
import productsMenu         # ERP main menu
import ordersMenu           # ERP orders menu

isLogged = False
isAdmin  = False

def loginMenu():
    myUtil.clear()
    print('-LOGIN MENU----')
    print('1 - Log In')
    print('2 - Sign Up')

def mainMenu():
    myUtil.clear()
    print('-MAIN MENU-----')
    print('1 - Product')
    print('2 - Order')
    print('0 - Exit')

#
# Log In function
#
def logIn():
    isLogged = False
    isAdmin  = False

    print('-LOG IN--------')
    userName     = input('User name: ')
    userPassword = getpass.getpass('Password : ')

    try:
        with myConn.conn.cursor() as cursor:
            cursor.execute('SELECT ACCESS_LEVEL FROM USER WHERE ((USERNAME = "{}") AND (PASSWORD = MD5("{}")));'.format(userName, userPassword))
            res = cursor.fetchone()

            isLogged = res is not None
            if isLogged:
                isAdmin = res['ACCESS_LEVEL'] == 2
            else:
                print('Invalid username or password!')
                myUtil.wait()
    except:
        print('Unable to fetch user data!')
        myUtil.wait()

    return isLogged, isAdmin

#
# Sing Up function
#
def signUp():
    print('-SIGN UP--------')
    userName = input('User name: ')

    try:
        with myConn.conn.cursor() as cursor:
            cursor.execute('SELECT ACCESS_LEVEL FROM USER WHERE (USERNAME = "{}");'.format(userName))
            res = cursor.fetchone()

            if res is not None:
                print('User already registered!')
            else:
                try:
                    with myConn.conn.cursor() as cursor: 
                        userPassword = getpass.getpass('Password: ')                        
                        cursor.execute('INSERT INTO USER (USERNAME, PASSWORD, ACCESS_LEVEL) VALUES ("{}", MD5("{}"), 1);'.format(userName, userPassword))
                        myConn.conn.commit()
                        print('User registered successfully!')
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f'Unable to fetch user data! {e}')

    myUtil.wait()

while not isLogged:
    loginMenu()
    op = input('=> ')

    if op == '1':
        isLogged, isAdmin = logIn()
    elif op == '2':
        signUp()

if isLogged:
    op  = ''

    while op != '0':
        mainMenu()

        op = input('=> ')

        match op:
            case '0':
                pass
            case '1':
                productsMenu.main(isAdmin)
            case '2':
                ordersMenu.main()
            case _:
                print('Invalid option!')
                myUtil.wait()

myUtil.clear()
