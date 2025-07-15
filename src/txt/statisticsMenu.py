##############################################################################
# File name: statisticsMenu.py                                               #
# Date     : 2025-07-12                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : This is orders statistics main menu of the ERP system           #
##############################################################################

import matplotlib.pyplot as plt 
import mysql_conn as myConn     # MySQL connection
import myUtil                   # Utilitary functions

def menu():
    myUtil.clear()
    print('-STATISTICS MENU-')
    print('1 - Product vs Sales Value')
    print('2 - Product vs Quantity Sold')
    print('3 - Category vs Sales Value')
    print('4 - Category vs Quantity Sold')
    print('0 - Return')

def statisticsProductValue():
    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('''SELECT
                                  P.NAME,
                                  SUM(P.PRICE * H.QUANTITY) AS VALUE

                              FROM ORDER_HISTORY H
                              INNER JOIN PRODUCT P
                               ON P.ID = H.PRODUCT
                              GROUP BY P.NAME
                              ORDER BY P.NAME;''')
            res = cursor.fetchall()

            if len(res) > 0:
                plt.title('Sales Statistics: Product vs Value')
                plt.plot([p['NAME'] for p in res], [p['VALUE'] for p in res])
                plt.xlabel('Product Name')
                plt.ylabel('Sales Value')
                plt.show()
            else:
                print('No statistics found to display.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def statisticsProductQuantity():
    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('''SELECT
                                  P.NAME,
                                  SUM(H.QUANTITY) AS QUANTITY

                              FROM ORDER_HISTORY H
                              INNER JOIN PRODUCT P
                               ON P.ID = H.PRODUCT
                              GROUP BY P.NAME
                              ORDER BY P.NAME;''')
            res = cursor.fetchall()

            if len(res) > 0:
                plt.title('Sales Statistics: Product vs Quantity')
                plt.plot([p['NAME'] for p in res], [p['QUANTITY'] for p in res])
                plt.xlabel('Product Name')
                plt.ylabel('Quantity Sold')
                plt.show()
            else:
                print('No statistics found to display.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def statisticsCategoryValue():
    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('''SELECT
                                  P.CATEGORY,
                                  SUM(P.PRICE * H.QUANTITY) AS VALUE

                              FROM ORDER_HISTORY H
                              INNER JOIN PRODUCT P
                               ON P.ID = H.PRODUCT
                              GROUP BY P.NAME
                              ORDER BY P.NAME;''')
            res = cursor.fetchall()

            if len(res) > 0:
                plt.title('Sales Statistics: Category vs Sales Value')
                plt.plot([p['CATEGORY'] for p in res], [p['VALUE'] for p in res])
                plt.xlabel('Product Category')
                plt.ylabel('Quantity Sold')
                plt.show()
            else:
                print('No statistics found to display.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def statisticsCategoryQuantity():
    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('''SELECT
                                  P.CATEGORY,
                                  SUM(H.QUANTITY) AS QUANTITY

                              FROM ORDER_HISTORY H
                              INNER JOIN PRODUCT P
                               ON P.ID = H.PRODUCT
                              GROUP BY P.NAME
                              ORDER BY P.NAME;''')
            res = cursor.fetchall()

            if len(res) > 0:
                plt.title('Sales Statistics: Category vs Quantity Sold')                
                plt.plot([p['CATEGORY'] for p in res], [p['QUANTITY'] for p in res])
                plt.xlabel('Product Category')
                plt.ylabel('Quantity Sold')
                plt.show()
            else:
                print('No statistics found to display.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    myUtil.clear()
    op  = ''

    while op != '0':
        menu()

        op = input('=> ')

        match op:
            case '0':
                pass
            case '1':
                statisticsProductValue()
            case '2':
                statisticsProductQuantity()
            case '3':
                statisticsCategoryValue()
            case '4':
                statisticsCategoryQuantity()
            case _:
                print('Invalid option!')
                myUtil.wait()