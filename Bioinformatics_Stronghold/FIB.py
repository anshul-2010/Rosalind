def fibonacci(n, k):
    """Given positive integers n<=40 and k<=5, calculate the 
    number of rabit pairs present after n months

    Args:
        n (int): Number of months after which to calculate for
        k (int): Number of rabbit pairs produced in one reproduction

    Returns:
        int: Total number of rabbit pairs present after n months
    """
    a = 1 # a refers to the month two months prior to current
    b = 1 # b refers to the month one month prior to the current
    while(n-2 > 0):
        c = a*k + b
        a = b
        b = c
        n -= 1
    return b

print(fibonacci(34, 2))
# 5726623061