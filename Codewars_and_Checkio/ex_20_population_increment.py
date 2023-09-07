def calculate_population(starting, percent_increase, number_increase, destination):
    """
    :param starting: Initial (starting) population.
    :type starting: int

    :param percent_increase: A percentage of population increment per year.
    :type percent_increase: int

    :param number_increase: Constant number of population increment.
    :type number_increase: int

    :param destination: The desired level of population.
    :type destination: int

    :return: A number of years to reach from starting to the desired population.
    :rtype: int
    """
    years = 0
    while starting < destination:
        growth_per_year = int(starting + (starting * (percent_increase / 100)) + number_increase)
        starting = growth_per_year
        years += 1
    return f"""It will take {years} years to outreach the {destination} population level.
The population will become {starting} and exceed the destination level by {starting - destination}\n"""


print(calculate_population(1000, 2, 50, 1200))
print(calculate_population(1500, 5, 100, 5000))
print(calculate_population(1500000, 2.5, 10000, 2000000))
