from libs.orm.User import User


class UserCollection:

    _collection = []

    def __init__(self):
        pass

    def append(self, u):
        self._collection.append(u)
