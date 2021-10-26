favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskel'],
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#if 'erin' not in favorite_languages.keys():
#    print("Erin, please take our poll!")
    