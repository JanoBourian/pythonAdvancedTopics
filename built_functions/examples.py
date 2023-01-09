## breakpoint() use

from dataclasses import dataclass

@dataclass
class Information:
    mesagge: str
    available_days: int

x = Information("Hello my friend", 15)
# breakpoint()
x.mesagge
# breakpoint()
x.available_days

## callable

array = [1, 2, 3]
function = lambda x: x + 1
print(f"Function {callable(function)}")
print(f"Array: {callable(array)}")

## chr
for _ in range(0, 128):
    print(chr(_))
    
## classmethod / staticmethod / property