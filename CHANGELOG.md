# Changelog


## [1.0.4] - 2025-05-09

### Changed

#### StrasssenAlgorithm.py
- Implemented Strassen's matrix multiplication algorithm for square matrices.
- Fixed incorrect use of division `/` by replacing with integer division `//` in `Split()` and `Merge()`.
- Included base case optimization for 2x2 matrices with direct computation of M1–M7.
- Added fallback `MatrixMultiply()` comparison for verification.
- Output uses Python 2 `print` syntax and may require update for Python 3 compatibility.

#### RedBlackTree.py
- Implemented red-black tree with full rotation and insertion fix-up logic.
- Used a sentinel `NIL` node to simplify leaf handling and balance checks.
- Added `inorder()` method to visualize the tree structure with color information.
- Used f-strings for modern Python output formatting.

#### Stack.py
- Created basic `Stack` class using list with `push`, `pop`, and `is_empty` methods.
- Added `None` return on underflow for robustness.
- Demonstrated usage with random values and sequential popping.


-----------------------------------------------------------

## [1.0.3] - 2025-05-08

### Changed

#### RadixSort.py
- Implemented LSD radix sort for non-negative integers using digit-wise bucket grouping.
- Ensured stability by using ordered bucket merging at each digit level.
- Wrapped logic in `__main__` guard and added formatted before/after output.

#### RandomizedSelect.py
- Added randomized selection algorithm for the i-th smallest element.
- Refactored partition logic into `randomized_partition()` with random pivot swapping.
- Ensured correctness by validating result against sorted list index.
- Formatted test outputs using Python 3 f-strings.

#### Queue.py
- Implemented fixed-size circular queue with head/tail pointer logic.
- Added `is_empty()` and `is_full()` checks to prevent overflow/underflow.
- Queue capacity constrained to `size - 1` to distinguish full from empty state.
- Demonstrated usage via sequential enqueue and dequeue in test block.

#### QuickSort.py
- Developed randomized quicksort using in-place Lomuto partition scheme.
- Added random pivot selection to reduce worst-case performance risk.
- Output formatted using Python 3 `print()` calls with sample test data.
- Guarded execution with `__main__` block for test isolation.


----------------------------------------------

## [1.0.2] - 2025-05-07

### Changed

#### MiddleSelect.py
- Added randomized quicksort and deterministic median-of-medians selection (`middle_select`) for order statistics.
- Improved robustness of recursive select logic with explicit count handling.
- Wrapped logic in `__main__` guard for standalone execution and testing.

#### OpenAddressingHash.py
- Implemented open addressing hash table with linear probing.
- Added fallback check for insertion failure if table is full.
- Ensured slot wrapping with modulo arithmetic.
- Output table and probe location in Python 3 format.

#### PowerProblem.py
- Implemented fast exponentiation using binary decomposition (`fast_pow`).
- Used integer division to avoid float errors in loop.
- Compared result against Python built-in `pow()` to validate correctness.
- Output structure formatted with f-strings.

#### LongestCommonSubsequence.py
- Refactored LCS into two functions: `lcs()` and helper `lcs_string()`.
- Introduced direction table (`trace`) for clean backtracking.
- Renamed variables and methods to PEP8-compliant styles.
- Prevented `None`-type string concatenation by using explicit empty string returns.

#### MergeSort.py
- Implemented top-down recursive merge sort with in-place merging.
- Refined `merge()` logic with clear indexing and merge boundaries.
- Ensured sort modifies list in-place, with structured test case.
- Guarded logic with `__main__` block for standalone execution.


------------------------------------------------------

## [1.0.1] - 2025-05-06

### Changed

#### HeapSort.py
- Replaced Python 2-style division `/` with integer division `//` for index calculation.
- Converted reverse loop slicing to `range(..., ..., -1)` for clarity and efficiency.
- Updated `heap_sort()` to return a copy of the array, preserving the original.
- Improved variable names and added inline documentation for heap operations.

#### InsertionSort.py
- Renamed `InsertionSort` to `insertion_sort` to follow PEP8 naming conventions.
- Replaced `print` statements with Python 3-compatible `print()` functions.
- Sorting logic updated to avoid in-place mutation by returning a new list.
- Enhanced readability with concise inline comments.

#### JumpList.py
- Renamed classes: `List` → `LevelList`, `JList` → `SkipList` to avoid naming conflicts and improve clarity.
- Refactored multi-level node insertion into a helper method `_insert_down`.
- Added boolean return value to deletion method for clearer success indication.
- Strengthened `down` pointer logic to ensure correct multi-level linking.

#### FibonacciNumber.py
- Renamed functions using snake_case: `naive_fibonacci`, `linear_fibonacci`, `logarithmic_fibonacci`.
- Used integer division `//` to fix potential indexing issues in matrix exponentiation.
- Added explicit handling for edge cases like `n=0` for numerical stability.
- Organized and preserved all three implementations for comparison and benchmarking.

#### Graph_BFS&DFS.py
- Renamed methods and variables (e.g., `AddVertex`, `BDFS`) to comply with PEP8 standards.
- Unified BFS and DFS traversal into a single method `bdfs(mode="BFS" | "DFS")`.
- Replaced nested loop duplication checks with a `visited` set to improve performance.
- Ensured topological safety by creating leaf nodes before referencing them as neighbors.
- Standardized output formatting with Python 3 `print()` and structured debug information.


------------------------------------------

## [1.0.0] - 2025-05-05

### Added
- Introduced `CHANGELOG.md` for tracking updates.
- Added structured test cases to all files for demonstration.
- Included display and debug output in all modules.

### Changed

#### BinarySearch.py
- Converted all `print` statements to Python 3 format.
- Fixed bug in binary search: changed `q = (p + r) / 2` to integer division.
- Added type annotations and modularized functions.
- Improved edge condition logic in binary search.

#### BinarySearchTree.py
- Refactored with `TreeNode` and `BinarySearchTree` classes for better OOP structure.
- Fixed bug in root transplant logic.
- Enhanced output clarity and added deletion verification.
- Prepared structure for future AVL tree support.

#### ChainingHash.py
- Changed all `print` to Python 3 syntax.
- Improved variable naming (`A`, `T`, `s` → `data`, `hash_table`, `slot_size`).
- Added docstrings to all functions.
- Added check before deletion to avoid exceptions.

#### Dijkstra.py
- Rewrote class structure to separate `Vertex` and `Graph` clearly.
- Renamed methods to follow PEP 8 (`add_vertex`, `add_edge`, etc.).
- Removed deprecated `cmp` usage; used `sort(key=lambda x: x[1])` instead.
- Refactored Dijkstra’s logic into `dijkstra()` and `_recursion()` for clarity.

#### DoubleLinkedList.py
- Changed `ListInsert`, `ListDelete`, etc., to PEP 8-compliant names.
- Replaced print with formatted `print()` functions.
- Added a `display()` method for full list traversal.
- Prevented deletion of sentinel `NIL` node with warning output.