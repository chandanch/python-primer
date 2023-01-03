"""
    Inheritance allows us to define common behaviour and functions in a common class,
    and inherit them in another class

    object - This is the base class for all the classes in python
"""


class SoftwareApplication:
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


class DocumentApplication(SoftwareApplication):
    """
        Document Application - Child Class or Sub Class
    """

    def write_document(self, content):
        """
            Write Document
        """
        print(f"Writing document: {content}")


document = DocumentApplication()

document.render_ui()
print(document.version)
print(document.write_document("hello there"))
document.close_application()

# check if an object is an instance of a class
print(isinstance(document, object))
# check if the class is inherited from another class
print(issubclass(DocumentApplication, object))