## breakpoint() use

from dataclasses import dataclass

@dataclass
class Information:
    mesagge: str
    available_days: int

x = Information("Hello my friend", 15)
breakpoint()
x.mesagge
breakpoint()
x.available_days