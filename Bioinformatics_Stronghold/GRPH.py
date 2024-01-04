def overlap(fasta_file):
    """Given a collection of DNA strings in FASTA format, obtain the
    adjacency list corresponding to O(3).

    Args:
        fasta_file (FASTA): Contains the collection of DNA strings
        having total length at most 10 kbp

    Returns:
        list: List of DNA string pairs in the adjacency list
    """
    f = open(fasta_file, "r").read()
    seq = f.split(">")
    seq = seq[1:]
    ids = [a[:a.index("\n")] for a in seq]
    seq = [a[a.index("\n"):].replace("\n","") for a in seq]
    
    overlaps = []
    
    for i in range(len(seq)):
        for j in range(len(seq)):
            if i == j:
                continue
            if seq[i][-3:] == seq[j][:3]:
                overlaps.append(ids[i]+" "+ids[j])
    
    return overlaps

fasta_file = "C:\\Users\\Dell\\Desktop\\Courses\\Rosalind\\Bioinformatics_Stronghold\\test.txt"
overlap_strings = overlap(fasta_file)
for i in overlap_strings:
    print(i)
    
# Input:
# >Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG
#
# Output:
# Rosalind_0498 Rosalind_2391
# Rosalind_0498 Rosalind_0442
# Rosalind_2391 Rosalind_2323