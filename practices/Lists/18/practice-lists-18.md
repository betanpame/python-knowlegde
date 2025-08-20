# Complex List Algorithms - Practice 18

**Difficulty:** ⭐⭐⭐⭐ (Medium)

**Related Topics:** Advanced Algorithms, Dynamic Programming, Complex Problem Solving

## Objectives

- Implement sophisticated list algorithms
- Handle complex data manipulation scenarios
- Apply advanced algorithmic concepts

## Description

Tackle advanced list processing challenges that require sophisticated algorithms and problem-solving skills. These problems mirror real-world data processing scenarios.

## Examples

```python
# Find longest increasing subsequence
sequence = [10, 9, 2, 5, 3, 7, 101, 18]
result = longest_increasing_subsequence(sequence)  # [2, 3, 7, 18] or similar

# Advanced pattern matching
data = [1, 2, 3, 2, 1, 4, 5, 4]
patterns = find_all_patterns(data, min_length=3)
```

## Your Tasks

1. **longest_increasing_subsequence(numbers)** - Find longest increasing subsequence
2. **find_all_patterns(data, min_length)** - Find repeated patterns in list
3. **solve_subset_sum(numbers, target)** - Find subset that sums to target
4. **merge_intervals(intervals)** - Merge overlapping intervals
5. **find_equilibrium_index(numbers)** - Find index where left sum equals right sum
6. **rearrange_alternating(positive, negative)** - Alternate positive and negative numbers
7. **find_majority_element(numbers)** - Find element appearing more than n/2 times
8. **sliding_window_maximum(numbers, window_size)** - Find maximum in each sliding window

## Hints

- Use dynamic programming for subsequence problems
- Pattern matching may require hash tables or string algorithms
- Subset sum is a classic DP problem
- Interval merging requires sorting and careful boundary checking
- Equilibrium index involves prefix/suffix sums
- Consider time and space complexity for large inputs

## Performance Requirements

- Should handle lists with up to 10,000 elements efficiently
- Algorithms should have reasonable time complexity
- Memory usage should be optimized where possible

Remember: These are challenging problems that test your algorithmic thinking!