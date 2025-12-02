"""Module providing a chess board and helper functions."""

SIZE = 8
WHITE, BLACK = 0, 1

# Black side initialization
r, n, b, q, k, p = "r", "n", "b", "q", "k", "p"
black_pieces = [r, n, b, q, k, p]

# White side initialization
R, N, B, Q, K, P = "R", "N", "B", "Q", "K", "P"
white_pieces = [R, N, B, Q, K, P]


def create_board():
    """Return a new 8x8 chess board in classic starting position."""
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
    """Return True if a board square contains no piece."""
    return piece == 0


def is_white(piece):
    """Return True if a piece is a white piece."""
    return piece in white_pieces


def is_black(piece):
    """Return True if a piece is a black piece."""
    return piece in black_pieces


def same_color(piece_a, piece_b):
    """Check if two pieces are of the same color."""
    if is_empty(piece_a) or is_empty(piece_b):
        return False
    return (is_white(piece_a) and is_white(piece_b)) or (
        is_black(piece_a) and is_black(piece_b)
    )


def diff_color(piece_a, piece_b):
    """Return True if two pieces are of different colors."""
    if is_empty(piece_a) or is_empty(piece_b):
        return False
    return (is_white(piece_a) and is_black(piece_b)) or (
        is_black(piece_a) and is_white(piece_b)
    )


def own_piece(piece, side):
    """Return True if the piece belongs to the given side."""
    return (side == WHITE and is_white(piece)) or (
        side == BLACK and is_black(piece)
    )


def pawn_direction(side):
    """Return the movement direction of pawns for the given side."""
    return -1 if side == WHITE else 1


def in_bounds(x, y):
    """Return True if (x, y) are valid board coordinates."""
    return 0 <= x < SIZE and 0 <= y < SIZE


def copy_board(board):
    """Return a deep copy of the board."""
    return [row[:] for row in board]


def pawn_moves(board, x, y, side):
    """Return all valid pawn moves from (x, y)."""
    moves = []
    direction = pawn_direction(side)

    # One step forward
    if in_bounds(x, y + direction) and is_empty(board[y + direction][x]):
        moves.append(((x, y), (x, y + direction)))

    # Capture to the right
    if in_bounds(x + 1, y + direction) and diff_color(
        board[y][x], board[y + direction][x + 1]
    ):
        moves.append(((x, y), (x + 1, y + direction)))

    # Capture to the left
    if in_bounds(x - 1, y + direction) and diff_color(
        board[y][x], board[y + direction][x - 1]
    ):
        moves.append(((x, y), (x - 1, y + direction)))

    return moves


def valid_moves(board, side):
    """Return all pseudo-legal moves (movement rules only, no check logic)."""
    moves = []

    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if not own_piece(piece, side):
                continue

            #
            # if piece.lower() == "p":
            #     moves.extend(pawn_moves(board, x_coord, y_coord, side))
            # elif piece.lower() == "n":
            #     moves.extend(knight_moves(board, x_coord, y_coord, side))
            # ...

    return moves
