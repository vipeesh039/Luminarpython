import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)

cursor=db.cursor()

sql="select * from stud"

cursor.execute(sql)

data=cursor.fetchone()
print(data)