from flask import Flask, request
import psycopg2

app = Flask(__name__)

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    database="MPBI",
    user="postgres",
    password="35789512357",
    host="localhost",
    port="5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Define a function to insert the data into the database
def insert_data(data):
    sql = "INSERT INTO user_input (data) VALUES (%s)"
    cur.execute(sql, (data,))
    conn.commit()
    print("Data inserted successfully!")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['allergies']
        insert_data(data)
        return "Data submitted successfully!"
    else:
        return '''
            <!DOCTYPE html>
<html>
<head>
<title>Allergies and Dietary Restrictions</title>
<style>
body {
font-family: Arial, sans-serif;
background-color: #f1f1f1;
}
h1 {
text-align: center;
}

form {
margin: 20px auto;
text-align: center;
}

input[type="text"] {
padding: 10px;
border: none;
border-radius: 5px;
background-color: white;
margin-right: 10px;
}

#result {
margin: 20px auto;
text-align: center;
}
</style>

</head>
<body>
<h1>Allergies and Dietary Restrictions</h1>
<p>Select any dietary restrictions or allergies you need to account for while preparing food:</p>
<form method="post">
<input type="text" id="allergies" name="allergies" placeholder="Type your allergies here" onkeyup="displaySelection()">
<button type="submit">Submit</button>
</form>
<div id="result"></div>
<script>
function displaySelection() {
var allergies = document.getElementById("allergies").value;

if (allergies === "") {
document.getElementById("result").innerHTML = "No dietary restrictions or allergies to account for.";
} else {
document.getElementById("result").innerHTML = "Account for " + allergies + " restrictions.";
}
}
</script>
</body>
</html>
        '''

if __name__ == '__main__':
    app.run(debug=True)
