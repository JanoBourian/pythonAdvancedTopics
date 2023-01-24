"""
Inheritance and creation of StatsList
"""


class StatsList(list):
    """
    This class add some statistics methods
    """

    def __init__(self, number_list):
        self.number_list = number_list

    def order_list(self):
        order_list = self.number_list.sort()
        print(self.number_list)
        return order_list

    def dummy_function(self):
        print(len(self.number_list))

    def __str__(self):
        return f"""
        list = {self.number_list}
        order_list = {self.order_list()}
        length = {self.number_list.__len__()}
        min_value = {min(self.number_list)}
        max_value = {max(self.number_list)}
        """


lista = StatsList([1, 2, 3, 4, 5, 6])
print(lista)
lista.dummy_function()
print(lista.order_list())

print(dir([]))
print(min([1, 2, 3, 4, 5, 6]))
print(max([1, 2, 3, 4, 5, 6]))
