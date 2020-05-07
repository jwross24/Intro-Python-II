from item import Item
from textwrap import TextWrapper
from typing import List


# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # Instantiate the {direction}_to attributes with None if they are not
    # specifically passed into the constructor
    def __init__(
            self, name: str, description: str, n_to=None, s_to=None,
            e_to=None, w_to=None, items: List[Item] = []
    ) -> None:
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def take_item(self, item_name: str) -> List[Item]:
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                item.on_take()
                return self.items

        print(f'There is no [{item_name}] here.')
        return self.items

    def print_room_name(self) -> None:
        print(f'\n{self.name}')
        print('='*len(self.name))

    def print_room_description(self) -> None:
        wrapper = TextWrapper()
        desc = wrapper.fill(text=self.description)
        print(desc)

    def print_room_items(self) -> None:
        print('\nItems in this room')
        print('==================')
        result = ' | '.join([item.name for item in self.items])
        print('This room is empty.' if result == '' else result)

    def print_room_info(self) -> None:
        self.print_room_name()
        self.print_room_description()
        self.print_room_items()
