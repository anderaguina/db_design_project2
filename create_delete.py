#MySQL for Python

import pymysql

try:
    # Open a database connection
    connection=pymysql.connect(
    host = 'localhost',     # Change this as needed!
    user = 'postgres',          # Change this as needed!
    password = 'postgres',  # Change this as needed!
    database = 'db_design_project2'     # Change this as needed!

# Create the UPDATE statement
sql = 'UPDATE tablename SET field1 = %s WHERE field2 = %s;'

# Run the UPDATE statement
if cursor.execute(sql,(value1, value2)) == 1:
    print("Table updated successfully")
else:
    print("Table NOT updated successfully")

# Create a cursor object
cursor = connection.cursor()

# Create the INSERT statement
sql = 'INSERT INTO tablename(field1, field2, ...) VALUES(%s, %s, ...);'

# Run the INSERT statement
if cursor.execute(sql, (value1, value2, ...)) == 1:
    print("Row inserted successfully")
else:
    print("Row could not be inserted")

# Commit and close the cursor
connection.commit()
cursor.close()
