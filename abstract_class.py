"""
    An abstract class can be considered as a blueprint for other classes.
    It allows you to create a set of methods that must be created
    within any child classes built from the abstract class.
    A class which contains one or more abstract methods is called an abstract class.
    An abstract method is a method that has a declaration but does not have an implementation.
    While we are designing large functional units we use an abstract class.
    When we want to provide a common interface for different implementations of a component,
    we use an abstract class

    Python comes with a module that provides the base for defining Abstract Base classes(ABC)
    and that module name is ABC.
    ABC works by decorating methods of the base class as abstract and then registering
    concrete classes as implementations of the abstract base. 
    A method becomes abstract when decorated with the keyword @abstractmethod
"""
from abc import ABC, abstractmethod, abstractproperty


class SoftwareApplication(ABC):
    """
        SoftwareApplication - Base Class or Parent class
    """

    def __init__(self):
        self.version = '1.2.2'

    def render_ui(self):
        """
            Base class member
        """
        print("Rendering UI")

    def close_application(self):
        """
            Base class member
        """
        print("Closing Application")

    @abstractmethod
    def process_data(self):
        """
            Process Data
        """


class DocumentManagerApplication(SoftwareApplication):
    """
        Document Manager
    """

    def process_data(self):
        print("Proccessing Documents and data")


document = DocumentManagerApplication()
document.process_data()
