class Widget:
    
    def __init__(self,name:str =""):
        self.name = name
        self.x = 50
        self.y = 50
    
    def size(self) -> tuple:
        return (self.x, self.y)
    
    def resize(self, x_value, y_value) -> tuple:
        self.x, self.y = x_value, y_value
        return self.size()
    
    def dispose(self):
        self.x, self.y = 0, 0