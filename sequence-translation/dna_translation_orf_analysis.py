#!/usr/bin/env 
Forward Strand ORFs:
# -*- coding: utf-8 -*-

import random

#add genetic code
genetic_code = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

#random DNA sequence
def generate_random_dna(length=200):
    return ''.join(random.choices("ATGC", k=length))

#define reverse compliment
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

#Translation
def translate_dna(dna):
    protein = []
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i + 3]
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            if amino_acid == '*':  # Stop codon
                break
            protein.append(amino_acid)
    return ''.join(protein)

#find ORFS
def find_orfs(dna):
    orfs = []
    for frame in range(3):
        sequence = dna[frame:]
        protein = translate_dna(sequence)
        if protein:
            orfs.append(protein)
    return orfs

#Function
def main():
    sequences = [generate_random_dna() for _ in range(10)]
    for i, seq in enumerate(sequences):
        print(f"\nSequence {i + 1}: {seq}")
        print("Forward Strand ORFs:")
        forward_orfs = find_orfs(seq)
        for orf in forward_orfs:
            print(orf)
        
        print("Reverse Strand ORFs:")
        reverse_seq = reverse_complement(seq)
        reverse_orfs = find_orfs(reverse_seq)
        for orf in reverse_orfs:
            print(orf)

if __name__ == "__main__":
    main()

