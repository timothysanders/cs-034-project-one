'''
Generate randomly ordered small size, randomly ordered medium size, nearly ordered,
ordered, reverse ordered) for general comparison

1. Random (General Case): small size, medium size

Description: A completely random array with no inherent order.
Purpose: Tests the general efficiency of sorting algorithms.

Expected Results:

QuickSort typically performs well (O(n log n) on average).
Merge Sort has a consistent O(n log n) but requires extra space.
Shell Sort may not be as fast as QuickSort but is space-efficient.

2. Nearly Sorted Dataset (Best Case for Shell Sort)
Description: An already sorted array with a few misplaced elements.
Purpose: Evaluates how algorithms handle nearly sorted data.

Expected Results:

Shell Sort should be very fast (almost O(n) due to reduced swaps).
Merge Sort and QuickSort still perform O(n log n), making them slower than Shell Sort in this case.

3. Reverse Ordered Dataset (Worst Case for QuickSort)

Description: A dataset sorted in descending order.
Purpose: Tests how algorithms handle worst-case scenarios.

Expected Results:

QuickSort (with a bad pivot selection strategy) can degrade to O(n²).
Merge Sort remains stable at O(n log n).
Shell Sort performs better than QuickSort in this case, but not as well as Merge Sort.

4. Large Dataset (Scalability Test)

Description: A very large dataset (e.g., 1,000,000 elements).
Purpose: Evaluates how each algorithm scales with increasing data size.

Expected Results:

QuickSort should be the fastest on average.
Merge Sort will be stable but will require extra space.
Shell Sort might not be ideal for very large datasets.


'''
