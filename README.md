# cs-034-project-one
Repository for CS-034 project deliverables

# Project Overview

Collaborate in groups to design, implement, and analyze the performance of various sorting
algorithms (e.g., Shell Sort, Merge Sort, or Quick Sort)

Objectives:

1. Design and implement three sorting algorithms: Shell Sort, QuickSort, Merge Sort


   Structure of Project

   
   Separate .py files for each sorting algorithm, and one for datasets:

   . shell_sort.py: Contains the shell_sort function.

   . quick_sort.py: Contains the quick_sort function.

   . merge_sort.py: Contains the merge_sort function.

   . datasets.py: Contains functions to generate all the different types of datasets,
     including general-purpose and algorithm-specific ones

   . A main script (e.g., main.py or test_sorting.py) to import and run the tests.
  

3. Analyze and compare the runtime performance and efficiency of each sorting algorithm.


   To analyze efficiency, we'll:

   . Generate these datasets programmatically.

   . Run each sorting algorithm on each dataset.

   . Measure execution time and memory usage.

   . Compare results to determine which algorithm is best suited for each case.


3. Apply these algorithms to practical datasets and scenarios.

   Pros: Good separation of concerns. Each sorting algorithm is self-contained. Dataset
   generation is also modular. Easier to test individual algorithms.
