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