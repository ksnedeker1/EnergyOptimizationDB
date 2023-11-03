# Adapted from https://github.com/osu-cs340-ecampus/flask-starter-app
from flask import Flask, render_template, json, redirect
# from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
# app.config['MYSQL_USER'] = 'cs340_snedekek'
# app.config['MYSQL_PASSWORD'] = '2194'
# app.config['MYSQL_DB'] = 'cs340_snedekek'
# app.config['MYSQL_CURSORCLASS'] = "DictCursor"


# mysql = MySQL(app)

tables = ['PowerSources', 'Substations', 'Cities', 'LocalGenerators', 'CityHQs', 'PowerSourceSubstationLinks', 
              'CitySubstationLinks', 'LocalGeneratorTypes', 'PowerSourceTypes', 'SubstationTypes']

# Routes
@app.route('/')
def root():
    # query = "SELECT * FROM diagnostic;"
    # query1 = 'DROP TABLE IF EXISTS diagnostic;';
    # query2 = 'CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);';
    # query3 = 'INSERT INTO diagnostic (text) VALUES ("MySQL is working!")';
    # query4 = 'SELECT * FROM diagnostic;';
    # cur = mysql.connection.cursor()
    # cur.execute(query1)
    # cur.execute(query2)
    # cur.execute(query3)
    # cur.execute(query4)
    # results = cur.fetchall()

    # return "<h1>MySQL Results</h1>" + str(results[0])
    return render_template('index.html', tables=tables)

@app.route('/powersources')
def powersources():
    return render_template('powersources.html', tables=tables)

@app.route('/substations')
def substations():
    return render_template('substations.html', tables=tables)

@app.route('/cities')
def cities():
    return render_template('cities.html', tables=tables)

@app.route('/localgenerators')
def localgenerators():
    return render_template('localgenerators.html', tables=tables)

@app.route('/cityhqs')
def cityhqs():
    return render_template('cityhqs.html', tables=tables)

@app.route('/powersourcesubstationlinks')
def powersourcesubstationlinks():
    return render_template('powersourcesubstationlinks.html', tables=tables)

@app.route('/citysubstationlinks')
def citysubstationlinks():
    return render_template('citysubstationlinks.html', tables=tables)

@app.route('/localgeneratortypes')
def localgeneratortypes():
    return render_template('localgeneratortypes.html', tables=tables)

@app.route('/powersourcetypes')
def powersourcetypes():
    return render_template('powersourcetypes.html', tables=tables)

@app.route('/substationtypes')
def substationtypes():
    return render_template('substationtypes.html', tables=tables)


# Listener
if __name__ == "__main__":
    app.run(port=15427, debug=True)
