#1.import mysql.connector 
import mysql.connector as sqlcon

#2.connection db to object 
mycon = sqlcon.connect(host="localhost",user="root",passwd="pratham@1")

#creating cursor instance : used to travese it row by row

curr=mycon.cursor()

#execute the query
new_database_name="demo"

if not mycon.database_exists(new_database_name):
    # If the database doesn't exist, create it
    create_database_query = f"CREATE DATABASE {new_database_name};"
    curr.execute(create_database_query)
    print(f"Database '{new_database_name}' has been created.")
else:
    # If the database already exists, print a message
    print(f"Database '{new_database_name}' already exists.")

# curr.execute(query)

print(curr)
mycon.close()
