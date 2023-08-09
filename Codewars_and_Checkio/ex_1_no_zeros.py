# Numbers ending with zeros are boring
# They might be fun in your world, but not here
# Get rid of them. Only the ending ones

def no_boring_zeros(n):
    for i in range(len(str(n))):
        if n % 10 == 0:
            n /= 10
    return int(n)


number = int(input("Type: "))
print(no_boring_zeros(number))
