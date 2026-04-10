# Write a NumPy program to sort a given 2D array of shape along the first axis, 
# then last axis and finally on flattened array without using the built-in sort function.


import numpy as np


def bubble_sort(lst):
    lst = lst.copy()  # undvik att ändra originalet
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst



def sort_custom(arr, axis=None):
    arr = arr.copy()

    # --- Fall 1: flatten-sortering ---
    if axis is None:
        flat = arr.flatten().tolist()
        sorted_flat = bubble_sort(flat)
        return np.array(sorted_flat).reshape(arr.shape)

    rows, cols = arr.shape

    # --- Fall 2: axis=0 (kolumnvis) ---
    if axis == 0:
        for col in range(cols):
            col_vals = arr[:, col].tolist()
            arr[:, col] = bubble_sort(col_vals)
        return arr

    # --- Fall 3: axis=1 (radvis) ---
    if axis == 1:
        for row in range(rows):
            row_vals = arr[row, :].tolist()
            arr[row, :] = bubble_sort(row_vals)
        return arr

    raise ValueError("Axis must be 0, 1, or None")

data = np.array([
    [30, 10, 20],
    [5,  25, 15],
    [50, 40, 45]
])

print(sort_custom(data, axis=0))
print()
print(sort_custom(data, axis=1))
print()
print(sort_custom(data))