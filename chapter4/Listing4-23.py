wallet = 100
friends = 0
try:
    per_friend = wallet / friends
except ZeroDivisionError as e:
    # if friends are 0
    per_friend = wallet / 1

print(per_friend)
