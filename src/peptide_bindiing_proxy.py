import random

# Load HLA sequences
hla_seqs = []
with open("data/hla_A_subset.fasta") as f:
    for line in f:
        if not line.startswith(">"):
            hla_seqs.append(line.strip())

# Load viral peptides
with open("data/viral_peptides_unique.csv") as f:
    peptides = [p.strip() for p in f if len(p.strip()) > 0]

print("HLA alleles:", len(hla_seqs))
print("Peptides:", len(peptides))

# Simulate binding: each allele binds random subset
binding = {}
for i, hla in enumerate(hla_seqs):
    bound = set(random.sample(peptides, k=int(0.05 * len(peptides))))
    binding[f"HLA_{i}"] = bound

# Save binding counts
with open("results/binding_counts.txt", "w") as f:
    for k, v in binding.items():
        f.write(f"{k}\t{len(v)}\n")

print("Binding simulation complete.")
