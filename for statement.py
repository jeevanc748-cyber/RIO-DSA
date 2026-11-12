words = ['cat','mat','bat']
for w in words:
    print(w,len(w))


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


print(users)