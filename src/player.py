from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name: str, current_room: Room) -> None:
        self.name = name
        self.current_room = current_room
