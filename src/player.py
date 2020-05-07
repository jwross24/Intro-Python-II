from item import Item
from room import Room
from typing import List

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(
            self, name: str, current_room: Room, inventory: List[Item] = []
    ) -> None:
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def move_to(self, direction: str) -> Room:
        next_room = getattr(self.current_room, direction + '_to')

        if next_room is not None:
            return next_room

        print("\nYou can't go that way.")
        return self.current_room

    def take_item(self, item_name: str) -> List[Item]:
        room_items = getattr(self.current_room, 'items')
        for item in room_items:
            if item.name == item_name:
                self.inventory.append(item)

        return self.inventory

    def drop_item(self, item_name: str) -> List[Item]:
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                self.current_room.items.append(item)
                item.on_drop()
                return self.inventory

        print("You don't have this item.")
        return self.inventory

    def print_inventory(self) -> None:
        print('\nInventory')
        print('=========')
        result = ' | '.join([item.name for item in self.inventory])
        print("You don't have any items yet." if result == '' else result)
