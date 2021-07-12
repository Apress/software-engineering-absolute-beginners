def details(name, surname, mobile_number):
    print(name + ' ' + surname  + ' mobile :' +  mobile_number)

# Run these two functions and see how the first one basically breaks the output because the order is wrong
details('Johnson', '0123456789', 'Don')
details(surname='Johnson', mobile_number='0123456789', name='Don')
