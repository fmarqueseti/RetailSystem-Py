##############################################################################
# File name: productsMenu.py                                                 #
# Date     : 2025-07-12                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : This is products main menu of the ERP system                    #
##############################################################################

import mysql_conn as myConn # MySQL connection
import myUtil               # Utilitary functions

def menu():
    myUtil.clear()
    print('-PRODUCTS MENU-')
    print('1 - Add')
    print('2 - Edit')
    print('3 - Delete')
    print('4 - List')
    print('0 - Return')

#
# Add product function
#
def addProduct():
    print('-PRODUCT--------')
    name = input('Name       : ')
    ingredients = input('Ingredients: ')
    category = input('Category   : ')
    price = float(input('Price      : '))

    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('INSERT INTO PRODUCT (NAME, INGREDIENTS, CATEGORY, PRICE) VALUES ("{}", "{}", "{}", {});'.format(name, ingredients, category, price))
            myConn.conn.commit()
            print('Product registered successfully!')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    myUtil.wait()    

#
# Delete product function
#
def deleteProduct():
    id = int(input('Product ID: '))

    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('DELETE FROM PRODUCT WHERE (ID = {});'.format(id))
            myConn.conn.commit()

            if cursor.rowcount > 0:
                print('Product deleted successfully!')
            else:
                print('Product not found!')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    myUtil.wait()

#
# List products function
#
def listProducts():
    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('SELECT ID, NAME, INGREDIENTS, CATEGORY, PRICE FROM PRODUCT;')
            res = cursor.fetchall()

            if len(res) > 0:
                for product in res:
                    print(product)

                delete = input('\nDelete product (y/N)?: ')

                if delete == 'Y' or delete == 'y':
                    deleteProduct()
            else:
                print('No products found to display.')
                myUtil.wait()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        myUtil.wait()

def main(isAdmin):
    myUtil.clear()
    adm = 'Access denied. Administrator privileges required.' # Access denied message
    op  = ''

    while op != '0':
        menu()

        op = input('=> ')

        match op:
            case '0':
                pass            
            case '1':
                if isAdmin:
                    addProduct()
                else:
                    print(adm)
                    myUtil.wait()
            case '3':
                if isAdmin:
                    deleteProduct()
                else:
                    print(adm)
                    myUtil.wait()
            case '4':
                listProducts()
            case _:
                print('Invalid option!')
                myUtil.wait()