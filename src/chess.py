"""Module providing a chess game and minimax algorithm playing chess"""

SIZE = 8
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

def valid_moves(board, side):
    own_pieces = white_pieces if side == 0 else black_pieces
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if piece in own_pieces:
                pass
    #under construction
