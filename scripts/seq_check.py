seq = "ATTCGCTTTCGCGGCTTCAAATCCGCGGTC"
if len(seq)<30:
    print ("too short")
if "N" in seq:
    print ("contains unknown bases")
else:
    print ("no unknown bases")
g = seq.count("G")
c = seq.count("C")
gc = (g +c) / len(seq) * 100
if gc > 60:
    print ("GC reach")
elif gc < 40:
    print ("AT reach")
else:
    print ("Balanced")
if seq.startswith("ATG") and len(seq) % 3 == 0:
    print ("possible ORF")
else: 
    print ("not an ORF")
