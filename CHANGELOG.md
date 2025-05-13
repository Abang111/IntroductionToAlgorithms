# Changelog

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