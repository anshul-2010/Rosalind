def gc_content(fasta_file):
    """Given a FASTA file of atmost 10 DNA strings, return the ID of the string with highest GC content
    followed by the GC content of the string

    Args:
        fasta_file (txt file): Contains the ID and strings in the format of FASTA file

    Returns:
        tuple: A tuple of ID and the GC content corresponding to the the DNA string of that ID
    """
    f = open(fasta_file, "r").read()
    seq = f.split(">")
    seq = seq[1:]
    ids = [a[:a.index("\n")] for a in seq]
    seq = [a[a.index("\n"):].replace("\n","") for a in seq]
    
    # Storing the gc content of every DNA sequence in the FASTA file
    gc_content = []
    # Storing the max position along with the max gc content
    max_gc = 0
    max_pos = -1
    for i in range(len(seq)):
        gc_count = 0
        total_count = len(seq[i])
        for j in range(total_count):
            if seq[i][j] == "G" or seq[i][j] == "C":
                gc_count += 1
        gc_percent = gc_count*100/total_count
        if max_gc < gc_percent:
            max_gc = gc_percent
            max_pos = i
        gc_content.append(gc_percent)
    
    return ids[max_pos], max_gc  

fasta_file = "C:\\Users\\Dell\\Downloads\\test.txt"
id_val, gc = gc_content(fasta_file)
print(id_val)
print(gc)

# Rosalind_3333
# 52.159468438538205