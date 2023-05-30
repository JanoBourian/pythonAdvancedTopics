""" 
Liskov Substitution Principle
A derived class can assume the place of its super class, and everything should work
"""


class KitcheAppliance():
    
    def on():
        pass
    
    def off():
        pass
    
    def set_temperature():
        pass
    
class Toaster(KitcheAppliance):
    
    def on():
        # some code 
        pass
    
    def off():
        # some code
        pass
    
    def set_temperature():
        # some code
        pass

class Juicer(KitcheAppliance):
    
    def on():
        # some code
        pass
    
    def off():
        # some code
        pass
    
    def set_temperature():
        # some code
        pass



class KitcheAppliance():
    
    def on():
        pass
    
    def off():
        pass

class KitcheApplianceWithTemperature(KitcheAppliance):
    
    def set_temperature():
        pass
    
class Toaster(KitcheApplianceWithTemperature):
    
    def on():
        # some code 
        pass
    
    def off():
        # some code
        pass
    
    def set_temperature():
        # some code
        pass

class Juicer(KitcheAppliance):
    
    def on():
        # some code
        pass
    
    def off():
        # some code
        pass
    