from src.index import store
from src.reservation import Reservation
from src.guest import Guest
from src.room import Room

prem_room = Room(401, 'premium')
bob = Guest('bob')


basic_room = Room(402, 'basic')
basic_first_floor = Room(401, 'basic')
sam = Guest('sam')


reservation_one = Reservation(basic_room, sam, 20, 25)


# sam.reservations()
