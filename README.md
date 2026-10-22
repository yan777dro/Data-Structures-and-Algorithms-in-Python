# Data Structures and Algorithms in Python

My implementations of classic data structures and algorithms in Python, written for learning and interview prep. Each file is self-contained, documented with docstrings, and covered by tests.

## Contents

| Topic | File | Time (avg) | Space |
|---|---|---|---|
| Linked List | `data_structures/linked_list.py` | Access O(n), insert at head O(1) | O(n) |
| Stack | `data_structures/stack.py` | Push/pop O(1) | O(n) |
| Queue | `data_structures/queue.py` | Enqueue/dequeue O(1) | O(n) |
| Binary Search Tree | `data_structures/bst.py` | Search/insert O(log n) | O(n) |
| Heap | `data_structures/heap.py` | Push/pop O(log n) | O(n) |
| Hash Table | `data_structures/hash_table.py` | Get/set O(1) | O(n) |
| Trie | `data_structures/trie.py` | Insert/search O(k) | O(n·k) |
| Binary Search | `searching/binary_search.py` | O(log n) | O(1) |
| Bubble Sort | `sorting/bubble_sort.py` | O(n²) | O(1) |
| Insertion Sort | `sorting/insertion_sort.py` | O(n²) | O(1) |
| Merge Sort | `sorting/merge_sort.py` | O(n log n) | O(n) |
| Quick Sort | `sorting/quick_sort.py` | O(n log n) | O(log n) |
| BFS / DFS | `graphs/traversal.py` | O(V + E) | O(V) |
| Dijkstra | `graphs/dijkstra.py` | O((V + E) log V) | O(V) |

## Repository layout

```
.
├── data_structures/
├── sorting/
├── searching/
├── graphs/
├── dynamic_programming/
└── tests/
```

## Getting started

Requires Python 3.10 or newer.

```bash
git clone https://github.com/yan777dro/Data-Structures-and-Algorithms-in-Python.git
cd Data-Structures-and-Algorithms-in-Python
pip install pytest
```

Run a single file:

```bash
python sorting/merge_sort.py
```

Run all tests:

```bash
pytest
```

## Progress

### Data structures
- [ ] Linked list (singly and doubly)
- [ ] Stack
- [ ] Queue and deque
- [ ] Binary search tree
- [ ] Heap / priority queue
- [ ] Hash table
- [ ] Trie
- [ ] Graph (adjacency list)

### Algorithms
- [ ] Binary search
- [ ] Bubble, insertion and selection sort
- [ ] Merge sort
- [ ] Quick sort
- [ ] BFS and DFS
- [ ] Dijkstra's shortest path
- [ ] Topological sort
- [ ] Dynamic programming (Fibonacci, knapsack, longest common subsequence)

## License

MIT
