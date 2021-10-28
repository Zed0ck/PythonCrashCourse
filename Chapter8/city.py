def describe_city(city, country='spain'):
    """Show country where city is"""
    print(f"{city.title()} is in {country.title()}.")

describe_city('tampere', 'finland')
describe_city('madrid')
describe_city('paris', 'france')