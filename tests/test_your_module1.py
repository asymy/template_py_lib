from template_py_lib.your_module1 import MyClass


def test_myclass():
    m = MyClass('name')
    assert m.name == 'name'


def test_myclass_print(capfd):
    m = MyClass('name')
    m.greet()
    out, err = capfd.readouterr()
    assert out == 'Hello, name!\n'
