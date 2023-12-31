def complementary(seq):
    """Given a DNA string, find the reverse complement of the DNA string

    Args:
        seq (str): Takes the given DNA string as input

    Returns:
        str: Returns the reverse complement of the DNA strand
    """
    seq = seq[::-1] #Best way to take the reverse of a string
    ans = ""
    complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
    for i in seq:
        ans = ans + complement[i]
    
    return ans

s = "ATCATTCAGTACGTAGCTACGGCCGCAGCT"
print(complementary(s))
# AGCTGCGGCCGTAGCTACGTACTGAATGAT