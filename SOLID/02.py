"""
Open Closed Principle
Open for extension, close for modification
"""

# Incorrect
class StorageLocker():
    
    def authenticate(self, client):
        if client == "aws":
            pass
        elif client == "azure":
            pass
        
        return client
        
    def upload(self, client, filename):
        if client == "aws":
            pass
        elif client == "azure":
            pass
        
        return filename

# Correct
from abc import ABC, abstractmethod

class Auth(ABC):
    
    @abstractmethod
    def authenticate(self):
        pass

class Uploader(ABC):
    
    @abstractmethod
    def updload_file(self):
        pass

class Aws(Auth, Uploader):
    
    def authenticate(self):
        pass
    
    def upload(self):
        pass

class Azure(Auth, Uploader):
    
    def authenticate(self):
        pass
    
    def upload(self):
        pass

class Gcp(Auth, Uploader):
    
    def authenticate(self):
        pass
    
    def upload(self):
        pass