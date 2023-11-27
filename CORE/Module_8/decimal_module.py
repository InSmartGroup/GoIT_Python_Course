from decimal import Decimal, getcontext

# print(0.1 + 0.2)  # the output is 0.30000000000000004
# print(0.1 + 0.2 == 0.3)  # returns False
# print(round(0.1 + 0.2, 2) == 0.3)  # it's possible to round, returns True

# print(Decimal(0.1))
# print(Decimal(0.2))
# print(Decimal(0.1) + Decimal(0.2))  # the output is 0.3000000000000000166533453694

# getcontext().prec = 5  # sets precision with decimal operations
# print(Decimal(0.1) + Decimal(0.2))  # now the output is 0.30000
# getcontext().prec = 1
# print(Decimal(0.1) + Decimal(0.2))  # now the output is 0.3

# print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3))  # retuns False anyway
# so, the decimal module is useless and pointless, fuck it
