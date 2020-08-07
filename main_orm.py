import csv
from libs.orm.UserCollection import UserCollection
from libs.orm.User import User

users = UserCollection()

with open('users.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        user = User(row)
        users.append(user)



print('--- end ---')
