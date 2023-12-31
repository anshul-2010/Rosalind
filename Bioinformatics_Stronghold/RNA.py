def transcription_1(seq):
    # Method 1
    """Given a DNA string, give its transcibed RNA string

    Args:
        seq (str): Takes the DNA sequence as the input

    Returns:
        str: Returns the transcribed RNA sequence
    """
    ans = ""
    for i in range(len(seq)):
        if(seq[i]=="T"):
            ans = ans + "U"
        else:
            ans = ans + seq[i]
    
    return ans

def transcription_2(seq):
    # Method 
    """Given a DNA string, give its transcibed RNA string

    Args:
        seq (str): Takes the DNA sequence as the input

    Returns:
        str: Returns the transcribed RNA sequence
    """
    seq = seq.replace("T","U")
    return seq

s = "ACTGCTAGCTAGCTAGCTAGCCTAGCGATCGTACGTAGCTG"
print(transcription_1(s))
# ACUGCUAGCUAGCUAGCUAGCCUAGCGAUCGUACGUAGCUG
print(transcription_2(s))
# ACUGCUAGCUAGCUAGCUAGCCUAGCGAUCGUACGUAGCUG
    
    