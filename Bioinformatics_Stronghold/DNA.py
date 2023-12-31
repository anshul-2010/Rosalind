
def count_dna_nucleotides(seq):
    """Count the number of each nucleotide base pair present in a DNA sequence

    Args:
        seq (str): Contains the DNA sequence to find the count for

    Returns:
        tuple: count of each nitrogenous base pair
    """
    adenine = 0 # Count the number of adenine base pairs
    thymine = 0 # Count the number of thymine base pairs
    guanine = 0 # Count the number of guanine base pairs
    cytosine = 0 # Count the number of cytosine base pairs
    for i in range(len(seq)):
        if(seq[i]=="A"):
            adenine += 1 
        elif(seq[i]=="T"):
            thymine += 1 
        elif(seq[i]=="G"):
            guanine += 1 
        else:
            cytosine += 1
            
    return adenine, thymine, guanine, cytosine

sequence = "ATGCCGATAGCATCGAAAGTCGCGATCGACGCGTACGCGCATACG"
print(count_dna_nucleotides(sequence))
# (12 7 13 13)