def offspring(genotype):
    """Given the number of species pairs' in a population exhibiting each of the
    genotypes: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa

    Args:
        genotype (list): List of integers corresponding to number of couples in the
        population possessing each genotype for a specific factor in consideration

    Returns:
        int: Returns the expected number of offsprings displaying the dominant
        phenotype in the next generation, considering every couple has 2 offsprings
    """
    # Probability of each genotype to probability of giving dominant offspring
    dominant = {0:1, 1:1, 2:1, 3:0.75, 4:0.5, 5:0}
    count = 0
    for i in range(len(genotype)):
        count += dominant[i] * genotype[i] * 2
    
    return count

# Get user input list of 6 integers
geno_input = [int(x) for x in input().split()]
# 17593 18758 16590 17389 18934 17946
print(offspring(geno_input))
# 150899.5