def hamming_distance(seq1, seq2):
    """Given two DNA strings of equal length, not exceeding 1kbp,
    return the Hamming distance between the two strings

    Args:
        seq1 (str): Takes one DNA sequence
        seq2 (str): Takes the other DNA sequence of same length

    Returns:
        int: Returns the Hamming distance between the sequences
    """
    # Given the length of both the strings is same
    hamm = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hamm += 1
    
    return hamm

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
print(hamming_distance(s,t))
# 7