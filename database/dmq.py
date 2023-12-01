# CRUD queries for PowerSourceTypes #############################################################
r_power_source_types = 'SELECT * FROM PowerSourceTypes'
r_power_source_type = 'SELECT * FROM PowerSourceTypes WHERE powerSourceTypeID = %s'
c_power_source_type = 'INSERT INTO PowerSourceTypes (type, outputLoad) VALUES (%s, %s)'
u_power_source_type = 'UPDATE PowerSourceTypes SET type = %s, outputLoad = %s WHERE powerSourceTypeID = %s'
d_power_source_type = 'DELETE FROM PowerSourceTypes WHERE powerSourceTypeID = %s'

# CRUD queries for PowerSources #############################################################
r_power_sources = 'SELECT * FROM PowerSources'
r_power_source = 'SELECT * FROM PowerSourceSubstationLinks WHERE powerSourceID = %s'
c_power_source = 'INSERT INTO PowerSources (name, powerSourceTypeID) VALUES (%s, %s)'
u_power_source = 'UPDATE PowerSources SET name = %s, powerSourceTypeID = %s WHERE powerSourceID = %s'
d_power_source = 'DELETE FROM PowerSources WHERE powerSourceID = %s'

# CRUD queries for SubstationTypes #############################################################
r_substation_types = 'SELECT * FROM SubstationTypes'
r_substation_type =  'SELECT * FROM SubstationTypes WHERE substationTypeID = %s'
c_substation_type = 'INSERT INTO SubstationTypes (size, maxLoad) VALUES (%s, %s)'
u_substation_type = 'UPDATE SubstationTypes SET size = %s, maxLoad = %s WHERE substationTypeID = %s'
d_substation_type = 'DELETE FROM SubstationTypes WHERE substationTypeID = %s'

# CRUD queries for Substations ##################################################################
r_substations = 'SELECT * FROM Substations'
r_substation = 'SELECT * FROM Substations WHERE substationID = %s'
c_substation = 'INSERT INTO Substations (name, currentLoad, substationTypeID) VALUES (%s, %s, %s)'
u_substation = 'UPDATE Substations SET name = %s, currentLoad = %s, substationTypeID = %s WHERE substationID = %s'
d_substation = 'DELETE FROM Substations WHERE substationID = %s'

# CRUD queries for Cities #######################################################################
r_cities = 'SELECT * FROM Cities'
r_city = 'SELECT * FROM Cities WHERE cityID = %s'
c_city = 'INSERT INTO Cities (name, population, energyDemand, currentLoad) VALUES (%s, %s, %s, %s)'
u_city = 'UPDATE Cities SET name = %s, population = %s, energyDemand = %s, currentLoad = %s WHERE cityID = %s'
d_city = 'DELETE FROM Cities WHERE cityID = %s'

# CRUD queries for CityHQs ####################################################################
r_city_hqs = 'SELECT * FROM CityHQs'
r_city_hq = 'SELECT * FROM CityHQs WHERE hqID = %s'
c_city_hq = 'INSERT INTO CityHQs (cityID, consumptionPolicy) VALUES (%s, %s)'
u_city_hq = 'UPDATE CityHQs SET cityID = %s, consumptionPolicy = %s WHERE hqID = %s'
d_city_hq = 'DELETE FROM CityHQs WHERE hqID = %s'

# CRUD queries for LocalGeneratorTypes ############################################################
r_local_generator_types = 'SELECT * FROM LocalGeneratorTypes'
r_local_generator_type = 'SELECT * FROM LocalGeneratorTypes WHERE generatorTypeID = %s'
c_local_generator_type = 'INSERT INTO LocalGeneratorTypes (type, outputLoad) VALUES (%s, %s)'
u_local_generator_type = 'UPDATE LocalGeneratorTypes SET type = %s, outputLoad = %s WHERE generatorTypeID = %s'
d_local_generator_type = 'DELETE FROM LocalGeneratorTypes WHERE generatorTypeID = %s'

# CRUD queries for LocalGenerators ############################################################
r_local_generators = 'SELECT * FROM LocalGenerators'
r_local_generator = 'SELECT * FROM LocalGenerators WHERE generatorID = %s'
c_local_generator = 'INSERT INTO LocalGenerators (cityID, generatorTypeID) VALUES (%s, %s)'
u_local_generator = 'UPDATE LocalGenerators SET cityID = %s, generatorTypeID = %s WHERE generatorID = %s'
d_local_generator = 'DELETE FROM LocalGenerators WHERE generatorID = %s'


# CRUD queries for PowerSourceSubstationLinks ####################################################
r_power_source_substation_links = 'SELECT * FROM PowerSourceSubstationLinks'
r_power_source_substation_link = 'SELECT * FROM PowerSourceSubstationLinks WHERE linkID = %s'
c_power_source_substation_link = 'INSERT INTO PowerSourceSubstationLinks (powerSourceID, substationID) VALUES (%s, %s)'
u_power_source_substation_link = 'UPDATE PowerSourceSubstationLinks SET powerSourceID = %s, substationID = %s WHERE linkID = %s'
d_power_source_substation_link = 'DELETE FROM PowerSourceSubstationLinks WHERE linkID = %s'


# CRUD queries for CitySubstationLinks ####################################################
r_city_substation_links = 'SELECT * FROM CitySubstationLinks'
r_city_substation_link = 'SELECT * FROM CitySubstationLinks WHERE linkID = %s'
d_city_substation_link = 'DELETE FROM CitySubstationLinks WHERE linkID = %s'
c_city_substation_link = 'INSERT INTO CitySubstationLinks (cityID, substationID) VALUES (%s, %s)'
u_city_substation_link = 'UPDATE CitySubstationLinks SET substationID = %s, cityID = %s WHERE linkID = %s'
