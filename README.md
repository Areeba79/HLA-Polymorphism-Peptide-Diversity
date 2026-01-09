🧬 HLA Polymorphism and Peptide Binding Diversity

A Computational Immunoinformatics Analysis

🔍 Background

The Human Leukocyte Antigen (HLA) system is the most polymorphic gene family in humans.
This extreme genetic diversity is believed to improve immune defense by enabling the presentation of a broad range of pathogen-derived peptides to T cells.

Understanding how HLA polymorphism enhances antigen presentation is critical for:

infectious disease immunity

vaccine development

transplant compatibility

evolutionary biology

🎯 Objectives

This project aims to computationally demonstrate that:

The HLA-A locus exhibits extreme sequence polymorphism

A large fraction of amino acid positions are variable across alleles

Individuals carrying different HLA alleles recognize a broader set of pathogen peptides

Heterozygote advantage explains evolutionary maintenance of HLA diversity

📁 Data Sources
🔹 HLA Protein Sequences

Source: IPD-IMGT/HLA database (official GitHub mirror)

Locus analyzed: HLA-A

Total alleles extracted: ~9000

🔹 Viral Epitope Peptides

Source: Immune Epitope Database (IEDB) public API

Data type: experimentally validated viral peptide epitopes

All data acquisition is fully reproducible using command-line tools.

⚙️ Methods
1. HLA Allele Extraction

Downloaded full HLA protein FASTA database

Filtered sequences belonging to the HLA-A locus

Removed malformed FASTA lines

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

60% of aligned amino-acid positions are polymorphic

Polymorphic sites cluster in functional antigen-binding regions

Simulated heterozygous individuals recognize substantially more peptides than homozygotes

These results provide computational support for:

Balancing selection and heterozygote advantage as evolutionary mechanisms maintaining HLA polymorphism.

🧠 Biological Interpretation

HLA molecules must balance:

structural stability of the protein

variability in peptide-binding pockets

Conserved residues maintain molecular structure,
while polymorphic residues diversify antigen recognition.

This enables:

population-level protection against emerging pathogens

survival advantage during epidemics

🛠 Tools & Technologies

Python (Biopython, NumPy, Matplotlib)

Clustal Omega (MSA)

Bash / Linux command-line tools

IEDB public epitope API

IPD-IMGT/HLA database



