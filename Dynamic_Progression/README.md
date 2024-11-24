# Matrix Chain Multiplication Problem

## Overview
Matrix multiplication is associative but not commutative. When multiplying multiple matrices, the order of multiplication (parenthesization) affects the number of computations required. The goal is to find the most efficient way to multiply matrices to minimize the number of scalar multiplications.

---

## Problem Description
### Part (a): 
#### Multiplying an m x n matrix by an n x p matrix:
- Takes **m × n × p** scalar multiplications.

#### Example:
Given matrices A₁, A₂, A₃, and A₄ with dimensions:
- A₁: 5 × 4
- A₂: 4 × 6
- A₃: 6 × 2
- A₄: 2 × 7

**Task:**  
- Compute all possible ways of performing the multiplication `A₁ × A₂ × A₃ × A₄`.
- Calculate the total number of scalar multiplications for each parenthesization.

---

### Part (b): 
#### Number of Alternative Parenthesizations
For multiplying matrices `A₁ × A₂ × ... × Aₙ`:
- Define `P(n)` as the number of different parenthesizations for `n` matrices.

1. Base Cases:
   - `P(1) = 1`
   - `P(2) = 1`

2. Recursive Case:
   - `P(n) = Σ(k=1 to n-1) P(k) × P(n-k)` for `n ≥ 3`

#### i) Prove that:
- `P(n + 1) ≥ P(n) + P(n - 1)`  
- Use the relationship between `P(n)` and Fibonacci numbers to show that `P(n)` grows exponentially.

#### ii) Exhaustive Search/Brute Force:
- Discuss whether brute force is efficient for evaluating `P(n)` parenthesizations.

---

### Part (c): Dynamic Programming Approach
#### Definitions:
Let `Aᵢⱼ` represent the multiplication of matrices from `Aᵢ` to `Aⱼ`. The matrix `Aᵢⱼ` has dimensions `pᵢ₋₁ × pⱼ`.

Define `m[i, j]` as the minimum (optimal) number of scalar multiplications needed to compute `Aᵢⱼ`.

#### i) Recurrence Relationship:
If the optimal solution of `Aᵢⱼ` involves splitting into `Aᵢₖ` and `Aₖ₊₁ⱼ` for some `i ≤ k < j`, derive the relationship:
- `m[i, j] = min (m[i, k] + m[k + 1, j] + pᵢ₋₁ × pₖ × pⱼ)`

#### ii) Example:
For matrices A₁, A₂, A₃, and A₄:
- Dimensions:  
  `p₀ = 5, p₁ = 4, p₂ = 6, p₃ = 2, p₄ = 7`
- Compute `m[1, 4]` using the recurrence relation.

---

### Part (d): Analysis of Dynamic Programming
Using the dynamic programming approach:
- Describe the time complexity.
- Explain the advantages over brute force for solving the matrix chain multiplication problem.
