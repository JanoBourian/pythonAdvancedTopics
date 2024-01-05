class Lion:
    
    def __init__(self, name:str) -> None:
        self.name = name
    
    def __repr__(self) -> str:
        return f"<Lion: {self.name}>"
    
    def __add__(self, other) -> int:
        return len(self.name) + len(other.name)

madmax = Lion("Madmax")
simba = Lion("Simba")

print(madmax)
print(madmax.name)
print(simba + madmax)