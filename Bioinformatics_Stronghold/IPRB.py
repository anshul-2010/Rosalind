def probability(k, m, n):
    """Given three positive integers k,m,n representing a population of k+m+n organisms,
    calculate the probability of producing an individual with the dominant phenotype

    Args:
        k (int): Number of Homozygous Dominant individuals
        m (int): Number of Heterozygous individuals
        n (int): Number of Homozygous Recessive individuals

    Returns:
        float: The probability of producing an individual with dominant phenotype
    """
    total_pop = k + m + n
    
    # Both mating organisms from same bucket
    both_dom = k * (k - 1) / 2 * 1
    both_het = m * (m - 1) / 2 * 0.75
    both_rec = n * (n - 1) / 2 * 0
    
    # Both mating organisms from different buckets
    dom_het = k * m * 1
    dom_rec = k * n * 1
    het_rec = m * n * 0.5
    
    # Calculating the total possibilities
    obey_pos = both_dom + both_het + both_rec + dom_het + dom_rec + het_rec
    total_pos = total_pop * (total_pop - 1) / 2
    # Probability
    total_prob = obey_pos / total_pos
    
    return total_prob