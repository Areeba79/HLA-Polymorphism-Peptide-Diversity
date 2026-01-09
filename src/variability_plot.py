from Bio import AlignIO
import matplotlib.pyplot as plt
from collections import Counter

alignment = AlignIO.read("data/hla_A_alignment.fasta", "fasta")
length = alignment.get_alignment_length()

variability = []

for i in range(length):
    column = alignment[:, i]
    counts = Counter(column)
    if "-" in counts:
        del counts["-"]
    variability.append(len(counts))

plt.figure(figsize=(10,4))
plt.plot(range(1, length+1), variability)
plt.xlabel("Alignment Position")
plt.ylabel("Number of Amino Acids Observed")
plt.title("Position-wise Variability in HLA-A Alignment")
plt.tight_layout()
plt.savefig("figures/plots/hlaA_variability.png")
plt.show()
