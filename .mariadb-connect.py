import pymysql.cursors
 
# Connect to the database
connection = pymysql.connect(
        host='localhost',
        user='root',
        password='hoge',
        db='test',
        port = 3307
        )

c = connection.cursor()
connection.close()
print("PythonからMariaDBに接続できました。")