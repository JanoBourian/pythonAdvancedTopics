class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Hello, I am {self.name}"