def get_city_country(city, country, population = ''):

    if population:
        full_name = city + ", " + country + ' - ' + 'population ' + str(population)
    else:
        full_name = city + ", " + country

    return full_name