##############################################################################
# File name: connection.py                                                   #
# Date     : 2025-07-15                                                      #
# Author   : Fábio Marques (fmarques@fmarques.eti.br)                        #
# Purpose  : Facade of connection with MySQL database (tkinter version)      #
##############################################################################

from tkinter import messagebox
import pymysql.cursors

class Connection():
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='****',
                password='****',
                database='****',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            messagebox.showerror('ERROR', f'Unable to connect database!')

    def validateLogin(self, userName, userPassword):
        isLogged = False
        isAdmin  = False

        try:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT ACCESS_LEVEL FROM USER WHERE ((USERNAME = "{}") AND (PASSWORD = MD5("{}")));'.format(userName, userPassword))
                res = cursor.fetchone()

                isLogged = res is not None
                if isLogged:
                    isAdmin = res['ACCESS_LEVEL'] == 2
        except:
            messagebox.showerror('ERROR', f'Unable to fetch user data!')

        return isLogged, isAdmin

    def userNameExists(self, userName):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT ACCESS_LEVEL FROM USER WHERE (USERNAME = "{}");'.format(userName))
                res = cursor.fetchone()

                return res is not None;
        except Exception as e:
            messagebox.showerror('ERROR', f'Unable to fetch user data! {e}')

    def signUpUser(self, userName, userPassword):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('INSERT INTO USER (USERNAME, PASSWORD, ACCESS_LEVEL) VALUES ("{}", MD5("{}"), 1);'.format(userName, userPassword))
                self.conn.commit()
                return True
        except Exception as e:
            messagebox.showerror('ERROR', F'Unable to fetch user data! {e}')

    def listProducts(self):
        try:
            with self.conn.cursor() as cursor: 
                cursor.execute('SELECT ID, NAME, INGREDIENTS, CATEGORY, PRICE FROM PRODUCT;')
                res = cursor.fetchall()

            return res
        except Exception as e:
            messagebox.showerror('An unexpected error occurred: {e}')

    def saveProduct(self, id, name, ingredients, category, price):
        try:
            with self.conn.cursor() as cursor: 
                if id == 0:
                    sql = 'INSERT INTO PRODUCT (NAME, INGREDIENTS, CATEGORY, PRICE) VALUES ("{}", "{}", "{}", {});'.format(name, ingredients, category, price)
                else:
                    sql = 'UPDATE PRODUCT SET NAME = "{}", INGREDIENTS = "{}", CATEGORY = "{}, PRICE = {} WHERE (ID = {})'.format(name, ingredients, category, price, id)

                cursor.execute(sql)
                self.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            messagebox.showerror('ERROR', f'An unexpected error occurred: {e}')
            return False

    def deleteProduct(self, id):
        try:
            with self.conn.cursor() as cursor: 
                cursor.execute('DELETE FROM PRODUCT WHERE (ID = {});'.format(id))
                self.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            messagebox.showerror('ERROR', f'An unexpected error occurred: {e}')
            return False
        
    def listOrders(self):
        try:
            with self.conn.cursor() as cursor: 
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

            return res
        except Exception as e:
            messagebox.showerror('ERROR', f'An unexpected error occurred: {e}')

    def registerDelivery(self, id):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''INSERT INTO ORDER_HISTORY
                                          SELECT
                                          ID,
                                          PRODUCT,
                                          QUANTITY

                                      FROM ORDER_ITEM
                                      WHERE (ID = {});'''.format(id))

                cursor.execute('''DELETE FROM ORDER_ITEM WHERE (ID = {});'''.format(id))
                self.conn.commit()

                return cursor.rowcount > 0
        except Exception as e:
            messagebox.showerror('ERROR', f'An unexpected error occurred: {e}')
            return False

    def statisticsCategory(self):
        try:
            with self.conn.cursor() as cursor: 
                cursor.execute('''SELECT
                                    P.CATEGORY,
                                    SUM(P.PRICE * H.QUANTITY) AS VALUE,
                                    SUM(H.QUANTITY) AS QUANTITY

                                FROM ORDER_HISTORY H
                                INNER JOIN PRODUCT P
                                ON P.ID = H.PRODUCT
                                GROUP BY P.CATEGORY
                                ORDER BY P.CATEGORY;''')
                print('statisticsCategory')
                return cursor.fetchall()
        except Exception as e:
            messagebox.showerror('ERORR', f'An unexpected error occurred: {e}')
            return list()

    def statisticsProduct(self):
        try:
            with self.conn.cursor() as cursor: 
                cursor.execute('''SELECT
                                    P.NAME,
                                    SUM(P.PRICE * H.QUANTITY) AS VALUE,
                                    SUM(H.QUANTITY) AS QUANTITY

                                FROM ORDER_HISTORY H
                                INNER JOIN PRODUCT P
                                ON P.ID = H.PRODUCT
                                GROUP BY P.NAME
                                ORDER BY P.NAME;''')
                print('statisticsProduct')
                return cursor.fetchall()
        except Exception as e:
            messagebox.showerror('ERORR', f'An unexpected error occurred: {e}')
            return list()
