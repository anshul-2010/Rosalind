def preprocess_pattern(pattern):
    """This function is used to preprocess the pattern to prepare it for
    Knuth Morris Prath (KMP) algorithm

    Args:
        pattern (str): The pattern (motif) to be found in DNA

    Returns:
        list: The preprocessing integer list corresponding to pattern
    """
    pat = [0] * len(pattern)
    loc = 0
    val = 0
    
    # Generating the integer list corresponding to pattern
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[loc]:
            loc += 1
            val += 1
        else:
            loc = 0
            val = 0
        pat[i] = val
        
    return pat

def KMP(text, pattern):
    """Finds the indices of appearances of pattern in the text

    Args:
        text (str): The DNA string 
        pattern (str): The pattern (motif) string

    Returns:
        list: list of integer indices denoting the locations of pattern in text
    """
    pat = preprocess_pattern(pattern)
    indices = []
    
    j = 0
    i = 0
    
    # Implementing KMP algorithm to obtain the indices
    while i < len(text):
        if text[i] == pattern[j]:
            j += 1
            i += 1
        else:
            if j != 0:
                j = pat[j-1]
            else:
                i += 1
        
        if j == len(pattern):
            indices.append(i-j+1)
            j = pat[j-1]
    
    return indices

txt = "CAGCGGAAGCAGCGGAACGTCAGCGGAACAGCGGACAGCGGATGCCAGCGGACATTCAGCGGAGCCAACAGCGGACAGCGGATGCAGCGGACCAGCGGATCAGCGGATCACCAGCGGATGCAGCGGACAGCGGACCAGCGGAACAGCGGAGGTTCAGCGGAGGCAGCGGACCAGCGGACTGCAGCGGAGTCAGCGGATTCAGCGGATTCAGCGGACAGCGGACGCCAGGCAGCGGACAGCGGAAGCAGCGGACTCAGCGGACAGCGGATTCAGCGGACCAGCGGACAGCGGAACGCAGCGGACCTACAGCGGAATCAGCGGATCAGCGGAGCACAGCGGATTGAGCTCCAGCGGAAACTTATACGGCAGCGGAAAGAAACTACAGCGGAAGTCAGCGGAACGGCAGCGGATGACTCAGCGGAGCAGCGGACTCAGCGGACTCTCAGCGGATACCAGCGGAGCAGCGGACAGCGGAGCTCAGCGGAAGGCCAGCGGATTCCAGCGGACCAGCGGAACCAGCGGAACAGCGGACAGCGGACAGCGGAAGCCAGCGGAGGTGCAGCGGATTCAGCGGAGGCCTATGATCAGCGGAGGCTCAGCGGACAGCGGAAGCAGCGGATACTCGCAGCGGACCAGCGGAATCCAGCGGAATCAGCGGAACGTGAGTCAGCGGATTAAATTAATTCAGCGGACAGCGGACGGCGCGTCCCAGCGGAGCAGCGGACAGCGGACAGCGGATCAGCGGACTCCAGCGGATCCAGCGGAGACCAGCGGAACAGCGGACAGCGGATCAGCGGAACCAGCGGACAGCGGACAGCGGACATTCACAGATCAGCGGATAGATGCGAACAGCGGACAGCGGATTCAGCGGACCAGCGGACAGCGGACGTGCAGCGGACAGCGGAAATCCAGCGGACAGCGGATCATTTGTCACCAGCGGACAGCGGA"
pat = "CAGCGGACA"
indices = KMP(txt, pat)
indices = [str(a) for a in indices]
index = ' '.join(indices)
print(index)
# 29 46 69 121 209 230 255 279 462 525 532 597 686 718 725 777 801 808 815 850 874 892 910 935 