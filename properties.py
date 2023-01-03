"""
    property() is an object that sits next to an attribute,
    and is used to set and get value of an attribute
"""
class Product:
    def __init__(self, price) -> None:
        self.__price = price

    # propery decorator is used to create a property object
    @property
    def price(self):
        return self.__price
    
    # <property_name>.setter is used to set the value of an property, basically the attribute
    # Note: if the setter is not specified then the property becomes an read-only property
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Must be greater than 0")
        self.__price = value

jammer = Product(12)

print(jammer.price)

