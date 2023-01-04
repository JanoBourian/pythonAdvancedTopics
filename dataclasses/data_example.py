from dataclasses import dataclass, field
import random
import string 

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    
    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

item = InventoryItem("name", 5.9, 1)
item_2 = InventoryItem("name", 5.9, 1)

## __eq__()
print(item.__eq__(item_2))
print(item.total_cost())
print(item)

## Example to field
@dataclass
class Example:
    mylist: list[int] = field(default_factory=list)

c = Example()
c.mylist += [1,2,3]
print(c)
print(c.mylist)

## Other example

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))
    
@dataclass(frozen = True, kw_only = True) # for no changes
class Person:
    name: str
    address: str
    id: str = field(init = False, default_factory=generate_id)
    email_addresses: list[str] = field(default_factory = list)
    active: bool = True
    _search_string: str = field(init = False, repr = False)
    
    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"

p = Person(name = "john", address = "ravenue")
print(p)