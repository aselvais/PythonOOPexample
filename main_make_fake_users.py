from faker import Faker
from random import uniform
import csv

fake = Faker()

with open('users.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    # spamwriter.writerow(['first_name','last_name','date_of_birth','email','phone_number','account_sum'])
    for i in range(100):
        spamwriter.writerow([fake.first_name(), fake.last_name(), fake.date_of_birth(), fake.email(), fake.phone_number(), uniform(10000, .2)])
