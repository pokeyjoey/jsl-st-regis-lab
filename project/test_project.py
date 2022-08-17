from src.index import store
from src.reservation import Reservation
from src.guest import Guest
from src.room import Room

#prem_room = Room(401, 'premium')
#bob = Guest('bob')


#basic_room = Room(402, 'basic')
#basic_first_floor = Room(401, 'basic')
#sam = Guest('sam')


#reservation_one = Reservation(basic_room, sam, 20, 25)

def test_can_create_guest():
    assert type(Guest('bob')) == Guest

def test_guest_initializes_with_name():
    bob = Guest('bob')
    assert bob.name == "bob"

def test_can_create_room():
    assert type(Room('402', 'basic')) == Room

def test_room_initializes_with_number_and_rate():
    basic_room = Room(402, 'basic')
    assert basic_room.room_number == 402
    assert basic_room.rate == 'basic'

def test_can_create_reservation():
    basic_first_floor = Room(401, 'basic')
    sam = Guest('sam')
    assert type(Reservation(basic_first_floor, sam, 20, 25)) == Reservation

def test_reservation_initialises_with_guest_room_start_day_end_day():
    basic_first_floor = Room(401, 'basic')
    sam = Guest('sam')
    reservation_one = Reservation(basic_first_floor, sam, 20, 25)
    assert reservation_one.guest == sam
    assert reservation_one.room == basic_first_floor
    assert reservation_one.start_day == 20
    assert reservation_one.end_day == 25

def test_room_reservations():
    basic_room = Room(402, 'basic')
    sam = Guest('sam')
    reservation_one = Reservation(basic_room, sam, 20, 25)
    assert  basic_room.reservations() == [reservation_one]

def test_guest_reservations():
    basic_room = Room(402, 'basic')
    sam = Guest('sam')
    reservation_one = Reservation(basic_room, sam, 20, 25)
    assert  sam.reservations() == [reservation_one]

def test_guest_rooms():
    basic_room = Room(402, 'basic')
    sam = Guest('sam')
    reservation_one = Reservation(basic_room, sam, 20, 25)
    assert  sam.rooms() == [basic_room]


