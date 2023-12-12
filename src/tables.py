# Python definitions for objects representing the row formats of each database table
# Used in the Controller's internal representation of the database backend

class PowerSourceType:
    def __init__(self, power_source_type_id, type, output_load):
        self.power_source_type_id = power_source_type_id
        self.type = type
        self.output_load = output_load


class PowerSource:
    def __init__(self, power_source_id, name, power_source_type_id):
        self.power_source_id = power_source_id
        self.name = name
        self.power_source_type_id = power_source_type_id


class PowerSourceSubstationLink:
    def __init__(self, link_id, power_source_id, substation_id):
        self.link_id = link_id
        self.power_source_id = power_source_id
        self.substation_id = substation_id


class SubstationType:
    def __init__(self, substation_type_id, size, max_load):
        self.substation_type_id = substation_type_id
        self.size = size
        self.max_load = max_load


class Substation:
    def __init__(self, substation_id, name, current_load, substation_type_id):
        self.substation_id = substation_id
        self.name = name
        self.current_load = current_load
        self.substation_type_id = substation_type_id


class City:
    def __init__(self, city_id, name, population, energy_demand, current_load):
        self.city_id = city_id
        self.name = name
        self.population = population
        self.energy_demand = energy_demand
        self.current_load = current_load


class CityHQ:
    def __init__(self, hq_id, city_id, consumption_policy):
        self.hq_id = hq_id
        self.city_id = city_id
        self.consumption_policy = consumption_policy


class CitySubstationLink:
    def __init__(self, link_id, city_id, substation_id):
        self.link_id = link_id
        self.city_id = city_id
        self.substation_id = substation_id


class LocalGeneratorType:
    def __init__(self, generator_type_id, type, output_load):
        self.generator_type_id = generator_type_id
        self.type = type
        self.output_load = output_load


class LocalGenerator:
    def __init__(self, generator_id, city_id, generator_type_id):
        self.generator_id = generator_id
        self.city_id = city_id
        self.generator_type_id = generator_type_id
