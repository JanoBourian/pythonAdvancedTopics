class ShowDecorators:
    
    def __init__(self, name = "", number = ""):
        self.name = name
        self.number = number
    
    @property
    def number(self):
        _number = "-".join([self._number[:3], self._number[3:6],self._number[6:]])
        return _number
    
    @number.setter
    def number(self, number):
        if len(number) >= 100:
            raise ValueError("Invalid phone number.")
        self._number = number
    
    @classmethod
    def create_basic_phone(cls, number):
        _cellphone = cls("Basic Phone", number)
        print(f"A basic phone was created {_cellphone}")
        return _cellphone
    
    @staticmethod
    def get_emergency_number() -> str:
        return "911"
    
    def __repr__(self):
        return "<ShowDecorators> name: {}, number: {}".format(self.name, self.number)

instance_1 = ShowDecorators("Aiton Taurus")
print(instance_1.name)

## Static method
instance_2 = ShowDecorators()
print(instance_2.get_emergency_number())
print(ShowDecorators.get_emergency_number())

## Class method
instance_3 = ShowDecorators.create_basic_phone("5599668899")
print(instance_3)
print(instance_3.number)

## Property
instance_4 = ShowDecorators("Aiton Taurus", "5599887720")
print(instance_4.number)