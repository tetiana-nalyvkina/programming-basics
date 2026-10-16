sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)
print(f"Number of sequences: {len(sequences)}")
print(f"First sequence: {sequences[0]}, last sequence: {sequences [-1]}")
sequences.append ("TATAAT")
print (f"Added sequence {sequences[-1]}")
Lengths = [len(seq) for seq in sequences]
print (f"Lengths of sequences: {Lengths}")
print (f"The longest sequence is {max(Lengths)} nucleotides long, the shortest is {min(Lengths)} nucleotides long. The average length is {sum(Lengths)/len(Lengths)}")
name, chrom, start, stop = gene
print (f"Gene {name} is located on the {chrom} chromosome and is {stop-start} bases long")
print ("if print gene [0] = BRCA0, then the error is TypeError: 'tuple' object does not support item assignment")
genes = [("BRCA1", 81188), ("TP53", 25759)]
print (f"Gene {genes[1][0]} is {genes[1][1]} bases long")


