# cs-034-project-one
Repository for CS-034 project deliverables


Separate .py files for each sorting algorithm, and one for datasets.

** Structure **

shell_sort.py: Contains the shell_sort function.

quick_sort.py: Contains the quick_sort function.

merge_sort.py: Contains the merge_sort function.

datasets.py: Contains functions to generate all the different types of datasets, including
general-purpose and algorithm-specific ones

Add specific dataset generation functions to the datasets.py file, with clear naming conventions.

A main script (e.g., main.py or test_sorting.py) to import and run the tests.

Pros: Good separation of concerns. Each sorting algorithm is self-contained. Dataset
generation is also modular. Easier to test individual algorithms.

Cons:
