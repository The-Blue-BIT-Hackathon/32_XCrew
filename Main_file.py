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
def insert_data(name, id):
    sql = "INSERT INTO users (name, id) VALUES (%s, %s)"
    values = (name, id)
    cur.execute(sql, values)
    conn.commit()
    print("Data inserted successfully!")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        insert_data(name, id)
        return "Data submitted successfully!"
    else:
        return '''
<html>
            <body>
                <link rel="stylesheet" href="xcrew.css">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap" rel="stylesheet">
                <h1>Enter Details</h1>
                <form method="post" class="login">
                    <p class="name1">Username:</p>
                    <input type="text" id="name" name="name"><br><br>
                    <label for="id" class="id1">Password:<br></label>
                    <input type="text" id="id" name="id"><br><br>
                    <button type="submit" value="Submit" id="submit" class="submit">Sign up</button>
                </form>
            </body>
    
            <style> /*CSS*/
            *{  margin:0px;
                padding: 0px;
                font-family: 'Poppins', sans-serif;
                background-color: #191825;
                
            }
            .login{
            width: 400px;
            overflow: none;
            margin: 50 0 0 470px;
            padding: 80px;
            background: #865DFF ;
            border-radius: 15px;
            border: 2px;
            box-shadow: 0 0 20px 10px rgba(0, 0, 0, 0.05);
            
            }
            h1{
                margin: 50px 0 10px 650px;
                color: #fff;
                padding: 50px 0 0px 0px;
            
            }
            
            #name{
                width: 400px;
                height: 40px;
                border: none;
                border-radius: 30px;
                padding-left: 10px;
                border: 5px;
                background-color: #E384FF;
                color: #fff;
                font-size: 25px;
                
            }
            #id{
                width: 400px;
                height: 40px;
                border: none;
                border-radius: 30px;
                padding-left: 8px;
                border: 5px;
                background: none;
                background-color: #E384FF;
                font-size: 25px;
                color: #fff;
            
            }
            button {
              text-align: center;
              cursor: pointer;
              border-radius: 10px;
              font-size: 20px;
              margin-top: 10px;
              padding: 5px 20px;
              position: relative;
            }
            button:hover {
                  opacity: 0.8;
            }
            .name1{
                position: relative;
                margin: 0px 0px 20px ;
                color: #fff;
                background: none;
                font-weight: 800;
                font-size: x-large;
            }
            .id1{
                color: #fff;
                background: none;
                font-weight: 800;
                font-size: x-large;
            }
            .submit{
                background: none;
            }
            
            .submit{
                font-family: 'Poppins', sans-serif;
                border: 1px solid #FFA3FD;
                background: none;
                padding: 10px 30px;
                font-size: 20px;
                margin:10px 10px 10px 120px;
                overflow:hidden;
                position: absolute;
                border-radius: 25px;
                font-weight: 600;
                
            }
            .submit{
                color: #FFA3FD;
            }
            .submit:hover{
                color:#fff ;
            }
            .submit::before{
                content: "";
                position: absolute;
                left: 0px;
                width: 100%;
                height: 0%;
                background: #FFA3FD;
                z-index: -1 ;
                transition: 2s;
            
            }
            .submit::before{
                top:0px;
                border-radius: 0% 0% 50% 50%;
            }
            
            .submit:hover::before{
                height: 180%;
            }
            #name:focus{
                outline: none;
            }
            #id:focus{
                outline: none;
            }
            </style>
            
 </html>

        '''

if __name__ == '__main__':
    app.run(debug=True)
