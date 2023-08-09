"""
Find the sum of all multiples of n below m
Keep in Mind:
1) n and m are natural numbers (positive integers)
2) m is excluded from the multiples

Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"
"""


def sum_mul(n, m):
    result = 0
    if n > 0 and m > 0:
        for i in range(n, m, n):
            result += i
            i += i
    else:
        return 'INVALID'

    return result


print(sum_mul(2, 9))
print(sum_mul(4, -7))
print(sum_mul(0, 0))
