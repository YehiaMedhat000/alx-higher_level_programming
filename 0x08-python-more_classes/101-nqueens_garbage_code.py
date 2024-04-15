#!/usr/bin/python3
def del_spots(chess_board, spot):
    """
    Delets the spots that are not valid for the N queens problem

    Args:
    chess_board -- The indices of the spots of the chess_board
    represented as a list of lists

    Returns:
    The new updated chess_board
    """

    row = spot[0]
    col = spot[1]
    diagonals = [row + col, row - col]
    result = []
    for i in range(len(chess_board)):
        # Get the diagonals
        pos = chess_board[i][0] + chess_board[i][1]
        neg = chess_board[i][0] - chess_board[i][1]

        # Begin deletion for rows and columns
        if chess_board[i][0] == row:
            continue
        elif chess_board[i][1] == col:
            continue
        # Check the diagonals
        elif pos == diagonals[0] or neg == diagonals[1]:
            continue

        result.append(chess_board[i])

    result.append(spot)
    return (result)

def reserve_spot(chess_board):
    """
    Reserves a spot in the chess_board where to place a queen

    Args:
    chess_board -- The chess_board with valid vacant places

    Returns:
    An updated version of the chess_boardwith the valid vacant
    places after placing the new queen
    """


    return (chess_board)
