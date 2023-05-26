# from __future__ import print_function
from pydantic import BaseModel

from typing import List


class Template(BaseModel):
    description: str
    item: List[int]


class Venue(Template):
    address: str
    name: str


# a = Child(name="a", surname="b")  # type: ignore

# child_fields = Child.__fields__
# parent_fields = Parent.__fields__

# unique_child_fields = [
#     key for key in Child.__fields__.keys() if key not in Parent.__fields__
# ]


# print(unique_child_fields)


venue = {"address": "Vokieciu g", "name": "Town Hall"}

template = {"description": "very nice", "items": [1, 2, 3]}


together = {
    "address": "Vokieciu g",
    "name": "Town Hall",
    "description": "very nice",
    "item": [1, 2, 3],
}

unique_venue_fields = [
    key for key in Venue.__fields__.keys() if key not in Template.__fields__
]

print(unique_venue_fields)
# for item in

# template_specific =
