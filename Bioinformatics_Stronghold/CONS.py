def consensus_profile(fasta_file):
    """Given a collection of atmost 10 DNA strings of equal length in FASTA format,
    calculate the consensus strign and profile matrix for the collection

    Args:
        fasta_file (txt): Contains the collection of DNA strings in FASTA file format

    Returns:
        tuple: Tuple of consensus string and profile matrix
    """
    
    # Read the FASTA file and store the DNA strings in a list
    f = open(fasta_file, "r").read()
    seq = f.split(">")
    seq = seq[1:]
    ids = [a[:a.index("\n")] for a in seq]
    seq = [a[a.index("\n"):].replace("\n","") for a in seq]
    
    length = len(seq[0])
    profile = [[0 for _ in range(length)] for _ in range(4)]

    position = {"A":0, "C":1, "G":2, "T":3}
    consensus = ""

    # Calculate the consensus string and profile matrix
    for i in range(length):
        count_max = 0
        base_max = "A"
        for j in range(len(seq)):
            profile[position[seq[j][i]]][i] += 1
            if profile[position[seq[j][i]]][i] > count_max:
                count_max = profile[position[seq[j][i]]][i]
                base_max = seq[j][i]

        consensus += base_max + ""
    
    for i in range(4):
        for j in range(length):
            profile[i][j] = str(profile[i][j])
    
    return consensus, profile

fasta_file = "C:\\Users\\Dell\\Desktop\\Courses\\Rosalind\\Bioinformatics_Stronghold\\test.txt"
con, pro = consensus_profile(fasta_file)
rev_position = {0:"A", 1:"C", 2:"G", 3:"T"}
L  = []

# Store the output in the desired format
print(con)
for i in range(len(pro)):
    prof_i = ' '.join(pro[i])
    print(rev_position[i], ":", prof_i)
    L.append(rev_position[i] + ": " + prof_i + " \n")
  
# Write the outputs in the correct format into a txt file  
file1 = open("C:\\Users\\Dell\\Downloads\\answer.txt", "w")
file1.write("{} \n".format(con))
file1.writelines(L)
file1.close()
    
# Input: 
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT

# Output:
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6