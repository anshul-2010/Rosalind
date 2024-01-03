def modified_fib(n,m):
    """Given two positive integers n and m, calculate the total number
    of rabbits that will be alive after the nth month, if all rabbits 
    die after m months

    Args:
        n (int): The number of months after which total rabbits alive is needed
        m (int): The number of months all rabbits can survive

    Returns:
        int: The total number of rabbits alive after nth month
    """
    population = [[0 for _ in range(m)] for i in range(n)]
    population[0][0] = 1
    
    # Using Dynamic Programming and Memoization
    for i in range(1, n):
        num_offsprings = 0
        for j in range(1, m):
            population[i][j] = population[i-1][j-1]
            num_offsprings += population[i-1][j]
        population[i][0] = num_offsprings
     
    # Calculating the total number of rabbits after nth month   
    total_rabbits = 0
    for i in range(m):
        total_rabbits += population[n-1][i]
    
    return total_rabbits
    
print(modified_fib(6,3))
# 4