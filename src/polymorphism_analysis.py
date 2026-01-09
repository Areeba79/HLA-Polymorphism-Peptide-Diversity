from Bio import AlignIO

alignment = AlignIO.read("data/hla_A_alignment.fasta", "fasta")

length = alignment.get_alignment_length()
polymorphic = 0

for i in range(length):
    column = alignment[:, i]
    if len(set(column)) > 1:
        polymorphic += 1

print("Alignment length:", length)
print("Polymorphic positions:", polymorphic)
print("Percent polymorphic:",
      round((polymorphic / length) * 100, 2), "%")
