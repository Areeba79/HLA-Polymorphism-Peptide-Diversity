import random
import matplotlib.pyplot as plt

# Load peptides
with open("data/viral_peptides_unique.csv") as f:
    peptides = [p.strip() for p in f if len(p.strip()) > 0]

# Simulate allele bindings
allele_bindings = []
for _ in range(100):
    allele_bindings.append(set(random.sample(peptides, int(0.05 * len(peptides)))))

# Homozygous coverage
homo = [len(a) for a in allele_bindings]

# Heterozygous coverage
hetero = []
for i in range(0, 98, 2):
    combined = allele_bindings[i].union(allele_bindings[i+1])
    hetero.append(len(combined))

print("Avg Homozygous Coverage:", sum(homo)/len(homo))
print("Avg Heterozygous Coverage:", sum(hetero)/len(hetero))

# Plot
plt.boxplot([homo, hetero], labels=["Homozygous", "Heterozygous"])
plt.ylabel("Number of Peptides Recognized")
plt.title("Heterozygote Advantage in HLA Peptide Recognition (Simulation)")
plt.savefig("figures/plots/heterozygote_advantage.png")
plt.show()
