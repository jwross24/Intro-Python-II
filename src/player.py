from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name: str, current_room: Room) -> None:
        self.name = name
        self.current_room = current_room

    def move_to(self, direction: str, current_room: Room) -> Room:
        next_room = getattr(current_room, direction + '_to')

        if next_room is not None:
            return next_room

        print("\nYou can't go that way.")
        return current_room
