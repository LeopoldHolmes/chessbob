"""
This file is a part of My-PyChess application.
In this file, we define heuristic constants required for the python chess
engine.
"""

pawnEvalWhite = (
    (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    (8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0),
    (2.0, 2.0, 3.0, 5.0, 5.0, 3.0, 2.0, 2.0),
    (0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5),
    (0.0, 0.0, 0.5, 2.0, 2.0, 0.5, 0.0, 0.0),
    (0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5),
    (0.5, 1.0, 0.5, -2.0, -2.0, 0.5, 1.0, 0.5),
    (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
)

pawnEvalBlack = tuple(reversed(pawnEvalWhite))

knightEval = (
    (-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0),
    (-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0),
    (-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0),
    (-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0),
    (-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0),
    (-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0),
    (-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0),
    (-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0),
)

bishopEvalWhite = (
    (-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0),
    (-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0),
    (-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0),
    (-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0),
    (-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0),
    (-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0),
    (-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0),
    (-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0),
)

bishopEvalBlack = tuple(reversed(bishopEvalWhite))

rookEvalWhite = (
    (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    (0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5),
    (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
    (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
    (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
    (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
    (-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5),
    (0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0),
)

rookEvalBlack = tuple(reversed(rookEvalWhite))

queenEval = (
    (-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0),
    (-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0),
    (-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0),
    (-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5),
    (0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5),
    (-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0),
    (-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0),
    (-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0),
)

kingEvalWhite = (
    (-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0),
    (-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0),
    (-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0),
    (-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0),
    (-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0),
    (-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0),
    (2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0),
    (2.0, 3.0, 3.0, 0.0, 0.0, 1.0, 3.0, 2.0),
)

kingEvalBlack = tuple(reversed(kingEvalWhite))