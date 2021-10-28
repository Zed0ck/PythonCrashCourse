def describe_city(city, country='spain'):
    """Show country where city is"""
    print(f"{city.title()} is in {country.title()}.")

describe_city('tampere', 'finland')
describe_city('madrid')
describe_city('paris', 'france')


# RETURN VALUE
def get_formatted_city(city, country):
    """Return formatted city and country"""
    formatted_city = f"{city.title()}, {country.title()}"
    return formatted_city

city_country = get_formatted_city('tampere', 'finland')
print(city_country)