from hotel_rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        
    @property
    def guests(self):
        return sum(room.guests for room in self.rooms)

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        return f"""Hotel {self.name} has {self.guests} total guests
Free rooms: {', '.join(free_rooms)}
Taken rooms: {', '.join(taken_rooms)}
"""
