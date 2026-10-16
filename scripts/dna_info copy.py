seq = "AATTCTGTAGCTGGTACCTATATATGCCCGTA"
print ('Sequence length:', len(seq), 'nucleotides')
g = seq.count ('G')
c = seq.count ( 'C')
gc = (g + c)/len(seq)*100
print ('GC count:', round (gc,2), '%')
print (f"First codon: {seq[0:3]}")
print (f"Last codon: {seq[-3:]}")
print (f"RNA sequence: {seq.replace("T", "U")}")
complement = seq.replace ("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
rev_comp = complement.upper()[::-1]
print (f"Reverse complement: {rev_comp}")
st_cod = seq.find("ATG")
if st_cod != -1:
    print (f"Start codon at position {st_cod}")
else:
    print ("No start codon in the sequence")


