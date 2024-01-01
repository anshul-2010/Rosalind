sequence = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V", 
            "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
            "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
            "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
            "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
            "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
            "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
            "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
            "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
            "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D", 
            "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
            "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
            "UGU":"C","CGU":"R", "AGU":"S", "GGU":"G",
            "UGC":"C","CGC":"R", "AGC":"S", "GGC":"G",
            "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
            "UGG":"W","CGG":"R", "AGG":"R", "GGG":"G"}

def protein(rna_seq):
    """Given an RNA string corresponding to a strand of mRNA,
    calculate the protein string encoded by it

    Args:
        rna_seq (str): RNA string corresponding to a strand of mRNA

    Returns:
        str: Returns the protein string encoded by the RNA string
    """
    protein_string = ""
    for i in range(0, len(rna_seq), 3):
        trimer = rna_seq[i:i+3]
        if sequence[trimer] == "Stop":
            break
        protein_string += sequence[trimer] + ""
    
    return protein_string

print(protein("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))
# MAMAPRTEINSTRING