from src.index import store

class Reservation:

    def __init__(self, room, guest, start_day, end_day):
        self._id = len(store['reservations']) + 1
        store['reservations'][self._id] = self
        self._guest = guest
        self._room = room
        self._start_day = start_day
        self._end_day = end_day

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self, guest):
        self._guest = guest

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self.room = room

    @property
    def start_day(self):
        return self._start_day

    @start_day.setter
    def start_day(self, start_day):
        self._start_day = start_day

    @property
    def end_day(self):
        return self._end_day

    @end_day.setter
    def end_day(self, end_day):
        self._end_day = end_day


