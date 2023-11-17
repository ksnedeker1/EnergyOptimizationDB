# Adapted from https://github.com/osu-cs340-ecampus/flask-starter-app
from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL
from src.resources.sampledata import sampledata
from src.controller import Controller
from database.db_credentials import host, user, passwd, db
from database.db_connector import connect_to_database, execute_query
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = passwd
app.config['MYSQL_DB'] = db
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)

def init_db():
    db_connection = connect_to_database()
    ddl_path = os.path.join(app.root_path, 'database/DDL_v2.sql')
    with open(ddl_path, 'r') as ddl_file:
        ddl_commands = ddl_file.read()
    for command in ddl_commands.split(';'):
        if command.strip():
            execute_query(db_connection, command)
    db_connection.close()

init_db()

tables = ['PowerSources', 'Substations', 'Cities', 'LocalGenerators', 'CityHQs', 'PowerSourceSubstationLinks',
              'CitySubstationLinks', 'LocalGeneratorTypes', 'PowerSourceTypes', 'SubstationTypes']

controller = Controller()
controller.load_db()


# Webpage routes
@app.route('/')
def root():
    return render_template('index.html', tables=tables)


@app.route('/powersources')
def powersources():
    return render_template('powersources.html', tables=tables, data=controller.power_sources)


@app.route('/substations')
def substations():
    return render_template('substations.html', tables=tables, data=controller.substations)


@app.route('/cities')
def cities():
    return render_template('cities.html', tables=tables, data=controller.cities)


@app.route('/localgenerators')
def localgenerators():
    return render_template('localgenerators.html', tables=tables, data=controller.local_generators)


@app.route('/cityhqs')
def cityhqs():
    return render_template('cityhqs.html', tables=tables, data=controller.city_hqs)


@app.route('/powersourcesubstationlinks')
def powersourcesubstationlinks():
    return render_template('powersourcesubstationlinks.html', tables=tables, data=controller.power_source_substation_links)


@app.route('/citysubstationlinks')
def citysubstationlinks():
    return render_template('citysubstationlinks.html', tables=tables, data=controller.city_substation_links)


@app.route('/localgeneratortypes')
def localgeneratortypes():
    return render_template('localgeneratortypes.html', tables=tables, data=controller.local_generator_types)


@app.route('/powersourcetypes')
def powersourcetypes():
    return render_template('powersourcetypes.html', tables=tables, data=controller.power_source_types)


@app.route('/substationtypes')
def substationtypes():
    return render_template('substationtypes.html', tables=tables, data=controller.substation_types)


# CRUD and data manipulation routes
@app.route('/load_sample_data', methods=['POST'])
def load_sample_data():
    init_db()
    controller.load_db()
    return redirect(url_for('root'))


@app.route('/clear_database', methods=['POST'])
def clear_database():
    controller.clear_all()
    return redirect(url_for('root'))


@app.route('/create_city', methods=['POST'])
def create_city():
    city_id = request.form['city_id']
    name = request.form['name']
    population = request.form['population']
    energy_demand = request.form['energy_demand']
    current_load = request.form['current_load']
    controller.create_city(city_id, name, population, energy_demand, current_load)
    return redirect(url_for('cities'))


@app.route('/update_cities', methods=['POST'])
def update_cities():
    city_ids = request.form.getlist('city_id[]')
    names = request.form.getlist('name[]')
    populations = request.form.getlist('population[]')
    energy_demands = request.form.getlist('energy_demand[]')
    current_loads = request.form.getlist('current_load[]')
    for i in range(len(city_ids)):
        controller.update_city(city_ids[i], names[i], populations[i], energy_demands[i], current_loads[i])
    return redirect(url_for('cities'))


@app.route('/delete_city', methods=['POST'])
def delete_city():
    city_id = request.form['delete_city_id']
    print(city_id, type(city_id))
    print(type(controller.cities[0].city_id))
    controller.delete_city(city_id)
    return redirect(url_for('cities'))


@app.route('/create_cityhq', methods=['POST'])
def create_cityhq():
    hq_id = request.form['hq_id']
    city_id = request.form['city_id']
    consumption_policy = request.form['consumption_policy']
    controller.create_city_hq(hq_id, city_id, consumption_policy)
    return redirect(url_for('cityhqs'))


