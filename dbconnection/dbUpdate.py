import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)

cursor=db.cursor()

sql="update stud set marks=50 where s_name='abhi'"


cursor.execute(sql)
db.commit()