# neetcode150

Python solutions to the [NeetCode 150](https://neetcode.io/practice) problem set.

## Layout

One package per topic, one module per problem. The problem statement lives in
each module's docstring, so the file is self-contained — statement, approach,
complexity, and solution in one place. `tests/` mirrors the source tree, one
test module per problem.

```
arrays_hashing/
  p01_contains_duplicate.py   # docstring = statement + approach + complexity
  p02_valid_anagram.py
tests/
  arrays_hashing/
    test_p01_contains_duplicate.py   # parametrized cases
TEMPLATE.py                   # copy this to start a new problem
```

Naming: `p<NN>_<snake_case_title>.py`, numbered in NeetCode's order within the
topic. The `p` prefix exists because a module name can't start with a digit.

Each solution keeps NeetCode's `class Solution` with its exact method signature,
so the file pastes straight into the site's editor.

## Adding a problem

```bash
cp TEMPLATE.py arrays_hashing/p02_valid_anagram.py
```

1. Paste the statement, examples, and constraints into the docstring.
2. Solve it.
3. Fill in **Approach** and **Complexity** — do this from memory, not by
   re-reading your code. If you can't state the idea in two sentences, you
   don't have it yet.
4. Add `tests/<topic>/test_p<NN>_<title>.py`: the given examples, plus empty input,
   single element, all-duplicates, and constraint boundaries.
5. Tick the box in the progress table below.

## Running

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pytest
```

Run one topic: `pytest tests/arrays_hashing -v`

## Progress

### Arrays & Hashing (0 / 9)

| # | Problem | Difficulty | Done |
| --- | --- | --- | --- |
| 01 | [Contains Duplicate](arrays_hashing/p01_contains_duplicate.py) | Easy | [ ] |
| 02 | Valid Anagram | Easy | [ ] |
| 03 | Two Sum | Easy | [ ] |
| 04 | Group Anagrams | Medium | [ ] |
| 05 | Top K Frequent Elements | Medium | [ ] |
| 06 | Encode and Decode Strings | Medium | [ ] |
| 07 | Product of Array Except Self | Medium | [ ] |
| 08 | Valid Sudoku | Medium | [ ] |
| 09 | Longest Consecutive Sequence | Medium | [ ] |

### Two Pointers (0 / 5)

Add rows as you go.

### Sliding Window (0 / 6)

### Stack (0 / 7)

### Binary Search (0 / 7)

### Linked List (0 / 11)

### Trees (0 / 15)

### Tries (0 / 3)

### Heap / Priority Queue (0 / 7)

### Backtracking (0 / 9)

### Graphs (0 / 13)

### Advanced Graphs (0 / 6)

### 1-D Dynamic Programming (0 / 12)

### 2-D Dynamic Programming (0 / 11)

### Greedy (0 / 8)

### Intervals (0 / 6)

### Math & Geometry (0 / 8)

### Bit Manipulation (0 / 7)
