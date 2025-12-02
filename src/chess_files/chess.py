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

def move_until_stop(board, x, y, directions):
    """Function to return all moves to a direction until a blockade"""
    moves = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        while in_bounds(nx, ny):
            target = board[ny][nx]

            if is_empty(target):
                moves.append(((x, y), (nx, ny)))
            else:
                #Capture possible if enemy
                if diff_color(board[y][x], target):
                    moves.append(((x, y), (nx, ny)))
                break

            nx += dx
            ny += dy

    return moves

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

def knight_moves(board, x, y):
    """Return all valid knight moves from (x, y)."""

    moves = []
    jumps = [
        (1, 2), (2, 1), (2, -1), (1, -2),
        (-1, -2), (-2, -1), (-2, 1), (-1, 2),
    ]

    for dx, dy in jumps:
        nx, ny = x + dx, y + dy
        if not in_bounds(nx, ny):
            continue

        target = board[ny][nx]
        if is_empty(target) or diff_color(board[y][x], target):
            moves.append(((x, y), (nx, ny)))

    return moves

def bishop_moves(board, x, y):
    """Return all valid bishop moves from (x, y)."""

    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
    return move_until_stop(board, x, y, directions)

def rook_moves(board, x, y):
    """Return all valid rook moves from (x, y)."""

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    return move_until_stop(board, x, y, directions)

def queen_moves(board, x, y):
    """Return all valid queen moves from (x, y)."""

    directions = [
        (1,1), (1,-1), (-1,1), (-1,-1),
        (1,0), (-1,0), (0,1), (0,-1)
    ]
    return move_until_stop(board, x, y, directions)

def king_moves(board, x, y):
    """Return all valid king moves from (x, y)."""

    moves = []
    dirs = [
        (1,0), (-1,0), (0,1), (0,-1),
        (1,1), (1,-1), (-1,1), (-1,-1)
    ]

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if not in_bounds(nx, ny):
            continue

        target = board[ny][nx]
        if is_empty(target) or diff_color(board[y][x], target):
            moves.append(((x, y), (nx, ny)))

    return moves

def valid_moves(board, side):
    """Return all legal moves (movement rules only for now)."""
    moves = []

    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if not own_piece(piece, side):
                continue

            p = piece.lower()

            if p == "p":
                moves.extend(pawn_moves(board, x, y, side))
            elif p == "n":
                moves.extend(knight_moves(board, x, y))
            elif p == "b":
                moves.extend(bishop_moves(board, x, y))
            elif p == "r":
                moves.extend(rook_moves(board, x, y))
            elif p == "q":
                moves.extend(queen_moves(board, x, y))
            elif p == "k":
                moves.extend(king_moves(board, x, y))

    return moves

def is_legal_move(board, side, move):
    """Return True if the move is in the list of valid moves."""
    return move in valid_moves(board, side)

def make_move(board, move):
    """Return a new board after applying the given move.

    move is ((x1, y1), (x2, y2)) or ((x1, y1), (x2, y2), promo_piece)
    """
    new_board = copy_board(board)
    (x1, y1), (x2, y2) = move[0], move[1]
    piece = new_board[y1][x1]

    new_board[y1][x1] = 0

    # En passant: pawn moves diagonally to an empty square
    if piece.lower() == "p" and x1 != x2 and is_empty(board[y2][x2]):
        direction = pawn_direction(WHITE if is_white(piece) else BLACK)
        captured_y = y2 - direction
        captured_x = x2
        new_board[captured_y][captured_x] = 0

    # Promotion support (even though we don't generate promo moves yet)
    if len(move) == 3 and piece.lower() == "p":
        promo = move[2]
        new_board[y2][x2] = promo.upper() if is_white(piece) else promo.lower()
    else:
        new_board[y2][x2] = piece

    return new_board

