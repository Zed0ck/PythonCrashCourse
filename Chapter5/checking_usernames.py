current_users = ['tonttu', 'sanni', 'santtu', 'kalle', 'admin']
new_users = ['SANTTU', 'vili', 'tonttu', 'juho', 'nukki']
current_users_upper = []
if current_users:
    for user in current_users:
        current_users_upper.append(user.upper())
else:
    print("There is no users in db.")

if new_users:
    for user in new_users:
        if user in current_users or user in current_users_upper:
            print(f"{user.title()}, you should choose different username.")
        else:
            print(f"Thank you {user.title()} for registering.")
else:
    print("There is no new users.")