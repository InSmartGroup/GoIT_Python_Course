def cost_delivery(*args, discount=0.0):
    """
    :param args: accepts any number of digits
    The first digit is the number of goods, and it breaks down the following way:
    First good costs 5, all the rest cost 2

    :param discount: optional
    If specified, the function returns the total price with a discount

    :return: the total price with or without a discount
    """
    num_goods = args[0]
    total_sum = 0

    for i in range(1, num_goods + 1):
        if i == 1:
            total_sum += 5
        else:
            total_sum += 2

    if discount:
        total_sum *= discount

    return total_sum


print(cost_delivery(3, 1, 3, 5))
print(cost_delivery(3, 1, 3, 5, discount=0.5))
