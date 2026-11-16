import pandas as pd
df = pd.read_csv("data/samples.csv")
print(f"Mean length: {df["length"].mean()}")
print(f'E.coli info: {df[df['organism'] == 'Escherichia coli']}')
print(f" GC larger than 42 and length larger than 1000: {df[(df['gc_content'] > 42) & (df['length'] > 1000)]}")
print(f"TOP3 of GC-content: {df.sort_values("gc_content", ascending=False).head(3)}")
df["length_kb"] = df["length"] / 1000
print(f"with added length in KB: {df}")
