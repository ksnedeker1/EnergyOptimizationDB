# Database-Driven Energy Optimization
### Oregon State University's CS 340 - Introduction to Databases
### Group 100: Kevin Ngo and Keifer Snedeker

For our CS340 term project, we chose to design and implement a database-driven website for simulating and tracking the flow of energy to satisfy the energy demands of cities.

Energy is created at Power Sources which are related M:N with Substations via the PowerSourceSubstationLinks table. Substations conceptually convert the high voltage energy of Power Sources to voltage levels suitable for Cities, and are related M:N with Cities via the CitySubstationLinks table. Cities are also capable of generating energy locally using Local Generators and are related 1:M via the Local Generators table. City HQs provide a means of scaling the energy demand of a city to simulate differences in overall energy efficiency between cities and are related 1:1 with a city. Additionally, the lookup tables LocalGeneratorTypes, PowerSourceTypes, and SubstationTypes define the available types of various entities and lower data redundancy in the tables of these entities.

CRUD operations can be done on each table through the table's associated webpage. By default, 'Read' is done when the page is loaded by populating the table with the rows currently present in that table. Users can 'Create' new rows by using a dedicated form which includes drop-down menus for fields related to FKs pre-populated with the human-readable names associated with each FK. Each table doubles as a form, so users can 'Update' a table by directly modifying the table's contents and clicking the 'Update' button when they are satisfied with their changes. Finally, users can 'Delete' a row by clicking the 'Delete' buttons present to the right of each row in the table.

## Citations

The general structure of our website, including semantics related to database connection, initialization, app execution, server-side hosting and python venv setup were directly taken from the [OSU Flask Starter App](https://github.com/osu-cs340-ecampus/flask-starter-app).

### app.py  
Adapted from [OSU Flask Starter App - app.py](https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/app.py)  
**Scope:** Some fundamental database initialization/connection and app execution semantics were adapted from the above link.  
**Originality:** The app.py from the Flask Starter App repo gave us a starting point, but aside from some lines related to database init/connection and app execution, the rest is original to our project and it's structure.  
**Date:** October 24, 2023

### db_connector.py
Sourced from [OSU Flask Starter App - db_connector.py](https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/database/db_connector.py)  
**Scope:** The contents of this file were provided by the OSU Flask Starter App resource available at the link above.  
**Originality:** No changes were made other than the removal of the dotenv approach which was replaced with directly-imported string variables.  
**Date:** November 22, 2023

### db_credentials.py (not included for security)
Sourced from [OSU Flask Starter App - db_credentials.py](https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/database/db_credentials.py)  
**Scope:** The contents of this file were provided by the OSU Flask Starter App resource available at the link above.  
**Originality:** Changed the definitions of variables to fit personal credentials.  
**Date:** November 22, 2023

### Flask (external library)
[Website](https://flask.palletsprojects.com/en/3.0.x/)  
Flask is the central Python web framework used in this project to handle template rendering (internally with Jinja2), URL routing, redirects, requests/responses, and more. This was used in alignment with the [OSU Flask Starter App](https://github.com/osu-cs340-ecampus/flask-starter-app).

### Flask-MySQLdb
[Website](https://pypi.org/project/Flask-MySQLdb/)  
Flask-MySQLdb is an extension for Flask integration with MySQL databases. This allowed our project to interface with the OSU-hosted MySQL database to manage connections and execute queries. This was used in alignment with the [OSU Flask Starter App](https://github.com/osu-cs340-ecampus/flask-starter-app).
