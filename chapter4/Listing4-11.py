people = [ {'name': 'ron', 'position':'middle'}, {'name':'nico', 'position':'bottom'}, {'name':'andy', 'position':'top'} ]

# One example using continue.
for person in people:
    for details_key, details_value in person.items():
        if person['position'] == 'bottom':
            continue
        print(details_value)

# One example using break.
for person in people:
    for details_key, details_value in person.items():
        if person['position'] == 'bottom':
           break
        print(details_value)

