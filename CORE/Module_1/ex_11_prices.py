# Given the prices below, separate the amounts in dollars and cents
price_1 = 34.34
price_2 = 12.01
price_3 = 17.42
price_4 = 4.93

sum_prices = sum([price_1, price_2, price_3, price_4])

dollars = int(sum_prices // 1)
cents = int((sum_prices - dollars) * 100)

print(f"The total sum is {dollars} dollars and {cents} cents")
