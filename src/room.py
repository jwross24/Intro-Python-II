from item import Item
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
