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

    # def load_db(self, sampledata):
    #     self.clear_all()

    #     for data in sampledata['cities']:
    #         self.create_city(**data)

    #     for data in sampledata['cityhqs']:
    #         self.create_city_hq(**data)

    #     for data in sampledata['citysubstationlinks']:
    #         self.create_city_substation_link(**data)

    #     for data in sampledata['localgenerators']:
    #         self.create_local_generator(**data)

    #     for data in sampledata['localgeneratortypes']:
    #         self.create_local_generator_type(**data)

    #     for data in sampledata['powersources']:
    #         self.create_power_source(**data)

    #     for data in sampledata['powersourcesubstationlinks']:
    #         self.create_power_source_substation_link(**data)

    #     for data in sampledata['powersourcetypes']:
    #         self.create_power_source_type(**data)

    #     for data in sampledata['substations']:
    #         self.create_substation(**data)

    #     for data in sampledata['substationtypes']:
    #         self.create_substation_type(**data)

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

    # CRUD for PowerSourceType ###################################################################
    def create_power_source_type(self, power_source_type_id, type, output_load):
        data = PowerSourceType(power_source_type_id, type, output_load)
        self.power_source_types.append(data)

    def read_power_source_type(self, power_source_type_id):
        for data in self.power_source_types:
            if data.power_source_type_id == power_source_type_id:
                return data
        return None

    def update_power_source_type(self, power_source_type_id, type=None, output_load=None):
        data = self.read_power_source_type(power_source_type_id)
        if data:
            data.type = type if type is not None else data.type
            data.output_load = output_load if output_load is not None else data.output_load
            return True
        return False

    def delete_power_source_type(self, power_source_type_id):
        data = self.read_power_source_type(power_source_type_id)
        if data:
            self.power_source_types.remove(data)
            return True
        return False

    # CRUD for PowerSource ######################################################################
    def create_power_source(self, name, power_source_type_id):
        db_connection = connect_to_database()
        execute_query(db_connection, c_power_source, (name, power_source_type_id))
        db_connection.close()
        self.load_db()

    def read_power_source(self, power_source_id):
        db_connection = connect_to_database()
        data = execute_query(db_connection, r_power_source_substation_link, (link_id))
        db_connection.close()
        data = data.fetchall()
        return data

    def update_power_source(self, power_source_id, name=None, power_source_type_id=None):
        data = self.read_power_source(power_source_id)
        if data:
            data.name = name if name is not None else data.name
            data.power_source_type_id = power_source_type_id if power_source_type_id is not None else data.power_source_type_id
            return True
        return False

    def delete_power_source(self, power_source_id):
        data = self.read_power_source(power_source_id)
        if data:
            self.power_sources.remove(data)
            return True
        return False

    # CRUD for PowerSourceSubstationLink ################################################################
    def create_power_source_substation_link(self, link_id, power_source_id, substation_id):
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
            data.power_source_id = power_source_id if power_source_id is not None else data.power_source_id
            data.substation_id = substation_id if substation_id is not None else data.substation_id
            return True
        return False

    def delete_power_source_substation_link(self, link_id):
        data = self.read_power_source_substation_link(link_id)
        if data:
            self.power_source_substation_links.remove(data)
            return True
        return False

    # CRUD for SubstationType ######################################################################
    def create_substation_type(self, substation_type_id, size, max_load):
        data = SubstationType(substation_type_id, size, max_load)
        self.substation_types.append(data)

    def read_substation_type(self, substation_type_id):
        for data in self.substation_types:
            if data.substation_type_id == substation_type_id:
                return data
        return None

    def update_substation_type(self, substation_type_id, size=None, max_load=None):
        data = self.read_substation_type(substation_type_id)
        if data:
            data.size = size if size is not None else data.size
            data.max_load = max_load if max_load is not None else data.max_load
            return True
        return False

    def delete_substation_type(self, substation_type_id):
        data = self.read_substation_type(substation_type_id)
        if data:
            self.substation_types.remove(data)
            return True
        return False

    # CRUD for Substation #######################################################################
    def create_substation(self, substation_id, name, current_load, substation_type_id):
        data = Substation(substation_id, name, current_load, substation_type_id)
        self.substations.append(data)

    def read_substation(self, substation_id):
        for data in self.substations:
            if data.substation_id == substation_id:
                return data
        return None

    def update_substation(self, substation_id, name=None, current_load=None, substation_type_id=None):
        data = self.read_substation(substation_id)
        if data:
            data.name = name if name is not None else data.name
            data.current_load = current_load if current_load is not None else data.current_load
            data.substation_type_id = substation_type_id if substation_type_id is not None else data.substation_type_id
            return True
        return False

    def delete_substation(self, substation_id):
        data = self.read_substation(substation_id)
        if data:
            self.substations.remove(data)
            return True
        return False

    # CRUD for Cities ###########################################################################
    def create_city(self, city_id, name, population, energy_demand, current_load):
        data = City(city_id, name, population, energy_demand, current_load)
        self.cities.append(data)

    def read_city(self, city_id):
        for data in self.cities:
            if data.city_id == city_id:
                return data
        return None

    def update_city(self, city_id, name=None, population=None, energy_demand=None, current_load=None):
        data = self.read_city(city_id)
        if data:
            data.name = name or data.name
            data.population = population or data.population
            data.energy_demand = energy_demand or data.energy_demand
            data.current_load = current_load or data.current_load
            return True
        return False

    def delete_city(self, city_id):
        data = self.read_city(city_id)
        if data:
            self.cities.remove(data)
            return True
        return False

    # CRUD for CityHQ ###########################################################################
    def create_city_hq(self, hq_id, city_id, consumption_policy):
        data = CityHQ(hq_id, city_id, consumption_policy)
        self.city_hqs.append(data)

    def read_city_hq(self, hq_id):
        for data in self.city_hqs:
            if data.hq_id == hq_id:
                return data
        return None

    def update_city_hq(self, hq_id, city_id=None, consumption_policy=None):
        data = self.read_city_hq(hq_id)
        if data:
            data.city_id = city_id if city_id is not None else data.city_id
            data.consumption_policy = consumption_policy if consumption_policy is not None else data.consumption_policy
            return True
        return False

    def delete_city_hq(self, hq_id):
        data = self.read_city_hq(hq_id)
        if data:
            self.city_hqs.remove(data)
            return True
        return False

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
        print(link_id)
        execute_query(db_connection, d_city_substation_link, (link_id))
        db_connection.close()
        self.load_db()

    # CRUD for LocalGeneratorType ############################################################
    def create_local_generator_type(self, generator_type_id, type, output_load):
        data = LocalGeneratorType(generator_type_id, type, output_load)
        self.local_generator_types.append(data)

    def read_local_generator_type(self, generator_type_id):
        for data in self.local_generator_types:
            if data.generator_type_id == generator_type_id:
                return data
        return None

    def update_local_generator_type(self, generator_type_id, type=None, output_load=None):
        data = self.read_local_generator_type(generator_type_id)
        if data:
            data.type = type if type is not None else data.type
            data.output_load = output_load if output_load is not None else data.output_load
            return True
        return False

    def delete_local_generator_type(self, generator_type_id):
        data = self.read_local_generator_type(generator_type_id)
        if data:
            self.local_generator_types.remove(data)
            return True
        return False

    # CRUD for LocalGenerator ################################################################
    def create_local_generator(self, generator_id, city_id, generator_type_id):
        data = LocalGenerator(generator_id, city_id, generator_type_id)
        self.local_generators.append(data)

    def read_local_generator(self, generator_id):
        for data in self.local_generators:
            if data.generator_id == generator_id:
                return data
        return None

    def update_local_generator(self, generator_id, city_id=None, generator_type_id=None):
        data = self.read_local_generator(generator_id)
        if data:
            data.city_id = city_id if city_id is not None else data.city_id
            data.generator_type_id = generator_type_id if generator_type_id is not None else data.generator_type_id
            return True
        return False

    def delete_local_generator(self, generator_id):
        data = self.read_local_generator(generator_id)
        if data:
            self.local_generators.remove(data)
            return True
        return False
