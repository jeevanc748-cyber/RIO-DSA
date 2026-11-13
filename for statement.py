<<<<<<< HEAD
words = ['cat','mat','bat']
for w in words:
    print(w,len(w))


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


=======
words = ['cat','mat','bat']
for w in words:
    print(w,len(w))


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


>>>>>>> f4eb38985d009c37b7c0da33d1ec68cfec51e7e7
print(users)