#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 22:40:48 2025

@author: andrea 
"""

import os
import subprocess
import argparse

# Set up command-line arguments
parser = argparse.ArgumentParser(description="NGS Tumor Sample Analysis Workflow")
parser.add_argument("--fastq_r1", required=True, help="Path to R1 FASTQ file")
parser.add_argument("--fastq_r2", required=True, help="Path to R2 FASTQ file")
parser.add_argument("--output_dir", default="analysis_output", help="Output directory")
parser.add_argument("--reference_genome", required=True, help="Path to reference genome index")
parser.add_argument("--gtf_file", required=True, help="Path to gene annotation GTF file")
args = parser.parse_args()

def run_fastqc(fastq_files, output_dir):
    """Run FastQC for quality assessment."""
    os.makedirs(output_dir, exist_ok=True)
    subprocess.run(["fastqc", "-o", output_dir] + fastq_files)

def run_trimming(fastq_r1, fastq_r2, output_dir):
    """Trim low-quality reads."""
    os.makedirs(output_dir, exist_ok=True)
    trimmed_r1 = os.path.join(output_dir, "trimmed_R1.fastq")
    trimmed_r2 = os.path.join(output_dir, "trimmed_R2.fastq")

    cmd = [
        "trimmomatic", "PE", fastq_r1, fastq_r2,
        trimmed_r1, "/dev/null",
        trimmed_r2, "/dev/null",
        "LEADING:3", "TRAILING:3", "SLIDINGWINDOW:4:20", "MINLEN:50"
    ]
    subprocess.run(cmd)
    return trimmed_r1, trimmed_r2

def run_alignment(trimmed_r1, trimmed_r2, reference_genome, output_dir):
    """Align reads to the reference genome."""
    os.makedirs(output_dir, exist_ok=True)
    sam_file = os.path.join(output_dir, "aligned.sam")

    cmd = ["hisat2", "-x", reference_genome, "-1", trimmed_r1, "-2", trimmed_r2, "-S", sam_file]
    subprocess.run(cmd)
    return sam_file

def convert_sam_to_bam(sam_file, output_dir):
    """Convert SAM to BAM and sort."""
    bam_file = os.path.join(output_dir, "aligned.bam")
    subprocess.run(["samtools", "view", "-b", "-o", bam_file, sam_file])
    subprocess.run(["samtools", "sort", "-o", bam_file, bam_file])
    return bam_file

def quantify_expression(bam_file, gtf_file, output_dir):
    """Quantify gene expression."""
    os.makedirs(output_dir, exist_ok=True)
    counts_file = os.path.join(output_dir, "gene_counts.txt")

    cmd = ["featureCounts", "-a", gtf_file, "-o", counts_file, bam_file]
    subprocess.run(cmd)
    return counts_file

# Perform steps
run_fastqc([args.fastq_r1, args.fastq_r2], args.output_dir)
trimmed_r1, trimmed_r2 = run_trimming(args.fastq_r1, args.fastq_r2, args.output_dir)
sam_file = run_alignment(trimmed_r1, trimmed_r2, args.reference_genome, args.output_dir)
bam_file = convert_sam_to_bam(sam_file, args.output_dir)
gene_counts = quantify_expression(bam_file, args.gtf_file, args.output_dir)

print(f"Gene expression quantification completed. Results saved in: {gene_counts}")
