favorite_languages = {
    'jen': 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    