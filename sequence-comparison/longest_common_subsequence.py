#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:53:42 2025

@author: andrea
"""

import random
import numpy as np

def generate_dna_sequence(length):
   
    return ''.join(random.choice("ACGT") for _ in range(length))

def longest_common_subsequence(seq1, seq2):
# %%
    m, n = len(seq1), len(seq2)

    dp = np.zeros((m + 1, n + 1), dtype=int)
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# simulate the 10 pairs
test_cases = [(random.randint(5, 20), random.randint(5, 20)) for _ in range(10)]

for idx, (len1, len2) in enumerate(test_cases, 1):
    seq1 = generate_dna_sequence(len1)
    seq2 = generate_dna_sequence(len2)
    lcs_result = longest_common_subsequence(seq1, seq2)
    print(f"Test Case {idx}:")
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    print(f"Longest Common Subsequence: {lcs_result}\n")
