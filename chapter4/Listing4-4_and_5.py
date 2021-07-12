set_one = [1, 2, 3, 4, 5]
set_two = set_one
if set_one is set_two:
    print('Both variables are pointing to the same list object')

set_one = [1, 2, 3, 4, 5]
set_two = set_one
if set_one is not set_two:
    print('Both variables are pointing to the same list object')
else:
    print('Both variables are not pointing to the same list object')