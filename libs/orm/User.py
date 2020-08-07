"""
User class
"""


class User:
    first_name = ""
    last_name = ""
    date_of_birth = ""
    email = ""
    phone_number = ""
    account_sum = 0

    def __init__(self, row=[]):
        self.first_name = row[0]
        self.last_name = row[1]
        self.date_of_birth = row[2]
        self.email = row[3]
        self.phone_number = row[4]
        self.account_sum = row[5]
        print("User instanciated")

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    
