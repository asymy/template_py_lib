"""Things to consider before writing a module.

- Where does this module fit into the scheme of the project?
- Is there another way of accomplishing this that doesnt require us to maintain code?
- How reusable is this module?
- How shareable is this module?
- Should I write this module?
- Should I share this module?

- What do I want to accomplish with this module?
- When do I need to access this information?
- When functions are necessary?
- What attributes are necessary?
- What is the best way of implimenting that?


"""


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
