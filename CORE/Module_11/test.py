# magic methods
class Test:
    public_field = 'this is public'
    _private_field = 'this is private'
    __hidden_field = 'this is secret'

s = Test()
print(s.public_field)  # usual manner
print(s._private_field)  # usual manner
print(s._Test__hidden_field)  # use an underscore followed by a class name to get to a hidden method

