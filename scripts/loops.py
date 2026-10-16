sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]
for seq in sequences:
    print (f"{seq} {len(seq)} bases")
lengths = []
for seq in sequences:
    lengths.append(len(seq))
print (f"Average length: {sum(lengths)/len(lengths)} bases")
n = 0
for seq in sequences:
    if "ATG" in seq:
        n = n+1
print (f"Number of sequences starting with start codone: {n}")
print ("Sequences longer than 5 bases:")
for seq in sequences:
    if len(seq) > 5:
        print (seq)
print ("GC content:")
for seq in sequences:
    n = 0
    for base in seq:
        if base == "G" or base == "C":
            n = n = n+1
            gc =  n/len(seq)*100
    print (seq, round (gc,1))
print ("Longest sequence codons:")
for seq in sequences:
    if len(seq) == max(lengths):
        for i in range(0, len(seq),3):
            print (seq[i:i+3])



