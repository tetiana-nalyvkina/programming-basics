import my_stats
gc_content = []
with open("data/samples.csv") as f:
    for line in f:
        values = line.split(",")
        gc_content.append(values[1])
gc_content.remove('gc_content')
for n in gc_content:
    if type(n) == str: 
        n_fl = float(n)
        gc_content.insert(1,n_fl)
        gc_content.remove(n)
print(round(my_stats.average(gc_content), 2))
      
