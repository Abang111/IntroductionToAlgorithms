# Changelog


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