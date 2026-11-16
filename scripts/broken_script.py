# broken_report.py
# GC content report for sequences in a FASTA file.
# This script has 5 bugs. Run it, read the FIRST error, fix it, run again.


def read_fasta ():
    sequences = {}
    name = None
    with open ("sequences.fasta") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line
    return sequences

def empty_file():
    if len(sequences) == 0 :
        print ("No sequences in the file")
    continue

def gc_content(seq):
    gc = ((seq.count("G") + seq.count("C")) / len(seq)) * 100
    return gc


def report(name, seq):
    gc = gc_content(seq)
    print(f"Sequence {name}: length {len(seq)}")
    print(f"  GC content: {gc:.1f}%")
    return gc


sequences = read_fasta()
empty_file
results = {}
for name, seq in sequences.items():
    results[name] = report(name, seq)

average = sum(results.values()) / len(results)
print(f"Average GC: {average:.1f}%")
