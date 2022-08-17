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

def test_can_create_guest(self):
    assert type(Guest()) == Guest

#def test_guest_initializes_with_name(self):
#    bob = Guest('bob')
#    assert bob.name == "bob"

#def test_can_create_room(self):
#    assert type(Room()) == Room

#def test_room_initializes_with_number_and_rate(Self):
#    basic_room = Room(402, 'basic')
#    assert basic_room.room_number == 402
#    assert basic_room.rate == 'basic'

#def test_can_create_reservation(self):
#    assert type(Reservation()) == Reservation

#def test_reservation_initialises_with_guest_room_start_day_end_day(self):
#    basic_first_floor = Room(401, 'basic')
#    sam = Guest('sam')
#    reservation_one = Reservation(basic_room, sam, 20, 25)
#    assert reservation_one.guest == sam
#    assert reservation_one.room == basic_first_floor
#    assert reservation_one.start_day == 20
#    assert reservation_one.end_day == 25

# sam.reservations()
