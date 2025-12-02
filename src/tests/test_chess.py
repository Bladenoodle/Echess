"""This module is for unit testing basic functionalities of the website"""

import pytest
from chess_files.chess import (
    create_board, is_empty, is_black, is_white, same_color, diff_color,
    own_piece, dir, in_bounds, copy_board, pawn_moves,
    WHITE, BLACK
)

def test_if_create_board_works():
    board = create_board()
    assert board == [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]

def test_is_empty():
    assert is_empty(0)
    assert not is_empty("p")
    assert not is_empty("K")

def test_is_white_black():
    assert is_white("P")
    assert is_white("N")
    assert not is_white("p")
    assert is_black("p")
    assert is_black("q")
    assert not is_black("R")

def test_same_color():
    assert same_color("P", "N")
    assert same_color("r", "b")
    assert not same_color("P", "b")
    assert not same_color("P", 0)
    assert not same_color(0, "p")

def test_diff_color():
    assert diff_color("P", "p")
    assert diff_color("n", "Q")
    assert not diff_color("P", "Q")
    assert not diff_color("b", "p")
    assert not diff_color("P", 0)

def test_own_piece():
    assert own_piece("P", WHITE)
    assert not own_piece("p", WHITE)
    assert own_piece("p", BLACK)
    assert not own_piece("R", BLACK)

def test_dir_function():
    assert dir(WHITE) == -1
    assert dir(BLACK) == 1

def test_in_bounds():
    assert in_bounds(0, 0)
    assert in_bounds(7, 7)
    assert not in_bounds(-1, 0)
    assert not in_bounds(0, -1)
    assert not in_bounds(8, 3)
    assert not in_bounds(3, 8)

def test_copy_board():
    board = create_board()
    new_board = copy_board(board)
    assert new_board == board
    new_board[0][0] = "X"
    assert new_board != board

def test_pawn_moves_white_forward():
    board = create_board()
    moves = pawn_moves(board, 0, 6, WHITE)
    assert ((0,6),(0,5)) in moves

def test_pawn_moves_white_blocked():
    board = create_board()
    board[5][0] = "x"
    moves = pawn_moves(board, 0, 6, WHITE)
    assert ((0,6),(0,5)) not in moves

def test_pawn_moves_white_capture():
    board = create_board()
    board[5][1] = "p"
    moves = pawn_moves(board, 0, 6, WHITE)
    assert ((0,6),(1,5)) in moves

def test_pawn_moves_black_forward():
    board = create_board()
    moves = pawn_moves(board, 0, 1, BLACK)
    assert ((0,1),(0,2)) in moves

def test_pawn_moves_black_capture():
    board = create_board()
    board[2][1] = "P"
    moves = pawn_moves(board, 0, 1, BLACK)
    assert ((0,1),(1,2)) in moves
