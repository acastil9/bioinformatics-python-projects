# DNA Sequence Comparison Using Dynamic Programming

## Overview

This project implements a longest common subsequence (LCS) algorithm in Python to compare DNA sequences and identify shared sequence patterns.

The project was developed during graduate bioinformatics coursework to explore algorithmic approaches to biological sequence comparison and to implement dynamic programming directly in Python.

## Objectives

- Compare pairs of DNA sequences computationally
- Implement the longest common subsequence algorithm
- Apply dynamic programming to a biological sequence problem
- Reconstruct the shared subsequence from the completed scoring matrix
- Practice translating an algorithmic concept into working Python code

## Implementation

The program constructs a dynamic programming matrix for two input DNA sequences. Each position in the matrix represents the solution to a smaller sequence-comparison problem.

When matching nucleotides are encountered, the algorithm extends the common subsequence. When the nucleotides differ, it selects the optimal result from previously calculated subproblems.

The completed matrix is then used to reconstruct the longest common subsequence shared by the two sequences.

## Files

### `longest_common_subsequence.py`
Python implementation of the longest common subsequence algorithm for DNA sequence comparison.

## Skills Demonstrated

- Python
- Dynamic programming
- Algorithm implementation
- Biological sequence analysis
- Matrix-based computation
- DNA sequence comparison
- Computational problem solving

## Project Context

This project was completed as part of graduate bioinformatics training and is included here to demonstrate the implementation of a fundamental sequence-comparison algorithm using Python.
