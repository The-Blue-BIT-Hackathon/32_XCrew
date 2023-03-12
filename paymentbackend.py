"""
Backend program for payments system. 
Users will pay real money for credits using UPI, these credits will be used for everyday purchases
Stores Username, password, balance in Mysql. (Db can be changed to PostgreSQL)
Requirement: SQL server connection (Input data of name/username, password, account balance/ AmountPayed)

Pending steps: UPI integration for buing credits and Frontend page for payments
Update: Used qrcode library instead to scan UPI id
"""
import mysql.connector
user1 = "root"
password1 = "1234"
database1 = "trial1"

user = []
global First_User, users, AmountPayed
First_User = False
users = []


def UPIpayment():
    import os
    import qrcode

    upi_id = input("Enter seller's UPI id: ")

    # Generate QR code for UPI id
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("seller_qr.png")

    """# Display QR code in command line
    if os.name == 'nt':
        os.system('start seller_qr.png')
    elif os.name == 'posix':
        os.system('open seller_qr.png')"""






def first_run(users):
    # Create a cursor object to execute queries
    mycursor = mydb.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), password VARCHAR(255), balance INT);")
    for user in users:
        username, password, balance = user[0], user[1], user[2]
        mycursor.execute(
            f"INSERT INTO users VALUES ('{username}','{password}','{balance}');")
    print("Table done! ")




def load_users():
    """
    Extract info from SQL table into 2D list
    """

    mycursor = mydb.cursor()
    mycursor.execute("SELECT username, password, balance FROM users")
    rows = mycursor.fetchall()
    users = []
    for row in rows:
        users.append([row[0], row[1], row[2]])

    # Close the cursor and connection
    mycursor.close()
    return users




def save_users():
    """
    Save user data to SQL server with attributes 
    username, password , balance
    """

    # Create a cursor object to execute queries
    mycursor = mydb.cursor()

    # Insert user data into table
    if user != []:
        u = user[0]
        new_password = user[1]
        new_balance = user[2]
        sql = f"UPDATE users SET password='{new_password}', balance={new_balance} WHERE username='{u}';"
        mycursor.execute(sql)

    print("change(s) made.")




def login(users, username, password):
    """
    Check if a username and password match an existing user.
    """
    global user

    for i in users:
        if i[0] == username:
            user = i
            break
    if user == []:
        return False
    elif user[1] == password:
        return True




def deduct_money(users, username, amount):
    """
    Deduct a specified amount from a user's balance.
    """

    balance = user[2]
    if balance >= amount:
        balance -= amount
        user[2] = balance
        save_users()
        print("Payment successful!")
    else:
        print("Insufficient balance!")




def add_user(users, username, password):
    mycursor = mydb.cursor()
    """
    Add a new user with 
    """
    track = f"['{username}',"
    if track not in str(users):
        users.append([username, password, 10000])
        if users != []:
            mycursor.execute(
                f"INSERT INTO users values('{username}','{password}','10000');")
        print("New user added!")

    else:
        print("User already exists!")




# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user=user1,
    password=password1,
    database=database1
)

# Load user data from file
try:
    users = load_users()
except:
    pass
if users == []:
    First_User = True

# Prompt user to log in or create a new account
while True:
    print("1. Log in")
    print("2. Create new account")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1" and users != []:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(users, username, password):
            amount = int(input("Enter amount to pay: "))
            deduct_money(users, username, amount)
        else:
            print("Invalid username or password.")
    elif choice == "2" or users == []:
        print("\n CREATING NEW ACCOUNT")
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        add_user(users, username, password)

    elif choice == '3':
        print(users)
        if First_User == True:
            first_run(users)
        mydb.commit()
        print("Changes commited Succesfully")
        break

    else:
        print("Invalid choice.")
