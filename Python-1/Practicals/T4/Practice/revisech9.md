# Comprehensive NumPy & OOP Reference Guide

## Table of Contents
- [NumPy Reference](#numpy-reference)
  - [1. Array Shape Fundamentals](#1-array-shape-fundamentals)
  - [2. Reshaping Arrays](#2-reshaping-arrays)
  - [3. Multidimensional Arrays](#3-multidimensional-arrays)
  - [4. Array Concatenation](#4-array-concatenation)
  - [5. Array Splitting](#5-array-splitting)
  - [6. Conditional Operations](#6-conditional-operations)
  - [7. Axis Concept Explained](#7-axis-concept-explained)
  - [8. Common Mistakes & Pitfalls](#8-common-mistakes--pitfalls)
  - [9. Quick Reference Rules](#9-quick-reference-rules)
  - [10. Self-Assessment Test](#10-self-assessment-test)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
  - [Inheritance Fundamentals](#inheritance-fundamentals)
  - [Abstraction Fundamentals](#abstraction-fundamentals)
- [Unique Coding Patterns](#unique-coding-patterns)
  - [Diamond Problem (Multiple Inheritance)](#diamond-problem-multiple-inheritance)
  - [Column Swapping with Fancy Indexing](#column-swapping-with-fancy-indexing)
  - [Abstract Base Class Implementation](#abstract-base-class-implementation)
  - [Sorting Arrays by Specific Row](#sorting-arrays-by-specific-row)
  - [Operator Overloading](#operator-overloading)
  - [Vectorized Operations](#vectorized-operations)

---

## NumPy Reference

### 1. Array Shape Fundamentals

**`arr.shape`**
- **Description**: Returns a tuple representing the dimensions of the array
- **Interpretation**: Number of elements at each level of nesting
- **Example**: `arr.shape` = (3, 4, 5) means 3 blocks, each containing 4 rows, each containing 5 elements

**Shape Interpretation Table**

| Array Example | Shape | Visual Interpretation |
|--------------|-------|----------------------|
| `[1, 2, 3]` | `(3,)` | 1D: 3 elements in a row |
| `[[1,2],[3,4]]` | `(2,2)` | 2D: 2 rows × 2 columns |
| `[[[1,2],[3,4]], [[5,6],[7,8]]]` | `(2,2,2)` | 3D: 2 blocks → 2 rows → 2 columns |
| `[[[[1,2],[3,4]]]]` | `(1,1,2,2)` | 4D: 1 group → 1 block → 2 rows → 2 columns |

**Reading Shape Left to Right**
- **Pattern**: "X of Y of Z of ... values"
- **Example**: Shape (2, 3, 4) = "2 blocks, each containing 3 rows, each containing 4 columns"

**Example Code:**
```python
import numpy as np

# 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print(f"1D shape: {arr1d.shape}")  # Output: (5,)

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D shape: {arr2d.shape}")  # Output: (2, 3)

# 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"3D shape: {arr3d.shape}")  # Output: (2, 2, 2)

# Understanding shape components
print(f"arr2d has {arr2d.shape[0]} rows and {arr2d.shape[1]} columns")
```

### 2. Reshaping Arrays

**`arr.reshape(dimensions)`**
- **Description**: Changes array structure without changing data
- **Rule 1**: Total elements before and after must match
- **Rule 2**: Only one dimension can be -1 (auto-calculated)
- **Rule 3**: Returns new array (original unchanged unless assigned)

**Valid Reshape Examples**

```python
import numpy as np

# Create base array
arr = np.arange(6)  # [0, 1, 2, 3, 4, 5]
print(f"Original shape: {arr.shape}")  # (6,)

# Basic reshape
arr2x3 = arr.reshape(2, 3)
print(f"2x3 shape: {arr2x3.shape}")
# [[0 1 2]
#  [3 4 5]]

arr3x2 = arr.reshape(3, 2)
print(f"3x2 shape: {arr3x2.shape}")
# [[0 1]
#  [2 3]
#  [4 5]]

# Using -1 for auto-calculation
arr_auto1 = arr.reshape(2, -1)  # NumPy calculates 3
print(f"2x-1 shape: {arr_auto1.shape}")  # (2, 3)

arr_auto2 = arr.reshape(-1, 2)  # NumPy calculates 3
print(f"-1x2 shape: {arr_auto2.shape}")  # (3, 2)

arr_auto3 = arr.reshape(1, -1)  # 1D to 2D row vector
print(f"1x-1 shape: {arr_auto3.shape}")  # (1, 6)

# 3D reshape
arr = np.arange(24)
arr_3d = arr.reshape(2, 3, 4)
print(f"3D shape: {arr_3d.shape}")  # (2, 3, 4)
```

**Invalid Reshape Examples**

```python
import numpy as np

arr = np.arange(6)

# ERROR: Total elements don't match
try:
    arr.reshape(4, 2)  # Needs 8 elements, but arr has only 6
except ValueError as e:
    print(f"Error: {e}")  # cannot reshape array of size 6 into shape (4,2)

# ERROR: Multiple -1 values
try:
    arr.reshape(-1, -1)  # Can't calculate two dimensions
except ValueError as e:
    print(f"Error: {e}")  # can only specify one unknown dimension

# ERROR: Invalid dimensions
try:
    arr.reshape(2, 4)  # 2*4=8 ≠ 6
except ValueError as e:
    print(f"Error: {e}")
```

**Reshape with -1 Trick**
```python
import numpy as np

# Complex auto-calculation examples
arr = np.arange(48)

# 3D with one unknown
result1 = arr.reshape(3, 4, -1)  # Calculates 48/(3*4) = 4
print(f"3x4x-1 shape: {result1.shape}")  # (3, 4, 4)

# 4D with one unknown
result2 = arr.reshape(2, 2, 3, -1)  # Calculates 48/(2*2*3) = 4
print(f"2x2x3x-1 shape: {result2.shape}")  # (2, 2, 3, 4)

# Flattening with -1
arr_2d = np.array([[1,2], [3,4], [5,6]])
flattened = arr_2d.reshape(-1)  # Converts to 1D
print(f"Flattened shape: {flattened.shape}")  # (6,)
```

### 3. Multidimensional Arrays

**Understanding Dimensions**

| Shape | Dimension | Common Name | Visualization |
|-------|-----------|-------------|---------------|
| `(n,)` | 1D | Vector/List | Single row of values |
| `(r, c)` | 2D | Matrix/Table | Rows and columns |
| `(b, r, c)` | 3D | Cube/Blocks | Multiple matrices stacked |
| `(a, b, r, c)` | 4D | Tensor | Multiple cubes grouped |
| `(d, a, b, r, c)` | 5D | Higher-order Tensor | Nested grouping |

**Memory Trick**: Left dimensions = containers, Right dimensions = actual values

**Practical Examples:**
```python
import numpy as np

# 1D: Shopping list
shopping = np.array(["milk", "eggs", "bread", "butter"])
print(f"Shopping list shape: {shopping.shape}")  # (4,)

# 2D: Student marks table
marks = np.array([
    [85, 90, 78],  # Student 1
    [92, 88, 95],  # Student 2
    [76, 85, 80]   # Student 3
])
print(f"Marks table shape: {marks.shape}")  # (3, 3)

# 3D: RGB image (height × width × channels)
image = np.random.randint(0, 256, (480, 640, 3))
print(f"Image shape: {image.shape}")  # (480, 640, 3)

# 4D: Batch of images
batch = np.random.randint(0, 256, (32, 480, 640, 3))
print(f"Batch shape: {batch.shape}")  # (32, 480, 640, 3)
```

**Accessing Elements in Different Dimensions:**
```python
import numpy as np

# 2D access
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Element at [1,2]: {arr2d[1, 2]}")  # 6
print(f"Row 1: {arr2d[1, :]}")  # [4, 5, 6]
print(f"Column 0: {arr2d[:, 0]}")  # [1, 4, 7]

# 3D access
arr3d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(f"Element at [0,1,0]: {arr3d[0, 1, 0]}")  # 3
print(f"Block 1: {arr3d[1, :, :]}")
# [[5, 6],
#  [7, 8]]
```

### 4. Array Concatenation

**`np.concatenate((array1, array2, ...), axis)`**
- **Description**: Joins arrays along existing axis
- **Critical Rule**: All dimensions except the concatenation axis must match
- **Returns**: New concatenated array

**Axis Interpretation Table**

| Axis | 2D Arrays | 3D Arrays | Visual Direction |
|------|-----------|-----------|------------------|
| `axis=0` | Add rows (vertical) | Add blocks (depth) | Downwards |
| `axis=1` | Add columns (horizontal) | Add rows (vertical) | Rightwards |
| `axis=2` | Not applicable | Add columns (horizontal) | Into page |
| `axis=n` | Add along nth dimension | Add along nth dimension | Along that axis |

**Concatenation Examples:**
```python
import numpy as np

# Example arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Array a:")
print(a)
print("Shape:", a.shape)  # (2, 2)

print("\nArray b:")
print(b)
print("Shape:", b.shape)  # (2, 2)

# axis=0: Stack vertically (add rows)
result0 = np.concatenate((a, b), axis=0)
print(f"\naxis=0 concatenation shape: {result0.shape}")  # (4, 2)
print(result0)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# axis=1: Stack horizontally (add columns)
result1 = np.concatenate((a, b), axis=1)
print(f"\naxis=1 concatenation shape: {result1.shape}")  # (2, 4)
print(result1)
# [[1 2 5 6]
#  [3 4 7 8]]
```

**3D Concatenation Examples:**
```python
import numpy as np

# 3D arrays
arr3d_1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr3d_2 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])

print("3D array 1 shape:", arr3d_1.shape)  # (2, 2, 2)
print("3D array 2 shape:", arr3d_2.shape)  # (2, 2, 2)

# axis=0: Add blocks
concatenated_0 = np.concatenate((arr3d_1, arr3d_2), axis=0)
print(f"\naxis=0 shape: {concatenated_0.shape}")  # (4, 2, 2)

# axis=1: Add rows within each block
concatenated_1 = np.concatenate((arr3d_1, arr3d_2), axis=1)
print(f"axis=1 shape: {concatenated_1.shape}")  # (2, 4, 2)

# axis=2: Add columns within each row
concatenated_2 = np.concatenate((arr3d_1, arr3d_2), axis=2)
print(f"axis=2 shape: {concatenated_2.shape}")  # (2, 2, 4)
```

**Common Concatenation Errors:**
```python
import numpy as np

# ERROR: Mismatched dimensions
a = np.array([[1, 2], [3, 4]])  # (2, 2)
b = np.array([[5, 6]])  # (1, 2)

try:
    # axis=0 requires same number of columns
    np.concatenate((a, b), axis=0)  # OK: (2,2) + (1,2) → (3,2)
    print("axis=0 concatenation successful")
    
    # axis=1 requires same number of rows
    np.concatenate((a, b), axis=1)  # ERROR: rows don't match
except ValueError as e:
    print(f"Concatenation error: {e}")
```

**Alternative Concatenation Functions:**
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# vstack: Vertical stacking (axis=0 for 1D arrays)
v_result = np.vstack((a, b))
print(f"vstack shape: {v_result.shape}")  # (2, 3)

# hstack: Horizontal stacking (axis=1 for 1D arrays)
h_result = np.hstack((a, b))
print(f"hstack shape: {h_result.shape}")  # (6,)

# stack: Creates new axis
s_result = np.stack((a, b), axis=0)
print(f"stack axis=0 shape: {s_result.shape}")  # (2, 3)

s_result = np.stack((a, b), axis=1)
print(f"stack axis=1 shape: {s_result.shape}")  # (3, 2)
```

### 5. Array Splitting

**`np.split(array, indices_or_sections, axis)`**
- **Description**: Divides array into multiple sub-arrays
- **Rule**: Must split into equal parts (unless using indices)
- **Returns**: List of sub-arrays

**Split Methods Table**

| Function | Description | Equal Parts Required |
|----------|-------------|---------------------|
| `np.split()` | General split | Yes (or specific indices) |
| `np.array_split()` | Allows unequal splits | No |
| `np.vsplit()` | Vertical split (axis=0) | Yes |
| `np.hsplit()` | Horizontal split (axis=1) | Yes |
| `np.dsplit()` | Depth split (axis=2) | Yes |

**Basic Splitting Examples:**
```python
import numpy as np

# Create array
arr = np.arange(12).reshape(3, 4)
print("Original array:")
print(arr)
print(f"Shape: {arr.shape}")
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Split along axis=0 (rows)
split_rows = np.split(arr, 3, axis=0)
print(f"\nSplit into 3 row chunks:")
for i, chunk in enumerate(split_rows):
    print(f"Chunk {i}: shape {chunk.shape}")
    print(chunk)
# Each chunk shape: (1, 4)

# Split along axis=1 (columns)
split_cols = np.split(arr, 2, axis=1)
print(f"\nSplit into 2 column chunks:")
for i, chunk in enumerate(split_cols):
    print(f"Chunk {i}: shape {chunk.shape}")
    print(chunk)
# Each chunk shape: (3, 2)
```

**Using Split Indices:**
```python
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Split at specific indices
split_at = [2, 5, 7]  # Split after elements 2, 5, and 7
result = np.split(arr, split_at)

print(f"Split at indices {split_at}:")
for i, chunk in enumerate(result):
    print(f"Part {i}: {chunk}")
# Parts: [0,1], [2,3,4], [5,6], [7,8,9]
```

**Handling Unequal Splits:**
```python
import numpy as np

arr = np.arange(10).reshape(2, 5)
print("Original array:")
print(arr)

# ERROR: Cannot split 5 columns into 3 equal parts
try:
    np.split(arr, 3, axis=1)
except ValueError as e:
    print(f"\nError with np.split: {e}")

# Solution: Use array_split for unequal parts
unequal_split = np.array_split(arr, 3, axis=1)
print("\nUsing np.array_split for 3 unequal parts:")
for i, chunk in enumerate(unequal_split):
    print(f"Part {i}: shape {chunk.shape}")
    print(chunk)
# Parts will have shapes: (2,2), (2,2), (2,1)
```

**Vertical and Horizontal Split Shortcuts:**
```python
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# vsplit - vertical split (split rows)
v_chunks = np.vsplit(arr, 3)  # Equivalent to split(axis=0)
print("Vertical split (vsplit):")
for chunk in v_chunks:
    print(chunk)
# Each chunk: 1 row × 4 columns

# hsplit - horizontal split (split columns)
h_chunks = np.hsplit(arr, 2)  # Equivalent to split(axis=1)
print("\nHorizontal split (hsplit):")
for chunk in h_chunks:
    print(chunk)
# Each chunk: 3 rows × 2 columns
```

**3D Array Splitting:**
```python
import numpy as np

# Create 3D array
arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"3D array shape: {arr_3d.shape}")  # (2, 3, 4)

# Split along axis=0 (blocks)
blocks_split = np.split(arr_3d, 2, axis=0)
print(f"\nSplit into {len(blocks_split)} blocks")
print(f"Each block shape: {blocks_split[0].shape}")  # (1, 3, 4)

# Split along axis=1 (rows)
rows_split = np.split(arr_3d, 3, axis=1)
print(f"\nSplit into {len(rows_split)} row groups")
print(f"Each group shape: {rows_split[0].shape}")  # (2, 1, 4)

# Split along axis=2 (columns)
cols_split = np.split(arr_3d, 2, axis=2)
print(f"\nSplit into {len(cols_split)} column groups")
print(f"Each group shape: {cols_split[0].shape}")  # (2, 3, 2)
```

### 6. Conditional Operations

**`np.where(condition, [x, y])`**
- **Description**: Return elements chosen from x or y depending on condition
- **Form 1**: `np.where(condition)` returns indices where condition is True
- **Form 2**: `np.where(condition, x, y)` returns x where condition is True, y otherwise
- **Shape Preservation**: Output shape matches input shape

**Basic Conditional Replacement:**
```python
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original array:", arr)

# Basic where: replace values > 5 with -1
result = np.where(arr > 5, -1, arr)
print("Values > 5 replaced with -1:", result)
# Output: [ 1  2  3  4  5 -1 -1 -1 -1 -1]

# Using different replacements
result2 = np.where(arr > 5, 100, arr * 2)
print(">5 → 100, else ×2:", result2)
# Output: [ 2  4  6  8 10 100 100 100 100 100]
```

**Finding Indices with where():**
```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Find indices where condition is True
indices = np.where(arr > 5)
print("Indices where arr > 5:")
print("Row indices:", indices[0])
print("Column indices:", indices[1])
print("Values at these indices:", arr[indices])

# The indices can be used for indexing
print("\nAccessing values using where indices:")
for row, col in zip(indices[0], indices[1]):
    print(f"arr[{row},{col}] = {arr[row, col]}")
```

**Multi-dimensional Conditional Operations:**
```python
import numpy as np

# 2D array example
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# Condition on 2D array
condition = arr > 50
print("Condition (arr > 50):")
print(condition)
# [[False False False]
#  [False False  True]
#  [ True  True  True]]

# Replace based on condition
result = np.where(condition, 999, arr)
print("\nReplace >50 with 999:")
print(result)
# [[ 10  20  30]
#  [ 40  50 999]
#  [999 999 999]]

# Complex condition
complex_result = np.where(
    (arr > 20) & (arr < 80),  # Condition
    arr * 2,                  # True case
    arr // 2                  # False case
)
print("\nComplex condition (20 < value < 80):")
print(complex_result)
```

**Multiple Conditions:**
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Multiple conditions using logical operators
result = np.where(
    (arr % 2 == 0) & (arr > 5),  # Even AND > 5
    "Even>5",
    np.where(
        arr % 2 != 0,            # Odd
        "Odd",
        "Even<=5"                # Even but ≤ 5
    )
)
print("Multiple conditions:")
for val, label in zip(arr, result):
    print(f"{val}: {label}")
```

**Working with where() Output:**
```python
import numpy as np

# Create sample data
scores = np.array([85, 92, 78, 45, 67, 89, 93, 55, 72, 61])
students = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])

# Find students who passed (score >= 60)
pass_indices = np.where(scores >= 60)[0]
print("Passing student indices:", pass_indices)
print("Passing students:", students[pass_indices])
print("Passing scores:", scores[pass_indices])

# Find failing students
fail_indices = np.where(scores < 60)[0]
print("\nFailing student indices:", fail_indices)
print("Failing students:", students[fail_indices])

# Calculate statistics
pass_rate = len(pass_indices) / len(scores) * 100
print(f"\nPass rate: {pass_rate:.1f}%")
```

### 7. Axis Concept Explained

**Fundamental Rule**: Axis specifies the dimension that will be **collapsed** or **operated along**

**Axis Visualization for Different Dimensions:**

**2D Array (Matrix):**
```
[[1, 2, 3],    axis=0: ↓ (vertical/rows)
 [4, 5, 6],    axis=1: → (horizontal/columns)
 [7, 8, 9]]
```

**3D Array (Cube):**
```
Block 0:      Block 1:
[[1,2],       [[5,6],      axis=0: between blocks
 [3,4]]        [7,8]]      axis=1: ↓ within blocks
                        axis=2: → within rows
```

**Axis Operations Explained:**
```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Original array:")
print(arr)
print(f"Shape: {arr.shape}")

# Sum along axis=0 (sum columns, collapse rows)
sum_axis0 = arr.sum(axis=0)
print(f"\nSum axis=0 (column sums): {sum_axis0}")
print(f"Shape after sum axis=0: {sum_axis0.shape}")  # (3,)

# Sum along axis=1 (sum rows, collapse columns)
sum_axis1 = arr.sum(axis=1)
print(f"\nSum axis=1 (row sums): {sum_axis1}")
print(f"Shape after sum axis=1: {sum_axis1.shape}")  # (2,)

# Mean along different axes
mean_axis0 = arr.mean(axis=0)  # Mean of each column
mean_axis1 = arr.mean(axis=1)  # Mean of each row
print(f"\nMean axis=0 (column means): {mean_axis0}")
print(f"Mean axis=1 (row means): {mean_axis1}")
```

**3D Axis Operations:**
```python
import numpy as np

# Create 3D array: 2 blocks, 3 rows, 4 columns
arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"3D array shape: {arr_3d.shape}")  # (2, 3, 4)

# Sum along axis=0: Collapse blocks
sum_axis0 = arr_3d.sum(axis=0)
print(f"\nSum axis=0 shape: {sum_axis0.shape}")  # (3, 4)
print("Result (sum of corresponding elements across blocks):")
print(sum_axis0)

# Sum along axis=1: Collapse rows within blocks
sum_axis1 = arr_3d.sum(axis=1)
print(f"\nSum axis=1 shape: {sum_axis1.shape}")  # (2, 4)
print("Result (sum of rows within each block):")
print(sum_axis1)

# Sum along axis=2: Collapse columns within rows
sum_axis2 = arr_3d.sum(axis=2)
print(f"\nSum axis=2 shape: {sum_axis2.shape}")  # (2, 3)
print("Result (sum of columns within each row):")
print(sum_axis2)
```

**Axis in Concatenation:**
```python
import numpy as np

# Understanding axis in concatenation
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# axis=0: Stack below (add to rows dimension)
concat_axis0 = np.concatenate((a, b), axis=0)
print("axis=0 concatenation:")
print(concat_axis0)
print(f"Shape: {concat_axis0.shape}")  # (4, 2)

# axis=1: Stack beside (add to columns dimension)
concat_axis1 = np.concatenate((a, b), axis=1)
print("\naxis=1 concatenation:")
print(concat_axis1)
print(f"Shape: {concat_axis1.shape}")  # (2, 4)
```

**Axis Mental Model:**
- **axis=0**: Think "vertical" or "between the outermost brackets"
- **axis=1**: Think "horizontal" or "between next level brackets"
- **axis=n**: Think "along the nth dimension from outside"

**Practical Axis Examples:**
```python
import numpy as np

# Student grades: 3 students, 4 subjects, 2 terms
grades = np.array([
    [[85, 90], [78, 82], [92, 88], [76, 80]],  # Student 1
    [[88, 85], [90, 92], [75, 78], [82, 85]],  # Student 2
    [[92, 94], [85, 88], [88, 90], [90, 92]]   # Student 3
])
print(f"Grades shape: {grades.shape}")  # (3, 4, 2)

# Average per student across all subjects and terms
student_avg = grades.mean(axis=(1, 2))
print(f"\nStudent averages: {student_avg}")

# Average per subject across all students and terms
subject_avg = grades.mean(axis=(0, 2))
print(f"Subject averages: {subject_avg}")

# Average per term across all students and subjects
term_avg = grades.mean(axis=(0, 1))
print(f"Term averages: {term_avg}")
```

### 8. Common Mistakes & Pitfalls

**1. Shape Mismatch in Concatenation**
```python
import numpy as np

# ERROR: Dimensions don't match for concatenation
a = np.array([[1, 2], [3, 4]])  # Shape (2, 2)
b = np.array([[5, 6, 7]])       # Shape (1, 3)

try:
    result = np.concatenate((a, b), axis=0)
except ValueError as e:
    print(f"Concatenation error: {e}")
    # All dimensions except axis must match
```

**2. Multiple -1 in Reshape**
```python
import numpy as np

arr = np.arange(12)

# ERROR: Can't have multiple -1
try:
    arr.reshape(-1, -1)
except ValueError as e:
    print(f"Reshape error: {e}")
    # Only one unknown dimension allowed
```

**3. Element Count Mismatch in Reshape**
```python
import numpy as np

arr = np.arange(10)  # 10 elements

# ERROR: 3×4 needs 12 elements
try:
    arr.reshape(3, 4)
except ValueError as e:
    print(f"Reshape error: {e}")
    # Total elements must match
```

**4. Incorrect Axis Assumption**
```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Common confusion: axis=0 vs axis=1
print("Array:")
print(arr)

# axis=0 sums columns (vertical)
print(f"\nsum(axis=0): {arr.sum(axis=0)}")  # [5, 7, 9]

# axis=1 sums rows (horizontal)
print(f"sum(axis=1): {arr.sum(axis=1)}")  # [6, 15]
```

**5. Using ^ Instead of ** for Exponentiation**
```python
import numpy as np

arr = np.array([2, 3, 4])

# CORRECT: Exponentiation
correct = arr ** 2  # Square each element
print(f"Correct (arr ** 2): {correct}")  # [4, 9, 16]

# WRONG: Bitwise XOR
wrong = arr ^ 2  # Bitwise XOR with 2
print(f"Wrong (arr ^ 2): {wrong}")  # [0, 1, 6]
```

**6. Forgetting NumPy Arrays are Homogeneous**
```python
import numpy as np

# All elements must be same type
mixed = np.array([1, 2.5, "three"])  # All converted to strings
print(f"Mixed array dtype: {mixed.dtype}")  # <U21 (Unicode string)
print(f"Mixed array: {mixed}")  # ['1' '2.5' 'three']
```

**7. Modifying Views Instead of Copies**
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
view = arr[1:4]  # Creates a view, not a copy
view[0] = 999    # Modifies original array!

print(f"Original array: {arr}")  # [1, 999, 3, 4, 5]

# Solution: Use copy()
arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:4].copy()
copy[0] = 999
print(f"Original after copy: {arr}")  # [1, 2, 3, 4, 5]
```

### 9. Quick Reference Rules

**Golden Rules Summary:**

1. **Shape Rule**: `arr.shape` returns (outer_dim, ..., inner_dim)
2. **Reshape Rule**: Total elements before = total elements after
3. **-1 Rule**: Only one dimension can be -1 (auto-calculated)
4. **Axis Rule**: Operations collapse along specified axis
5. **Concatenation Rule**: All dimensions except axis must match
6. **Split Rule**: Must split into equal parts (use array_split for unequal)

**Memory Aids:**

- **Shape**: "Read left to right: containers of containers of values"
- **Axis**: "The dimension that disappears after operation"
- **Reshape**: "Rearrange boxes, don't change number of items"
- **-1**: "Let NumPy do the math for this dimension"

**Quick Mental Checks:**

1. Before reshape: Multiply old dimensions = Multiply new dimensions
2. Before concatenate: Check all non-axis dimensions match
3. For axis operations: Result dimension = original dimension - 1
4. For where(): Output shape = input shape

### 10. Self-Assessment Test

**Test Your Understanding:**

```python
import numpy as np

# Question 1: Understanding shape
arr1 = np.arange(12).reshape(3, 4)
print("Q1: arr1 shape is", arr1.shape)
# Your answer: (3, 4)

# Question 2: Reshape with -1
arr2 = np.arange(20).reshape(4, -1)
print("Q2: arr2 shape is", arr2.shape)
# Your answer: (4, 5) because 20/4 = 5

# Question 3: 3D array shape
arr3 = np.arange(24).reshape(2, 3, 4)
print("Q3: arr3 has", arr3.shape[0], "blocks,",
      arr3.shape[1], "rows, and",
      arr3.shape[2], "columns")
# Your answer: 2 blocks, 3 rows, 4 columns

# Question 4: Axis sum
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
sum_axis0 = arr4.sum(axis=0)
sum_axis1 = arr4.sum(axis=1)
print("Q4: sum(axis=0) =", sum_axis0)
print("    sum(axis=1) =", sum_axis1)
# Your answer: [5 7 9] and [6 15]

# Question 5: Concatenation
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
concat_0 = np.concatenate((a, b), axis=0)
concat_1 = np.concatenate((a, b), axis=1)
print("Q5: axis=0 concatenation shape:", concat_0.shape)
print("    axis=1 concatenation shape:", concat_1.shape)
# Your answer: (4, 2) and (2, 4)

# Question 6: Conditional replacement
arr6 = np.array([10, 20, 30, 40, 50])
result = np.where(arr6 > 25, arr6 * 2, arr6)
print("Q6: where(arr > 25, arr*2, arr) =", result)
# Your answer: [10 20 60 80 100]
```

**Answer Key:**
1. (3, 4)
2. (4, 5)
3. 2 blocks, 3 rows, 4 columns
4. [5 7 9] and [6 15]
5. (4, 2) and (2, 4)
6. [10 20 60 80 100]

---

## Object-Oriented Programming (OOP)

### Inheritance Fundamentals

**Basic Inheritance Syntax:**
```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Parent: {self.name}")

class Child(Parent):  # Child inherits from Parent
    def __init__(self, name, age):
        super().__init__(name)  # Call parent constructor
        self.age = age
    
    def display(self):
        super().display()  # Call parent method
        print(f"Child age: {self.age}")

# Usage
child = Child("Alice", 10)
child.display()
# Output:
# Parent: Alice
# Child age: 10
```

**Types of Inheritance:**

1. **Single Inheritance:**
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):  # Single parent
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Woof!
```

2. **Multiple Inheritance:**
```python
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):  # Multiple parents
    pass

duck = Duck()
print(duck.fly())   # Flying
print(duck.swim())  # Swimming
```

3. **Multi-level Inheritance:**
```python
class Vehicle:
    def transport(self):
        return "Transporting"

class Car(Vehicle):
    def drive(self):
        return "Driving on road"

class ElectricCar(Car):
    def charge(self):
        return "Charging"

tesla = ElectricCar()
print(tesla.transport())  # Transporting (from Vehicle)
print(tesla.drive())      # Driving on road (from Car)
print(tesla.charge())     # Charging (own method)
```

**Method Resolution Order (MRO):**
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

obj = D()
print(obj.method())  # B (because of MRO)
print(D.mro())  # [D, B, C, A, object]
```

### Abstraction Fundamentals

**Abstract Base Classes (ABC):**
```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass  # Must be implemented by child classes
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return "This is a shape"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage
rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")           # 15
print(f"Perimeter: {rect.perimeter()}") # 16
print(rect.describe())                  # This is a shape

# ERROR: Cannot instantiate abstract class
try:
    shape = Shape()
except TypeError as e:
    print(f"Error: {e}")
```

**Complete Abstraction Example:**
```python
from abc import ABC, abstractmethod
import math

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    @abstractmethod
    def calculate_salary(self):
        pass
    
    def display_info(self):
        return f"ID: {self.emp_id}, Name: {self.name}"

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Usage
employees = [
    FullTimeEmployee("Alice", "FT001", 5000),
    PartTimeEmployee("Bob", "PT001", 20, 80)
]

for emp in employees:
    print(f"{emp.display_info()}, Salary: ${emp.calculate_salary()}")
```

---

## Unique Coding Patterns

### Diamond Problem (Multiple Inheritance)

**Problem Demonstration:**
```python
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

# Create instance
obj = D()

# Which method gets called?
print(f"Method called: {obj.method()}")
print(f"\nMethod Resolution Order (MRO):")
for i, cls in enumerate(D.mro()):
    print(f"{i+1}. {cls.__name__}")

# Output:
# Method called: Method from B
# MRO: D → B → C → A → object
```

**Solution with super():**
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        # Call next in MRO (C.method)
        result = super().method()
        return f"B → {result}"

class C(A):
    def method(self):
        # Call next in MRO (A.method)
        result = super().method()
        return f"C → {result}"

class D(B, C):
    def method(self):
        # Call next in MRO (B.method)
        result = super().method()
        return f"D → {result}"

obj = D()
print(obj.method())
# Output: D → B → C → A
```

### Column Swapping with Fancy Indexing

**Basic Column Swap:**
```python
import numpy as np

# Create sample array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Original array:")
print(arr)

# Swap column 0 and column 1
arr[:, [0, 1]] = arr[:, [1, 0]]
print("\nAfter swapping column 0 and 1:")
print(arr)
# Column 0 becomes: [2, 5, 8]
# Column 1 becomes: [1, 4, 7]
```

**Multiple Column Reordering:**
```python
import numpy as np

# Student data: [ID, Age, Score, Grade]
students = np.array([
    [101, 18, 85, 1],
    [102, 19, 92, 2],
    [103, 18, 78, 1],
    [104, 20, 88, 2],
    [105, 19, 95, 1]
])
print("Original student data:")
print(students)

# Reorder columns: [Score, Grade, Age, ID]
students = students[:, [2, 3, 1, 0]]
print("\nReordered: [Score, Grade, Age, ID]")
print(students)

# Swap Age and Grade columns
students[:, [1, 2]] = students[:, [2, 1]]
print("\nAfter swapping Grade and Age:")
print(students)
```

**Advanced Column Operations:**
```python
import numpy as np

# Create matrix
matrix = np.arange(1, 26).reshape(5, 5)
print("Original 5x5 matrix:")
print(matrix)

# Reverse column order
reversed_cols = matrix[:, ::-1]
print("\nColumns reversed:")
print(reversed_cols)

# Move last column to first
cols_reordered = matrix[:, [-1] + list(range(matrix.shape[1] - 1))]
print("\nLast column moved to first:")
print(cols_reordered)

# Sort columns by column sum
col_sums = matrix.sum(axis=0)
sorted_indices = np.argsort(col_sums)
sorted_matrix = matrix[:, sorted_indices]
print("\nColumns sorted by sum:")
print(sorted_matrix)
print(f"Column sums: {col_sums[sorted_indices]}")
```

### Abstract Base Class Implementation

**Complete Salary Calculation System:**
```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary
    
    @abstractmethod
    def calculate_gross_salary(self):
        pass
    
    @abstractmethod
    def calculate_deductions(self):
        pass
    
    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        deductions = self.calculate_deductions()
        return gross - deductions
    
    def display_payslip(self):
        print(f"\n{'='*40}")
        print(f"PAYSLIP")
        print(f"{'='*40}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Basic Salary: ${self.basic_salary:,.2f}")
        print(f"Gross Salary: ${self.calculate_gross_salary():,.2f}")
        print(f"Deductions: ${self.calculate_deductions():,.2f}")
        print(f"{'-'*40}")
        print(f"NET SALARY: ${self.calculate_net_salary():,.2f}")
        print(f"{'='*40}")

class RegularEmployee(Employee):
    def __init__(self, name, employee_id, basic_salary, da_percent=40, hra_percent=20):
        super().__init__(name, employee_id, basic_salary)
        self.da_percent = da_percent  # Dearness Allowance
        self.hra_percent = hra_percent  # House Rent Allowance
    
    def calculate_gross_salary(self):
        da = self.basic_salary * (self.da_percent / 100)
        hra = self.basic_salary * (self.hra_percent / 100)
        return self.basic_salary + da + hra
    
    def calculate_deductions(self):
        # Assume 10% tax, 5% PF
        tax = self.basic_salary * 0.10
        pf = self.basic_salary * 0.05
        return tax + pf

class ContractEmployee(Employee):
    def __init__(self, name, employee_id, basic_salary, bonus=0):
        super().__init__(name, employee_id, basic_salary)
        self.bonus = bonus
    
    def calculate_gross_salary(self):
        return self.basic_salary + self.bonus
    
    def calculate_deductions(self):
        # Contract employees have different deduction rules
        tax = min(self.basic_salary * 0.05, 1000)  # Max $1000 tax
        return tax

# Usage
employees = [
    RegularEmployee("John Smith", "EMP001", 50000),
    ContractEmployee("Jane Doe", "CONT001", 30000, bonus=5000),
    RegularEmployee("Bob Johnson", "EMP002", 60000, da_percent=35, hra_percent=25)
]

for emp in employees:
    emp.display_payslip()
```

### Sorting Arrays by Specific Row

**Sorting 2D Array by Row Values:**
```python
import numpy as np

# Create sample array
arr = np.array([[34, 43, 73],
                [82, 22, 12],
                [53, 94, 66]])
print("Original array:")
print(arr)

# Sort entire array based on values in row 1 (index 1)
sort_indices = arr[1, :].argsort()
sorted_arr = arr[:, sort_indices]
print("\nSorted based on row 1 values (82, 22, 12):")
print(sorted_arr)
# Row 1 was [82, 22, 12] → sorted to [12, 22, 82]
# All rows rearrange columns accordingly
```

**Multi-criteria Sorting:**
```python
import numpy as np

# Student data: [Math, Physics, Chemistry] scores for 5 students
scores = np.array([
    [85, 90, 78],  # Student 1
    [92, 88, 95],  # Student 2
    [76, 85, 80],  # Student 3
    [88, 92, 85],  # Student 4
    [95, 76, 88]   # Student 5
])
students = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

print("Original scores:")
for student, score_row in zip(students, scores):
    print(f"{student}: {score_row}")

# Sort by Physics scores (column 1)
physics_indices = scores[:, 1].argsort()
sorted_by_physics = scores[physics_indices]
sorted_students = students[physics_indices]

print("\nSorted by Physics scores:")
for student, score_row in zip(sorted_students, sorted_by_physics):
    print(f"{student}: {score_row} (Physics: {score_row[1]})")

# Sort by total score
total_scores = scores.sum(axis=1)
total_indices = total_scores.argsort()[::-1]  # Descending
sorted_by_total = scores[total_indices]
sorted_students_total = students[total_indices]

print("\nSorted by total score (descending):")
for student, score_row in zip(sorted_students_total, sorted_by_total):
    total = score_row.sum()
    print(f"{student}: {score_row} (Total: {total})")
```

**Stable Sorting with argsort:**
```python
import numpy as np

# Create array with duplicate values
arr = np.array([[5, 3, 1],
                [2, 4, 2],
                [3, 1, 3]])
print("Original array:")
print(arr)

# Sort by first row, then by second row for ties
sort_indices = np.lexsort((arr[1, :], arr[0, :]))
sorted_arr = arr[:, sort_indices]
print("\nSorted by row 0, then row 1 for ties:")
print(sorted_arr)
# Column order based on: (5,2,3), (3,4,1), (1,2,3)
```

### Operator Overloading

**Basic Comparison Operators:**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overload greater than operator
    def __gt__(self, other):
        # Compare magnitude
        mag_self = (self.x**2 + self.y**2) ** 0.5
        mag_other = (other.x**2 + other.y**2) ** 0.5
        return mag_self > mag_other
    
    # Overload less than operator
    def __lt__(self, other):
        mag_self = (self.x**2 + self.y**2) ** 0.5
        mag_other = (other.x**2 + other.y**2) ** 0.5
        return mag_self < mag_other
    
    # Overload equality operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Overload string representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Overload addition operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Overload multiplication operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Usage
v1 = Vector(3, 4)  # Magnitude: 5
v2 = Vector(1, 1)  # Magnitude: ~1.414
v3 = Vector(3, 4)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v3: {v3}")
print(f"\nv1 > v2: {v1 > v2}")  # True (5 > 1.414)
print(f"v1 < v2: {v1 < v2}")  # False
print(f"v1 == v3: {v1 == v3}")  # True
print(f"v1 + v2: {v1 + v2}")  # Vector(4, 5)
print(f"v1 * 2: {v1 * 2}")    # Vector(6, 8)
```

**Complete Student Comparison System:**
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # Dictionary of subject:score
    
    def total_marks(self):
        return sum(self.marks.values())
    
    def average_marks(self):
        return self.total_marks() / len(self.marks)
    
    # Overload greater than based on total marks
    def __gt__(self, other):
        return self.total_marks() > other.total_marks()
    
    # Overload less than based on total marks
    def __lt__(self, other):
        return self.total_marks() < other.total_marks()
    
    # Overload greater than or equal
    def __ge__(self, other):
        return self.total_marks() >= other.total_marks()
    
    # Overload less than or equal
    def __le__(self, other):
        return self.total_marks() <= other.total_marks()
    
    # Overload equality
    def __eq__(self, other):
        return self.total_marks() == other.total_marks()
    
    # Overload string representation
    def __str__(self):
        return f"{self.name}: Total={self.total_marks()}, Avg={self.average_marks():.1f}"
    
    # Overload addition (create group)
    def __add__(self, other):
        group_name = f"{self.name}&{other.name}"
        # Combine marks by averaging
        combined_marks = {}
        all_subjects = set(self.marks.keys()) | set(other.marks.keys())
        for subject in all_subjects:
            score1 = self.marks.get(subject, 0)
            score2 = other.marks.get(subject, 0)
            combined_marks[subject] = (score1 + score2) / 2
        return Student(group_name, combined_marks)

# Usage
student1 = Student("Alice", {"Math": 85, "Science": 90, "English": 88})
student2 = Student("Bob", {"Math": 78, "Science": 85, "English": 92})
student3 = Student("Charlie", {"Math": 92, "Science": 88, "English": 85})

print("Student Information:")
print(student1)
print(student2)
print(student3)

print("\nComparisons:")
print(f"Alice > Bob: {student1 > student2}")
print(f"Bob < Charlie: {student2 < student3}")
print(f"Alice == Charlie: {student1 == student3}")

# Sort students
students = [student1, student2, student3]
sorted_students = sorted(students, reverse=True)
print("\nStudents sorted by total marks (descending):")
for student in sorted_students:
    print(f"  {student}")

# Combine students
group = student1 + student2
print(f"\nCombined group: {group}")
```

### Vectorized Operations

**Temperature Conversion Example:**
```python
import numpy as np

# Convert Fahrenheit to Celsius for entire array
fahrenheit = np.array([32, 68, 86, 104, 212, 50, 77, 95])
print(f"Fahrenheit temperatures: {fahrenheit}")

# Vectorized conversion
celsius = (fahrenheit - 32) * 5/9
print(f"Celsius temperatures: {celsius}")
print(f"Rounded Celsius: {np.round(celsius, 1)}")

# Create temperature categories
categories = np.where(
    celsius < 0, "Freezing",
    np.where(celsius < 10, "Cold",
    np.where(celsius < 20, "Cool",
    np.where(celsius < 30, "Warm", "Hot")))
)
print("\nTemperature categories:")
for f, c, cat in zip(fahrenheit, celsius, categories):
    print(f"{f}°F = {c:.1f}°C → {cat}")
```

**Advanced Vectorized Calculations:**
```python
import numpy as np

# Student performance analysis
num_students = 100
num_subjects = 5

# Generate random scores (0-100)
scores = np.random.randint(0, 101, (num_students, num_subjects))
print(f"Scores shape: {scores.shape}")
print(f"First 5 students' scores:")
print(scores[:5])

# Vectorized calculations
total_scores = scores.sum(axis=1)
average_scores = scores.mean(axis=1)
max_scores = scores.max(axis=1)
min_scores = scores.min(axis=1)

print(f"\nFirst 5 students' statistics:")
print("Total\tAverage\tMax\tMin")
for i in range(5):
    print(f"{total_scores[i]}\t{average_scores[i]:.1f}\t{max_scores[i]}\t{min_scores[i]}")

# Grade assignment using vectorization
def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

# Vectorize the function
vectorized_grade = np.vectorize(assign_grade)
grades = vectorized_grade(average_scores)

print(f"\nGrade distribution:")
unique_grades, grade_counts = np.unique(grades, return_counts=True)
for grade, count in zip(unique_grades, grade_counts):
    percentage = (count / num_students) * 100
    print(f"{grade}: {count} students ({percentage:.1f}%)")

# Find top 10% students
percentile_90 = np.percentile(total_scores, 90)
top_students = np.where(total_scores >= percentile_90)[0]
print(f"\nTop 10% students (score >= {percentile_90:.0f}): {len(top_students)} students")
```

**Matrix Operations with Vectorization:**
```python
import numpy as np

# Image processing example
# Simulate grayscale image (0-255)
image = np.random.randint(0, 256, (10, 10))
print("Original image (10x10):")
print(image)

# Vectorized operations for image processing
# 1. Brighten image (add 50 to all pixels)
brightened = np.clip(image + 50, 0, 255)
print("\nBrightened image (+50):")
print(brightened)

# 2. Create high contrast
contrast = np.where(image > 128, 255, 0)
print("\nHigh contrast (threshold 128):")
print(contrast)

# 3. Apply blur (simple average filter)
def apply_blur(img):
    blurred = np.zeros_like(img, dtype=float)
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            blurred[i, j] = np.mean(img[i-1:i+2, j-1:j+2])
    return blurred.astype(int)

# Vectorized blur (more efficient)
def apply_blur_vectorized(img):
    # Using convolution concept (simplified)
    kernel = np.ones((3, 3)) / 9
    blurred = np.zeros_like(img, dtype=float)
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            blurred[i, j] = np.sum(img[i-1:i+2, j-1:j+2] * kernel)
    return blurred.astype(int)

blurred_image = apply_blur_vectorized(image)
print("\nBlurred image:")
print(blurred_image)

# 4. Edge detection (simplified)
edges = np.abs(image[1:, :] - image[:-1, :]) + np.abs(image[:, 1:] - image[:, :-1])
edges = np.pad(edges, ((0,1), (0,1)), mode='constant')
print("\nEdge detection result:")
print(edges.astype(int))
```

This comprehensive guide covers all essential NumPy operations, OOP concepts, and unique coding patterns with practical examples and explanations.