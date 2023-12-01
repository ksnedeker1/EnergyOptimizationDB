r_power_source_types = 'SELECT * FROM PowerSourceTypes'


r_power_sources = 'SELECT * FROM PowerSources'
c_power_source = 'INSERT INTO PowerSources (name, powerSourceTypeID) VALUES (%s, %s)'


r_substation_types = 'SELECT * FROM SubstationTypes'
r_substations = 'SELECT * FROM Substations'
r_cities = 'SELECT * FROM Cities'
r_city_hqs = 'SELECT * FROM CityHQs'
r_local_generator_types = 'SELECT * FROM LocalGeneratorTypes'
r_local_generators = 'SELECT * FROM LocalGenerators'





r_power_source_substation_links = 'SELECT * FROM PowerSourceSubstationLinks'
r_power_source_substation_link = 'SELECT * FROM PowerSourceSubstationLinks WHERE linkID = %s'
c_power_source_substation_link = 'INSERT INTO PowerSourceSubstationLinks (powerSourceID, substationID) VALUES (%s, %s)'




r_city_substation_links = 'SELECT * FROM CitySubstationLinks'
r_city_substation_link = 'SELECT * FROM CitySubstationLinks WHERE linkID = %s'
d_city_substation_link = 'DELETE FROM CitySubstationLinks WHERE linkID = %s'
c_city_substation_link = 'INSERT INTO CitySubstationLinks (cityID, substationID) VALUES (%s, %s)'
u_city_substation_link = 'UPDATE CitySubstationLinks SET substationID = %s, cityID = %s WHERE linkID = %s'
