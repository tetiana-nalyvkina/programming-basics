sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]
for seq in sequences:
    length = len(seq)
    print (seq, length)

lengths = []
for seq in sequences:
    lengths.append (len(seq))
av_len = round (sum (lengths) / len (lengths), 2)
print (f"Average sequence length: {av_len} bp")

orf = 0
for seq in sequences:
    if seq.startswith("ATG"):
        orf = orf + 1
print (f'{orf} sequences start with start-codon')

print ("Sequences longer than 5 bases:")
for seq in sequences:
    if len(seq) > 5:
        print (seq)

print ("GC-count of sequences:")
for seq in sequences:
    n = 0
    for base in seq:
        if base == "G" or base == "C":
            n = n + 1
    gc_count = round(((n / len(seq))*100), 2)    
    print (seq, gc_count)    

print ("Codons of the longest sequence:")
for seq in sequences:
    if len(seq) == max (lengths):
        for i in range (0, max(lengths), 3):
                if len(seq[i:i+3])==3:
                    print (seq[i:i+3])
