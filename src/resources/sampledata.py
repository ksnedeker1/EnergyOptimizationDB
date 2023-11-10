sampledata = {
    'cities': [
        {'city_id': '1', 'name': 'Snedekeria', 'population': '3200000', 'energy_demand': '2922.37', 'current_load': '3200'},
        {'city_id': '2', 'name': 'Ngopolis', 'population': '2000000', 'energy_demand': '1826.48', 'current_load': '1900'},
        {'city_id': '3', 'name': 'Databaseburg', 'population': '400000', 'energy_demand': '365.30', 'current_load': '400'},
    ],
    'cityhqs': [
        {'hq_id': '1', 'city_id': '1', 'consumption_policy': '0.50'},
        {'hq_id': '2', 'city_id': '2', 'consumption_policy': '0.50'},
        {'hq_id': '3', 'city_id': '3', 'consumption_policy': '0.50'},
    ],
    'citysubstationlinks': [
        {'link_id': '1', 'substation_id': '1', 'city_id': '1'},
        {'link_id': '2', 'substation_id': '1', 'city_id': '2'},
        {'link_id': '3', 'substation_id': '2', 'city_id': '1'},
        {'link_id': '4', 'substation_id': '3', 'city_id': '2'},
        {'link_id': '5', 'substation_id': '4', 'city_id': '3'},
    ],
    'localgenerators': [
        {'generator_id': '1', 'city_id': '3', 'generator_type_id': '1'},
        {'generator_id': '2', 'city_id': '3', 'generator_type_id': '1'},
        {'generator_id': '3', 'city_id': '3', 'generator_type_id': '1'},
    ],
    'localgeneratortypes': [
        {'generator_type_id': '1', 'type': 'Rooftop Solar', 'output_load': '50.00'},
    ],
    'powersources': [
        {'power_source_id': '1', 'name': 'LargeCoal1', 'power_source_type_id': '1'},
        {'power_source_id': '2', 'name': 'LargeCoal2', 'power_source_type_id': '1'},
        {'power_source_id': '3', 'name': 'LargeNuclear1', 'power_source_type_id': '2'},
        {'power_source_id': '4', 'name': 'MediumHydro1', 'power_source_type_id': '3'},
        {'power_source_id': '5', 'name': 'MediumSolar1', 'power_source_type_id': '4'},
        {'power_source_id': '6', 'name': 'MediumSolar2', 'power_source_type_id': '4'},
    ],
    'powersourcesubstationlinks': [
        {'link_id': '1', 'power_source_id': '1', 'substation_id': '1'},
        {'link_id': '2', 'power_source_id': '2', 'substation_id': '1'},
        {'link_id': '3', 'power_source_id': '3', 'substation_id': '2'},
        {'link_id': '4', 'power_source_id': '4', 'substation_id': '3'},
        {'link_id': '5', 'power_source_id': '5', 'substation_id': '4'},
        {'link_id': '6', 'power_source_id': '6', 'substation_id': '4'},
    ],
    'powersourcetypes': [
        {'power_source_type_id': '1', 'type': 'Large Coal', 'output_load': '1200.00'},
        {'power_source_type_id': '2', 'type': 'Large Nuclear', 'output_load': '2000.00'},
        {'power_source_type_id': '3', 'type': 'Medium Hydro', 'output_load': '700.00'},
        {'power_source_type_id': '4', 'type': 'Medium Solar', 'output_load': '125.00'},
    ],
    'substations': [
        {'substation_id': '1', 'name': 'SnNgSub1', 'current_load': '2400', 'substation_type_id': '1'},
        {'substation_id': '2', 'name': 'SnSub1', 'current_load': '2000', 'substation_type_id': '1'},
        {'substation_id': '3', 'name': 'NgSub1', 'current_load': '700', 'substation_type_id': '2'},
        {'substation_id': '4', 'name': 'DaSub1', 'current_load': '250', 'substation_type_id': '3'},
    ],
    'substationtypes': [
        {'substation_type_id': '1', 'size': 'Mega', 'max_load': '2500.00'},
        {'substation_type_id': '2', 'size': 'Medium', 'max_load': '1000.00'},
        {'substation_type_id': '3', 'size': 'Small', 'max_load': '500.00'},
    ]
}
