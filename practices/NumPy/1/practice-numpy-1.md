# Practice NumPy 1: Array Operations and Mathematical Functions

**Difficulty:** ⭐⭐⭐☆☆ (Medium)

**Related Topics:** NumPy arrays, mathematical operations, percentage calculations

## Objective

Master NumPy for numerical computing, array operations, and mathematical calculations including percentage computations.

## Requirements

Create functions that demonstrate NumPy capabilities:

1. `array_creation_and_manipulation()` - Different ways to create and manipulate arrays
2. `percentage_calculator(data, **options)` - Calculate various percentage metrics
3. `statistical_operations(datasets)` - Perform statistical analysis on arrays
4. `matrix_operations()` - Work with 2D arrays and matrix operations
5. `data_analysis_pipeline(raw_data)` - Complete data processing pipeline

## NumPy Concepts to Cover

- Array creation: zeros, ones, arange, linspace, random
- Array operations: arithmetic, broadcasting, indexing, slicing
- Statistical functions: mean, median, std, percentiles
- Mathematical functions: sqrt, sin, cos, log, exp
- Array reshaping and dimension manipulation

## Examples

```python
import numpy as np

# Percentage calculations
scores = np.array([85, 92, 78, 96, 88])
percentages = percentage_calculator(scores, total=100, precision=2)
# Should calculate: pass rate, average percentage, grade distribution

# Statistical operations
data = np.random.normal(100, 15, 1000)  # Normal distribution
stats = statistical_operations([data])
```

## Hints

- Install NumPy: `pip install numpy`
- Use `np.array()` to create arrays from lists
- Broadcasting allows operations between arrays of different shapes
- Use `axis` parameter for operations along specific dimensions
- NumPy is much faster than pure Python for numerical operations
- Use appropriate data types (int, float) for memory efficiency

## Practice Cases

Your functions should handle:

1. 1D and 2D arrays with various data types
2. Percentage calculations with different base values
3. Statistical operations with missing data (NaN values)
4. Large datasets for performance testing
5. Edge cases like empty arrays and division by zero