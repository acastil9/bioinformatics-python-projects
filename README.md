# Bioinformatics Python Projects

A collection of Python projects developed during my graduate training in bioinformatics and computational biology. These projects demonstrate foundational sequence analysis, algorithm implementation, and next-generation sequencing workflow development.

## Projects

### 🧬 DNA Sequence Translation and ORF Analysis

Python implementation of fundamental DNA sequence-processing operations, including reverse-complement generation, codon translation, and open reading frame analysis.

**Key concepts:** DNA sequence manipulation, genetic code, translation, ORFs, biological sequence analysis

**Technologies:** Python

➡️ [View project](./sequence-translation/)

---

### 🧬 DNA Sequence Comparison Using Dynamic Programming

Implementation of the longest common subsequence (LCS) algorithm for comparing DNA sequences. The project uses dynamic programming to construct a scoring matrix and reconstruct a shared subsequence between two nucleotide sequences.

**Key concepts:** Dynamic programming, sequence comparison, algorithm design, matrix-based computation

**Technologies:** Python, NumPy

➡️ [View project](./sequence-comparison/)

---

### 🧪 NGS RNA-Seq Expression Analysis Pipeline

Python-based workflow integrating commonly used command-line bioinformatics tools for processing next-generation sequencing data from raw reads through gene-level quantification.

**Workflow:**

`FASTQ → FastQC → Trimmomatic → HISAT2 → SAMtools → featureCounts`

**Key concepts:** RNA-seq, quality control, read trimming, sequence alignment, alignment processing, gene-level quantification, workflow automation

**Technologies:** Python, FastQC, Trimmomatic, HISAT2, SAMtools, featureCounts

➡️ [View project](./ngs-pipeline/)

---

## Technical Skills Demonstrated

- Python programming
- Bioinformatics algorithm implementation
- DNA sequence analysis
- Dynamic programming
- Next-generation sequencing workflows
- RNA-seq data processing
- Command-line bioinformatics tools
- Workflow development and automation
- Biological data interpretation

## Repository Structure

```text
bioinformatics-python-projects/
├── sequence-translation/
│   ├── README.md
│   ├── dna_translation_orf_analysis.py
│   └── annotated_gene_results.docx
│
├── sequence-comparison/
│   ├── README.md
│   └── longest_common_subsequence.py
│
└── ngs-pipeline/
    ├── README.md
    └── ngs_expression_pipeline.py