@app.route('/update_city_hqs', methods=['POST'])
def update_city_hqs():
    hq_ids = request.form.getlist('hq_id[]')
    city_ids = request.form.getlist('city_id[]')
    consumption_policies = request.form.getlist('consumption_policy[]')
    for i in range(len(hq_ids)):
        controller.update_city_hq(hq_ids[i], city_ids[i], consumption_policies[i])
    return redirect(url_for('cityhqs'))


@app.route('/delete_city_hq', methods=['POST'])
def delete_city_hq():
    hq_id = request.form['delete_hq_id']
    controller.delete_city_hq(hq_id)
    return redirect(url_for('cityhqs'))


@app.route('/create_city_substation_link', methods=['POST'])
def create_city_substation_link():
    substation_id = request.form['substationID']
    city_id = request.form['cityID']
    controller.create_city_substation_link(city_id, substation_id)
    return redirect(url_for('citysubstationlinks'))


@app.route('/update_city_substation_links', methods=['POST'])
def update_city_substation_links():
    link_ids = request.form.getlist('link_id[]')
    substation_ids = request.form.getlist('substation_id[]')
    city_ids = request.form.getlist('city_id[]')
    for i in range(len(link_ids)):
        controller.update_city_substation_link(link_ids[i], city_id=city_ids[i], substation_id=substation_ids[i])
    return redirect(url_for('citysubstationlinks'))


@app.route('/delete_city_substation_link', methods=['POST'])
def delete_city_substation_link():
    link_id = request.form['delete_link_id']
    controller.delete_city_substation_link(link_id)
    return redirect(url_for('citysubstationlinks'))


@app.route('/create_local_generator', methods=['POST'])
def create_local_generator():
    generator_id = request.form['generatorID']
    city_id = request.form['cityID']
    generator_type_id = request.form['generatorTypeID']
    controller.create_local_generator(generator_id, city_id, generator_type_id)
    return redirect(url_for('localgenerators'))


@app.route('/update_local_generators', methods=['POST'])
def update_local_generators():
    generator_ids = request.form.getlist('generator_id[]')
    city_ids = request.form.getlist('city_id[]')
    generator_type_ids = request.form.getlist('generator_type_id[]')
    for i in range(len(generator_ids)):
        controller.update_local_generator(generator_ids[i], city_ids[i], generator_type_ids[i])
    return redirect(url_for('localgenerators'))


@app.route('/delete_local_generator', methods=['POST'])
def delete_local_generator():
    generator_id = request.form['delete_generator_id']
    controller.delete_local_generator(generator_id)
    return redirect(url_for('localgenerators'))


@app.route('/create_local_generator_type', methods=['POST'])
def create_local_generator_type():
    generator_type_id = request.form['generator_type_id']
    type_ = request.form['type']
    output_load = request.form['output_load']
    controller.create_local_generator_type(generator_type_id, type_, output_load)
    return redirect(url_for('localgeneratortypes'))


@app.route('/update_local_generator_types', methods=['POST'])
def update_local_generator_types():
    generator_type_ids = request.form.getlist('generator_type_id[]')
    types = request.form.getlist('type[]')
    output_loads = request.form.getlist('output_load[]')
    for i in range(len(generator_type_ids)):
        controller.update_local_generator_type(generator_type_ids[i], types[i], float(output_loads[i]))
    return redirect(url_for('localgeneratortypes'))


@app.route('/delete_local_generator_type', methods=['POST'])
def delete_local_generator_type():
    generator_type_id = request.form['delete_generator_type_id']
    controller.delete_local_generator_type(generator_type_id)
    return redirect(url_for('localgeneratortypes'))


@app.route('/create_power_source', methods=['POST'])
def create_power_source():
    power_source_id = request.form['power_source_id']
    name = request.form['name']
    power_source_type_id = request.form['power_source_type_id']
    controller.create_power_source(power_source_id, name, power_source_type_id)
    return redirect(url_for('powersources'))


@app.route('/update_power_sources', methods=['POST'])
def update_power_sources():
    power_source_ids = request.form.getlist('power_source_id[]')
    names = request.form.getlist('name[]')
    power_source_type_ids = request.form.getlist('power_source_type_id[]')
    for i in range(len(power_source_ids)):
        controller.update_power_source(power_source_ids[i], names[i], power_source_type_ids[i])
    return redirect(url_for('powersources'))


