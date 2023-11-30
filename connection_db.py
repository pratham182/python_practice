import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="pratham@1")
c=conn.cursor()
c.execute("show databases","use Flight_search","CREATE TABLE EMPLOYEE(Name VARCHAR2(20), Email VARCHAR2(100), DOB DATE)  ")


for i in c:
    print(i)


