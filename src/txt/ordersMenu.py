##############################################################################
# File name: ordersMenu.py                                                   #
# Date     : 2025-07-12                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : This is orders main menu of the ERP system                      #
##############################################################################

import mysql_conn as myConn     # MySQL connection
import myUtil                   # Utilitary functions
import statisticsMenu           # Orders statistics functions

def menu():
    myUtil.clear()
    print('-ORDERS MENU---')
    print('1 - List')
    print('2 - Statistics')
    print('0 - Return')

def deliveryOrder():
    id = int(input('Order ID: '))

    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('''INSERT INTO ORDER_HISTORY
                              SELECT
                                  ID,
                                  PRODUCT,
                                  QUANTITY

                              FROM ORDER_ITEM
                              WHERE (ID = {});'''.format(id))

            cursor.execute('''DELETE FROM ORDER_ITEM WHERE (ID = {});'''.format(id))
            myConn.conn.commit()

            if cursor.rowcount > 0:
                print('Order delivered successfully!')
            else:
                print('Order not found!')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    myUtil.wait()   

def listOrders():
    try:
        with myConn.conn.cursor() as cursor: 
            cursor.execute('''SELECT
                                  I.ID,
                                  P.NAME AS PRODUCT,
                                  P.INGREDIENTS,
                                  P.CATEGORY,
                                  P.PRICE,
                                  I.QUANTITY,
                                  I.DELIVERY_ADDR,
                                  I.NOTES

                              FROM ORDER_ITEM I
                              INNER JOIN PRODUCT P
                              ON  P.ID = I.PRODUCT;''')
            res = cursor.fetchall()

            if len(res) > 0:
                for order in res:
                    print(order)

                delivery = input('\nDo you want to register the delivery of an order (y/N)?: ')

                if delivery == 'Y' or delivery == 'y':
                    deliveryOrder()
            else:
                print('No orders found to display.')
                myUtil.wait()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        myUtil.wait()

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
                listOrders()
            case '2':
                statisticsMenu.main()
            case _:
                print('Invalid option!')
                myUtil.wait()