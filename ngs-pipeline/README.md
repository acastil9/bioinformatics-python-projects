# NGS RNA-Seq Expression Analysis Pipeline

## Overview

This project implements a Python-based workflow for processing next-generation sequencing (NGS) data through major stages of an RNA-seq expression analysis pipeline.

The workflow coordinates established bioinformatics command-line tools for sequence quality assessment, read trimming, alignment, alignment-file processing, and gene-level quantification.

The project was developed during graduate bioinformatics coursework to practice building a reproducible computational workflow that connects multiple stages of NGS data processing.

## Workflow

The pipeline follows the general sequence:

**FASTQ reads → Quality Control → Read Trimming → Alignment → BAM Processing → Gene Quantification**

The workflow integrates:

1. **FastQC** — assesses sequencing-read quality
2. **Trimmomatic** — performs quality and adapter trimming
3. **HISAT2** — aligns sequencing reads to a reference genome
4. **SAMtools** — processes alignment files
5. **featureCounts** — generates gene-level read counts

## Pipeline Stages

### 1. Quality Control
FastQC is used to evaluate the quality of the input sequencing reads before downstream processing.

### 2. Read Trimming
Trimmomatic removes low-quality sequence and unwanted adapter contamination prior to alignment.

### 3. Read Alignment
HISAT2 maps the processed sequencing reads against a reference genome.

### 4. Alignment Processing
SAMtools is used to work with the resulting alignment files and prepare them for downstream analysis.

### 5. Gene-Level Quantification
featureCounts assigns aligned reads to genomic features to produce gene-level count data suitable for downstream expression analysis.

## Files

### `ngs_expression_pipeline.py`
Python script implementing the NGS processing workflow and coordinating the external bioinformatics tools used at each stage.

## Tools and Technologies

- Python
- FastQC
- Trimmomatic
- HISAT2
- SAMtools
- featureCounts
- FASTQ/SAM/BAM sequencing data
- RNA-seq workflow design

## Skills Demonstrated

- Python scripting
- NGS data processing
- RNA-seq analysis workflows
- Command-line bioinformatics
- Workflow automation
- Sequence quality control
- Read alignment
- Gene-level quantification
- Integration of multiple bioinformatics tools

## Reproducibility

Running the complete workflow requires the external bioinformatics programs referenced above, along with appropriate sequencing reads, a reference genome, and genome annotation files.

File paths and environment-specific configuration may need to be adjusted before running the script on a different system.

## Project Context

This project was completed as part of graduate bioinformatics training and is included here to demonstrate Python-based workflow development and integration of commonly used tools for next-generation sequencing analysis.
