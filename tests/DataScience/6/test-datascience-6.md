# Advanced NumPy Operations - Test 6

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Master advanced NumPy operations including array broadcasting, linear algebra, advanced indexing, statistical functions, and array manipulation techniques for efficient numerical computing.

## Objectives

- Understand and apply array broadcasting rules
- Perform linear algebra operations with NumPy
- Use advanced indexing and masking techniques
- Apply statistical and mathematical functions
- Optimize numerical computations for performance

## Your Tasks

1. **array_broadcasting()** - Master broadcasting operations
2. **linear_algebra_operations()** - Perform matrix operations
3. **advanced_indexing()** - Use fancy indexing and boolean masks
4. **statistical_operations()** - Calculate statistics across axes
5. **array_performance()** - Optimize array operations

## Example

```python
import numpy as np
import time
from scipy import linalg
import matplotlib.pyplot as plt

def array_broadcasting():
    """Demonstrate NumPy broadcasting operations."""
    print("=== Array Broadcasting Operations ===")
    
    # Basic broadcasting examples
    print("Basic Broadcasting:")
    
    # Scalar with array
    arr = np.array([1, 2, 3, 4, 5])
    scalar_add = arr + 10
    scalar_mult = arr * 2
    
    print(f"Array: {arr}")
    print(f"Array + 10: {scalar_add}")
    print(f"Array * 2: {scalar_mult}")
    
    # 1D array with 2D array
    arr_1d = np.array([1, 2, 3])
    arr_2d = np.array([[10, 20, 30],
                       [40, 50, 60],
                       [70, 80, 90]])
    
    broadcast_add = arr_2d + arr_1d
    print(f"\\n2D array:\\n{arr_2d}")
    print(f"1D array: {arr_1d}")
    print(f"Broadcast addition:\\n{broadcast_add}")
    
    # Broadcasting with different shapes
    print("\\nBroadcasting with Different Shapes:")
    
    # (3, 1) + (1, 4) -> (3, 4)
    col_vector = np.array([[1], [2], [3]])
    row_vector = np.array([10, 20, 30, 40])
    
    broadcast_result = col_vector + row_vector
    print(f"Column vector (3,1):\\n{col_vector}")
    print(f"Row vector (1,4): {row_vector}")
    print(f"Broadcast result (3,4):\\n{broadcast_result}")
    
    # 3D broadcasting
    arr_3d = np.random.random((2, 3, 4))
    arr_2d_broadcast = np.array([[1, 2, 3, 4]])
    
    broadcast_3d = arr_3d + arr_2d_broadcast
    print(f"\\n3D array shape: {arr_3d.shape}")
    print(f"2D array shape: {arr_2d_broadcast.shape}")
    print(f"Broadcast result shape: {broadcast_3d.shape}")
    
    # Broadcasting rules demonstration
    def can_broadcast(shape1, shape2):
        \"\"\"Check if two shapes can be broadcast together.\"\"\""
        # Reverse the shapes (broadcasting works from right to left)
        shape1_rev = shape1[::-1]
        shape2_rev = shape2[::-1]
        
        # Pad shorter shape with 1s
        max_len = max(len(shape1_rev), len(shape2_rev))
        shape1_padded = [1] * (max_len - len(shape1_rev)) + list(shape1_rev)
        shape2_padded = [1] * (max_len - len(shape2_rev)) + list(shape2_rev)
        
        # Check compatibility
        for s1, s2 in zip(shape1_padded, shape2_padded):
            if s1 != 1 and s2 != 1 and s1 != s2:
                return False, None
        
        # Calculate result shape
        result_shape = tuple(max(s1, s2) for s1, s2 in zip(shape1_padded, shape2_padded))
        return True, result_shape
    
    # Test broadcasting compatibility
    test_shapes = [
        ((3, 1), (1, 4)),
        ((3, 4), (4,)),
        ((2, 3, 4), (3, 4)),
        ((2, 1, 4), (3, 1)),
        ((3, 4), (2, 3, 4)),
        ((3, 4), (5, 6))  # This should fail
    ]
    
    print("\\nBroadcasting Compatibility Tests:")
    for shape1, shape2 in test_shapes:
        compatible, result_shape = can_broadcast(shape1, shape2)
        status = "✓" if compatible else "✗"
        result = f" -> {result_shape}" if compatible else ""
        print(f"  {status} {shape1} + {shape2}{result}")
    
    # Practical broadcasting examples
    print("\\nPractical Broadcasting Examples:")
    
    # Normalize data (subtract mean, divide by std)
    data = np.random.normal(100, 15, (1000, 5))
    
    # Calculate statistics along axis 0 (rows)
    means = np.mean(data, axis=0, keepdims=True)
    stds = np.std(data, axis=0, keepdims=True)
    
    # Normalize using broadcasting
    normalized = (data - means) / stds
    
    print(f"Original data shape: {data.shape}")
    print(f"Means shape: {means.shape}")
    print(f"Normalized data shape: {normalized.shape}")
    print(f"Normalized means: {np.mean(normalized, axis=0)}")
    print(f"Normalized stds: {np.std(normalized, axis=0)}")
    
    return {
        "scalar_operations": {"add": scalar_add, "mult": scalar_mult},
        "broadcast_2d": broadcast_result,
        "broadcast_3d_shape": broadcast_3d.shape,
        "compatibility_tests": [(shape1, shape2, can_broadcast(shape1, shape2)) for shape1, shape2 in test_shapes],
        "normalized_stats": {"means": np.mean(normalized, axis=0), "stds": np.std(normalized, axis=0)}
    }

def linear_algebra_operations():
    """Perform linear algebra operations with NumPy."""
    print("\\n=== Linear Algebra Operations ===")
    
    # Matrix creation
    print("Matrix Creation:")
    
    # Identity matrix
    identity = np.eye(3)
    print(f"Identity matrix (3x3):\\n{identity}")
    
    # Diagonal matrix
    diagonal = np.diag([1, 2, 3, 4])
    print(f"\\nDiagonal matrix:\\n{diagonal}")
    
    # Random matrices
    np.random.seed(42)
    matrix_a = np.random.random((3, 3))
    matrix_b = np.random.random((3, 3))
    vector = np.random.random(3)
    
    print(f"\\nMatrix A:\\n{matrix_a}")
    print(f"\\nMatrix B:\\n{matrix_b}")
    print(f"\\nVector: {vector}")
    
    # Matrix operations
    print("\\nMatrix Operations:")
    
    # Matrix multiplication
    matrix_mult = np.dot(matrix_a, matrix_b)
    matrix_mult_alt = matrix_a @ matrix_b  # Alternative syntax
    
    print(f"Matrix multiplication (A @ B):\\n{matrix_mult}")
    print(f"Results match: {np.allclose(matrix_mult, matrix_mult_alt)}")
    
    # Element-wise operations
    element_add = matrix_a + matrix_b
    element_mult = matrix_a * matrix_b
    element_power = matrix_a ** 2
    
    print(f"\\nElement-wise addition:\\n{element_add}")
    print(f"\\nElement-wise multiplication:\\n{element_mult}")
    print(f"\\nElement-wise power:\\n{element_power}")
    
    # Matrix-vector operations
    print("\\nMatrix-Vector Operations:")
    
    matvec_result = np.dot(matrix_a, vector)
    matvec_alt = matrix_a @ vector
    
    print(f"Matrix-vector multiplication: {matvec_result}")
    print(f"Results match: {np.allclose(matvec_result, matvec_alt)}")
    
    # Linear algebra functions
    print("\\nLinear Algebra Functions:")
    
    # Determinant
    det_a = np.linalg.det(matrix_a)
    print(f"Determinant of A: {det_a:.6f}")
    
    # Matrix inverse
    try:
        inv_a = np.linalg.inv(matrix_a)
        print(f"\\nInverse of A:\\n{inv_a}")
        
        # Verify inverse: A @ A^-1 = I
        identity_check = matrix_a @ inv_a
        print(f"\\nA @ A^-1 (should be identity):\\n{identity_check}")
        print(f"Is close to identity: {np.allclose(identity_check, np.eye(3))}")
        
    except np.linalg.LinAlgError:
        print("Matrix A is singular (non-invertible)")
    
    # Eigenvalues and eigenvectors
    eigenvals, eigenvecs = np.linalg.eig(matrix_a)
    print(f"\\nEigenvalues: {eigenvals}")
    print(f"Eigenvectors:\\n{eigenvecs}")
    
    # SVD (Singular Value Decomposition)
    u, s, vt = np.linalg.svd(matrix_a)
    print(f"\\nSVD - U shape: {u.shape}, S shape: {s.shape}, Vt shape: {vt.shape}")
    
    # Reconstruct matrix from SVD
    reconstructed = u @ np.diag(s) @ vt
    print(f"SVD reconstruction error: {np.linalg.norm(matrix_a - reconstructed):.10f}")
    
    # QR decomposition
    q, r = np.linalg.qr(matrix_a)
    print(f"\\nQR decomposition - Q shape: {q.shape}, R shape: {r.shape}")
    
    # Verify QR decomposition
    qr_reconstructed = q @ r
    print(f"QR reconstruction error: {np.linalg.norm(matrix_a - qr_reconstructed):.10f}")
    
    # Matrix norms
    print("\\nMatrix Norms:")
    
    norms = {
        "Frobenius": np.linalg.norm(matrix_a, 'fro'),
        "2-norm": np.linalg.norm(matrix_a, 2),
        "1-norm": np.linalg.norm(matrix_a, 1),
        "inf-norm": np.linalg.norm(matrix_a, np.inf)
    }
    
    for norm_type, value in norms.items():
        print(f"  {norm_type}: {value:.6f}")
    
    # Solving linear systems
    print("\\nSolving Linear Systems:")
    
    # Ax = b
    b = np.random.random(3)
    x_solution = np.linalg.solve(matrix_a, b)
    
    print(f"System: Ax = b")
    print(f"b: {b}")
    print(f"Solution x: {x_solution}")
    
    # Verify solution
    verification = matrix_a @ x_solution
    print(f"Verification (Ax): {verification}")
    print(f"Error: {np.linalg.norm(verification - b):.10f}")
    
    return {
        "matrices": {"A": matrix_a, "B": matrix_b, "vector": vector},
        "operations": {
            "matrix_mult": matrix_mult,
            "element_add": element_add,
            "matvec": matvec_result
        },
        "properties": {
            "determinant": det_a,
            "eigenvalues": eigenvals,
            "singular_values": s
        },
        "norms": norms,
        "linear_system": {"solution": x_solution, "error": np.linalg.norm(verification - b)}
    }

def advanced_indexing():
    """Demonstrate advanced indexing and masking techniques."""
    print("\\n=== Advanced Indexing Operations ===")
    
    # Create sample data
    np.random.seed(42)
    data = np.random.randint(0, 100, (6, 8))
    
    print(f"Sample data:\\n{data}")
    
    # Boolean indexing
    print("\\nBoolean Indexing:")
    
    # Simple boolean mask
    mask_high = data > 50
    high_values = data[mask_high]
    
    print(f"Values > 50: {high_values}")
    print(f"Count of values > 50: {np.sum(mask_high)}")
    
    # Complex boolean conditions
    mask_range = (data >= 20) & (data <= 80)
    range_values = data[mask_range]
    
    print(f"\\nValues between 20 and 80: {range_values}")
    print(f"Count: {np.sum(mask_range)}")
    
    # Boolean indexing with modification
    data_copy = data.copy()
    data_copy[data_copy > 90] = 90  # Cap values at 90
    
    print(f"\\nData after capping at 90:\\n{data_copy}")
    
    # Fancy indexing
    print("\\nFancy Indexing:")
    
    # Select specific rows and columns
    row_indices = [0, 2, 4]
    col_indices = [1, 3, 5]
    
    fancy_selection = data[np.ix_(row_indices, col_indices)]
    print(f"Selected rows {row_indices}, cols {col_indices}:\\n{fancy_selection}")
    
    # Advanced fancy indexing
    rows = np.array([1, 3, 5])
    cols = np.array([2, 4, 6])
    diagonal_selection = data[rows, cols]
    
    print(f"\\nDiagonal selection: {diagonal_selection}")
    
    # Conditional indexing
    print("\\nConditional Indexing:")
    
    # Find indices of elements meeting criteria
    indices_high = np.where(data > 75)
    print(f"Indices where data > 75: {list(zip(indices_high[0], indices_high[1]))}")
    
    # Use where for conditional selection
    conditional_result = np.where(data > 50, data, 0)
    print(f"\\nConditional result (>50 keep, else 0):\\n{conditional_result}")
    
    # Multiple conditions with where
    multi_conditional = np.where(data > 75, 'high', np.where(data > 25, 'medium', 'low'))
    print(f"\\nMulti-conditional classification:\\n{multi_conditional}")
    
    # Advanced masking operations
    print("\\nAdvanced Masking:")
    
    # Create 3D data
    data_3d = np.random.random((4, 5, 6))
    
    # Mask based on condition across all dimensions
    mask_3d = data_3d > 0.7
    high_3d = data_3d[mask_3d]
    
    print(f"3D data shape: {data_3d.shape}")
    print(f"High values (>0.7) count: {np.sum(mask_3d)}")
    print(f"High values: {high_3d[:10]}...")  # Show first 10
    
    # Masking along specific axes
    print("\\nAxis-specific Operations:")
    
    # Find rows where any element > 80
    row_mask = np.any(data > 80, axis=1)
    rows_with_high = data[row_mask]
    
    print(f"Rows with any element > 80:\\n{rows_with_high}")
    
    # Find columns where all elements < 90
    col_mask = np.all(data < 90, axis=0)
    cols_all_low = data[:, col_mask]
    
    print(f"\\nColumns where all elements < 90:\\n{cols_all_low}")
    
    # Advanced selection techniques
    print("\\nAdvanced Selection Techniques:")
    
    # Select top-k elements
    flat_data = data.flatten()
    top_k = 10
    top_indices = np.argpartition(flat_data, -top_k)[-top_k:]
    top_values = flat_data[top_indices]
    
    print(f"Top {top_k} values: {np.sort(top_values)[::-1]}")
    
    # Select unique elements
    unique_values, counts = np.unique(data, return_counts=True)
    print(f"\\nUnique values count: {len(unique_values)}")
    print(f"Most frequent value: {unique_values[np.argmax(counts)]} (appears {np.max(counts)} times)")
    
    # Masked array operations
    print("\\nMasked Array Operations:")
    
    # Create masked array
    masked_data = np.ma.masked_where(data < 30, data)
    
    print(f"Masked array (values < 30 masked):")
    print(f"  Mean of unmasked: {masked_data.mean():.2f}")
    print(f"  Std of unmasked: {masked_data.std():.2f}")
    print(f"  Count of unmasked: {masked_data.count()}")
    
    return {
        "boolean_indexing": {
            "high_values_count": np.sum(mask_high),
            "range_values_count": np.sum(mask_range)
        },
        "fancy_indexing": {
            "fancy_selection": fancy_selection,
            "diagonal_selection": diagonal_selection
        },
        "conditional": {
            "high_indices_count": len(indices_high[0]),
            "conditional_result_nonzero": np.count_nonzero(conditional_result)
        },
        "advanced_masking": {
            "high_3d_count": np.sum(mask_3d),
            "rows_with_high_count": np.sum(row_mask),
            "cols_all_low_count": np.sum(col_mask)
        },
        "top_values": np.sort(top_values)[::-1],
        "unique_stats": {"count": len(unique_values), "most_frequent": unique_values[np.argmax(counts)]},
        "masked_stats": {"mean": masked_data.mean(), "count": masked_data.count()}
    }

def statistical_operations():
    """Perform statistical operations and analysis."""
    print("\\n=== Statistical Operations ===")
    
    # Create sample dataset
    np.random.seed(42)
    
    # Multi-dimensional data
    data = np.random.normal(100, 15, (1000, 5))  # 1000 samples, 5 features
    
    print(f"Dataset shape: {data.shape}")
    
    # Basic statistics
    print("\\nBasic Statistics:")
    
    basic_stats = {
        "mean": np.mean(data, axis=0),
        "median": np.median(data, axis=0),
        "std": np.std(data, axis=0),
        "var": np.var(data, axis=0),
        "min": np.min(data, axis=0),
        "max": np.max(data, axis=0)
    }
    
    for stat_name, values in basic_stats.items():
        print(f"  {stat_name}: {values}")
    
    # Percentiles and quantiles
    print("\\nPercentiles and Quantiles:")
    
    percentiles = [25, 50, 75, 90, 95, 99]
    percentile_values = np.percentile(data, percentiles, axis=0)
    
    for i, p in enumerate(percentiles):
        print(f"  {p}th percentile: {percentile_values[i]}")
    
    # Distribution statistics
    print("\\nDistribution Statistics:")
    
    from scipy import stats as scipy_stats
    
    # Skewness and kurtosis for each feature
    for i in range(data.shape[1]):
        feature_data = data[:, i]
        skewness = scipy_stats.skew(feature_data)
        kurtosis = scipy_stats.kurtosis(feature_data)
        
        print(f"  Feature {i}: Skewness = {skewness:.4f}, Kurtosis = {kurtosis:.4f}")
    
    # Correlation analysis
    print("\\nCorrelation Analysis:")
    
    correlation_matrix = np.corrcoef(data.T)
    print(f"Correlation matrix shape: {correlation_matrix.shape}")
    print(f"Correlation matrix:\\n{correlation_matrix}")
    
    # Find highest correlations
    correlation_copy = correlation_matrix.copy()
    np.fill_diagonal(correlation_copy, 0)  # Remove self-correlations
    
    max_corr_idx = np.unravel_index(np.argmax(np.abs(correlation_copy)), correlation_copy.shape)
    max_corr = correlation_copy[max_corr_idx]
    
    print(f"\\nHighest correlation: {max_corr:.4f} between features {max_corr_idx[0]} and {max_corr_idx[1]}")
    
    # Rolling statistics
    print("\\nRolling Statistics:")
    
    # Create time series data
    time_series = np.cumsum(np.random.normal(0, 1, 100))
    window_size = 10
    
    rolling_mean = np.convolve(time_series, np.ones(window_size)/window_size, mode='valid')
    
    print(f"Time series length: {len(time_series)}")
    print(f"Rolling mean length: {len(rolling_mean)}")
    print(f"Last 5 rolling means: {rolling_mean[-5:]}")
    
    # Statistical tests
    print("\\nStatistical Tests:")
    
    # Normality test (Shapiro-Wilk for small samples)
    sample_data = data[:50, 0]  # First 50 samples of first feature
    shapiro_stat, shapiro_p = scipy_stats.shapiro(sample_data)
    
    print(f"Shapiro-Wilk test: statistic = {shapiro_stat:.6f}, p-value = {shapiro_p:.6f}")
    print(f"Normal distribution: {'Yes' if shapiro_p > 0.05 else 'No'} (α = 0.05)")
    
    # T-test between two features
    t_stat, t_p = scipy_stats.ttest_ind(data[:, 0], data[:, 1])
    print(f"\\nT-test between features 0 and 1:")
    print(f"  t-statistic = {t_stat:.6f}, p-value = {t_p:.6f}")
    print(f"  Significantly different: {'Yes' if t_p < 0.05 else 'No'} (α = 0.05)")
    
    # Advanced statistics
    print("\\nAdvanced Statistics:")
    
    # Covariance matrix
    cov_matrix = np.cov(data.T)
    print(f"Covariance matrix shape: {cov_matrix.shape}")
    
    # Principal component analysis (simplified)
    eigenvals, eigenvecs = np.linalg.eig(cov_matrix)
    explained_variance_ratio = eigenvals / np.sum(eigenvals)
    
    print(f"Explained variance ratio: {explained_variance_ratio}")
    print(f"First PC explains {explained_variance_ratio[0]:.2%} of variance")
    
    # Histogram analysis
    print("\\nHistogram Analysis:")
    
    feature_0 = data[:, 0]
    hist, bin_edges = np.histogram(feature_0, bins=20)
    
    print(f"Feature 0 histogram:")
    print(f"  Bins: {len(bin_edges)-1}")
    print(f"  Most frequent bin: {bin_edges[np.argmax(hist)]:.2f} - {bin_edges[np.argmax(hist)+1]:.2f}")
    print(f"  Frequency: {np.max(hist)}")
    
    return {
        "basic_stats": basic_stats,
        "percentiles": dict(zip(percentiles, percentile_values.T.tolist())),
        "correlation_matrix": correlation_matrix,
        "max_correlation": {"value": max_corr, "features": max_corr_idx},
        "rolling_stats": {"mean": rolling_mean[-5:].tolist()},
        "normality_test": {"statistic": shapiro_stat, "p_value": shapiro_p, "is_normal": shapiro_p > 0.05},
        "t_test": {"statistic": t_stat, "p_value": t_p, "is_different": t_p < 0.05},
        "pca": {"explained_variance": explained_variance_ratio.tolist()},
        "histogram": {"max_frequency": int(np.max(hist)), "bin_count": len(bin_edges)-1}
    }

def array_performance():
    """Optimize array operations for performance."""
    print("\\n=== Array Performance Optimization ===")
    
    # Performance comparison: Python lists vs NumPy arrays
    print("Performance Comparison:")
    
    # Large arrays
    size = 1000000
    
    # Python list operations
    python_list = list(range(size))
    
    start_time = time.time()
    python_result = [x * 2 for x in python_list]
    python_time = time.time() - start_time
    
    print(f"Python list multiplication: {python_time:.4f} seconds")
    
    # NumPy array operations
    numpy_array = np.arange(size)
    
    start_time = time.time()
    numpy_result = numpy_array * 2
    numpy_time = time.time() - start_time
    
    print(f"NumPy array multiplication: {numpy_time:.4f} seconds")
    print(f"NumPy speedup: {python_time / numpy_time:.1f}x")
    
    # Memory efficiency
    print("\\nMemory Efficiency:")
    
    import sys
    
    python_memory = sys.getsizeof(python_list)
    numpy_memory = numpy_array.nbytes
    
    print(f"Python list memory: {python_memory:,} bytes")
    print(f"NumPy array memory: {numpy_memory:,} bytes")
    print(f"Memory ratio: {python_memory / numpy_memory:.1f}x")
    
    # Vectorization examples
    print("\\nVectorization Examples:")
    
    # Inefficient: using loops
    data = np.random.random(10000)
    
    start_time = time.time()
    result_loop = np.zeros_like(data)
    for i in range(len(data)):
        result_loop[i] = np.sqrt(data[i]) * 2 + 1
    loop_time = time.time() - start_time
    
    # Efficient: vectorized operations
    start_time = time.time()
    result_vectorized = np.sqrt(data) * 2 + 1
    vectorized_time = time.time() - start_time
    
    print(f"Loop-based computation: {loop_time:.4f} seconds")
    print(f"Vectorized computation: {vectorized_time:.4f} seconds")
    print(f"Vectorization speedup: {loop_time / vectorized_time:.1f}x")
    print(f"Results match: {np.allclose(result_loop, result_vectorized)}")
    
    # Broadcasting vs explicit loops
    print("\\nBroadcasting vs Explicit Loops:")
    
    matrix = np.random.random((1000, 1000))
    vector = np.random.random(1000)
    
    # Using loops
    start_time = time.time()
    result_loops = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result_loops[i, j] = matrix[i, j] + vector[j]
    loops_time = time.time() - start_time
    
    # Using broadcasting
    start_time = time.time()
    result_broadcast = matrix + vector
    broadcast_time = time.time() - start_time
    
    print(f"Explicit loops: {loops_time:.4f} seconds")
    print(f"Broadcasting: {broadcast_time:.4f} seconds")
    print(f"Broadcasting speedup: {loops_time / broadcast_time:.1f}x")
    print(f"Results match: {np.allclose(result_loops, result_broadcast)}")
    
    # Efficient array operations
    print("\\nEfficient Array Operations:")
    
    # Use views instead of copies when possible
    large_array = np.random.random((1000, 1000))
    
    # View (no copy)
    start_time = time.time()
    view_slice = large_array[::2, ::2]  # Every other element
    view_time = time.time() - start_time
    
    # Copy
    start_time = time.time()
    copy_slice = large_array[::2, ::2].copy()
    copy_time = time.time() - start_time
    
    print(f"View creation: {view_time:.6f} seconds")
    print(f"Copy creation: {copy_time:.6f} seconds")
    print(f"View is faster: {copy_time > view_time}")
    
    # Memory-efficient operations
    print("\\nMemory-Efficient Operations:")
    
    # In-place operations
    test_array = np.random.random(100000)
    original_id = id(test_array)
    
    # In-place operation
    test_array *= 2
    after_inplace_id = id(test_array)
    
    print(f"In-place operation preserves array identity: {original_id == after_inplace_id}")
    
    # Out-of-place operation
    test_array2 = np.random.random(100000)
    original_id2 = id(test_array2)
    test_array2 = test_array2 * 2
    after_outplace_id = id(test_array2)
    
    print(f"Out-of-place operation creates new array: {original_id2 != after_outplace_id}")
    
    # Optimal data types
    print("\\nOptimal Data Types:")
    
    # Compare different data types
    int_data = np.arange(1000000, dtype=np.int64)
    float_data = np.arange(1000000, dtype=np.float64)
    float32_data = np.arange(1000000, dtype=np.float32)
    
    print(f"int64 memory: {int_data.nbytes:,} bytes")
    print(f"float64 memory: {float_data.nbytes:,} bytes")
    print(f"float32 memory: {float32_data.nbytes:,} bytes")
    print(f"float32 memory saving: {(1 - float32_data.nbytes / float_data.nbytes) * 100:.1f}%")
    
    return {
        "performance_comparison": {
            "python_time": python_time,
            "numpy_time": numpy_time,
            "speedup": python_time / numpy_time
        },
        "memory_efficiency": {
            "python_memory": python_memory,
            "numpy_memory": numpy_memory,
            "memory_ratio": python_memory / numpy_memory
        },
        "vectorization": {
            "loop_time": loop_time,
            "vectorized_time": vectorized_time,
            "speedup": loop_time / vectorized_time
        },
        "broadcasting": {
            "loops_time": loops_time,
            "broadcast_time": broadcast_time,
            "speedup": loops_time / broadcast_time
        },
        "memory_operations": {
            "view_time": view_time,
            "copy_time": copy_time,
            "view_faster": copy_time > view_time
        },
        "data_types": {
            "int64_memory": int_data.nbytes,
            "float64_memory": float_data.nbytes,
            "float32_memory": float32_data.nbytes,
            "float32_saving": (1 - float32_data.nbytes / float_data.nbytes) * 100
        }
    }

# Main execution
if __name__ == "__main__":
    print("=== Advanced NumPy Operations ===")
    
    print("\\n1. Array Broadcasting:")
    broadcasting_results = array_broadcasting()
    
    print("\\n2. Linear Algebra:")
    linalg_results = linear_algebra_operations()
    
    print("\\n3. Advanced Indexing:")
    indexing_results = advanced_indexing()
    
    print("\\n4. Statistical Operations:")
    stats_results = statistical_operations()
    
    print("\\n5. Array Performance:")
    performance_results = array_performance()
    
    print("\\n" + "="*60)
    print("=== ADVANCED NUMPY OPERATIONS COMPLETE ===")
    print("✓ Array broadcasting and shape manipulation")
    print("✓ Linear algebra and matrix operations")
    print("✓ Advanced indexing and boolean masking")
    print("✓ Statistical analysis and hypothesis testing")
    print("✓ Performance optimization techniques")
    print("✓ Memory-efficient array operations")
```

## Hints

- Broadcasting rules work from right to left on array dimensions
- Use `@` operator for matrix multiplication, `*` for element-wise
- Boolean indexing with `&`, `|`, and `~` for complex conditions
- Use `axis` parameter in statistical functions for dimension-specific operations
- Vectorized operations are much faster than Python loops

## Test Cases

Your functions should handle:

1. Broadcasting between arrays of different but compatible shapes
2. Complex linear algebra operations including decompositions
3. Advanced indexing with boolean masks and fancy indexing
4. Statistical operations across different axes and dimensions
5. Performance-optimized array operations with proper vectorization

## Bonus Challenge

Create a machine learning algorithm using only NumPy operations, implement a neural network from scratch, and build a comprehensive data analysis pipeline!
