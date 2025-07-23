# Test Control Flow 2: Loop Control Statements

**Difficulty:** ⭐⭐⭐☆☆ (Medium)

**Related Topics:** break, continue, pass statements, loop control

## Objective

Master loop control statements to create efficient and controlled loop execution.

## Requirements

Implement functions that demonstrate effective use of `break`, `continue`, and `pass`:

1. `find_first_prime(start, end)` - Find first prime number in range using break
2. `skip_negative_sum(numbers)` - Sum only positive numbers using continue
3. `process_with_placeholder(data)` - Use pass for placeholder logic
4. `controlled_input_loop()` - Interactive loop with proper break conditions
5. `nested_loop_control(matrix, target)` - Control nested loops effectively

## Examples

```python
# Finding first prime with break
first_prime = find_first_prime(10, 30)  # Should return 11

# Skipping negatives with continue
numbers = [-1, 2, -3, 4, -5, 6]
positive_sum = skip_negative_sum(numbers)  # Should return 12 (2+4+6)
```

## Hints

- `break` exits the innermost loop completely
- `continue` skips the rest of the current iteration
- `pass` does nothing but maintains syntax validity
- Use labeled break alternative: return from function
- Consider loop-else clause for break detection

## Test Cases

Your functions should handle:

1. Empty ranges and lists
2. Nested loops with multiple break/continue points
3. Complex conditions requiring early exit
4. Placeholder code that will be implemented later
5. User input validation with retry loops
