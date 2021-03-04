#  1. import mysql connector
import mysql.connector
#  2. establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)
#  3. create cursor object

cursor=db.cursor()

sql="create table stud(s_id varchar(30),s_name varchar(30),marks int)"

cursor.execute(sql)

#data=cursor.fetchone()
#print(data)