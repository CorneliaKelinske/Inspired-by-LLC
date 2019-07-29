from csv import DictReader

with open('smaller_data.csv', 'r') as ufo_data_file:
    ufo_data_dictionary_reader = DictReader(ufo_data_file)
    data = list(ufo_data_dictionary_reader)
    sightings_per_city = {}

    for row in data:
        location  = row["Location"]
        if location not in sightings_per_city:
            sightings_per_city[location] = 1
        sightings_per_city[location] += 1
       
       
print(sightings_per_city)