@app.route('/delete_power_source', methods=['POST'])
def delete_power_source():
    power_source_id = request.form['delete_power_source_id']
    controller.delete_power_source(power_source_id)
    return redirect(url_for('powersources'))


@app.route('/create_power_source_substation_link', methods=['POST'])
def create_power_source_substation_link():
    link_id = request.form['link_id']
    power_source_id = request.form['power_source_id']
    substation_id = request.form['substation_id']
    controller.create_power_source_substation_link(link_id, power_source_id, substation_id)
    return redirect(url_for('powersourcesubstationlinks'))


@app.route('/update_power_source_substation_links', methods=['POST'])
def update_power_source_substation_links():
    link_ids = request.form.getlist('link_id[]')
    power_source_ids = request.form.getlist('power_source_id[]')
    substation_ids = request.form.getlist('substation_id[]')
    for i in range(len(link_ids)):
        controller.update_power_source_substation_link(link_ids[i], power_source_ids[i], substation_ids[i])
    return redirect(url_for('powersourcesubstationlinks'))


@app.route('/delete_power_source_substation_link', methods=['POST'])
def delete_power_source_substation_link():
    link_id = request.form['delete_link_id']
    controller.delete_power_source_substation_link(link_id)
    return redirect(url_for('powersourcesubstationlinks'))


@app.route('/create_power_source_type', methods=['POST'])
def create_power_source_type():
    power_source_type_id = request.form['power_source_type_id']
    type_ = request.form['type']
    output_load = request.form['output_load']
    controller.create_power_source_type(power_source_type_id, type_, output_load)
    return redirect(url_for('powersourcetypes'))


@app.route('/update_power_source_types', methods=['POST'])
def update_power_source_types():
    power_source_type_ids = request.form.getlist('power_source_type_id[]')
    types = request.form.getlist('type[]')
    output_loads = request.form.getlist('output_load[]')
    for i in range(len(power_source_type_ids)):
        controller.update_power_source_type(power_source_type_ids[i], types[i], output_loads[i])
    return redirect(url_for('powersourcetypes'))


@app.route('/delete_power_source_type', methods=['POST'])
def delete_power_source_type():
    power_source_type_id = request.form['delete_power_source_type_id']
    controller.delete_power_source_type(power_source_type_id)
    return redirect(url_for('powersourcetypes'))


@app.route('/create_substation', methods=['POST'])
def create_substation():
    substation_id = request.form['substation_id']
    name = request.form['name']
    current_load = request.form['current_load']
    substation_type_id = request.form['substation_type_id']
    controller.create_substation(substation_id, name, current_load, substation_type_id)
    return redirect(url_for('substations'))


@app.route('/update_substations', methods=['POST'])
def update_substations():
    substation_ids = request.form.getlist('substation_id[]')
    names = request.form.getlist('name[]')
    current_loads = request.form.getlist('current_load[]')
    substation_type_ids = request.form.getlist('substation_type_id[]')
    for i in range(len(substation_ids)):
        controller.update_substation(substation_ids[i], names[i], current_loads[i], substation_type_ids[i]
        )
    return redirect(url_for('substations'))


@app.route('/delete_substation', methods=['POST'])
def delete_substation():
    substation_id = request.form['delete_substation_id']
    controller.delete_substation(substation_id)
    return redirect(url_for('substations'))


@app.route('/create_substation_type', methods=['POST'])
def create_substation_type():
    substation_type_id = request.form['substation_type_id']
    size = request.form['size']
    max_load = request.form['max_load']
    controller.create_substation_type(substation_type_id, size, max_load)
    return redirect(url_for('substationtypes'))


@app.route('/update_substation_types', methods=['POST'])
def update_substation_types():
    substation_type_ids = request.form.getlist('substation_type_id[]')
    sizes = request.form.getlist('size[]')
    max_loads = request.form.getlist('max_load[]')
    for i in range(len(substation_type_ids)):
        controller.update_substation_type(substation_type_ids[i], sizes[i], max_loads[i]
        )
    return redirect(url_for('substationtypes'))


@app.route('/delete_substation_type', methods=['POST'])
def delete_substation_type():
    substation_type_id = request.form['delete_substation_type_id']
    controller.delete_substation_type(substation_type_id)
    return redirect(url_for('substationtypes'))


# Listener
if __name__ == "__main__":
    app.run(port=15427, debug=True)
