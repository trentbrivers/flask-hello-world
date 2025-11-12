import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Trent Rivers in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://flaskgres_user:RDS8pFdV9v2mrARfaRZPYInr4tG1Cdj6@dpg-d49ttpbipnbc7399q8q0-a/flaskgres")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://flaskgres_user:RDS8pFdV9v2mrARfaRZPYInr4tG1Cdj6@dpg-d49ttpbipnbc7399q8q0-a/flaskgres")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://flaskgres_user:RDS8pFdV9v2mrARfaRZPYInr4tG1Cdj6@dpg-d49ttpbipnbc7399q8q0-a/flaskgres")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://flaskgres_user:RDS8pFdV9v2mrARfaRZPYInr4tG1Cdj6@dpg-d49ttpbipnbc7399q8q0-a/flaskgres")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string =""
    response_string+= "<table>" #Opening tag for table in HTML
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string+= "<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://flaskgres_user:RDS8pFdV9v2mrARfaRZPYInr4tG1Cdj6@dpg-d49ttpbipnbc7399q8q0-a/flaskgres")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"