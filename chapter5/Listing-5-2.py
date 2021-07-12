number = 10
if number == 10:
    print(10)
else:
    print('not 10')

'''
First refactoring initialises a default value before we check for 10
'''
message = 'not 10'
if number == 10:
        message = '10'
print(message)

'''
Second refactoring returns early when 10 is found. This works great in a function.
'''
def check_ten():
    if number == 10:
        return '10'
    return 'not 10'

print(check_ten())
