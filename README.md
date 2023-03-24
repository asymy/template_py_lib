# README

< A little about your library. >

# Install

- versioning

```bash
python setup.py sdist bdist_wheel
pip install dist/your_library_name-<version>.tar.gz
```

- uninstall

```bash
pip uninstall your_library_name
```

# Using the library

```python
from template_py_lib.your_module1 import MyClass
m = MyClass('Alison')
m.greet()
```

# Requesting changes

- create issue
- create pull request

# Making changes

## Install development environment

```bash
python -m venv venv
# Linux
source venv/bin/activate
# Windows
. venv/Scripts/activate
# update pip
python -m pip install --upgrade pip
# install dev requirements
pip install -r requirements-dev.txt
# install requirements
pip install -r requirements.txt
```
- install package in editable mode

```bash
pip install -e .
```

## Style Guide

- Use [pep8](https://www.python.org/dev/peps/pep-0008/) style guide
    - Use four spaces for indentation. Don't use tabs.
    - Use lowercase letters and underscores for variable and function names.
    - Use CamelCase for class names.
    - Use uppercase letters for constants.
    - Use spaces around operators and after commas.
    - Put a space before and after comparison operators (==, !=, <, >, etc.).
    - Use single quotes for string literals unless the string contains a single quote.
    - Use double quotes for docstrings and triple quotes for multi-line strings.
    - Try to limit line length to 79 characters (Maximum 100 characters).
    - Put two blank lines between top-level definitions and one blank line between method definitions.
- Use docstrings:
A docstring is a string literal that appears as the first statement in a function definition, and it describes what the function does.
Use docstrings to explain the purpose of the function, any arguments it takes, and what it returns.
- Use google doc string format.
This format uses triple quotes to enclose the docstring, and includes sections for a brief summary, arguments, returns, and examples.
Here's an example:

```python
def my_function(arg1, arg2):
    """This is a brief summary of my_function.

    Args:
        arg1: Description of arg1.
        arg2: Description of arg2.

    Returns:
        Description of the return value.

    Examples:
        >>> my_function(1, 2)
        3
    """
    # Function code goes here
```
- Be concise and clear:
Use clear and concise language when documenting functions.
Avoid jargon and use plain language that's easy to understand.
- Include examples:
Including examples in your docstrings can help users understand how to use your function.
Use the >>> syntax to indicate a Python interactive session.

# TODO

- Choose a license, a few common ones are provided
    - MIT: The MIT License is the most permissive of the licenses you provided, as it allows for the greatest freedom to use, modify, distribute, and even commercialize the software, with very few restrictions.
    - BSD3: The BSD 3-Clause License is also a very permissive license, as it allows for modification, distribution, and commercial use of the software, with few restrictions. The main differences between the MIT and BSD 3-Clause licenses are the attribution requirement and the use of names and trademarks.
    - LGPL: The GNU Lesser General Public License is a weaker copyleft license than the GPL, as it allows for the use of the licensed library in proprietary programs without releasing the entire program under the LGPL. This makes it more permissive than the GPL, but less permissive than the MIT and BSD 3-Clause licenses.
    - GPL: The GNU General Public License is a strong copyleft license that requires any derivative works to be released under the same license terms, making it less permissive than the MIT, BSD 3-Clause, and LGPL licenses. While the GPL allows for modification and distribution of the software, it places more restrictions on the use and distribution of the software than the other licenses.

