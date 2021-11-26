import json

def get_stored_number():
    """Get stored number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_favorite_number():
    """Prompt for a new favorite number."""
    favorite_number = input("Give me your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def print_favorite_number():
    """Print a favorite number."""
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"Your favorite number is {favorite_number}!")
    else:
        favorite_number = get_new_favorite_number()
        print(f"I'll remember your favorite number {favorite_number}!")

print_favorite_number()
