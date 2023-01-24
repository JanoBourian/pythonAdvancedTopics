from .Device import Device

class Lector(Device):
    """[summary]

    Args:
        Device (name:str, connected_by:str, type:str): 
        About initialization:
            name (str): name to device
            connected_by (str): port of conection
            type (str): CD, DVD, Blu Ray, 
    """
    def __init__(self, name:str, connected_by:str, type:str):
        super().__init__(name, connected_by)
        self.type = type
        self.status = True
    
    def play(self) -> None:
        if self.status: 
            print("Paused...")
        else:
            print("Play...")
        self.status = not self.status

    def __str__(self):
        return f"{super().__str__()} {self.type} is in {'Play' if self.status else 'Paused'} "
        


    