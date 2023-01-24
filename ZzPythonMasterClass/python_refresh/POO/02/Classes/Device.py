class Device: 
    def __init__(self, name:str, connected_by:str):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"Device: {self.name} ({self.connected_by})"
    
    def disconnect(self) -> None: 
        self.connected = False
        print(f"Disconnected {self.name} ({self.connected_by})")
