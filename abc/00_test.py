from typing import Any
from abc import ABC

class Test:
    
    def __init__(self, name:str):
        self.name = name
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[__name] = __value

testing = Test("This in the name")
print(testing.__dict__)
testing.last_name = "other name"
print(testing.__dict__)