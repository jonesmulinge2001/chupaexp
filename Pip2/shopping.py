milk_price = int(input('Enter the price of milk: '))
bread_price = int(input('Enter the price for bread: '))
sugar_price = int(input('Enter the price for sugar: '))
eggs_price = int(input('Enter the price for eggs: '))
bb_price = int(input('Enter the price for bb: '))

# total cost
total_cost = (milk_price + bread_price + sugar_price + bb_price + eggs_price)
if total_cost > 500:
    # discount of 10% is given
    cost_to_pay = (total_cost * 0.9)
    print(f'Your cost has been reduced. Pay {cost_to_pay}')
else:
    print(f'Payable amount is {total_cost}')