# Project Definition Document

## Purpose

The goal of this project is to develop a chess-playing AI using Python.  
The AI evaluates given chess positions and selects the optimal move using the minimax algorithm with alpha–beta pruning.

This project focuses on learning game AI techniques, decision trees, and search optimization.


## Users

There is only one user role:

- User who inputs a chess position and receives the best move suggestion.


## Planned Functionality

### Core Functionality

- Represent an 8×8 chessboard internally
- Generate possible moves for the current position
- Implement the minimax algorithm
- Optimize the search with alpha–beta pruning
- Input format:
  - 8×8 board state (list or matrix structure)  
  - Turn indicator
- Output: best move for the current side

### Future Improvements

- Graphical user interface
- Full chess rules and full move generation
- Transposition table / position hashing
- Iterative deepening search

## Technical Overview

Language: Python

The AI evaluates future positions by simulating moves in a tree structure, assuming optimal play from the opponent (minimax).  
Alpha–beta pruning reduces unnecessary branches, improving efficiency.

Theoretical complexity: O(b^(d/2))  
- b = average branching factor  
- d = search depth

## References

- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning  
- https://indiaai.gov.in/article/understanding-the-minmax-algorithm-in-ai  
- https://stackoverflow.com/questions/16328690/how-do-you-derive-the-time-complexity-of-alpha-beta-pruning
