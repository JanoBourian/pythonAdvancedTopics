class NameOfClass():
    class_attribute = True

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __str__(self):
        return f"{self.param1} - {self.param2}"

    def method(self):
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        pass

    @staticmethod
    def stc_method(param1, param2):
        pass
