def make_car(manufacturer, model, **info):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key, value in info.items():
        car_info[key] = value
    return car_info


car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)

print(car)