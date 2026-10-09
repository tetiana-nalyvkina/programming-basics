seq = "AATTCTGTAGCTGGTACCTATATATGCCCGTA"
print ('Sequence length:', len(seq), 'nucleotides')
g = seq.count ('G')
c = seq.count ( 'C')
gc = (g + c)/len(seq)*100
print ('GC count:', round (gc,2), '%')

