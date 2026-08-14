# Code Intuition Examples

A collection of small C++ programs for practicing core language concepts — written while working through codeintution course on DSA patterns. Additionally, supplementary material from learncpp.com. I am writing, debugging, and developing different programs in what I learn.

## Resources
[learncpp.com](https://www.learncpp.com/).
[codeintuition.io](https://www.codeintuition.io/)

## Contents

- [`programlab.cpp`](programlab.cpp) — basic I/O practice (`std::cin`/`std::cout`, functions, variables)
- [`Array/singleArray.cpp`](Array/singleArray.cpp) — static vs. dynamic arrays, traversal (index, range-based, pointer arithmetic)
- [`Array/multiArray.cpp`](Array/multiArray.cpp) — 2D/3D array construction, dynamic allocation, and traversal
- [`Array/rowMajorTraversal.cpp`](Array/rowMajorTraversal.cpp) — row-major traversal of a matrix using `vector<vector<int>>`
- [`Array/palindromeChecker.cpp`](Array/palindromeChecker.cpp) — two-pointer palindrome check on a string

## Building

Each file is self-contained with its own `main()`. Compile individually with g++:

```powershell
g++ -std=c++17 -o out Array/singleArray.cpp
./out
```
