class MyClass:
    """A simple class that greets the user by name.

    Attributes:
        name (str): The name of the person to greet.
    """

    def __init__(self, name):
        """Initializes a new instance of the MyClass class.

        Args:
            name (str): The name of the person to greet.
        """
        self.name = name

    def greet(self):
        """Prints a greeting message to the console.

        Returns:
            None.
        """
        print(f"Hello, {self.name}!")
