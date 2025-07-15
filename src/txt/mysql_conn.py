import pymysql.cursors

conn = pymysql.connect(
    host='127.0.0.1',
    user='****',
    password='****',
    database='****',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
