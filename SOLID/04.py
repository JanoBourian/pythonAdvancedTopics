"""
Interface Segregation Principle
Interfaces should be granularly split and be as small as possible
"""

class MobileDevice():
    
    def voice(self):
        raise NotImplementedError
    
    def text(self):
        raise NotImplementedError
    
    def camera(self):
        raise NotImplementedError

class BestMobileDeviceEver(MobileDevice):
    
    def voice(self):
        # implementation for this method
        pass
    
    def text(self):
        # implementation for this method
        pass
    
    def camera(self):
        # implementation for this method
        pass

class OldSchoolMobileDevice(MobileDevice):
    
    def voice(self):
        # implementation for this method
        pass
    
    def text(self):
        # implementation for this method
        pass
    
    def camera(self):
        raise NotImplementedError
    
# Correct
from abc import ABC, abstractmethod

class Phone(ABC):
    
    @abstractmethod
    def voice(self):
        pass 

class Text(ABC):
    
    @abstractmethod
    def text_method(self):
        pass 
    
class Camera(ABC):
    
    @abstractmethod
    def photo(self):
        pass 

class BestMobilePhoneEver(Phone, Text, Camera):
    
    def voice(self):
        # Implementation for this method
        pass
    
    def text_method(self):
        # Implementation for this method
        pass
    
    def photo(self):
        # Implementation for this method
        pass 
    

class OldSchoolMobilePhone(Phone, Text):
    
    def voice(self):
        # Implementation for this method
        pass
    
    def text_method(self):
        # Implementation for this method
        pass