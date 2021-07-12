price = 30
money_in_wallet = 25
change_left = 0
if money_in_wallet < price:
    print('You do not have enough money')
elif price == money_in_wallet:
    print('You have the exact amount')
elif money_in_wallet > price:
    change_left = money_in_wallet - price
    print('You have ' + str(change_left) + ' left')
