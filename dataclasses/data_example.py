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

p = Person(name = "john", address = "ravenue")
print(p)

## Error examples
from dataclasses import dataclass, field
from typing import Union

@dataclass
class ErrorResponseBody:
    data: str = field(default = "")
    cerror: str = field(default="Process was not executed correctly")
    ierror: int = field(default=0)

@dataclass
class ResponseBody:
    data: dict
    cerror: str = field(default="Process executed successfully")
    ierror: int = field(default=0)

@dataclass
class ReturnResponse:
    """Class for creating a general return response inside aws lambda
    """
    body: Union[dict[ResponseBody], dict[ErrorResponseBody]] 
    status_code: int = field(default = 200)
    is_base64encode: bool = field(default = False)
    headers: dict = field(default_factory = lambda: {"Content-Type": "application/json"})

error_response_body = ErrorResponseBody()
print(error_response_body)

successfully_response_body = ResponseBody({"idDocument": "id"})
print(successfully_response_body)

successfully_response = ReturnResponse({"response": successfully_response_body})
print(successfully_response)

error_response = ReturnResponse({"response": ErrorResponseBody().__dict__}, 500)
print(error_response.__dict__)
