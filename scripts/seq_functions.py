sequences = ["ATG", "GCGGAT", "ATTATCACATGGATCAGATTTCGCAACGTTGCAA"]

def gc_content(seq):
    g_count = seq.count('G')
    c_count = seq.count('C')
    gc_count = (g_count + c_count)/len(seq) * 100
    gc_count_rounded = round(gc_count, 2)
    return gc_count_rounded

def reverse_complement(seq):
    complement = seq.replace ('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
    upper_complement = complement.upper()
    reverse_complement = upper_complement[::-1]
    return reverse_complement

def base_count(seq):
    a_count = seq.count('A')
    t_count = seq.count('T')
    g_count = seq.count('G')
    c_count = seq.count('C')
    base_counts = {'A': a_count, 'T': t_count, 'G': g_count, 'C': c_count}
    return base_counts

def is_usable(seq,min_length=30):
    length = min_length >= len(seq)
    return length

for seq in sequences:
    gc = gc_content(seq)
    rev_comp = reverse_complement (seq)
    bc = base_count(seq)
    usable = is_usable(seq)
    print(f"For sequence {seq}, the GC content is {gc}%, reverse complement is {rev_comp}, base count {bc} and is usable: {usable}.")