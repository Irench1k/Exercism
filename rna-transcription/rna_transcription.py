def to_rna(dna_strand: str):
    rna_strand = ""
    for k in dna_strand:
        if k == "G":
            rna_strand += "C"
        elif k == "C":
            rna_strand += "G"
        elif k == "T":
            rna_strand += "A"
        elif k == "A":
            rna_strand += "U"
    return rna_strand


print(to_rna("CGAT"))
