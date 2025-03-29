# CS-034: Project One
- Comparative Analysis of Performance and Efficiency: *Shell Sort*, *QuickSort*, and *Merge Sort*
- Contributors: Megan Ng (Yu Yu Ng), Michael Jung, and Tim Sanders

# Project Overview
Collaborate in groups to design, implement, and analyze the performance of various sorting algorithms (e.g., Shell Sort, Merge Sort, or Quick Sort)

### Objectives
- Design and implement three sorting algorithms: Shell Sort, QuickSort, Merge Sort
### Structure of Project
- Separate .py files for each sorting algorithm, and one for datasets:
  - [`shell_sort.py`](shell_sort.py): Contains the shell_sort function.
  - [`quick_sort.py`](quicksort.py): Contains the quick_sort function.
  - [`merge_sort.py`](merge_sort.py): Contains the merge_sort function.
  - [`datasets.py`](datasets.py): Contains functions to generate all the different types of datasets, including general-purpose and algorithm-specific ones 
  - [`main.py`](main.py): The main script to import and run the tests.
### Analysis and Comparison of Runtime Performance and Efficiency
- To analyze efficiency, we
  - Generate datasets programmatically.
  - Run each sorting algorithm on each dataset.
  - Measure execution time and memory usage.
  - Compare results to determine which algorithm is best suited for each case.
### Getting Started
- To run the program, you will first need to install the dependencies that are found in the `requirements.txt` file.
- Begin by creating a virtual environment
```commandline
python -m venv .venv
```
- Then activate the virtual environment and install the requirements specified
```commandline
source .venv/bin/activate
pip install -r requirements.txt
```
- After you have installed the requirements successfully, you can run the `main.py` file
```python
python main.py
```
- The output generated will contain tables that will be similar to what is shown below
```text
-------------------------
GENERAL RESULTS
-------------------------
                             Dataset     Size  Shell Sort Time (s)  Shell Sort Swaps  QuickSort Time (s)  QuickSort Swaps  MergeSort Time (s)  MergeSort Swaps
0                             Random    10000             0.016713            136872            0.006576            38558            0.012135         24837980
1                      Nearly Sorted    10000             0.006543             12453            0.005185            21771            0.010279            76263
2                     Reverse Sorted    10000             0.008953             52042            0.004979            20773            0.010199         49944667
3                    Many Duplicates    10000             0.006563             18959            0.005962            59512            0.011043         18791860
4                   Even Distributed    10000             0.005426                 0            0.004777            14998            0.009590                0
5   Uneven Distributed (Front Heavy)    10000             0.011817             86087            0.006415            45829            0.011663         37462166
6     Uneven Distributed (End Heavy)    10000             0.011915             87061            0.006319            42218            0.011428         12330821
7        Sorted with Indices Swapped    10000             0.013416            107264            0.004394             4782            0.011363          5775216
8              Exponentially Growing    10000             0.005752                 0            0.003996                0            0.009952                0
9                            Fractal    10000             0.011011             73800            0.005573            22954            0.010885         24995000
10                  Sorted in Groups    10000             0.005453                 0            0.003954                0            0.009583                0
11                             Evens    10000             0.016626            150240            0.006570            30918            0.012040         24925574
12                              Odds    10000             0.017034            153924            0.006428            31214            0.012027         24983248
13                     One Duplicate    10000             0.005308                 0            0.006238            64608            0.009193                0
14               Multiple Duplicates    10000             0.007781             34756            0.006168            56042            0.011529         22625983
15          Large Random (1,000,000)  1000000             5.149169          51760157            0.995269          4790189            1.849917     249927443318

```