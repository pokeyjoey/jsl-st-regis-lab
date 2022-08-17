from src.index import store

class Room:

    def __init__(self, room_number, rate):
        self._id = len(store['rooms']) + 1
        store['rooms'][self.id] = self
        self._room_number = room_number
        self._rate = rate

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, room_number):
        self._room_number = room_number

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate

    def reservations(self):
        #return all of the reservations for this room
        reservations = [reservation for reservation in store['reservations'].values() if reservation.room.id == self.id]
        return reservations

