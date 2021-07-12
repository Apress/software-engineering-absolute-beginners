class MyError(Exception):
    pass

# Test the exception
name = 'pierre'
try:
    if name != 'john':
       raise MyError('Name is not equal to John')
except MyError as e:
    print(repr(e))
