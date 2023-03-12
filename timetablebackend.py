"""
Extracts food data from SQL and uses matplotlib to draw timetable in png format
"""


import mysql.connector
global plot_timetable

mydb = mysql.connector.connect(
    user='root',
    password='1234',
    database='trial1',
    host='localhost'
)
cursor = mydb.cursor()

# cursor.execute("""INSERT INTO timetable (Breakfast, Lunch, Snacks, Dinner) values
# ("tea", "Dal\nRice", "Coffee", "Rice"),
# ("Cheese Sandwich" , "Chole Bhature\nSalad", "Cream Roll", "Dal\nGulab Jamun"),
# ("Cheese Sandwich" , "Chole Bhature\nSalad", "Cream Roll", "Dal\nGulab Jamun"),
# ("Cheese Sandwich" , "Chole Bhature\nSalad", "Cream Roll", "Dal\nGulab Jamun"),
# ("Cheese Sandwich" , "Chole Bhature\nSalad", "Cream Roll", "Dal\nGulab Jamun"),
# ("Cheese Sandwich" , "Chole Bhature\nSalad", "Cream Roll", "Dal\nGulab Jamun"),
# ("Cheese Sandwich" , "Chole Bhature\nSalad", "Cream Roll", "Dal\nGulab Jamun"),
# ("Cheese Sandwich" , "Chole Bhature\nSalad", "Cream Roll", "Dal\nGulab Jamun");""")
# mydb.commit()

cursor.execute("SELECT Breakfast, Lunch, Snacks, Dinner FROM timetable;")
food_data = []
for row in cursor:
    food_data.append([row[0], row[1], row[2], row[3]])


mydb.commit()
cursor.close()
mydb.close()


def plot_timetable(food_data):
    import matplotlib.pyplot as plt

    data = [[' ', 'Breakfast', 'Lunch', 'Snacks', 'Dinner'],
            ['Daily'],
            ['Sunday'],
            ['Monday'],
            ['Tuesday'],
            ['Wednesday'],
            ['Thursday'],
            ['Friday'],
            ['Saturday']]
    for i in range(len(food_data)):
        data[i+1].extend(food_data[i])
    table = plt.table(cellText=data, loc='center')

    table.auto_set_font_size(True)
    table.scale(1.1, 2)
    plt.axis('off')

    plt.savefig("timetable.png")


plot_timetable(food_data)
