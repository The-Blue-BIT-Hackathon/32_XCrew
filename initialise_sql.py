"""
Run this to initialise MySQL Schema on your machine

Edit user,password and database 
"""

import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    user='root',
    password='1234',
    database='trial1',
    host='localhost'
)
# Create a cursor object
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS XCrewDB;")
cursor.execute("USE XCrewDB;")

# Create users table
query = """CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50) PRIMARY KEY,
        password VARCHAR(50),
        balance INT) ;"""
cursor.execute(query)

# Create allergies table
query = """CREATE TABLE IF NOT EXISTS allergies (
        username VARCHAR(50) PRIMARY KEY,
        allergy VARCHAR(50) );
"""
cursor.execute(query)


# Create prefferences table
query = """CREATE TABLE IF NOT EXISTS prefferences (
        username VARCHAR(50) PRIMARY KEY,
        Punjabi CHAR(1),Rajasthani CHAR(1),Gujarathi CHAR(1),Maharashtrian CHAR(1),Bengali CHAR(1),
        SouthIndian CHAR(1),NorthIndian CHAR(1)) ;
"""
cursor.execute(query)

# Create timetable table
query = """CREATE TABLE IF NOT EXISTS timetable (
        Day CHAR(10),
        Breakfast VARCHAR(20),Lunch VARCHAR(20),Snacks VARCHAR(20),Dinner VARCHAR(20));

"""
cursor.execute(query)

# Close the cursor and connection
mydb.commit()
cursor.close()
mydb.close()


