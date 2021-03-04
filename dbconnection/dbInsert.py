import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)

cursor=db.cursor()

sql="insert into stud values('101','abhi',40)"


cursor.execute(sql)
db.commit()