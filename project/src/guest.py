from src.index import store

class Guest:

    def __init__(self, name):
        self._id = len(store['guests']) + 1
        store['guests'][self._id] = self
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def reservations(self):
        # return all the reservations of a guest
        reservations = [reservation for reservation in store['reservations'].values() if reservation.guest.id == self.id]
        return reservations

    def rooms(self):
        #returns all of the rooms a guest has made a reservation for
        rooms =  [reservation.room for reservation in self.reservations()]
        return rooms
