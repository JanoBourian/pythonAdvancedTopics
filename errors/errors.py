class InvalidDocument(Exception):
    def __init__(self, **kwargs):
        self.value = kwargs.get("value", "")
    
    def __str__(self):
        return self.value

error = InvalidDocument(value="Zero")
print(error)
print(error.value)