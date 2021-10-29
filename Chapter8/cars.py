def make_car(manufacturer, model, **feature):
    """Build a dictionary of a car"""
    feature['manufacturer'] = manufacturer
    feature['model'] = model
    return feature

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)