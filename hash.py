import auth as stauth

users = [
    {
    'user': 'admin',
    'password': '81214524'
    },
    {
    'user': 'dba',
    'password': 'teste123'
    }
]

hashed_passwords = stauth.Hasher(list(map(lambda user: user['password'], users))).generate()

for i in range(len(users)):
    print(f"{users[i]['user']}: {hashed_passwords[i]}")