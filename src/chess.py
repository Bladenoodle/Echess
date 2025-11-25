"""Module providing a chess game and minimax algorithm playing chess"""

SIZE = 8
WHITE, BLACK = 0, 1

#Black side init
r, n, b, q, k, p = "r", "n", "b", "q", "k", "p"
black_pieces = [r, n, b, q, k, p]

#White side init
R, N, B, Q, K, P= "R", "N", "B", "Q", "K", "P"
white_pieces = [R, N, B, Q, K, P]

def create_board():
    """Return a new 8x8 chess board with as a 2D list 
    containing classic chess starting position. 
    [
    [r, n, b, q, k, b, n, r],
    [p, p, p, p, p, p, p, p],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [P, P, P, P, P, P, P, P],
    [R, N, B, Q, K, B, N, R],
    ]
    """
    return [
    [r, n, b, q, k, b, n, r],
    [p, p, p, p, p, p, p, p],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [P, P, P, P, P, P, P, P],
    [R, N, B, Q, K, B, N, R],
    ]

def is_empty(piece):
    """Check if selected space is empty"""
    return piece == 0

def is_white(piece):
    """Check if selected space holds a white piece"""
    return piece in white_pieces

def is_black(piece):
    """Check if selected space holds a black piece"""

    return piece in black_pieces

def same_color(a, b):
    """Check if two selected spaces hold same coloured pieces"""
    if is_empty(a) or is_empty(b):
        return False
    return (is_white(a) and is_white(b)) or (is_black(a) and is_black(b))

def diff_color(a, b):
    if is_empty(a) or is_empty(b):
        return False
    return (is_white(a) and is_black(b)) or (is_black(a) and is_white(b))

def own_piece(piece, side):
    """Check if selected piece is own sided"""
    return (side == WHITE and is_white(piece)) or (side == BLACK and is_black(piece))

def dir(side):
    """Pawn direction indicator depending on side"""
    return -1 if side == WHITE else 1

def in_bounds(x, y):
    """Check if selected space is in bound"""
    return 0 <= x < SIZE and 0 <= y < SIZE

def copy_board(board):
    """Function for copying a board"""
    return [row[:] for row in board]
def pawn_moves(board, x, y, side):
    moves = []
    d = dir(side)
    if in_bounds(x, y + d) and is_empty(board[y + d][x]):
        moves.append(((x, y), (x, y + d)))
    if in_bounds(x + 1, y + d) and diff_color(board[y][x], board[y + d][x + 1]):
        moves.append(((x, y), (x + 1, y + d)))
    if in_bounds(x - 1, y + d) and diff_color(board[y][x], board[y + d][x - 1]):
        moves.append(((x, y), (x - 1, y + d)))

    return moves

def valid_moves(board, side):
    moves = []
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if not own_piece(piece, side):
                continue

            # if piece.lower() == "p":
            #     moves.extend(pawn_moves(board, x, y, side))
            # elif piece.lower() == "n":
            #     moves.extend(knight_moves(board, x, y, side))
            # elif piece.lower() == "b":
            #     moves.extend(bishop_moves(board, x, y, side))
            # elif piece.lower() == "r":
            #     moves.extend(rook_moves(board, x, y, side))
            # elif piece.lower() == "q":
            #     moves.extend(queen_moves(board, x, y, side))
            # elif piece.lower() == "k":
            #     moves.extend(king_moves(board, x, y, side))

    # later: filter with in_check to keep only legal moves
    return moves