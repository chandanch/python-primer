"""
    Polymorphism is a behaviour in which a method can take multiple forms in different classes
    i.e. a method can be implemented in multiple ways in different classes or in dervied classes
    The method's type is determined at the run time. This is also known as run-time polymorphism
"""

# Duck Typing - Duck Typing is a term commonly related to dynamically typed programming languages
# and polymorphism. The idea behind this principle is that
# the code itself does not care about whether an object is a duck,
# but instead it does only care about whether it quacks.

# Duck Typing refers to the principle of not constraining or binding the code
# to specific data types.



class India():
    """
        Example
    """

    def capital(self):
        """
            Example
        """
        print("New Delhi is the capital of India.")

    def language(self):
        """
            Example
        """
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        """
            Example
        """
        print("India is a developing country.")


class USA():
    def capital(self):
        """
            Example
        """
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        """
            Example
        """
        print("English is the primary language of USA.")

    def type(self):
        """
            Example
        """
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    # methods capital(), language() and type() follow duck typing
    # since we are determining the type at the run time and python just cares if
    # the object these below methods
    country.capital()
    country.language()
    country.type()
