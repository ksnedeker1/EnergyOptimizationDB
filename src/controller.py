# Handles the functional interfacing of CRUD operations between the Python layer and MySQL database backend.
# Also provides functionalities for clearing the database, loading the sample data, and FK-to-Name decoding.
# Manages an internal representation of the database backend.

from src.tables import *
from database.db_connector import connect_to_database, execute_query
from database.dmq import *


class Controller:
    def __init__(self):
        self.cities = []
        self.city_hqs = []
        self.city_substation_links = []
        self.local_generators = []
        self.local_generator_types = []
        self.power_sources = []
        self.power_source_substation_links = []
        self.power_source_types = []
        self.substations = []
        self.substation_types = []

    def clear_all(self):
        self.cities = []
        self.city_hqs = []
        self.city_substation_links = []
        self.local_generators = []
        self.local_generator_types = []
        self.power_sources = []
        self.power_source_substation_links = []
        self.power_source_types = []
        self.substations = []
        self.substation_types = []

    def load_db(self):
        self.clear_all()
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_power_sources).fetchall()
        for row in data:
            self.power_sources.append(PowerSource(*list(row.values())))
        data = execute_query(db_connection, r_substations).fetchall()
        for row in data:
            self.substations.append(Substation(*list(row.values())))
        data = execute_query(db_connection, r_cities).fetchall()
        for row in data:
            self.cities.append(City(*list(row.values())))
        data = execute_query(db_connection, r_local_generators).fetchall()
        for row in data:
            self.local_generators.append(LocalGenerator(*list(row.values())))
        data = execute_query(db_connection, r_city_hqs).fetchall()
        for row in data:
            self.city_hqs.append(CityHQ(*list(row.values())))
        data = execute_query(db_connection, r_power_source_substation_links).fetchall()
        for row in data:
            self.power_source_substation_links.append(PowerSourceSubstationLink(*list(row.values())))
        data = execute_query(db_connection, r_city_substation_links).fetchall()
        for row in data:
            self.city_substation_links.append(CitySubstationLink(*list(row.values())))
        data = execute_query(db_connection, r_local_generator_types).fetchall()
        for row in data:
            self.local_generator_types.append(LocalGeneratorType(*list(row.values())))
        data = execute_query(db_connection, r_power_source_types).fetchall()
        for row in data:
            self.power_source_types.append(PowerSourceType(*list(row.values())))
        data = execute_query(db_connection, r_substation_types).fetchall()
        for row in data:
            self.substation_types.append(SubstationType(*list(row.values())))
        db_connection.close()

    # Getters for FK-Name decoding ############################################################
    def get_power_sources(self):
        return [(ps.power_source_id, ps.name) for ps in self.power_sources]

    def get_substations(self):
        return [(s.substation_id, s.name) for s in self.substations]

    def get_cities(self):
        return [(c.city_id, c.name) for c in self.cities]

    def get_power_source_types(self):
        return [(t.power_source_type_id, t.type) for t in self.power_source_types]

    def get_substation_types(self):
        return [(t.substation_type_id, t.size) for t in self.substation_types]

    def get_local_generator_types(self):
        return [(t.generator_type_id, t.type) for t in self.local_generator_types]

    # CRUD for PowerSourceType ###################################################################
    def create_power_source_type(self, type, output_load):
        db_connection = connect_to_database()
        execute_query(db_connection, c_power_source_type, (type, output_load))
        db_connection.close()
        self.load_db()

    def read_power_source_type(self, power_source_type_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_power_source_type, (power_source_type_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_power_source_type(self, power_source_type_id, type=None, output_load=None):
        data = self.read_power_source_type(power_source_type_id)
        if data:
            new_type = type if type is not None else data.type
            new_output_load = output_load if output_load is not None else data.outputLoad
            db_connection = connect_to_database()
            execute_query(db_connection, u_power_source_type, (new_type, new_output_load, power_source_type_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_power_source_type(self, power_source_type_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_power_source_type, (power_source_type_id))
        db_connection.close()
        self.load_db()

    # CRUD for PowerSource ######################################################################
    def create_power_source(self, name, power_source_type_id):
        if not power_source_type_id:
            power_source_type_id = None
        db_connection = connect_to_database()
        execute_query(db_connection, c_power_source, (name, power_source_type_id))
        db_connection.close()
        self.load_db()

    def read_power_source(self, power_source_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_power_source, (power_source_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_power_source(self, power_source_id, name=None, power_source_type_id=None):
        data = self.read_power_source(power_source_id)
        if data:
            new_name = name if name is not None else data.name
            if power_source_type_id == "":
                new_power_source_type_id = None
            elif power_source_type_id is not None:
                new_power_source_type_id = power_source_type_id
            else:
                new_power_source_type_id = data.power_source_type_id
            db_connection = connect_to_database()
            execute_query(db_connection, u_power_source, (new_name, new_power_source_type_id, power_source_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_power_source(self, power_source_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_power_source, (power_source_id))
        db_connection.close()
        self.load_db()

    # CRUD for PowerSourceSubstationLink ################################################################
    def create_power_source_substation_link(self, power_source_id, substation_id):
        db_connection = connect_to_database()
        execute_query(db_connection, c_power_source_substation_link, (power_source_id, substation_id))
        db_connection.close()
        self.load_db()

    def read_power_source_substation_link(self, link_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_power_source_substation_link, (link_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_power_source_substation_link(self, link_id, power_source_id=None, substation_id=None):
        data = self.read_power_source_substation_link(link_id)
        if data:
            new_power_source_id = power_source_id if power_source_id is not None else data.powerSourceID
            new_substation_id = substation_id if substation_id is not None else data.substationID
            db_connection = connect_to_database()
            execute_query(db_connection, u_power_source_substation_link,
                          (new_power_source_id, new_substation_id, link_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_power_source_substation_link(self, link_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_power_source_substation_link, (link_id))
        db_connection.close()
        self.load_db()

    # CRUD for SubstationType ######################################################################
    def create_substation_type(self, size, max_load):
        db_connection = connect_to_database()
        execute_query(db_connection, c_substation_type, (size, max_load))
        db_connection.close()
        self.load_db()

    def read_substation_type(self, substation_type_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_substation_type, (substation_type_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_substation_type(self, substation_type_id, size=None, max_load=None):
        data = self.read_substation_type(substation_type_id)
        if data:
            new_size = size if size is not None else data.size
            new_max_load = max_load if max_load is not None else data.maxLoad
            db_connection = connect_to_database()
            execute_query(db_connection, u_substation_type, (new_size, new_max_load, substation_type_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_substation_type(self, substation_type_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_substation_type, (substation_type_id))
        db_connection.close()
        self.load_db()

    # CRUD for Substation #######################################################################
    def create_substation(self, name, current_load, substation_type_id):
        if not substation_type_id:
            substation_type_id = None
        db_connection = connect_to_database()
        execute_query(db_connection, c_substation, (name, current_load, substation_type_id))
        db_connection.close()
        self.load_db()

    def read_substation(self, substation_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_substation, (substation_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_substation(self, substation_id, name=None, current_load=None, substation_type_id=None):
        data = self.read_substation(substation_id)
        if data:
            new_name = name if name is not None else data.name
            new_current_load = current_load if current_load is not None else data.currentLoad
            if substation_type_id == "":
                new_substation_type_id = None
            elif substation_type_id is not None:
                new_substation_type_id = substation_type_id
            else:
                new_substation_type_id = data.substationTypeID
            db_connection = connect_to_database()
            execute_query(db_connection, u_substation,
                          (new_name, new_current_load, new_substation_type_id, substation_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_substation(self, substation_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_substation, (substation_id))
        db_connection.close()
        self.load_db()

    # CRUD for Cities ###########################################################################
    def create_city(self, name, population, energy_demand, current_load):
        db_connection = connect_to_database()
        execute_query(db_connection, c_city, (name, population, energy_demand, current_load))
        db_connection.close()
        self.load_db()

    def read_city(self, city_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_city, (city_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_city(self, city_id, name=None, population=None, energy_demand=None, current_load=None):
        data = self.read_city(city_id)
        if data:
            new_name = name if name is not None else data.name
            new_population = population if population is not None else data.population
            new_energy_demand = energy_demand if energy_demand is not None else data.energyDemand
            new_current_load = current_load if current_load is not None else data.currentLoad
            db_connection = connect_to_database()
            execute_query(db_connection, u_city,
                          (new_name, new_population, new_energy_demand, new_current_load, city_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_city(self, city_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_city, (city_id))
        db_connection.close()
        self.load_db()

    # CRUD for CityHQ ###########################################################################
    def create_city_hq(self, city_id, consumption_policy):
        db_connection = connect_to_database()
        execute_query(db_connection, c_city_hq, (city_id, consumption_policy))
        db_connection.close()
        self.load_db()

    def read_city_hq(self, hq_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_city_hq, (hq_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_city_hq(self, hq_id, city_id=None, consumption_policy=None):
        data = self.read_city_hq(hq_id)
        if data:
            new_city_id = city_id if city_id is not None else data.cityID
            new_consumption_policy = consumption_policy if consumption_policy is not None else data.consumptionPolicy
            db_connection = connect_to_database()
            execute_query(db_connection, u_city_hq, (new_city_id, new_consumption_policy, hq_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_city_hq(self, hq_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_city_hq, (hq_id))
        db_connection.close()
        self.load_db()

    # CRUD for CitySubstationLink ##################################################################
    def create_city_substation_link(self, substation_id, city_id):
        db_connection = connect_to_database()
        execute_query(db_connection, c_city_substation_link, (city_id, substation_id))
        db_connection.close()
        self.load_db()

    def read_city_substation_link(self, link_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_city_substation_link, (link_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_city_substation_link(self, link_id, city_id=None, substation_id=None):
        data = self.read_city_substation_link(link_id)
        if data:
            new_substation_id = substation_id if substation_id is not None else current_data['substationID']
            new_city_id = city_id if city_id is not None else current_data['cityID']
            db_connection = connect_to_database()
            execute_query(db_connection, u_city_substation_link, (new_city_id, new_substation_id, link_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_city_substation_link(self, link_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_city_substation_link, (link_id))
        db_connection.close()
        self.load_db()

    # CRUD for LocalGeneratorType ############################################################
    def create_local_generator_type(self, type, output_load):
        db_connection = connect_to_database()
        execute_query(db_connection, c_local_generator_type, (type, output_load))
        db_connection.close()
        self.load_db()

    def read_local_generator_type(self, generator_type_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_local_generator_type, (generator_type_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_local_generator_type(self, generator_type_id, type=None, output_load=None):
        data = self.read_local_generator_type(generator_type_id)
        if data:
            new_type = type if type is not None else data.type
            new_output_load = output_load if output_load is not None else data.outputLoad
            db_connection = connect_to_database()
            execute_query(db_connection, u_local_generator_type, (new_type, new_output_load, generator_type_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_local_generator_type(self, generator_type_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_local_generator_type, (generator_type_id))
        db_connection.close()
        self.load_db()

    # CRUD for LocalGenerator ################################################################
    def create_local_generator(self, city_id, generator_type_id):
        if not city_id:
            city_id = None
        if not generator_type_id:
            generator_type_id = None
        db_connection = connect_to_database()
        execute_query(db_connection, c_local_generator, (city_id, generator_type_id))
        db_connection.close()
        self.load_db()

    def read_local_generator(self, generator_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_local_generator, (generator_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_local_generator(self, generator_id, city_id=None, generator_type_id=None):
        data = self.read_local_generator(generator_id)
        if data:
            new_city_id = city_id if city_id != "" else None
            new_generator_type_id = generator_type_id if generator_type_id != "" else None
            db_connection = connect_to_database()
            execute_query(db_connection, u_local_generator, (new_city_id, new_generator_type_id, generator_id))
            db_connection.close()
            self.load_db()
            return True
        return False

    def delete_local_generator(self, generator_id):
        db_connection = connect_to_database()
        execute_query(db_connection, d_local_generator, (generator_id))
        db_connection.close()
        self.load_db()
