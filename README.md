🧬 HLA Polymorphism and Peptide Binding Diversity
A Computational Immunoinformatics Analysis
🔍 Background

The Human Leukocyte Antigen (HLA) system is the most polymorphic gene family in humans.
This extreme genetic diversity enhances immune defense by enabling presentation of a broad spectrum of pathogen-derived peptides to T cells.

Understanding HLA polymorphism is critical for:

🦠 Infectious disease immunity

💉 Vaccine development

🧫 Transplant compatibility

🧬 Evolutionary biology

🎯 Objectives

This project computationally demonstrates that:

The HLA-A locus exhibits extreme sequence polymorphism

A large fraction of amino-acid positions are variable across alleles

Individuals carrying different HLA alleles recognize more pathogen peptides

Heterozygote advantage and balancing selection explain evolutionary maintenance of HLA diversity

📁 Data Sources
🔹 HLA Protein Sequences

Source: IPD-IMGT/HLA Database (official GitHub mirror)

Locus analyzed: HLA-A

Total alleles extracted: ~9,000

🔹 Viral Epitope Peptides

Source: Immune Epitope Database (IEDB) Public API

Data type: Experimentally validated viral peptide epitopes

✅ All datasets are acquired using fully reproducible command-line pipelines.

⚙️ Methods
1. HLA Allele Extraction

Downloaded full HLA protein FASTA database

Filtered sequences belonging to the HLA-A locus

Removed malformed FASTA entries

2. Multiple Sequence Alignment

Randomly subsampled 300 HLA-A alleles

Performed protein sequence alignment using Clustal Omega

Generated aligned FASTA for polymorphism analysis

3. Polymorphism Quantification

Calculated number of polymorphic amino-acid positions

Computed percentage of variable sites across alignment

4. Position-wise Variability Analysis

Counted unique amino acids per alignment column

Visualized residue-level variability across the sequence

5. Peptide Binding Diversity Modeling

Used viral epitope peptides from IEDB

Simulated allele-specific peptide repertoires

Compared peptide coverage between:

Homozygous genotypes (single allele)

Heterozygous genotypes (two distinct alleles)

📊 Key Results

HLA-A shows extreme allelic diversity with thousands of known variants

>60% of aligned amino-acid positions are polymorphic

Polymorphic residues cluster in functional antigen-binding regions

Simulated heterozygous individuals recognize substantially more peptides than homozygotes

These findings provide computational support for:

Balancing selection and heterozygote advantage as key evolutionary mechanisms maintaining HLA polymorphism.

🧠 Biological Interpretation

HLA molecules must balance:

✅ Structural stability of the protein

🔀 Variability in peptide-binding pockets

Conserved residues maintain molecular structure,
while polymorphic residues diversify antigen recognition.

This enables:

Population-level protection against emerging pathogens

Increased survival during epidemic outbreaks

🛠 Tools & Technologies

Python: Biopython, NumPy, Matplotlib

Multiple Sequence Alignment: Clustal Omega

Shell scripting: Bash / Linux command-line tools

Databases:

IPD-IMGT/HLA

Immune Epitope Database (IEDB)
